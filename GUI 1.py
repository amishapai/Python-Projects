import tkinter as tk
from tkinter import messagebox
#prime number code
def prime(num):
    l=True
    if num<0:
        num = -1* num
        
    a=[]
    b=[]
    prime=1
    for i in range (2, int(num/2 + 1)):
        if (num%i==0):
            a.append(i)
    
    for k in a:
        for j in range(2,k):
                if(k%j==0):
                    b.append(k)
                    break;            
    for l in b:
            if (l in a):
                a.remove(l)

    if (a==[]):
            return(num)
    else:
            return(a[-1])
        


def get_input():
    try:
        num = int(entry.get())
        result_label.config(text=f"Highest prime factor is {prime(num)}",font=("Times New Roman", 18, "italic"), fg="orange",bg= "#4B0082", anchor="center")
    except ValueError:
        # Display an error message if the conversion fails
        messagebox.showerror("Error", "Please enter a valid integer.")
def exit_app():
    root.destroy()

   
#create root window
root = tk.Tk()
lbl = tk.Label(root, text = "Enter a Number", font=("Times New Roman", 21, "bold"), fg="orange", bg="#4B0082", anchor="center")
lbl.pack(pady=15)


# Create an Entry widget for input
entry = tk.Entry(root, width=20)
entry.pack(pady=10)

# Create a button to trigger input retrieval
button = tk.Button(root, text="Calculate",  font=("Times New Roman", 12), fg="black", bg="lightgray", relief="raised",  command=get_input)
button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="",bg="#4B0082")
result_label.pack()

exit_button = tk.Button(root, text="Exit", command=exit_app,font=("Times New Roman", 12), fg="black", bg="lightgray", relief="raised",)
exit_button.pack(pady=10)

# root window title and dimension
root.title("Prime Number")

root.configure(bg="#4B0082")
# Set geometry (widthxheight)
root.geometry('500x250')

# Execute Tkinter
root.mainloop()
