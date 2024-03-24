import os
import tkinter as tk
from PIL import Image, ImageTk


def display_win_screen():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    image_path = os.path.join(current_directory, "winscreen.jpg")

    # Create the main application window
    root = tk.Tk()
    root.title("Image Display")

    # Load the image
    image = Image.open(image_path)

    # Convert the Image object into a Tkinter-compatible photo image
    tk_image = ImageTk.PhotoImage(image)

    # Create a label widget to display the image
    label = tk.Label(root, image=tk_image)
    label.pack()

    # Run the Tkinter event loop
    root.mainloop()
    return root


if __name__ == "__main__":
    display_win_screen()
