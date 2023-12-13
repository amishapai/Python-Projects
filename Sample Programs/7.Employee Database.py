Employee={}
print("Choose your option:\n 1.Create Employee \n 2.Add New Employee \n 3.Search Employee \n 4.Delete Employee\n 5.Display")
while True:
    choice=int(input("Enter the Choice: "))
    if choice==1:
        n=int(input("Enter the Number of Employees:"))
        for i in range(n):
         print("Enter the Employee Details")
         EmpID=int(input("Enter Employee ID:"))
         EmpName=input("Enter Employee Name:")
         EmpDOB=input("Enter Employee DOB:")
         Designation=input("Enter Employee Designation:")
         EmpDetails=[]
         EmpDetails.append(EmpName)
         EmpDetails.append(EmpDOB)
         EmpDetails.append(Designation)
         Employee[EmpID]=EmpDetails
        print(Employee)
         
    elif choice==2:
         EmpID=int(input("Enter Employee ID:"))
         EmpName=input("Enter Employee Name:")
         EmpDOB=input("Enter Employee DOB:")
         Designation=input("Enter Employee Designation:")
         EmpDetails=[]
         EmpDetails.append(EmpName)
         EmpDetails.append(EmpDOB)
         EmpDetails.append(Designation)
         Employee[EmpID]=EmpDetails
         print(Employee)
    elif choice==3:
        EId=int(input("Enter Employee ID to display:"))
        print(Employee.get(EId))
    elif choice==4:
        EId=int(input("Enter Employee ID to delete:"))
        Employee.pop(EId)
        print(Employee)
    elif choice==5:
        Status=bool(Employee)
        if Status == False:
            print("No Employee Details")
        else:
            print(Employee)
    else:
        print ("Invalid choice")
        break

        
