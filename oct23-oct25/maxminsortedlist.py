num=int(input("enter no of inputes to be inserted"))
integers=[]
for i in range(num):
    integer=int(input("enter the integer:"))
    integers.append(integer)
length=len(integers)
print("length of list is",length)
low=min(integers)
print("lowest of list is:",low)
high=max(integers)
print("highest of list is:",high)
sort=sorted(integers)
print("sorted list is:",sort)
sort.reverse()
print("reverse of list is:",sort)
sum1=sum(integers)
print("sum of integers is:",sum1)

