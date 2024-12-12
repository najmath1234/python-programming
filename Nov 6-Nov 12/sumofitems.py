mylist=list(map(int,input("Enter numbers seperated by spaces:").split()))
total=0
for item in mylist:
    total+=item
print("sum of all items in the list:", total)
