#18/10/2023- DAY 1 PROGRAM

#1
print("Hello World :)")

#2
a=1.928
b=29.233
add= a+b
sub=a-b
mul=a*b
div=a/b
print(add,sub,mul,div, end=" ")
print("")

#3
num=float(input("ENTER NUMBER 1: "))
num1=float(input("ENTER NUMBER 2: "))

adds= num+num1
print("The sum of {0} and {1} is {2}".format(num,num1,adds))

#4
import math
rad=float(input("Enter radius of circle: "))
area= math.pi*pow(rad,2)
print("Area of the circle is %.2f"%area)
print("Without math function:")
area= 3.14*rad**2
print(area)

#5
x= int(input("Enter value for x "))
y= int(input("Enter value for y "))
t=x;x=y;y=t
print("x and y after swapping are x={0} and y={1}".format(x,y))

print("Without third variable")
x,y =y,x 
x= int(input("Enter value for x "))
y= int(input("Enter value for y "))
x=x+y
y=x-y
x=x-y
print(x,y)

#6
ch= input(("Enter character"))
print("ASCII is " , ord(ch))
