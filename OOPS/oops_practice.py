'''
class Student:

    college_name = "ABC" #class attribute(same for all objects)
    name = "Anonymous" #object attribute > class attribute(precedence)

    
    #Default contructor
    def __init__():
        pass
    #Actually two constructors are not created in single class
    #And this constructor is called by itself

    #parametrized constructors
    def __init__(self, name, marks) :
        self.name = name 
        self.marks = marks
        print("Adding news student in Database..")


s1 = Student("Khalid", 89)
print(s1.name, s1.marks)

s2 = Student("Furqan", 90)
print(s2.name, s2.marks)
'''

# Methods
# Methods are functions that belong to objects
'''
class Student:

    def __init__(self,name,marks):
        
        self.name = name
        self.marks = marks

    def welcome(self):
        print(f"Welcome {self.name}")
    def get_marks(self):
        print(f"{self.marks}")

s1 = Student("Khalid", 98)
print(s1.name, s1.marks)

print(s1.welcome())
print(s1.get_marks())
'''

# Practice Question
# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.
'''
class Student: 

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(f"Hi, {self.name} your avg marks are: ", sum/3)

s1 = Student("Khalid",[98,90,94])
s1.get_avg()
# we can chage the name directly
s1.name = "Furqan"
s1.get_avg()
'''

# practice Question
# Create Account class with 2 attributes-balance & account no.
# Create methods for debit, ctedit & printing the balance.
'''
class Account:
    def __init__(self, bal, acc_no) :
        self.balance = bal
        self.account_no = acc_no
    
    def debit(self, amount):
        self.balance -= amount
        print(f"RS. {amount} is debited from your account")
        print(f"Total balance: ",self.get_total())

    def credit(self, amount):
        self.balance += amount
        print(f"{amount} is added to your account")
        print(f"Total balance: {self.get_total()}")

    def get_total(self):
        return self.balance
    
customer1 = Account(10000, 12345)
print(customer1.balance, customer1.account_no)
customer1.debit(1000)
customer1.credit(1000)
'''

# practice Question
'''
class Car:
    def __init__(self, brand, model, year) :
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        print(f"Brand: {self.brand}\n Model: {self.model}\n Year: {self.year}")

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Tesla", "Model S", 2022)
car1.display_info()
car2.display_info()
'''

# Static Method Question
# Methods that donot use the self parameter(work at the class level)
'''
class Math_Operation:
    @staticmethod   #decorator
    def add(x, y):
        return x + y
    
    @staticmethod
    def sub(x, y):
        return x - y
    
    #@staticmethod
    def college():
        print(f"College Name: Ali Trust College")
    
print(Math_Operation.add(5,4))
print(Math_Operation.sub(25, 20))
Math_Operation.college()
'''

# Private(like) attributes & methods
# Those methods & attributes not accessible outside class
'''
class Account:
    def __init__(self, acc_no, acc_pass) :
        self.__acc_no = acc_no      # putting two underscore make it private(Unaccessible outside class)
        self.__acc_pass = acc_pass

customer = Account("12345", "asdfg")
print(customer.acc_no, customer.acc_pass)

# Another Example
class Person:
    def __init__(self) :
        __name = "anonymous"

    def __hello(self):
        print("Hello person, this is private method")
        print("cannot accessible outside class.")

    def welcome(self):
        self.__hello()
    
s1 = Person()
print(s1.welcome())  #will give error 
print(s1.__hello())  #will give error
'''
'''
# Inheritance 
# When one class derives the properties & methods of another class
class Car:
    def __init__(self, type) :
        self.type = type

    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped...")

class ToyotaCar(Car):
    def __init__(self, name, type) :
        super().__init__(type) #Super method use to access parent class methods
        self.name = name
        super().start()

car1 = ToyotaCar("Fortuner", "electric")
car2 = ToyotaCar("prius", "Diesel")
print(car1.type)
'''

# INheritance Practice Questions
# Questions No: 01
'''
class Vehicle :
    def __init__(self, make, model, year) :
        self.make = make 
        self.model = model
        self.year = year

    def calculate_mileage(self, miles, gallons):
        return miles / gallons
    
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

class Truck(Vehicle):
    def __init__(self, make, model, year, capacity):
        super().__init__(make, model, year)
        self.capacity = capacity

my_car = Car("Honda", "Civic", 2024, 4)
my_truck = Truck("Ford", "F_150", 2015, 1000)

print(my_car.calculate_mileage(200,10))
print(my_car.num_doors)
'''

# Question NO: 02
'''
class Shapes:
    def __init__(self, color) :
        self.color = color

    def get_color(self):
        return self.color
    
    def calculate_area(self):
        raise NotImplementedError
    
    def calculate_parameter(self):
        raise NotImplementedError
    
class Circle(Shapes):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    def calculate_area(self):
        import math
        return math.pi * self.radius * self.radius
    def calculate_parameter(self):
        import math
        return 2 * math.pi * self.radius
    
class Square(Shapes):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length
    def calculate_area(self):
        return self.side_length * self.side_length
    def calculate_parameter(self):
        return 4 * self.side_length
    
circle = Circle("RED", 5)
square = Square("Blue", 5)

print(circle.color)
print(circle.calculate_area())
print(circle.calculate_parameter())
'''

# Question No: 03
'''
class Employee:
    def __init__(self, name, department, salary) :
        self.name = name
        self.department = department
        self.salary = salary

    def get_info(self):
        return f"Name: {self.name}\nDepartment: {self.department}\nSalary: {self.salary}"
    

class Manager(Employee):
    def __init__(self, name, department, salary, team_members):
        super().__init__(name, department, salary)
        self.team_members = team_members
    def get_info(self):
        info = super().get_info()
        info += f"\n{self.team_members}"
        return info
    
class Salesperson(Employee):
    def __init__(self, name, department, salary, commission_rate):
        super().__init__(name, department, salary)
        self.commission_rate = commission_rate
    def get_info(self):
        info = super().get_info()
        info += f"\n{self.commission_rate}"
        return info
    
employee1 = Employee("Furqan Abbass", "Marketing", 50000)
manager1 = Manager("Khalid Nawaz", "Sales", 75000, ["Alice", "Bob"])
salesperson1 = Salesperson("Ijaz Khan", "Sales", 40000, 0.1)

print(employee1.get_info())
print("\n.....\n")
print(manager1.get_info())
print("\n.....\n")
print(salesperson1.get_info())
'''

# Polymorphism
'''
class Complex:
    def __init__(self, real, img) :
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +", self.img,"j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
        
num1 = Complex(5, 4)
num2 = Complex(3, 2)

num3 = num1 + num2
num1.showNumber()
num2.showNumber()
num3.showNumber()
'''

# Encapsulation


class Car:
    def __init__(self, make, model, year) -> None:
        self.__make = make
        self.__model = model
        self.__year = year

    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year
    
    def set_make(self, make):
        return self.__make
    def set_model(self, model):
        return self.__model
    def set_year(self, year):
        return self.__year
    
my_car = Car("Toyota", "Corolla", 2013)

print("Make: ",  my_car.get_make())
print("Model:",  my_car.get_model())
print("Year: ",  my_car.get_year())

my_car.set_make("Honda")
my_car.set_model("Civic")
my_car.set_year(2023)

print("Updated: ", my_car.get_make())
print("Updated: ", my_car.get_model())
print("Updated: ", my_car.get_year())

