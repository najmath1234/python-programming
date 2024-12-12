Student={
    'Name':input("Enter a student name:"),
    'Roll_no':input("Enter Rollno:"),
    'Register_no':input("Enter Register no:"),
    'Department':input("Enter department:"),
    'Semester':input("Enter semester:")
    }
print("Student details:",Student)
total_mark=int(input("Enter total mark of the student:"))
Student['total_mark']=total_mark
if total_mark>=90:
    Grade='A'
elif total_mark>=80:
    Grade='B'
elif total_mark>=75:
    Grade='C'
elif total_mark>=60:
    Grade='D'
elif total_mark>=50:
    Grade='P'
else:
    Grade='F'
Student['Grade']=Grade
print("\n Updated details:",Student)
del Student['Roll_no']
print("\n after deletionthe updated details is:",Student)
