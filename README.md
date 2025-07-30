# AI Security Course Setup Guide

This guide will help you set up your development environment for the AI Security course. Follow the instructions for your operating system to install all required tools.

## Required Tools Overview

- **Python 3.10+** - Programming language for AI/ML development
- **Visual Studio Code** - Code editor and development environment
- **VS Code Extensions** - Enhanced functionality for Python and Jupyter notebooks
- **Git** - Version control system
- **Jupyter** - Interactive notebook environment

---

## 🐍 Python Installation

### Windows

**Web Install:**
1. Visit [python.org](https://www.python.org/downloads/windows/)
2. Download the latest Python 3.10+ installer
3. Run the installer and **check "Add Python to PATH"**
4. Select "Install for all users" (recommended)
5. Verify installation by opening Command Prompt and typing: `python --version`

**Command Line (using Chocolatey):**
```powershell
# Install Chocolatey first (if not installed)
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install Python
choco install python
```

**Command Line (using Winget):**
```powershell
winget install Python.Python.3.12
```

### macOS

**Web Install:**
1. Visit [python.org](https://www.python.org/downloads/macos/)
2. Download the latest Python 3.10+ installer
3. Run the installer package
4. Verify installation: `python3 --version`

**Command Line (using Homebrew):**
```bash
# Install Homebrew first (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python
```

### Linux (Ubuntu/Debian)

**Command Line (APT):**
```bash
# Update package list
sudo apt update

# Install Python and pip
sudo apt install python3 python3-pip python3-venv

# Verify installation
python3 --version
pip3 --version
```

**Linux (CentOS/RHEL/Fedora):**
```bash
# For CentOS/RHEL
sudo yum install python3 python3-pip

# For Fedora
sudo dnf install python3 python3-pip

# Verify installation
python3 --version
pip3 --version
```

---

## 💻 Visual Studio Code Installation

### Windows

**Web Install:**
1. Visit [code.visualstudio.com](https://code.visualstudio.com/)
2. Click "Download for Windows"
3. Run the installer with default settings
4. Launch VS Code

**Command Line:**
```powershell
# Using Chocolatey
choco install vscode

# Using Winget
winget install Microsoft.VisualStudioCode
```

### macOS

**Web Install:**
1. Visit [code.visualstudio.com](https://code.visualstudio.com/)
2. Click "Download for Mac"
3. Open the downloaded .zip file
4. Drag VS Code to Applications folder

**Command Line:**
```bash
# Using Homebrew
brew install --cask visual-studio-code
```

### Linux

**Web Install:**
1. Visit [code.visualstudio.com](https://code.visualstudio.com/)
2. Download the appropriate package (.deb, .rpm, or .tar.gz)
3. Install using your package manager

**Command Line (Ubuntu/Debian):**
```bash
# Download and install Microsoft GPG key
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'

# Update package list and install
sudo apt update
sudo apt install code
```

**Command Line (CentOS/RHEL/Fedora):**
```bash
# Add Microsoft repository
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'

# Install (CentOS/RHEL)
sudo yum check-update
sudo yum install code

# Install (Fedora)
sudo dnf check-update
sudo dnf install code
```

---

## 🔧 VS Code Extensions Installation

After installing VS Code, you'll need these essential extensions: 

### Required Extensions:
- **Python** (ms-python.python) - Python language support
- **Pylance** (ms-python.vscode-pylance) - Enhanced Python language server
- **Jupyter** (ms-toolsai.jupyter) - Jupyter notebook support

### Recommended Extensions:
- **Python Black Formatter** - Code formatting
- **Flake8** - Code linting
- **YAML** - YAML file support
- **JSON** - Enhanced JSON support

### Method 1: Install via VS Code Interface
1. Open VS Code
2. Click the Extensions icon (four squares) in the sidebar
3. Search for and install each extension:

### Method 2: Install via Command Line
Open a terminal and run these commands:

```bash
# Essential Python extensions
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-toolsai.jupyter

# Additional helpful extensions
code --install-extension ms-vscode.vscode-json
code --install-extension redhat.vscode-yaml
code --install-extension ms-python.black-formatter
code --install-extension ms-python.flake8
code --install-extension ms-python.autopep8
```



---

## 🌿 Git Installation

### Windows

**Web Install:**
1. Visit [git-scm.com](https://git-scm.com/download/win)
2. Download and run the installer
3. Use default settings (recommended)

**Command Line:**
```powershell
# Using Chocolatey
choco install git

# Using Winget
winget install Git.Git
```

### macOS

**Command Line:**
```bash
# Using Homebrew
brew install git

# Or use Xcode Command Line Tools
xcode-select --install
```

### Linux

**Command Line:**
```bash
# Ubuntu/Debian
sudo apt install git

# CentOS/RHEL
sudo yum install git

# Fedora
sudo dnf install git
```

---

## 📓 Jupyter Installation

Jupyter will be installed automatically when you create your Python virtual environment using the provided requirements.txt file. However, if you want to install it globally:

### All Platforms
```bash
# Install Jupyter
pip install jupyter

# Or install JupyterLab (modern interface)
pip install jupyterlab
```

---

## ✅ Verification Steps

After installation, verify everything is working:

1. **Python**: Open terminal/command prompt and run:
   ```bash
   python --version
   # or on macOS/Linux
   python3 --version
   ```

2. **VS Code**: Launch VS Code and verify it opens correctly

3. **Git**: Run in terminal:
   ```bash
   git --version
   ```

4. **VS Code Extensions**: In VS Code, go to Extensions and verify the Python and Jupyter extensions are installed and enabled

---

## 🆘 Troubleshooting

### Python not found in PATH
- **Windows**: Reinstall Python and ensure "Add Python to PATH" is checked
- **macOS/Linux**: Add Python to your shell profile (`.bashrc`, `.zshrc`)

### VS Code Extensions not working
- Restart VS Code after installing extensions
- Check that Python interpreter is correctly selected (Ctrl/Cmd + Shift + P → "Python: Select Interpreter")

### Permission issues (Linux/macOS)
- Use `sudo` for system-wide installations
- Consider using virtual environments for project-specific installations

---

## 🎯 Next Steps

Once you have all tools installed:

1. Follow the instructions in `setup_verification.ipynb` to create a virtual environment
2. Test your installation using `verify_setup.py`
3. Install the required packages from `requirements.txt`

## 📞 Support

If you encounter issues during setup:
1. Check the troubleshooting section above
2. Search for your specific error message online
3. Consult your course instructor or technical support

---

*This setup guide ensures you have all necessary tools for the AI Security course. Keep this document handy for reference throughout the course.*
