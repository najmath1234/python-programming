Malayalam=int(input("enter marks for Malayalam out of 50*:"))
English=int(input("enter marks for English out of 50*:"))
Arabic=int(input("enter mark for Arabic out of 50*:"))
Physics=int(input("enter marks for Physics out of 50*:"))
Maths=int(input("enter marks for Maths out of 50*:"))
total_mark=Malayalam+English+Arabic+Physics+Maths
print("total mark is",total_mark)
avg=total_mark/250
percentage=avg*100
print("total percentage is",percentage)
