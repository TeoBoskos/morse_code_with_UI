from dictionary_morse import dictionary
from dictionary_morse import available_characters
from output import output_fun
from clear import clear_fun
import tkinter as tk
import ttkbootstrap as ttk

output_str = ""

# Create the main window.
root = tk.Tk()
root.title("Morse Code Translator")
root.geometry("800x600")

# Title label.
title_label = tk.Label(root, text="Morse Code Translator", font = 'Ariel 22 bold')
title_label.pack(pady=20)

# Label for user input.
input_label = tk.Label(root, text="Enter text:", font=("Ariel", 18))
input_label.pack(pady=20)

# Entry for user input.
entry_str = tk.StringVar()
input_entry = ttk.Entry(root, width=50, font=("Ariel", 16), textvariable=entry_str)
input_entry.pack()

# Bind the 'Enter' key to the output function.
input_entry.bind("<Return>", lambda event: output_fun(available_characters, dictionary, output_str, entry_str, output_value))

# Translate button.
translate_button = tk.Button(root, text="Translate", font=("Ariel", 18), command=lambda: output_fun(available_characters, dictionary, output_str, entry_str, output_value))
translate_button.pack(pady=40)

# Label for output.
output_value = tk.StringVar()
output_label = tk.Label(root, text="Output", font=("Ariel", 18), wraplength=550, textvariable=output_value)
output_label.pack()

# Clear button.
clear_button = tk.Button(root, text="Clear", font=("Ariel", 18), command=lambda: clear_fun(entry_str, output_value))
clear_button.pack(pady=40)

# Run the tkinter loop.
root.mainloop()
print("Goodbye")