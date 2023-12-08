'''import tkinter as tk

def get_input():
    try:
        entered_text = entry.get()
        entered_integer = int(entered_text)
        result_label.config(text=f"You entered: {entered_integer}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

root = tk.Tk()
root.title("Tkinter Input Example")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

button = tk.Button(root, text="Get Input", command=get_input)
button.pack(pady=10)

# Explicitly set the dimensions of the window
root.geometry("400x200")

# Start the Tkinter event loop
root.mainloop()'''

'''import tkinter as tk

def get_input():
    try:
        entered_text = entry.get()
        entered_integer = int(entered_text)
        result_label.config(text=f"You entered: {entered_integer}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

root = tk.Tk()
root.title("Tkinter Input Example")

# Using the grid geometry manager
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=1, column=0, padx=10, pady=10)

button = tk.Button(root, text="Get Input", command=get_input)
button.grid(row=2, column=0, padx=10, pady=10)

# Explicitly set the dimensions of the window
root.geometry("400x200")

# Start the Tkinter event loop
root.mainloop()'''

'''import tkinter as tk

def get_input():
    try:
        entered_text = entry.get()
        entered_integer = int(entered_text)
        result_label.config(text=f"You entered: {entered_integer}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

root = tk.Tk()
root.title("Tkinter Input Example")

# Using the place geometry manager
entry = tk.Entry(root, width=30)
entry.place(x=10, y=10)

result_label = tk.Label(root, text="")
result_label.place(x=10, y=40)

button = tk.Button(root, text="Get Input", command=get_input)
button.place(x=10, y=70)

# Explicitly set the dimensions of the window
root.geometry("400x200")

# Start the Tkinter event loop
root.mainloop()'''


'''import tkinter as tk   
#create root window
root = tk.Tk()
lbl = tk.Label(root, text = "Enter a prime number")
lbl.pack(pady=15)


# Create an Entry widget for input
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create a button to trigger input retrieval
button = tk.Button(root, text="Enter a Prime Number", command=get_input)
button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# root window title and dimension
root.title("Prime Number")
# Set geometry (widthxheight)
root.geometry('500x500')

# Execute Tkinter
root.mainloop()'''
'''import tkinter as tk

root = tk.Tk()
root.title("Formatting Example")

# Label with formatting
label = tk.Label(root, text="Formatted Label", font=("Helvetica", 16, "bold"), fg="blue", bg="yellow", anchor="center")
label.pack(pady=10)

# Button with formatting
button = tk.Button(root, text="Click me!", font=("Arial", 12), fg="white", bg="green", relief="raised", width=15)
button.pack(pady=10)

root.mainloop()'''

import tkinter as tk

root = tk.Tk()

# Button with relief set to "raised"
button_raised = tk.Button(root, text="Raised", relief="raised")
button_raised.pack(pady=10)

# Button with relief set to "sunken"
button_sunken = tk.Button(root, text="Sunken", relief="sunken")
button_sunken.pack(pady=10)

# Button with relief set to "ridge"
button_ridge = tk.Button(root, text="Ridge", relief="ridge")
button_ridge.pack(pady=10)

# Button with relief set to "groove"
button_groove = tk.Button(root, text="Groove", relief="groove")
button_groove.pack(pady=10)

# Button with relief set to "flat"
button_flat = tk.Button(root, text="Flat", relief="flat")
button_flat.pack(pady=10)

# Button with relief set to "solid"
button_solid = tk.Button(root, text="Solid", relief="solid")
button_solid.pack(pady=10)

root.mainloop()



