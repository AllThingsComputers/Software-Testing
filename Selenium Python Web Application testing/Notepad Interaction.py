from pywinauto import Application, Desktop
import pyautogui
import time

# Start Notepad
app = Application(backend="uia").start("notepad.exe")

# Get the Notepad window
dlg = Desktop(backend="uia").window(title="Untitled - Notepad", visible_only=True)

# Set focus to Notepad
dlg.set_focus()

# Wait for 2 seconds
time.sleep(2)

# Type some text into Notepad using pyautogui
pyautogui.write("Hello, World!", interval=0.1)

# Print control identifiers of the Notepad window
dlg.print_control_identifiers()
