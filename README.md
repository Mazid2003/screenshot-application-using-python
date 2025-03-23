# 📸 Screenshot Capture Application using python

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

**⭐ 1. Install Required Dependencies**

Ensure Python is installed, then install the required package:

pip install pyautogui

**⭐ 2. Run the Script**

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

**🚀 How to Clone & Run Your Project**

Once you upload your project to GitHub, others can clone and run it easily. Here’s how:

**1️⃣ Clone the Repository**

Anyone can clone your project using Git by running:

git clone https://github.com/Mazid2003/screenshot-application-using-python.git

Or, they can download the ZIP file from GitHub and extract it manually.

**2️⃣ Navigate to the Project Directory**

After cloning, navigate into the project folder:

cd YourRepositoryName

**3️⃣ Install Dependencies**

Ensure Python is installed, then install the required package:

pip install pyautogui

**4️⃣ Run the Screenshot Script**

After setup, they can execute the script:

python screenshot.py

The screenshot will be stored in the screenshots folder inside the project directory.

**📌 Updating the Project**

If you make updates, others can pull the latest changes using:

git pull origin main

**💬 Want to Collaborate?**

Feel free to fork the repo, submit PRs, and give your feedback! 🔥💡

**📚 License**

This project is open-source and available under the MIT License.




