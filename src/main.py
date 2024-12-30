#!/usr/bin/env python3

import sys
import traceback
from subprocess import run, PIPE
from PySide6.QtWidgets import QApplication
from gui.main_window import MainWindow
from monitor.monitor_controller import MonitorController

def control_osd(command):
    """
    Execute commands for OSD control
    command values:
    1: OSD On/Off
    2: Up
    3: Down
    4: Right
    5: Left
    10: Select/Enter
    """
    try:
        result = run(['ddcutil', 'setvcp', 'CA', str(command)], 
                    capture_output=True, 
                    text=True)
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
        return result.returncode == 0
    except Exception as e:
        print(f"OSD control error: {str(e)}")
        return False

def main():
    try:
        print("Starting application...")
        app = QApplication(sys.argv)
        
        # DDCutil check
        if not MonitorController.check_ddcutil():
            print("DDCutil is required but not available. Please install it first.")
            return 1
            
        print("Creating main window...")
        window = MainWindow()
        print("Showing main window...")
        window.show()
        print("Entering main event loop...")
        return app.exec()
    except Exception as e:
        print(f"Critical error in main: {str(e)}")
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main()) 