#Q1

class BankAccount: # create a new class

    # Attribute or Variables
    account_number = 0
    balance = 0.0

    # Constructor or methods
    def deposit(self, amount):
        self.balance+=amount
    
    def withdraw(self, amount):
        self.balance-=amount

    def get_balance(self):
        return self.balance
    
class ATM: # create a Object
    SBI = BankAccount()
    SBI.deposit(20000)
    SBI.withdraw(3000)
    print("The Current SBI balance is:", SBI.get_balance())

    ICICI = BankAccount()
    ICICI.deposit(4500)
    print("The Current ICICI balance is:", ICICI.get_balance())

    HDFC = BankAccount()
    HDFC.deposit(1200000)
    HDFC.withdraw(10000)
    print("The current HDFC balance is:", HDFC.get_balance())




#Q2

class Rectangle:
    length = 23
    width = 6.5

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2*(self.length + self.width)
    
class Test:
    rect1 = Rectangle()

    area1 = rect1.area()
    peri1 = rect1.perimeter()

    print(area1)
    print(peri1)




#Q3


class NumberChecker:

    def is_even(self):
        if self.number % 2 == 0:
            return True
        else:
            return False
        
num = int(input("Entr the number"))
if num %2 == 0:
    print("Even number")
else:
    print("Odd number")





#Q4

class TemperatureConverter:

    # method
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
    
temp = float(input("Enter the temperature"))
unit = input("Convert to °F or °C")

if unit == "F":
    print(temp,"°C is", TemperatureConverter.celsius_to_fahrenheit(temp),"°F")

elif unit == "C":
    print(temp,"°F is", TemperatureConverter.fahrenheit_to_celsius(temp),"°C")

else:
    print('Invalid unit')








#Q5

class Person:
    def __init__(self, name, age): # Constructor

        self.name = name
        self.age = age

    def greet(self):
        print("Hello, My name is ", self.name)
        print(" I'm ", self.age, "years old")

class Test:
    John = Person("Jhon", 21)
    Satyarth = Person("Satyarth", 25)
    Priyanka = Person("Priyanka",19)
    
    John.greet()
    Satyarth.greet()
    Priyanka.greet()