# main.py

import tkinter as tk
from gui import AppGUI
# Make sure to import the new loading function
from model_handler import load_models

def main():
    """The main function to set up and run the application."""
    # 1. Load the AI models first. This will run before the window appears.
    load_models()
    
    # 2. Create the main window object.
    root = tk.Tk()

    # 3. Create an instance of our GUI class.
    app = AppGUI(root)

    # 4. Start the event loop.
    root.mainloop()

if __name__ == '__main__':
    main()
