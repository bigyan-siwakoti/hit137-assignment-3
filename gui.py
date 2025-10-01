
import tkinter as tk
from model_handler import generate_image_from_prompt
from tkinter import filedialog
from model_handler import classify_image
import threading
class AppGUI:
    """
    This class is responsible for creating and managing the Tkinter GUI.
    """
    def __init__(self, root):
        # The 'root' is the main window.
        self.root = root
        self.root.title("HIT137 AI Application") # Sets the window title.
        
        # --- Create Top Frame for Model Selection ---
        # 1. Create the frame and attach it to the root window.
        self.top_frame = tk.Frame(self.root)
        
        # 2. Use pack() to place it. 'side=tk.TOP' makes it stick to the top.
        #    'fill=tk.X' makes it stretch horizontally to fill the window's width.
        self.top_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        # --- Create Bottom Frame for Information ---
        # 1. Create the second frame.
        self.bottom_frame = tk.Frame(self.root)

        # 2. Pack it to the bottom of the window.
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)
        # --- Add widgets to the Top Frame ---
        # 1. Create a Label widget. The first argument is the PARENT (self.top_frame).
        self.model_label = tk.Label(self.top_frame, text="Model Selection:")

        # 2. Pack the label to the LEFT side of the top_frame.
        self.model_label.pack(side=tk.LEFT, padx=(0, 10))

        # 3. Create a Button widget, also inside self.top_frame.
        self.load_button = tk.Label(self.top_frame, text="Group 43 assesment 3", fg="blue")

        # 4. Pack the button to the RIGHT side of the top_frame.
        self.load_button.pack(side=tk.RIGHT)
        
        # --- Create Middle Frame for Main Content ---
        # This frame will hold the input and output sections.
        # fill=tk.BOTH and expand=True make this frame take up all available space.
        self.middle_frame = tk.Frame(self.root)
        self.middle_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # --- Create Input Frame (on the left side of middle_frame) ---
        self.input_frame = tk.Frame(self.middle_frame, borderwidth=2, relief="groove")
        self.input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        # Add a title label to the input frame
        self.input_label = tk.Label(self.input_frame, text="describe your image")
        self.input_label.pack(pady=5)
        # Add an Entry widget for user text input
        self.prompt_entry = tk.Entry(self.input_frame, width=50)
        self.prompt_entry.pack(pady=5)

        self.run_model_button = tk.Button(
            self.input_frame, 
            text="generate image", 
            command=self.on_run_model_click
        )
        self.run_model_button.pack(pady=10)
        
        # --- Add widgets for Model 2 ---
        self.browse_button = tk.Button(
            self.input_frame,
            text="Browse Image for Classification",
            command=self.on_browse_click
        )
        self.browse_button.pack(pady=10)

        self.run_model_2_button = tk.Button(
            self.input_frame,
            text="Classify Image",
            command=self.on_run_model_2_click
        )
        self.run_model_2_button.pack(pady=5)

        # --- Create Output Frame (on the right side of middle_frame) ---
        self.output_frame = tk.Frame(self.middle_frame, borderwidth=2, relief="groove")
        self.output_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        #---hit and trial 02, trying to put output in screen just for self reminder, if missed try below title label output frame----
        self.output_label = tk.Label(self.output_frame, text="progress of generating image")
        self.output_label.pack(pady=5)

        # Text widget for Model 1 (Text-to-Image)
        self.output_text_1 = tk.Text(self.output_frame, height=2)
        self.output_text_1.pack(fill=tk.X, padx=5, pady=2)

        # Text widget for Model 2 (Image Classification)
        self.output_text_2 = tk.Text(self.output_frame, height=5)
        self.output_text_2.pack(fill=tk.X, padx=5, pady=2)
        #----hit and trial 02 end----
        # Add a title label to the output frame
        self.output_label = tk.Label(self.output_frame, text="Classfication of image")
        self.output_label.pack(pady=5)

        # --- Create Bottom Frame for Information ---
        # (The code for the bottom_frame remains the same)
        self.bottom_frame = tk.Frame(self.root)
        # ... rest of the bottom_frame code ...
        
        # --- Add widgets to the Bottom Frame ---
        # 1. Create a Label for the title, parent is self.bottom_frame.
        self.info_label = tk.Label(self.bottom_frame, text="OOP Concepts Explanation:")

        # 2. Pack it to the top of the bottom_frame. 'anchor="w"' aligns the text to the west (left).
        self.info_label.pack(anchor="w")

        # 3. Create a Text widget for detailed explanations.
        #    height=5 sets the height to 5 lines of text.
        self.info_text = tk.Text(self.bottom_frame, height=5)

        # 4. Pack it below the label. 'fill=tk.X' makes it stretch to fill the frame's width.
        self.info_text.pack(fill=tk.X)
    def on_run_model_click(self):
        """
        Handles the event when the 'Run Model 1' button is clicked.
        """
        # 1. Get the text from the entry widget
        prompt = self.prompt_entry.get()

        # 2. Call the function from our model_handler
        if prompt:
            generate_image_from_prompt(prompt)
        else:
            print("Prompt cannot be empty.")
    #---trial---hope dont messup UI-----
    def on_browse_click(self):
        """
        Opens a file dialog to select an image.
        """
        # Ask the user to select a file.
        # We store the selected file path in self.image_path
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            print(f"Selected image: {self.image_path}")
            # You could optionally display the selected file path in a label.

    def on_run_model_2_click(self):
        """
        Handles the event when the 'Run Model 2' button is clicked.
        """
        # Check if an image has been selected
        if hasattr(self, 'image_path') and self.image_path:
            # Call the function from our model_handler
            classification_result = classify_image(self.image_path)
            
            # TODO: Display the result in the output_frame
            print(classification_result)
        else:
            print("Please browse for an image first.")
    #---trial end--- 
      
    #attemp number 04
    # gui.py (inside the AppGUI class)
    def on_run_model_click(self):
        prompt = self.prompt_entry.get()
        if prompt:
            # Clear previous results
            self.output_text_1.delete("1.0", tk.END)
            # Call the function and get the status message
            status_message = generate_image_from_prompt(prompt)
            # Insert the new status message
            self.output_text_1.insert(tk.END, status_message)
        else:
            print("Prompt cannot be empty.")

    def on_run_model_2_click(self):
        if hasattr(self, 'image_path') and self.image_path:
            # Clear previous results
            self.output_text_2.delete("1.0", tk.END)
            # Call the function and get the classification results
            classification_result = classify_image(self.image_path)
            # Insert the new results
            self.output_text_2.insert(tk.END, classification_result)
        else:
            print("Please browse for an image first.")
    # attempt number 04 end
    
    #fixing glitch not respon issue#
    # gui.py (inside the AppGUI class)

    def on_run_model_click(self):
        prompt = self.prompt_entry.get()
        if prompt:
            self.output_text_1.delete("1.0", tk.END)
            self.output_text_1.insert(tk.END, "Generating image... Please wait.")
            # Create and start a new thread
            threading.Thread(target=self.run_image_generation, args=(prompt,)).start()
        else:
            print("Prompt cannot be empty.")

    def run_image_generation(self, prompt):
        # This function runs in the background thread
        status_message = generate_image_from_prompt(prompt)
        # Update the GUI from the main thread
        self.output_text_1.delete("1.0", tk.END)
        self.output_text_1.insert(tk.END, status_message)

    def on_run_model_2_click(self):
        if hasattr(self, 'image_path') and self.image_path:
            self.output_text_2.delete("1.0", tk.END)
            self.output_text_2.insert(tk.END, "Classifying image... Please wait.")
            # Create and start a new thread for model 2
            threading.Thread(target=self.run_image_classification, args=(self.image_path,)).start()
        else:
            print("Please browse for an image first.")

    def run_image_classification(self, image_path):
        # This function runs in the background thread
        classification_result = classify_image(image_path)
        # Update the GUI from the main thread
        self.output_text_2.delete("1.0", tk.END)
        self.output_text_2.insert(tk.END, classification_result)
    #end fixing glitch not respon issue#
     
def main():
    """The main function to set up and run the application."""
    # 1. Create the main window object.
    root = tk.Tk()

    # 2. Create an instance of our GUI class.
    app = AppGUI(root)

    # 3. Start the event loop to keep the window open.
    root.mainloop()

# This is a standard Python practice. It means the 'main()' function will
# only run when you execute this gui.py file directly.
if __name__ == '__main__':
    main()