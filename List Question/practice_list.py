# Q1
fruits = ["apple", "banana", "papaya", "peach", "watermelon"]
print(fruits)


#Q2
num = [2,4,3,5,6,7,]
num_2 = [i **2 for i in num]
print(num_2)


#Q3
cities = ["Indore", "Pune", "Hydrabaad", "Banglore", "Noida"]
print(cities[0])
print(cities[-1])

#Q4
square = [i**2 for i in range(1,11)]
print(square)

#Q5
fruit = ["apple", "banana", "papaya", "peach", "watermelon", "orange", "cherry", "mango"]
for i in range(0, len(fruit)):
    for j in range(i+1, len(fruit)):
        if fruit[i] > fruit[j]:
            fruit[i],fruit[j] = fruit[j],fruit[i]

print(fruit)


#Q6
age = [10,24,35,42,21,18,45,15]
adults = []
for ages in age:
    if ages>=18:
        adults.append(ages)
print(adults)


#Q7
color_1 = ["Red", "Green", "Yellow"]
color_2 = ["Blue", "Black", "White"]
new_Color = color_1 + color_2

print(new_Color)


#Q8
animals = ["cat", "dog", "tiger", "lion", "wolf", "fish"]
animal = "dog"
if  animal in animals:
    animals.remove(animal)
print(animals)


#Q9
numb_1 = [1, 2, 3, 4, 5]
numb_2 = [i **2 for i in numb_1]
sum = 0

for i in numb_2:
    sum+=i
print(sum)


#Q10
char = ["dog", "yellow", "mango", "tomato", 123]
reversed_char = char[::-1]
print(reversed_char)


