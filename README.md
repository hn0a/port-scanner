# Keylogger

A Python keylogger script that logs keystrokes to a file using the pynput library.

## Introduction

This project is a simple keylogger written in Python. It captures and logs keyboard events to a text file. The keylogger uses the `pynput` library to listen to keyboard events and the `logging` module to record the events in a file.

## Requirements

- Python 3.x
- `pynput` library (install with `pip install pynput`)

## Installation

To use this keylogger, you need to have Python installed on your system. Follow the instructions below to set up the project:

1. **Clone this repository**

2. **Navigate to the directory:**
   ```sh
   cd keylogger
   ```

3. **Create and activate a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```
   *Using a virtual environment ensures that your project's dependencies are isolated from other projects and system-wide packages, which helps avoid potential conflicts.*

4. **Install the required dependencies:**
   ```sh
   pip install pynput
   ```

## Usage

To run the keylogger script, execute the following command in your terminal:

```sh
python keylogger.py
```

The script will start listening for keyboard events and log them to a file named `keylog.txt`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
