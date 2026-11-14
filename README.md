# Universal Converter – Engineering Edition

A high-precision scientific and engineering unit conversion application built with Python and Tkinter.

## Overview

Universal Converter is a desktop unit conversion application inspired by the classic Microsoft Convert interface. It combines a traditional Windows-style graphical interface with a high-precision conversion engine.

## Features

- **21 Conversion Categories** covering scientific and engineering measurements.
- **High-Precision Calculations** using Python's Decimal arithmetic.
- **Temperature Conversion** with support for affine conversions.
- **Classic Windows Interface** with a simple, familiar layout.
- **Unit Swapping** to quickly reverse conversions.
- **Conversion History** to keep track of previous calculations.
- **Favourites** to save and reuse frequently used conversions.
- **Standalone Windows Executable** built using PyInstaller.

## Supported Categories

1. Length
2. Temperature
3. Mass
4. Time
5. Area
6. Volume
7. Speed
8. Acceleration
9. Force
10. Pressure
11. Energy
12. Power
13. Torque
14. Density
15. Frequency
16. Angle
17. Electric Current
18. Voltage
19. Resistance
20. Capacitance
21. Electric Charge

## Technology Stack

- **Language:** Python
- **GUI:** Tkinter
- **Numerical Precision:** Decimal
- **Testing:** unittest
- **Packaging:** PyInstaller

## Installation and Usage

### Option 1: Windows Executable

Download `UniversalConverter.exe` from the project's GitHub Releases page and run it.

### Option 2: Run from Source

1. Clone the repository:

   ```bash
   git clone https://github.com/FranzHermann12/UniversalConverter.git
   ```

2. Open the project directory:

   ```bash
   cd UniversalConverter
   ```

3. Launch the application:

   ```bash
   python -m gui.app
   ```

## Running Tests

Run the automated test suite:

```bash
python -m unittest discover -s tests -v
```

The project currently includes 25 automated tests covering conversion categories and invalid inputs.

## Project Structure

```text
UniversalConverter/
│
├── assets/
│   └── icon.ico
│
├── core/
│   └── engine.py
│
├── data/
│   └── units.py
│
├── features/
│
├── gui/
│   └── app.py
│
├── tests/
│   └── test_engine.py
│
├── main.py
├── UniversalConverter.spec
├── README.md
├── LICENSE
└── .gitignore
```

## Version

**Current Version:** 1.0.0

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

**FranzHermann12**

GitHub: https://github.com/FranzHermann12

---
