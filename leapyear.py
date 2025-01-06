year=int(input("enter a year"))
for i in range(2025,year+1):
    if(i%4==0 and i%100!=0 or(i%400==0)):
        print(i)
