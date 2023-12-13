n= int(input("Enter the number of terms: "))
fiblist=[0,1]
gratio=[]
for i in range(0,n):
    fiblist.append(fiblist[i]+fiblist[i+1])
print("Series are ", fiblist)

for i in range(2,len(fiblist)):
    gratio.append(float(fiblist[i]/fiblist[i-1]))
print("Golden ratio is ", gratio)
