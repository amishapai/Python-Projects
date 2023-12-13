#Consider a sequence of numbers with some missing values. Write a python program for inserting the missing values,
#and remove some of the values, from the sequenc. Also add few more values to the sequence.

l=[]
while True:
    choice= int(input("Choose operation: \n 1. Create list: 2.Add value at the end : 3. Insert value at position \n 4. Remove value : 5. Display list : 0.Exit"))
    if choice== 1:
        n= int (input ("Enter number of elements of list:"))
        for i in range(0,n):
            a=int(input("Enter number:"))
            l.append(a)
        print("List is ", l)
    elif choice ==2:
        a= int(input("Enter value "))
        l.append(a)
        print(l)
    elif choice==3:
        a= int(input("Enter index "))
        b= int(input("Enter value "))
        l.insert(a,b)
        print(l)
    elif choice==4:
        a=int(input("Enter value "))
        l.remove(a); print(l)
    elif choice==5:
        print(l)
    elif choice ==0:
        break
    else:
        print('Please enter a valid option')
