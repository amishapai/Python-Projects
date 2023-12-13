
#Find height of ball thrown by basketball player

a=-16 #constant 
b=int(input("Enter velocity: "))
pHeight=float(input("Enter player height: "))

t=float(-b/(2*a))
print ("Time : ",t, "seconds")

h=(a*(t**2))+(b*t)

print ("Height is: ",h)

h = h +pHeight
print("Total height is: ", h, "feet")
