def fibanocci(num):
    a=0
    b=1
    print("fibanocci series:")
    for i in range (num):
        f=print(a,end=" ")
        a,b=b,a+b
num1=int(input("Enter a number:"))
f=fibanocci(num1)
