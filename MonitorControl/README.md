# MonitorControl

A desktop application providing a user-friendly interface for monitor management on Linux systems using ddcutil.

## Overview

MonitorControl is a comprehensive monitor management solution that leverages ddcutil to provide advanced control over display settings. Built with Qt6, it offers a modern, responsive interface for both basic and advanced monitor configurations.

## Key Features

### Core Features
- 🖥️ Monitor Management
  - Automatic detection of connected monitors
  - Display of monitor information (model, capabilities)
  - Multi-monitor support

- 🎮 Basic Controls
  - Brightness adjustment
  - Contrast adjustment
  - Color temperature control
  - Input source selection

### Advanced Features
- 💾 Profile Management
  - Custom preset configurations
  - Quick switching between profiles
  - Profile import/export

- ⚙️ System Integration
  - DBus system integration
  - Persistent settings storage
  - Safe command execution

- 🎨 Advanced Controls
  - Color profile management
  - Auto-adjustment scheduling
  - Customizable hotkeys
  - Status monitoring and notifications

## Technical Architecture

### Components
1. **System Layer**
   - ddcutil interface
   - Monitor communication handler
   - Permission management

2. **Application Layer**
   - Settings manager
   - Profile handler
   - Event system
   - Configuration storage

3. **Presentation Layer**
   - Modern Qt6-based GUI
   - State management
   - User input handling

## System Requirements

### Operating System
- Linux (X11 or Wayland)
- Properly configured DDC/CI support
- Appropriate permissions for monitor communication

### Required System Packages
- ddcutil
- i2c-tools
- Python 3.x
- qt6-base

### Python Dependencies
- PyQt6
- python-dbus
- pyyaml
- sqlite3 (built-in)

## Project Structure

```
MonitorControl/
├── src/
│   ├── gui/              # Qt6-based GUI components
│   │   ├── dashboard/    # Main dashboard interface
│   │   └── settings/     # Settings panel
│   ├── monitor/          # Monitor control logic
│   │   ├── ddcutil/      # DDC/CI communication
│   │   ├── profiles/     # Profile management
│   │   └── scheduler/    # Auto-adjustment
│   ├── system/           # System integration
│   │   ├── dbus/         # DBus communication
│   │   └── security/     # Permission handling
│   └── main.py          # Application entry point
├── tests/               # Test suite
├── requirements.txt     # Python dependencies
├── LICENSE             # MIT License
└── README.md          # This file
```

## Installation

1. Install system dependencies:
```bash
# For Ubuntu/Debian
sudo apt-get install ddcutil i2c-tools qt6-base-dev python3-dbus

# For Fedora
sudo dnf install ddcutil i2c-tools qt6-base python3-dbus
```

2. Clone the repository:
```bash
git clone https://github.com/z-kahraman/CursorAI.git
cd MonitorControl
```

3. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Linux
```

4. Install Python dependencies:
```bash
pip install -r requirements.txt
```

5. Configure system permissions:
```bash
# Add user to i2c group
sudo usermod -aG i2c $USER

# Enable i2c module
sudo modprobe i2c-dev
```

## Usage

### Basic Usage

1. Start the application:
```bash
python src/main.py
```

2. Use the dashboard for quick access to:
   - Monitor selection
   - Basic controls (brightness, contrast)
   - Profile switching
   - Status monitoring

### Advanced Configuration

Access the settings panel for:
- Detailed monitor controls
- Profile management
- Application preferences
- Keyboard shortcut configuration
- Scheduling options

## Development

### Setting Up Development Environment

1. Install development dependencies:
```bash
pip install pytest pytest-cov black flake8
```

2. Run tests:
```bash
pytest tests/
```

3. Format code:
```bash
black src/
```

### Development Phases

1. **Foundation**
   - Basic GUI setup
   - ddcutil integration
   - Monitor detection
   - Basic controls

2. **Core Features**
   - Complete control interface
   - Profile management
   - Settings persistence
   - Error handling

3. **Advanced Features**
   - Hotkey support
   - Scheduling
   - Multi-monitor optimization
   - Advanced color management

## Security

- Secure handling of system permissions
- Safe execution of ddcutil commands
- Protection against invalid settings
- Comprehensive error handling and recovery

## Troubleshooting

### Common Issues
- Monitor not detected: Verify i2c permissions and DDC/CI support
- Permission errors: Ensure user is in the i2c group
- Display server compatibility: Check X11/Wayland configuration
- Command execution failures: Verify ddcutil installation and permissions

## Future Plans

- Support for additional monitor protocols
- Network-based remote control
- Plugin system for extensibility
- Integration with color calibration tools

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions:

- Open an issue on GitHub
- Check existing issues for solutions
- Review the documentation
- Verify your system meets all requirements

## Acknowledgments

- ddcutil development team
- Qt development team
- DBus and Linux community
- All contributors and testers
