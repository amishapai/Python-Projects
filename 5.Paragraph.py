#Read the paragraph from the user and count the number of words, and frequency of words appearing, and search for the specific word

str=input("Enter string/paragraph: ")

#print string/paragraph
print("Entered paragraph \n"+str)

#The split() method splits string into a list.
#len() counts the number of terms in the list
str1=str.lower()
wordCount=len(str.split())
print("Total number of words: ", wordCount)
counts=dict()
words=str.split()
for word in words:
    if word in counts:
        counts[word]=counts[word]+1
    else:
        counts[word]=1
for key in list(counts.keys()):
    print(key, ":", counts[key])
searchWord=input("Enter the word to search: ")
result=str1.find(searchWord.lower())
if result!=-1:
    print("Word is present")
else:
    print("Word is not present")
