# PortScanner

A simple port scanner script written in Python. This script scans ports on a specified IP address to determine if they are open or closed.

## Features

- Scans ports from 1 to 1024
- Displays open ports in green
- Optionally displays closed ports in red with the `-v` or `--verbose` option
- Interactive IP address input if not provided as an argument

## Usage

### Basic Usage

To scan an IP address:

```bash
python3 port_scanner.py 127.0.0.1
```

### Verbose Mode

To also display closed ports:

```bash
python3 port_scanner.py 127.0.0.1 -v
```

### Interactive Input

If no IP address is provided, the script will prompt for it:

```bash
python3 port_scanner.py
```

## Requirements

- Python 3.x
- `colorama` library (install with `pip install colorama`)

## Installation

1. Clone this repository

2. Navigate to the directory:

```bash
cd port-scanner
```

3. Install the required dependencies:

```bash
pip install colorama
```

## License

This project is licensed under the MIT License.
```
