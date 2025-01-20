from pywinauto import Application, Desktop

# Start the Calculator application
app = Application(backend="uia").start("calc.exe")

# Get the main window of Calculator
dlg = Desktop(backend="uia").Calculator

# Perform actions (e.g., type calculation)
dlg.type_keys("2*3=")

# Print control identifiers
dlg.print_control_identifiers()

# Minimize the window
dlg.minimize()

# Restore the minimized window
Desktop(backend="uia").window(title="Calculator", visible_only=False).restore()
