# 📸 Automated Screenshot Capture App

**✨ Project Overview**

This project is a simple yet powerful automated screenshot application developed in Python. It allows users to take a full-screen screenshot with a camera-like flash effect and saves the image in a designated folder with a timestamped filename.

**✨ Features**

✅ Instant Screenshot Capture – Captures the full screen automatically.

✅ Flash Effect – Mimics a camera flash before capturing the screenshot.

✅ Organized Storage – Saves screenshots in a predefined directory with timestamps.

✅ Cross-Platform Support – Works on Windows, macOS, and Linux.

✅ Lightweight & Fast – Uses minimal system resources for efficient execution.

**🎡 How It Works?**

The script checks if the screenshots folder exists; if not, it creates one.

A flash effect is triggered using Tkinter, momentarily displaying a white screen to simulate a camera flash.

A screenshot is captured using PyAutoGUI and saved in the specified directory as screenshot_YYYY-MM-DD_HH-MM-SS.png.

**💪 Technologies Used**

Python – Core programming language.

PyAutoGUI – Handles screenshot capture.

Tkinter – Creates a flash effect for visual feedback.

OS & Time Modules – Manages file system operations and timestamps.

**🚀 Installation & Usage**

⭐ 1. Install Required Dependencies

Ensure Python is installed, then install the required package:

pip install pyautogui

⭐ 2. Run the Script

Execute the Python script to take a screenshot:

python screenshot.py

The captured screenshot will be stored in the screenshots folder inside your project directory.

screenshots is a floder where all the screenshots will be stored

screenshot.py is the pythonscript 

screenshot.ico is the main icon of the image > where you can find most of the icons in 'icons8' website it downloads in the '.png' format then you need to convert it into '.ico' format

**📊 Future Enhancements**

✅ Add a GUI with buttons for manual screenshot capture.

✅ Implement hotkey support for quick screenshot capture.

✅ Enable region-specific screenshots instead of full-screen capture.

**📚 License**

This project is open-source and available under the MIT License.




