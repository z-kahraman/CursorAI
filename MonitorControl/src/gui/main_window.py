from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                               QHBoxLayout, QComboBox, QSlider, QLabel,
                               QPushButton, QCheckBox, QFrame, QGridLayout,
                               QProgressBar)
from PySide6.QtCore import Qt, QSignalBlocker, QTimer
from PySide6.QtGui import QIcon
from monitor.monitor_controller import MonitorController

class MainWindow(QMainWindow):
    # Preset values for different modes
    PRESETS = {
        'default': {'brightness': 50, 'contrast': 50},
        'reading': {'brightness': 40, 'contrast': 45},
        'movie': {'brightness': 45, 'contrast': 55},
        'gaming': {'brightness': 70, 'contrast': 60}
    }

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Monitor Control")
        self.setMinimumSize(800, 600)
        
        # Initialize monitor controller
        self.monitor_controller = MonitorController()
        
        # Connect worker signals
        self.monitor_controller._on_finished = self._on_operation_finished
        self.monitor_controller._on_error = self._on_error
        self.monitor_controller._on_settings_updated = self._on_settings_updated
        self.monitor_controller._on_monitors_updated = self._on_monitors_updated
        
        # Flag to prevent recursive updates
        self._updating = False
        self._operation_in_progress = False
        
        # Setup refresh timer
        self.refresh_timer = QTimer(self)
        self.refresh_timer.timeout.connect(self.refresh_current_monitor)
        self.refresh_timer.start(5000)  # Refresh every 5 seconds
        
        # Setup UI
        self.setup_ui()
    
    def setup_ui(self):
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Monitor selection
        monitor_layout = QHBoxLayout()
        monitor_label = QLabel("Select Monitor:")
        self.monitor_combo = QComboBox()
        self.update_monitor_list()
        monitor_layout.addWidget(monitor_label)
        monitor_layout.addWidget(self.monitor_combo)
        
        # Refresh button
        refresh_btn = QPushButton("Refresh")
        refresh_btn.clicked.connect(self.refresh_current_monitor)
        monitor_layout.addWidget(refresh_btn)
        monitor_layout.addStretch()
        
        # DCR control
        dcr_layout = QHBoxLayout()
        dcr_label = QLabel("Dynamic Contrast:")
        self.dcr_checkbox = QCheckBox()
        dcr_layout.addWidget(dcr_label)
        dcr_layout.addWidget(self.dcr_checkbox)
        dcr_layout.addStretch()
        
        # Brightness control
        brightness_layout = QHBoxLayout()
        brightness_label = QLabel("Brightness:")
        self.brightness_slider = QSlider(Qt.Horizontal)
        self.brightness_slider.setRange(0, 100)
        self.brightness_value = QLabel("50%")
        brightness_layout.addWidget(brightness_label)
        brightness_layout.addWidget(self.brightness_slider)
        brightness_layout.addWidget(self.brightness_value)
        
        # Contrast control
        contrast_layout = QHBoxLayout()
        contrast_label = QLabel("Contrast:")
        self.contrast_slider = QSlider(Qt.Horizontal)
        self.contrast_slider.setRange(0, 100)
        self.contrast_value = QLabel("50%")
        contrast_layout.addWidget(contrast_label)
        contrast_layout.addWidget(self.contrast_slider)
        contrast_layout.addWidget(self.contrast_value)

        # Preset buttons layout
        presets_layout = QHBoxLayout()
        presets_label = QLabel("Presets:")
        presets_layout.addWidget(presets_label)
        
        # Default button
        default_btn = QPushButton("Reset to Default")
        default_btn.clicked.connect(lambda: self.apply_preset('default'))
        presets_layout.addWidget(default_btn)
        
        # Reading mode button
        reading_btn = QPushButton("Reading Mode")
        reading_btn.clicked.connect(lambda: self.apply_preset('reading'))
        presets_layout.addWidget(reading_btn)
        
        # Movie mode button
        movie_btn = QPushButton("Movie Mode")
        movie_btn.clicked.connect(lambda: self.apply_preset('movie'))
        presets_layout.addWidget(movie_btn)
        
        # Gaming mode button
        gaming_btn = QPushButton("Gaming Mode")
        gaming_btn.clicked.connect(lambda: self.apply_preset('gaming'))
        presets_layout.addWidget(gaming_btn)
        
        presets_layout.addStretch()
        
        # OSD Controls
        osd_frame = QFrame()
        osd_frame.setFrameStyle(QFrame.Panel | QFrame.Raised)
        osd_layout = QVBoxLayout(osd_frame)
        
        osd_label = QLabel("OSD Controls")
        osd_label.setAlignment(Qt.AlignCenter)
        osd_layout.addWidget(osd_label)
        
        # OSD Button Grid
        button_grid = QGridLayout()
        
        # Menu button
        menu_btn = QPushButton("Menu")
        menu_btn.clicked.connect(lambda: self.control_osd(MonitorController.OSD_BUTTON_MENU))
        button_grid.addWidget(menu_btn, 1, 1)
        
        # Up button
        up_btn = QPushButton("▲")
        up_btn.clicked.connect(lambda: self.control_osd(MonitorController.OSD_BUTTON_UP))
        button_grid.addWidget(up_btn, 0, 1)
        
        # Down button
        down_btn = QPushButton("▼")
        down_btn.clicked.connect(lambda: self.control_osd(MonitorController.OSD_BUTTON_DOWN))
        button_grid.addWidget(down_btn, 2, 1)
        
        # Left button
        left_btn = QPushButton("◄")
        left_btn.clicked.connect(lambda: self.control_osd(MonitorController.OSD_BUTTON_LEFT))
        button_grid.addWidget(left_btn, 1, 0)
        
        # Right button
        right_btn = QPushButton("►")
        right_btn.clicked.connect(lambda: self.control_osd(MonitorController.OSD_BUTTON_RIGHT))
        button_grid.addWidget(right_btn, 1, 2)
        
        # Select button
        select_btn = QPushButton("Select")
        select_btn.clicked.connect(lambda: self.control_osd(MonitorController.OSD_BUTTON_SELECT))
        button_grid.addWidget(select_btn, 2, 2)
        
        osd_layout.addLayout(button_grid)
        
        # Monitor info section
        info_frame = QFrame()
        info_frame.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        info_layout = QVBoxLayout(info_frame)
        
        self.monitor_info = QLabel("Monitor Information")
        self.monitor_info.setWordWrap(True)
        info_layout.addWidget(self.monitor_info)
        
        # Progress bar for operations
        self.progress_bar = QProgressBar()
        self.progress_bar.setTextVisible(False)
        self.progress_bar.hide()
        
        # Status label
        self.status_label = QLabel()
        self.status_label.hide()
        
        # Add progress bar and status label to main layout
        status_layout = QHBoxLayout()
        status_layout.addWidget(self.status_label)
        status_layout.addWidget(self.progress_bar)
        
        # Add all layouts to main layout
        main_layout.addLayout(monitor_layout)
        main_layout.addLayout(dcr_layout)
        main_layout.addLayout(brightness_layout)
        main_layout.addLayout(contrast_layout)
        main_layout.addLayout(presets_layout)
        main_layout.addWidget(osd_frame)
        main_layout.addWidget(info_frame)
        main_layout.addLayout(status_layout)
        main_layout.addStretch()
        
        # Connect signals
        self.brightness_slider.valueChanged.connect(
            lambda value: self.brightness_value.setText(f"{value}%"))
        self.contrast_slider.valueChanged.connect(
            lambda value: self.contrast_value.setText(f"{value}%"))
        self.brightness_slider.sliderReleased.connect(self.on_brightness_released)
        self.contrast_slider.sliderReleased.connect(self.on_contrast_released)
        self.monitor_combo.currentIndexChanged.connect(self.on_monitor_changed)
        self.dcr_checkbox.stateChanged.connect(self.on_dcr_changed)
    
    def _on_operation_finished(self):
        """Handle worker operation completion"""
        self._operation_in_progress = False
        self.progress_bar.hide()
        self.status_label.hide()
        
        # Auto refresh after operation
        if self.monitor_combo.currentData():
            self.monitor_controller.refresh_settings(self.monitor_combo.currentData())

    def _on_error(self, error_msg):
        """Handle worker errors"""
        self.status_label.setText(f"Error: {error_msg}")
        self.status_label.show()
        self._operation_in_progress = False
        self.progress_bar.hide()
        
        # Auto refresh after error
        if self.monitor_combo.currentData():
            self.monitor_controller.refresh_settings(self.monitor_combo.currentData())

    def _on_settings_updated(self, settings):
        """Handle settings update from worker"""
        if self.monitor_combo.currentData():
            self.update_monitor_info(self.monitor_combo.currentData(), settings)
            self.update_monitor_settings_ui(settings)

    def _on_monitors_updated(self, monitors):
        """Handle monitors update from worker"""
        self.update_monitor_list_ui(monitors)

    def update_monitor_list_ui(self, monitors):
        """Update monitor list UI with new monitors"""
        current_monitor = self.monitor_combo.currentData()
        
        self.monitor_combo.clear()
        for monitor in monitors:
            self.monitor_combo.addItem(monitor['name'], monitor['id'])
            
        if current_monitor:
            index = self.monitor_combo.findData(current_monitor)
            if index >= 0:
                self.monitor_combo.setCurrentIndex(index)

    def update_monitor_settings_ui(self, settings):
        """Update UI with monitor settings"""
        try:
            self._updating = True
            
            # Block signals temporarily to prevent recursive updates
            with QSignalBlocker(self.brightness_slider):
                self.brightness_slider.setValue(settings['brightness'])
                self.brightness_value.setText(f"{settings['brightness']}%")
                
            with QSignalBlocker(self.contrast_slider):
                self.contrast_slider.setValue(settings['contrast'])
                self.contrast_value.setText(f"{settings['contrast']}%")
                
            with QSignalBlocker(self.dcr_checkbox):
                self.dcr_checkbox.setChecked(bool(settings['dcr']))
        finally:
            self._updating = False

    def show_operation_progress(self, message):
        """Show operation progress"""
        if not self._operation_in_progress:
            self._operation_in_progress = True
            self.progress_bar.setRange(0, 0)  # Indeterminate progress
            self.progress_bar.show()
            self.status_label.setText(message)
            self.status_label.show()

    def on_brightness_released(self):
        """Handle brightness slider release"""
        if self._updating or self._operation_in_progress:
            return
            
        value = self.brightness_slider.value()
        if self.monitor_combo.currentData():
            self.show_operation_progress("Setting brightness...")
            self.monitor_controller.set_brightness(
                self.monitor_combo.currentData(), 
                value
            )
    
    def on_contrast_released(self):
        """Handle contrast slider release"""
        if self._updating or self._operation_in_progress:
            return
            
        value = self.contrast_slider.value()
        if self.monitor_combo.currentData():
            self.show_operation_progress("Setting contrast...")
            self.monitor_controller.set_contrast(
                self.monitor_combo.currentData(), 
                value
            )
    
    def on_monitor_changed(self, index):
        """Handle monitor selection change"""
        if index >= 0:
            monitor_id = self.monitor_combo.currentData()
            self.show_operation_progress("Loading monitor settings...")
            self.monitor_controller.get_monitor_settings(monitor_id)
    
    def on_dcr_changed(self, state):
        """Handle DCR checkbox state change"""
        if self._updating or self._operation_in_progress:
            return
            
        if self.monitor_combo.currentData():
            enabled = state == Qt.Checked
            self.show_operation_progress("Setting DCR...")
            self.monitor_controller.set_dcr(
                self.monitor_combo.currentData(),
                enabled
            )
    
    def control_osd(self, button):
        """Control OSD menu with the given button command"""
        if self._operation_in_progress:
            return
            
        if self.monitor_combo.currentData():
            self.show_operation_progress("Sending OSD command...")
            return self.monitor_controller.control_osd(
                self.monitor_combo.currentData(),
                button
            )

    def refresh_current_monitor(self):
        """Refresh current monitor settings"""
        if self._operation_in_progress:
            return
            
        if self.monitor_combo.currentData():
            monitor_id = self.monitor_combo.currentData()
            self.show_operation_progress("Refreshing monitor settings...")
            self.monitor_controller.refresh_settings(monitor_id)

    def apply_preset(self, preset_name):
        """Apply a preset mode to the current monitor"""
        if not self.monitor_combo.currentData() or self._operation_in_progress:
            return
            
        preset = self.PRESETS.get(preset_name)
        if not preset:
            return
        
        try:
            self._updating = True
            monitor_id = self.monitor_combo.currentData()
            
            self.show_operation_progress(f"Applying {preset_name} preset...")
            
            # Ensure DCR is disabled
            self.monitor_controller.set_dcr(monitor_id, False)
            with QSignalBlocker(self.dcr_checkbox):
                self.dcr_checkbox.setChecked(False)
            
            # Update monitor settings
            self.monitor_controller.set_brightness(monitor_id, preset['brightness'])
            self.monitor_controller.set_contrast(monitor_id, preset['contrast'])
            
            # Update UI
            with QSignalBlocker(self.brightness_slider):
                self.brightness_slider.setValue(preset['brightness'])
                self.brightness_value.setText(f"{preset['brightness']}%")
                
            with QSignalBlocker(self.contrast_slider):
                self.contrast_slider.setValue(preset['contrast'])
                self.contrast_value.setText(f"{preset['contrast']}%")
        finally:
            self._updating = False 

    def update_monitor_info(self, monitor_id, settings):
        """Update monitor information display"""
        if not settings.get('original'):
            self.monitor_info.setText("No detailed information available")
            return
            
        info_text = []
        info_text.append(f"Monitor ID: {monitor_id}")
        
        # Add all original VCP values
        info_text.append("\nMonitor Settings:")
        for code, data in settings['original'].items():
            info_text.append(f"- {data['name']}: {data['value']}")
        
        self.monitor_info.setText('\n'.join(info_text))
    
    def update_monitor_settings(self, monitor_id):
        """Update UI with current monitor settings"""
        try:
            self._updating = True
            settings = self.monitor_controller.get_monitor_settings(monitor_id)
            
            # Update monitor info
            self.update_monitor_info(monitor_id, settings)
            
            # Block signals temporarily to prevent recursive updates
            with QSignalBlocker(self.brightness_slider):
                self.brightness_slider.setValue(settings['brightness'])
                self.brightness_value.setText(f"{settings['brightness']}%")
                
            with QSignalBlocker(self.contrast_slider):
                self.contrast_slider.setValue(settings['contrast'])
                self.contrast_value.setText(f"{settings['contrast']}%")
                
            with QSignalBlocker(self.dcr_checkbox):
                self.dcr_checkbox.setChecked(bool(settings['dcr']))
        finally:
            self._updating = False
    
    def update_monitor_list(self):
        """Update the monitor list in the combo box"""
        monitors = self.monitor_controller.get_monitors()
        current_monitor = self.monitor_combo.currentData()
        
        self.monitor_combo.clear()
        for monitor in monitors:
            self.monitor_combo.addItem(monitor['name'], monitor['id'])
            
        # Try to reselect the previous monitor if it still exists
        if current_monitor:
            index = self.monitor_combo.findData(current_monitor)
            if index >= 0:
                self.monitor_combo.setCurrentIndex(index)
    
    def update_monitor_settings_ui(self, settings):
        """Update UI with monitor settings"""
        try:
            self._updating = True
            
            # Block signals temporarily to prevent recursive updates
            with QSignalBlocker(self.brightness_slider):
                self.brightness_slider.setValue(settings['brightness'])
                self.brightness_value.setText(f"{settings['brightness']}%")
                
            with QSignalBlocker(self.contrast_slider):
                self.contrast_slider.setValue(settings['contrast'])
                self.contrast_value.setText(f"{settings['contrast']}%")
                
            with QSignalBlocker(self.dcr_checkbox):
                self.dcr_checkbox.setChecked(bool(settings['dcr']))
        finally:
            self._updating = False 