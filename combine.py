import tkinter as tk

def button_click():
    label.config(text="Button Clicked!")

window = tk.Tk()
window.title("Simple Tkinter App")

label = tk.Label(window, text="Hello, Tkinter!")
label.pack(pady=20)

button = tk.Button(window, text="Click Me", command=button_click)
button.pack()

window.mainloop()

import tkinter as tk

def show_text():
    text = entry.get()
    output_label.config(text="You entered: " + text)

window = tk.Tk()
window.title("Entry and Output App")

entry = tk.Entry(window)
entry.pack(pady=10)

show_button = tk.Button(window, text="Show Text", command=show_text)
show_button.pack()

output_label = tk.Label(window, text="")
output_label.pack(pady=10)

window.mainloop()
import tkinter as tk

def show_state():
    if checkbox_var.get():
        state_label.config(text="Checkbox is checked")
    else:
        state_label.config(text="Checkbox is unchecked")

window = tk.Tk()
window.title("Checkbox Example")

checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(window, text="Check me!", variable=checkbox_var, command=show_state)
checkbox.pack(pady=10)

state_label = tk.Label(window, text="Checkbox is unchecked")
state_label.pack()

window.mainloop()