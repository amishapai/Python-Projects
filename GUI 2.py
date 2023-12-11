import tkinter as tk
from tkinter import messagebox
lists=[]
root = tk.Tk()

# Entry for number of elements
num_elements_label = tk.Label(root, text="Enter the number of elements:",font=("Times New Roman", 18, "italic"), fg="orange",bg= "#4B0082", anchor="center")
num_elements_label.pack(pady=10)

num_elements_entry = tk.Entry(root)
num_elements_entry.pack(pady=10)

def get_num_elements():
    try:
        max_elements = int(num_elements_entry.get())
        if max_elements > 0:
            show_element_entry(max_elements)
        else:
            messagebox.showerror("Error", "Please enter a positive integer.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

enter_num_elements_button = tk.Button(root, text="Enter", command=get_num_elements,font=("Times New Roman", 12), fg="black", bg="lightgray", relief="raised")
enter_num_elements_button.pack(pady=10)

element_count = 0
element_entry_label = None
element_entry = None
enter_button = None

def show_element_entry(max_elements):
    global element_entry_label, element_entry, enter_button
    num_elements_label.destroy()
    num_elements_entry.destroy()
    enter_num_elements_button.destroy()

    element_entry_label = tk.Label(root, text="Enter element:",font=("Times New Roman", 18, "italic"), fg="orange",bg= "#4B0082", anchor="center")
    element_entry_label.pack(pady=10)

    element_entry = tk.Entry(root)
    element_entry.pack(pady=10)

    enter_button = tk.Button(root, text="Enter", command= lambda: process_element(max_elements))
    enter_button.pack(pady=10)

def process_element(max_elements):
    global element_count, element_entry, element_entry_label, enter_button
    try:
        element = int(element_entry.get())
        lists.append(element)
        print(f"Entered element: {element}")
        element_count += 1

        if element_count == max_elements:
            print(lists)
            element_entry_label.destroy()
            element_entry.destroy()
            enter_button.destroy()
            messagebox.showinfo("Information", "All elements entered.")
        else:
            element_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

root.title("List Operation")

root.configure(bg="#4B0082")
# Set geometry (widthxheight)
root.geometry('500x250')
root.mainloop()
