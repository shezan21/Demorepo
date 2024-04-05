#Q1


class Shape:  # Step 1
    def area(self):
        return 0
    
class Circle(Shape):  #Step 2
    def __init__(self, radius):
        self.radius = radius

    def area(self):  #Step 3
        return 3.14 * self.radius ** 2
    
radius  = int(input("Enter the radius"))  #Step 4

class Test:
    r = Circle(radius)

    print(r.area())  #Step 5






#Q2


class Vehicle:  #Step 1
    def fuel_efficiency(self):
        return 0

class Car(Vehicle):  #Step 2
    def __init__(self, distance, fuel_consumed):
        self.distance = distance
        self.fuel_consumed = fuel_consumed

    def fuel_efficiency(self):  #Step 3
        return self.distance / self.fuel_consumed

distance = int(input("Enter the distance"))  #Step 4
fuel_consumed = int(input("Enter the fuel consumption"))

class Test:
    car = Car(distance, fuel_consumed)

    print(car.fuel_efficiency())  #Step 5







#Q3


class Animal:  #Step 1
    def sound(self):
        return ""
    
class Dog(Animal): #Step 2 & Step 3
    def sound(self):
        return "Woof! for Dog"

class Cat(Animal): #Step 2 & Step 3
    def sound(self):
        return "Meow! for Cat"
    

class Test:  #Step 4
    dog = Dog()
    cat  = Cat()


    print(dog.sound())  #Step 5
    print(cat.sound())




#Q4


class Person:
    def greet(self):
        return "Hello"
    
class Student(Person):
    def greet(self):
        return "Hi there!"
    
class Test:
    student = Student()

    print(student.greet())




#Q5


class Employee:
    def calculate_salary(self):
        return 0
    
class Manager(Employee):
    def __init__(self, base_salary, bonus):
        self.base_salary = base_salary
        self.bonus = bonus
    def calculate_salary(self):
        return self.base_salary + self.bonus
    
base_salary = int(input("Enter the  base salary"))
bonus = int(input("Enter the bonus"))

class Test:
    salary = Manager(base_salary, bonus)

    print(salary.calculate_salary())
