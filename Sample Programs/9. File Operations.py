def write ():
    string=input("Enter the paragraph:")
    file= open ("D:\\my_file.txt",'w')
    file.write(string)
    file.close()

def read():
    file = open ("D:\\my_file.txt") 
    data=file.read()
    file.close()
    print("---------------")
    print("original content")
    print(data)
    print("---------------")
    print("modified content")
    print(data.title())
    print("---------------")
    print("In reverse order")
    print(data[::-1])
write()
read()
