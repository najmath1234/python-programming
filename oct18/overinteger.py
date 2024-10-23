num=int(input("enter the no of intergers to be inputed:"))
integers=[]
for i in range(num):
        integer=int(input("enter the integer:"))
        integers.append(integer)
        if (integer>100):
           integers[i]="over"
print(integers)
