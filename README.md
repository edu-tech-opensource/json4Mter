
```markdown
# 🐍 Python Script Execution Guide for Json Formatter

This guide will walk you through the steps to execute a Python script from scratch on a computer that has nothing installed (Python, Tkinter, and Requests) for both **Windows** and **macOS**.

---

## 🛠️ Prerequisites

Before you begin, ensure your computer meets the following requirements:
- **Windows 10/11** or **macOS 10.15 (Catalina)** or later.
- An active internet connection to download necessary software.

---

## 🚀 Steps to Execute a Python Script

### 1. **Install Python** 🐍

#### For Windows:
1. Visit the official Python website: [python.org](https://www.python.org/).
2. Download the latest version of Python for Windows.
3. Run the installer.
   - Check the box **"Add Python to PATH"** during installation.
   - Click **"Install Now"**.
4. Verify the installation:
   - Open Command Prompt (`Win + R`, type `cmd`, and press Enter).
   - Type `python --version` and press Enter. You should see the installed Python version.

#### For macOS:
1. Open Terminal (`Cmd + Space`, type `Terminal`, and press Enter).
2. Install Homebrew (if not already installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. Install Python using Homebrew:
   ```bash
   brew install python
   ```
4. Verify the installation:
   - Type `python3 --version` and press Enter. You should see the installed Python version.

---

### 2. **Install Required Libraries** 📚

#### For Windows and macOS:
1. Open Command Prompt (Windows) or Terminal (macOS).
2. Install `tkinter` and `requests` using `pip`:
   ```bash
   pip install requests
   ```
   - `tkinter` is included with Python by default, so no need to install it separately.

---

### 3. **Download or Create Your Python Script** 📄

1. Clone this repository or download the Python script to your computer.
2. Save the script in a folder of your choice.

---

### 4. **Run the Python Script** ▶️

#### For Windows:
1. Open Command Prompt.
2. Navigate to the folder where your script is located:
   ```bash
   cd path\to\your\script
   ```
3. Run the script:
   ```bash
   python script_name.py
   ```

#### For macOS:
1. Open Terminal.
2. Navigate to the folder where your script is located:
   ```bash
   cd /path/to/your/script
   ```
3. Run the script:
   ```bash
   python3 script_name.py
   ```

---

## 🎉 Congratulations! 🎉

You’ve successfully executed your Python script from scratch! 🐍✨

---

## ❓ Need Help?

If you encounter any issues, feel free to [open an issue](https://github.com/edu-tech-opensource/json4Mter/issues) on this repository.

---

Made by Alex Rodriguez
