from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Employee Data Entry')

Emp = dict()
loopCheck = [False]

def getDetails(i, entry):
    empDetails = []
    getID = enterID.get()
    empDetails.append(enterName.get())
    Emp[getID] = empDetails
    
    if i < entry:
        iDLabel.config(text=f"Add employee {i + 1} ID:")
        nameLabel.config(text=f"Add employee {i + 1} name:")
        enterButton['state'] = 'normal'
    else:
        messagebox.showinfo("Stop Entering", "You have reached the specified number of entries.")
        add.destroy()

def getEntry(entry):
    global enterButton, iDLabel, nameLabel, enterID, enterName
    try:
        int(entry)
        checkType.config(text="OK")

        iDLabel = Label(add, text="bruh")
        nameLabel = Label(add, text="bruh")

        iDLabel.pack()
        enterID = Entry(add)
        enterID.pack()
        nameLabel.pack()
        enterName = Entry(add)
        enterName.pack()

        def handleButtonClick(i=[1], entry=int(entry)):
            getDetails(i[0], entry)
            i[0] += 1

        enterButton = Button(add, text='ADD', command=lambda: handleButtonClick())
        enterButton.pack()

    except ValueError:
        checkType.config(text="Please enter a valid integer number")

def openAddWindow():
    global add
    loopCheck[0] = True
    add = Toplevel(root)
    add.title('Add Employees')
    entry = entryVar.get()
    entryLabel.config(text=f"Enter details for {entry} employees:")
    getEntry(entry)

entryLabel = Label(root, text="Enter the number of employees:")
entryLabel.pack()

entryVar = StringVar()
entryEntry = Entry(root, textvariable=entryVar)
entryEntry.pack()

checkType = Label(root, text="")
checkType.pack()

getButton = Button(root, text="Submit", command=openAddWindow)
getButton.pack()

root.mainloop()
