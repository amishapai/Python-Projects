import tkinter as tk
from tkinter import messagebox
lists=[]
root = tk.Tk()

# Entry for number of elements
num_elements_label = tk.Label(root, text="Enter the number of elements:",font=("Times New Roman", 18, "italic"), fg="orange",bg= "#4B0082", anchor="center")
num_elements_label.pack(pady=30, padx=40)
num_elements_entry = tk.Entry(root)
num_elements_entry.pack(pady=10)
root.geometry('500x200')
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
    root.geometry('500x200')
    element_entry_label = tk.Label(root, text="Enter element:",font=("Times New Roman", 18, "italic"), fg="orange",bg= "#4B0082", anchor="center")
    element_entry_label.pack(pady=30)

    element_entry = tk.Entry(root)
    element_entry.pack(pady=10)

    enter_button = tk.Button(root, text="Enter", command= lambda: process_element(max_elements))
    enter_button.pack(pady=10)

def process_element(max_elements):
    global element_count, element_entry, element_entry_label, enter_button
    try:
        element = int(element_entry.get())
        lists.append(element)
        element_count += 1

        if element_count == max_elements:
            element_entry_label.destroy()
            element_entry.destroy()
            enter_button.destroy()
            messagebox.showinfo("Information", "All elements entered.")
            choice()
        else:
            element_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

def choice():
            global listlabel, choicelabel, choiceentry, choicebutton
            global ch
            root.geometry('500x300')
            listlabel=tk.Label(root, text=f"List is: {lists}",font=("Times New Roman", 18, "italic"), fg="orange",bg= "#4B0082", anchor="center")    
            listlabel.pack(pady=10)
            choicelabel=tk.Label(root, text="Choose operation: \n 1. Append Value \n 2. Insert Position \n 3. Remove value \n 4. Display \n 0. Exit",font=("Times New Roman", 12), fg="orange",bg= "#4B0082", anchor="center")
            choicelabel.pack(pady=10)
            choiceentry = tk.Entry(root)
            choiceentry.pack(pady=10)
            choicebutton = tk.Button(root, text="Enter", command= operations)
            choicebutton.pack(pady=10)
                


def operations():
        global appendlabel, appendentry, appendbutton, insertlabel, insertentryv, insertpos, insertentryp, insertbutton,removelabel, removeentry, removebutton, lis
        lis=""
        try:
            ch= int(choiceentry.get())
            listlabel.destroy()
            choicelabel.destroy()
            choiceentry.destroy()
            choicebutton.destroy()
            if ch== 1:
                root.geometry('500x200')
                appendlabel=tk.Label(root, text="Enter Value:",font=("Times New Roman", 15), fg="orange",bg= "#4B0082", anchor="center")
                appendlabel.pack(pady=30)
                appendentry = tk.Entry(root)
                appendentry.pack(pady=10)
                appendbutton = tk.Button(root, text="Enter", command= one)
                appendbutton.pack(pady=10)
                   
            elif ch==2:
                root.geometry('500x250')
                insertlabel=tk.Label(root, text="Enter Value:",font=("Times New Roman", 15), fg="orange",bg= "#4B0082", anchor="center")
                insertlabel.pack(pady=10)
                insertentryv = tk.Entry(root)
                insertentryv.pack(pady=10)
                insertpos=tk.Label(root, text="Enter Position:",font=("Times New Roman", 15), fg="orange",bg= "#4B0082", anchor="center")
                insertpos.pack(pady=10)
                insertentryp = tk.Entry(root)
                insertentryp.pack(pady=10)
                insertbutton = tk.Button(root, text="Enter", command= two)
                insertbutton.pack(pady=10)

            elif ch==3:
                root.geometry('500x200')
                removelabel=tk.Label(root, text="Enter Value:",font=("Times New Roman", 15), fg="orange",bg= "#4B0082", anchor="center")
                removelabel.pack(pady=30)
                removeentry = tk.Entry(root)
                removeentry.pack(pady=10)
                removebutton = tk.Button(root, text="Enter", command= three)
                removebutton.pack(pady=10)

            elif ch==4:
                root.geometry('500x200')
                lis=', '.join(str(v) for v in lists)
                messagebox.showinfo("List", lis)
                choice()
            elif ch==0:
                root.destroy()
            else:
                messagebox.showerror("Error", "Please enter a valid option.")
                choice()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer.")
                
            
def one():
    try:
        append=int(appendentry.get())
        lists.append(append)
        appendlabel.destroy()
        appendentry.destroy()
        appendbutton.destroy()
        choice()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")
def two():
    try:
        insertv=int(insertentryv.get())
        insertp=int(insertentryp.get())
        lists.insert(insertp,insertv)
        insertlabel.destroy()
        insertpos.destroy()
        insertentryv.destroy()
        insertentryp.destroy()
        insertbutton.destroy()
        choice()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

def three():
    try:
        remove=int(removeentry.get())
        lists.remove(remove)
        removelabel.destroy()
        removeentry.destroy()
        removebutton.destroy()
        choice()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

root.title("List Operation")


root.configure(bg="#4B0082")
# Set geometry (widthxheight)
root.mainloop()
