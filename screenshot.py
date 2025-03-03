import pyautogui
import time
import os
import tkinter as tk

screenshot_folder = "C:\\Users\\USER\\Desktop\\project\\screenshots"

if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

def flash_effect():
    
    flash = tk.Tk()
    flash.geometry(f"{flash.winfo_screenwidth()}x{flash.winfo_screenheight()}")
    flash.configure(bg="white")
    flash.attributes("-topmost",True)
    flash.update()
    flash.after(50,flash.destroy())
 
def take_screenshot():
    flash_effect()
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_path = os.path.join(screenshot_folder, f"screenshot_{timestamp}.png")
    pyautogui.screenshot(screenshot_path)

take_screenshot()