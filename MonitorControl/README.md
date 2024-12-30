# MonitorControl

A sophisticated Linux monitor control system that provides an intuitive interface for managing display settings through ddcutil.

## Overview

MonitorControl is a powerful desktop application that leverages ddcutil to provide advanced monitor management capabilities on Linux systems. It offers intelligent control over monitor settings with features ranging from basic brightness adjustments to sophisticated color profile management, all through a modern Qt6-based interface.

## Key Features

### Core Functionality
- 🖥️ Automatic detection of connected monitors with multi-monitor support
- 🌡️ Comprehensive monitor controls:
  - Brightness and contrast adjustment
  - Color temperature management
  - Input source selection
- 📊 Real-time display of monitor information and capabilities

### Advanced Features
- ⚡ Power-saving profiles and modes
- 👀 Eye strain reduction settings
- 🎨 Color profile management
- ⌚ Scheduled adjustments
- ⌨️ Customizable hotkey support
- 💾 Profile management and persistence

## System Requirements

### Operating System
- Linux (X11 or Wayland)
- Properly configured DDC/CI support
- Appropriate permissions for monitor communication

### Required System Packages
- ddcutil
- i2c-tools
- Python 3.8 or higher
- Qt6 base packages

### Python Dependencies
- PySide6 >= 6.4.0
- PyYAML >= 6.0
- dbus-python >= 1.2.18
- SQLite3 (built-in)

## Project Structure

```
MonitorControl/
├── src/
│   ├── gui/         # Qt6-based GUI components
│   │   ├── dashboard/   # Main dashboard interface
│   │   └── settings/    # Settings panel components
│   ├── monitor/     # Monitor control logic
│   │   ├── ddcutil/     # DDC/CI communication
│   │   ├── profiles/    # Profile management
│   │   └── scheduler/   # Adjustment scheduling
│   └── main.py      # Application entry point
├── requirements.txt # Python dependencies
├── LICENSE         # MIT License
└── README.md      # This file
```

## Installation

1. Install system dependencies:
```bash
# For Ubuntu/Debian
sudo apt-get install ddcutil i2c-tools qt6-base-dev

# For Fedora
sudo dnf install ddcutil i2c-tools qt6-base
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

5. Configure ddcutil permissions:
```bash
sudo usermod -aG i2c $USER
```

## Usage

1. Start the application:
```bash
python src/main.py
```

2. The application will appear in your system tray

### Basic Configuration

1. Right-click the system tray icon
2. Open "Settings" to access:
   - Monitor selection and information
   - Basic and advanced controls
   - Profile management
   - Hotkey configuration
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

### Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Troubleshooting

### Common Issues
- Monitor not detected: Verify i2c permissions and DDC/CI support
- Permission errors: Ensure user is in the i2c group
- Display server compatibility: Check X11/Wayland configuration

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions:

- Open an issue on GitHub
- Check existing issues for solutions
- Review the documentation in the `docs` folder
- Verify your system meets all requirements

## Acknowledgments

- ddcutil development team
- Contributors and maintainers
- The Python community
- Qt for Python (PySide6) team
