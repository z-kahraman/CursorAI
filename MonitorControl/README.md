<<<<<<< HEAD
# Monitor Control

A GUI application developed for controlling monitor settings via DDC/CI protocol on Linux systems.

## Features

- Brightness and contrast controls
- Dynamic Contrast Ratio (DCR) control
- OSD menu control
- Predefined modes (Reading, Movie, Gaming)
- Multi-monitor support
- Background operations

## Requirements

- Python 3.8+
- PySide6
- ddcutil

### System Requirements

```bash
# Install ddcutil
sudo apt-get install ddcutil

# Enable i2c module
sudo modprobe i2c-dev
```

### Python Dependencies

```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/username/MonitorControl.git
cd MonitorControl
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python src/main.py
```

## Usage

1. Select a monitor
2. Adjust brightness and contrast using sliders
3. Enable/disable DCR
4. Control OSD menu
5. Use predefined modes

## Troubleshooting

1. "ddcutil is not installed" error:
   - Make sure ddcutil is installed
   - Make sure i2c-dev module is loaded

2. "Permission denied" error:
   - Add your user to i2c group:
     ```bash
     sudo usermod -a -G i2c $USER
     ```
   - Restart the system

## License

This project is licensed under the MIT License. 
=======
# CursorAI Projects
>>>>>>> 71b554d9127bcb71348a5bdd2d388aacb4c5fb3a
