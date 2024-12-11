class employee:
        employee_id=0
        basic=0
        ta=0	
        da=0
        def salary(self):
                print("salary",self.basic+self.ta+self.da)
emp1=employee()
emp1.basic=20000
emp1.ta=500
emp1.da=1000
emp1.salary()
emp2=employee()
emp2.basic=30000
emp2.ta=500
emp2.da=1500
emp2.salary()
