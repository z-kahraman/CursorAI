import subprocess
import json
import re
from PySide6.QtCore import QThread, Signal, QObject, QRunnable, QThreadPool

class WorkerSignals(QObject):
    """Signals for worker threads"""
    finished = Signal()
    error = Signal(str)
    settings_updated = Signal(dict)
    monitors_updated = Signal(list)

class MonitorWorker(QRunnable):
    """Worker class to handle monitor operations in background"""
    def __init__(self, operation, *args):
        super().__init__()
        self.operation = operation
        self.args = args
        self.signals = WorkerSignals()
        self._monitors_cache = []
        self._settings_cache = {}

    def run(self):
        try:
            if hasattr(self, self.operation):
                getattr(self, self.operation)(*self.args)
        except Exception as e:
            self.signals.error.emit(str(e))
        finally:
            self.signals.finished.emit()

    def _set_vcp_value(self, monitor_id, vcp_code, value):
        """Set VCP feature value"""
        try:
            subprocess.run(
                ['ddcutil', 'setvcp', str(vcp_code), str(value),
                 '--display', str(monitor_id)],
                capture_output=True,
                text=True,
                check=True
            )
        except subprocess.CalledProcessError as e:
            print(f"Error setting VCP {vcp_code}: {e}")
            print(f"Error output: {e.stderr}")
            raise

    def detect_monitors(self):
        """Detect monitors in background"""
        try:
            result = subprocess.run(['ddcutil', 'detect'],
                                  capture_output=True,
                                  text=True,
                                  check=True)
            
            monitors = []
            current_monitor = {}
            
            for line in result.stdout.split('\n'):
                line = line.strip()
                
                if line.startswith('Display'):
                    if current_monitor:
                        monitors.append(current_monitor)
                    current_monitor = {'id': None, 'name': 'Unknown Monitor', 'capabilities': []}
                    
                    match = re.search(r'Display (\d+)', line)
                    if match:
                        current_monitor['id'] = int(match.group(1))
                
                elif 'Manufacturer:' in line:
                    manufacturer = line.split('Manufacturer:')[1].strip()
                    current_monitor['name'] = manufacturer
                
                elif 'Model:' in line:
                    model = line.split('Model:')[1].strip()
                    current_monitor['name'] = f"{current_monitor['name']} - {model}"
                
                elif 'Serial number:' in line:
                    serial = line.split('Serial number:')[1].strip()
                    current_monitor['serial'] = serial
            
            if current_monitor:
                monitors.append(current_monitor)
            
            self._monitors_cache = monitors
            self.signals.monitors_updated.emit(monitors)
            
        except Exception as e:
            self.signals.error.emit(str(e))

    def get_monitor_settings(self, monitor_id):
        """Get monitor settings in background"""
        try:
            settings = {}
            result = subprocess.run(
                ['ddcutil', 'getvcp', 
                 str(MonitorController.VCP_BRIGHTNESS), 
                 str(MonitorController.VCP_CONTRAST),
                 str(MonitorController.VCP_DCR),
                 '--display', str(monitor_id)],
                capture_output=True,
                text=True,
                check=True
            )
            
            for line in result.stdout.split('\n'):
                if 'VCP' not in line:
                    continue
                    
                match = re.search(r'VCP ([0-9A-Fa-f]+) ([^:]+):\s+current value =\s+(\d+)', line)
                if match:
                    code = int(match.group(1), 16)
                    name = match.group(2).strip()
                    value = int(match.group(3))
                    settings[code] = {'name': name, 'value': value}
            
            result = {
                'brightness': settings.get(MonitorController.VCP_BRIGHTNESS, {}).get('value', 50),
                'contrast': settings.get(MonitorController.VCP_CONTRAST, {}).get('value', 50),
                'dcr': settings.get(MonitorController.VCP_DCR, {}).get('value', 0),
                'original': settings
            }
            
            self._settings_cache[monitor_id] = result
            self.signals.settings_updated.emit(result)
            
        except Exception as e:
            self.signals.error.emit(str(e))

    def set_brightness(self, monitor_id, value):
        """Set brightness in background"""
        try:
            if self._settings_cache.get(monitor_id, {}).get('dcr', 0):
                self._set_vcp_value(monitor_id, MonitorController.VCP_DCR, 0)
            self._set_vcp_value(monitor_id, MonitorController.VCP_BRIGHTNESS, value)
            if monitor_id in self._settings_cache:
                del self._settings_cache[monitor_id]
        except Exception as e:
            self.signals.error.emit(str(e))

    def set_contrast(self, monitor_id, value):
        """Set contrast in background"""
        try:
            if self._settings_cache.get(monitor_id, {}).get('dcr', 0):
                self._set_vcp_value(monitor_id, MonitorController.VCP_DCR, 0)
            self._set_vcp_value(monitor_id, MonitorController.VCP_CONTRAST, value)
            if monitor_id in self._settings_cache:
                del self._settings_cache[monitor_id]
        except Exception as e:
            self.signals.error.emit(str(e))

    def set_dcr(self, monitor_id, enabled):
        """Set DCR in background"""
        try:
            value = 1 if enabled else 0
            self._set_vcp_value(monitor_id, MonitorController.VCP_DCR, value)
            if monitor_id in self._settings_cache:
                del self._settings_cache[monitor_id]
        except Exception as e:
            self.signals.error.emit(str(e))

    def control_osd(self, monitor_id, button):
        """Control OSD in background"""
        try:
            # First try to enable OSD if it's disabled
            try:
                subprocess.run(
                    ['ddcutil', 'setvcp', str(MonitorController.VCP_OSD), '2',
                     '--display', str(monitor_id)],
                    capture_output=True,
                    text=True,
                    check=True
                )
            except subprocess.CalledProcessError:
                pass
                
            self._set_vcp_value(monitor_id, MonitorController.VCP_OSD, button)
        except Exception as e:
            self.signals.error.emit(str(e))

