class Car:

    def __init__(self, company, price, color):

        self.company = company

        self.price = price

        self.color = color 

    def display_details(self):

        print("\nCar Details:")

        print("Company:", self.company)

        print("Price:", self.price)

        print("Color: ",self.color)


cars = []

for i in range(3):

    print("Enter details for Car  ",i+1)

    company = input("Enter Car Company: ")

    price = float(input("Enter Car Price: "))

    color = input("Enter Car Color: ")

    cars.append(Car(company, price, color))

 



for  car in cars:



    car.display_details()

