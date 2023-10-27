# Keybind_Instructions

# ⌨ Bind the default Windows 11 shortcut list to your keyboard.

# Displays a window with a list of Windows 11 keyboard shortcuts when CRTL + 1 are pressed.

# Copyright (C) 2023, Sourceduty - All Rights Reserved.
# THE CONTENTS OF THIS PROJECT ARE PROPRIETARY.

import tkinter as tk
from tkinter import simpledialog

# Function to display the shortcuts when CTRL + 1 is pressed
def display_shortcuts(event):
    shortcuts = """
    Win + A: Open Action Center.
    Win + C: Open Chat from Microsoft Teams.
    Win + D: Show or hide the desktop.
    Win + E: Open File Explorer.
    Win + I: Open Settings.
    Win + L: Lock your PC.
    Win + M: Minimize all windows.
    Win + R: Open the Run dialog box.
    Win + S: Open Search.
    Win + X: Open the Quick Link menu (also right-clicking the Start button does this).
    Win + Tab: Open Task View.
    Win + ,: Peek at the desktop.
    Win + . or Win + ;: Open the emoji panel.
    Win + Shift + S: Take a screenshot using Snip & Sketch.
    Win + H: Open voice typing.
    Win + Space: Switch input language and keyboard layout.
    """
    simpledialog.messagebox.showinfo("Windows 11 Shortcuts", shortcuts)

# Create the main window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Bind CTRL + 1 to the display_shortcuts function
root.bind('<Control-1>', display_shortcuts)

# Start the main loop
root.mainloop()
