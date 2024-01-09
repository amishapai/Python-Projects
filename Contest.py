'''num=int(input())
for i in range (0,num):
    dig=[]
    for i in range (0,3):
        dig.append(input())
    c=[]
    dig=list(dig)
    for i in dig:
        if i in c:
            dig.remove(i)
            for j in dig:
                if j==i:
                    dig.remove(i)
        else:
            c.append(i)
    print(dig[0])'''


'''num=int(input())
for i in range (0,num):
    dig=[]
    for i in range (0,3):
        dig.append(input())
    c=[]
    dig=list(dig)
    if dig[0]==dig[1]:
        print(dig[2])
    elif dig[1]==dig[2]:
        print(dig[0])
    else:
        print(dig[1])'''


'''num=int(input())
for i in range (0,num):
    dig=input()
    dig= ''.join(list(map(lambda x: x.strip(), dig.split())))
    c=[]
    dig=list(dig)
    if dig[0]==dig[1]:
        print(dig[2])
    elif dig[1]==dig[2]:
        print(dig[0])
    else:
        print(dig[1])'''



'''
l=['a','b','c','d','e','f','g','h']
r=[1,2,3,4,5,6,7,8]
num=int(input())
for j in range (0,num):
    pos=input()
    for i in r:
        if int(i)==int(pos[1]):
            continue;
        else:
            print(str(pos[0]+str(i)))
    for i in l:
        if str(i)==str(pos[0]):
            continue;
        else:
            print(str(i)+str(pos[1]))

 
'''
num=int(input())
for i in range (0,num):
    count=0
    n=int(input())
    dig=input()
    dig= ''.join(list(map(lambda x: x.strip(), dig.split())))
    count=0
    for j in range (0,n-1):
        for i in range (j+1,n):
            if (int(dig[j])==int(dig[i])):
                count+=1
    if count>n:
        print(n)
    else:
        print(count)
num=int(input())
for i in range (0,num):
    count=0
    n=int(input())
    dig=input()
    dig= ''.join(list(map(lambda x: x.strip(), dig.split())))
    cop=list(dig)
    count=0
    for k in cop:
        cop.remove(k)
    for j in range (0,n-1):
        for i in range (j+1,n):
            if (int(dig[j])==int(dig[i])):
                count+=1




