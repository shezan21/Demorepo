#Q1


# class Student:
#     def __init__(self, n, a, r, m, g):
#         self.name = n
#         self.age = a
#         self.roll_number = r
#         self.major = m
#         self.GPA = g

#     name = ""
#     age = 0
#     roll_number = 0
#     major = ""
#     GPA = 0

#     def printGPA(self):
#         print(f"The current GPA is : {self.GPA}")



# class Undergraduate(Student):
#     def __init__(self, n, a, r, m, g, y):
#         super().__init__(n, a, r, m, g)
#         self.year = y

#     year = 0

# class Graduate(Student):
#     def __init__(self, n, a, r, m, g, t):
#         super().__init__(n, a, r, m, g)
#         self.thesis = t

#     thesis = ""

# class Test:
#     studennt_1 = Graduate("Danny", 26, 241563, "Psy", 7.42, "Doctoral")
#     student_2 = Undergraduate("Rahul", 27, 475412, "B.Tech", 6.51, "IoT")

#     studennt_1.printGPA()
#     student_2.printGPA()






#Q2


# class Vehicle:
#     def __init__(self, make, model, year, color, price):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color
#         self.price = price
    

#     make = ""
#     model = ""
#     year = 0
#     color = ""
#     price = 0

#     def printPrice(self):
#         print(f"The current price is : {self.price}")

# class Car(Vehicle):
#     def __init__(self, make, model, year, color, price, seat):
#         super().__init__(make, model, year, color, price)
#         self.seat = seat

#         seat = 0

# class Motorcycle(Vehicle):
#     def __init__(self, make, model, year, color, price, engine_size):
#         super().__init__(make, model, year, color, price)
#         self.engine_size = engine_size

#         engine_size = 0

# class Test:
#     car1 = Car("Tata", "Nexon", 2024, "Balck", 18000, 5)
#     motercycle1 = Motorcycle("Kawasaki", "Ninja", 2023, "Green", 850000, "1043 cc")

#     car1.printPrice()
#     motercycle1.printPrice()



#Q3


# class Furniture:
#     def __init__(self, material, color, dimensions, price):
#         self.material = material
#         self.color = color
#         self.dimensions = dimensions
#         self.price = price

#     material = ""
#     color = ""
#     dimensions = ""
#     price = 0

#     def printPrice(self):
#         print(f"The current price is : {self.price}")

# class Table(Furniture):
#     def __init__(self, material, color, dimension, price, legs):
#         super().__init__(material, color, dimension, price)
#         self.legs = legs

#         legs = 0

# class Chair(Furniture):
#     def __init__(self, material, color, dimension, price, height):
#         super().__init__(material, color, dimension, price)
#         self.height = height

#         height = 0

# class Test:
#     table1 = Table("Wooden", "White", "10 x 10 x 10 cm", 10000, 4)
#     chair1 = Chair(" PU leather", "Black & Red", "134 x 66 x 52 cm", 8000, "135 cm")

#     table1.printPrice()
#     chair1.printPrice()




#Q4


# class Animal:
#     def __init__(self, species, age, diet, habitat, population):
#         self.species = species
#         self.age = age
#         self.diet = diet
#         self.habitat = habitat
#         self.population = population
    
#     def printPopulation(self):
#         print(f"Total population is : {self.population}")

# class Mammal(Animal):
#     def __init__(self, species, age, diet, habitat, population, fur):
#         super().__init__(species, age, diet, habitat, population)
#         self.fur = fur
        
#         fur = ""

# class Bird(Animal):
#     def __init__(self, species, age, diet, habitat, population, feathers):
#         super().__init__(species, age, diet, habitat, population)
#         self.feathers = feathers
        
#         feathers = ""

# class Test:
#     mammal1 = Mammal("Wolf", 21, "bison", "Forest", 7500, "White")
#     bird1 = Bird("Golden Eagle", 40, "Fish", "GrassLand", 170000, "Golden-Buff")

#     mammal1.printPopulation()
#     bird1.printPopulation()




#Q5

class Employee:
    def __init__(self, name, age, position, department, salary):
        self.name = name
        self.age = age
        self.position = position
        self.department = department
        self.salary = salary

    def printSalary(self):
        print("The salary is :", self.salary)

class SoftwareEngineer(Employee):
    def __init__(self, name, age, position, department, salary, programminglanguages):
        super().__init__(name, age, position, department, salary)
        self.programminglanguages = programminglanguages

        programminglanguages = ""

class MarketingSpecialist(Employee):
    def __init__(self, name, age, position, department, salary, marketingtools):
        super().__init__(name, age, position, department, salary)
        self.marketingtools = marketingtools
        
        marketingtools = ""

class Test:
    employee1 = SoftwareEngineer("Armaan", 29, "Software Engineer", "IT", 300000, "Python, JavaScript, HTML, CSS")
    employee2 = MarketingSpecialist("Kabir", 30, "Marketing Specialist", "Marketing", 200000, "Google, Facebook, Instagram")

    employee1.printSalary()
    employee2.printSalary()
