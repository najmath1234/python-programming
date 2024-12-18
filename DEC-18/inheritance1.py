class fruits:
        def eat(self):
            print("we can eat fruits")
class orange(fruits):
    pass
#def eat(self):
# print("orange is a sor ftuit")
class apple(fruits):
    def eat(self):
        print("apple is sweet")
org1=orange()
appl=apple()
org1.eat()
appl.eat()
