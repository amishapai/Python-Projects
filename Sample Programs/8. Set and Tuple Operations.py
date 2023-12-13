#Implement set and tuple operations

#create empty set and tuple

setdata=set()
tupdata=tuple()

#Run infinite loop for menu

while 1:
    choice = input("Enter your choice \n S: Set Operations \n T: Tuple operations \n N: Terminate ")
    if choice =='S':
        while 1:
            ch=int(input("Enter operation: \n1:Add element ; 2:Remove element ; 3:Update element ; 4:Display ; 0:Terminate "))
            if ch==1:
                data=input("Enter element ")
                setdata.add(data)
                print(setdata)
            elif ch==2:
                data=input("Enter element ")
                setdata.discard(data)
                print(setdata)
            elif ch==3:
                data=(input("Enter element "))
                data1=set()
                data1.add(data)
                setdata.update(data1)
                print(setdata)
            elif ch==4:
                print(setdata)
            elif ch==0:
                break
            else:
                print("Invalid choice")
    elif choice == "T" :
        while 1:
            ch=int(input("Enter Operation \n1:Add element ; 2:Delete Tuple ; 3:Display ; 0:Terminate "))
            if ch==1:
                data=input("Enter element ")
                tupdata+=(data,)
                print(tupdata)
            elif ch==2:
                del tupdata
                print("Tuple deleted")
            elif ch==3:
                try:
                    print(tupdata)
                except:
                    print("Tuple has been deleted")
            elif ch==0:
                break
            else:
                print("Invalid Choice")
    elif choice == "N":
        break
    else:
        print("Invalid Choice")
        
