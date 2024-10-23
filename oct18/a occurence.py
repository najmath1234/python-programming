names=[]
word=input("enter first names seperated by spaces:")
names.append(word)
a_count=0
for name in names:
    a_count+=name.lower().count('a')
    print("the letter 'a' appears",a_count,"times in the list") 
