#To find highest Prime number

num= int(input("Enter the number "))
a=[]; b=[]

for i in range(2,int(num/2)+1):
    if num%i==0:
        a.append(i)

for j in a:
    for m in range(2,j):
        if(j%m==0):
            b.append(j)
            break

for k in b:
    for l in a:
        if(l==k):
            a.remove(k)


if a!=[]:
    print("Max prime number is ", a[-1])
else:
    print("Max prime number is ",num)




#To find the largest prime factor

n= int(input("Enter the number "))

maxPrime=0

#to check even number

while n%2==0:
    maxPrime=n
    n=n/2

for i in range(3,int(n**0.5)+1,2):
    while n%i==0:
        maxPrime=i
        n=n/i
#if n is greater assigned maxprime

if n>2:
    maxPrime=n

print("Max prime number is ", maxPrime)