class MonitorController:
    # VCP Feature codes
    VCP_BRIGHTNESS = 0x10
    VCP_CONTRAST = 0x12
    VCP_DCR = 0xF4  # Dynamic Contrast Ratio
    VCP_OSD = 0xCA  # OSD Control

    # OSD Command values
    OSD_BUTTON_MENU = 1    # Menu/Exit
    OSD_BUTTON_UP = 2      # Up
    OSD_BUTTON_DOWN = 3    # Down
    OSD_BUTTON_RIGHT = 4   # Right/Plus
    OSD_BUTTON_LEFT = 5    # Left/Minus
    OSD_BUTTON_SELECT = 10 # Select/Enter

    def __init__(self):
        print("Initializing MonitorController...")
        self._monitors_cache = []
        self._settings_cache = {}
        self.threadpool = QThreadPool()
        
        # Initial monitor detection
        self._start_worker('detect_monitors')

    def _start_worker(self, operation, *args, **kwargs):
        """Start a worker thread for the given operation"""
        worker = MonitorWorker(operation, *args)
        
        # Connect common signals
        worker.signals.error.connect(self._on_error)
        worker.signals.finished.connect(self._on_finished)
        
        # Connect operation specific signals
        if operation == 'detect_monitors':
            worker.signals.monitors_updated.connect(self._on_monitors_updated)
        elif operation == 'get_monitor_settings':
            worker.signals.settings_updated.connect(self._on_settings_updated)
        
        # Start the worker
        self.threadpool.start(worker)

    def _on_error(self, error_msg):
        print(f"Monitor controller error: {error_msg}")

    def _on_finished(self):
        pass

    def _on_monitors_updated(self, monitors):
        self._monitors_cache = monitors

    def _on_settings_updated(self, settings):
        pass

    @staticmethod
    def check_ddcutil():
        """Check if ddcutil is installed and accessible"""
        try:
            result = subprocess.run(['ddcutil', '--version'], 
                         capture_output=True, 
                         text=True,
                         check=True)
            print(f"ddcutil version: {result.stdout.strip()}")
            return True
        except Exception as e:
            print(f"ddcutil check failed: {str(e)}")
            return False

    def get_monitors(self):
        """Get list of connected monitors"""
        return self._monitors_cache

    def refresh_monitors(self):
        """Force refresh of monitor list"""
        self._start_worker('detect_monitors')
        return self._monitors_cache

    def get_monitor_settings(self, monitor_id):
        """Get current settings for a specific monitor"""
        if monitor_id in self._settings_cache:
            return self._settings_cache[monitor_id]
        
        self._start_worker('get_monitor_settings', monitor_id)
        return {'brightness': 50, 'contrast': 50, 'dcr': 0, 'original': {}}

    def refresh_settings(self, monitor_id):
        """Force refresh of monitor settings"""
        if monitor_id in self._settings_cache:
            del self._settings_cache[monitor_id]
        return self.get_monitor_settings(monitor_id)

    def set_brightness(self, monitor_id, value):
        """Set monitor brightness (0-100)"""
        self._start_worker('set_brightness', monitor_id, value)

    def set_contrast(self, monitor_id, value):
        """Set monitor contrast (0-100)"""
        self._start_worker('set_contrast', monitor_id, value)

    def get_dcr_status(self, monitor_id):
        """Get DCR status"""
        settings = self.get_monitor_settings(monitor_id)
        return settings.get('dcr', 0)

    def set_dcr(self, monitor_id, enabled):
        """Set DCR status"""
        self._start_worker('set_dcr', monitor_id, enabled)

    def control_osd(self, monitor_id, button):
        """Control monitor OSD"""
        self._start_worker('control_osd', monitor_id, button)
        return True 