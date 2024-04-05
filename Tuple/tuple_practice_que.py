#Q1
fruits = ("apple", "fig", "banana", "papaya", "watermelon", "strawberry", "peach")
fruit_char = [fruit for fruit in fruits if len(fruit) > 5] 
print(fruit_char)



#Q2
number = (221, 54, 63, 75, 63, 57, 6310, 63)
count_num = number.count(63)
print("The element 63 appears", count_num, "time in the tuple" )



#Q3


#Q4
my_tuple = (221, 54, 63, 75, 63, 57, 635, 6310)

first_element = my_tuple[0]
fourth_element = my_tuple[4]
last_element = my_tuple[-1]

print(first_element)
print(fourth_element)
print(last_element)


#Q5

tuple_1 = ("apple", "banana", "orange")
tuple_2 = ("mango", "papaya", "peach")

new_tuple = tuple_1 + tuple_2
print(new_tuple)


#Q6
char = ((2, 'banana'), (1, 'apple'), (4, 'orange'), (3, 'grape'))
char_1 = list(char)
for i in range(0, len(char_1)):
    for j in range(i +1, len(char_1)):
        if char_1[i] > char_1[j]:
            char_1[i], char_1[j] = char_1[j], char_1[i]
print(char_1)





#Q7 Check if all elements in a tuple are of the same data type.

tuple_4 = (1,2,3,4,5)
tuple_5 = (24.5,65,97,60,43)

if all(isinstance(element, type(tuple_4[0])) for element in tuple_4):
    print("All elements in tuple_4 are of the same data type")

elif all(isinstance(element, type(tuple_5[0])) for element in tuple_5):
    print("All elements in tuple_5 are of the same data type")
else:
    print("Not all elements in tuple_4 and tuple_5 are of the same data type")


#Q8

table = (50,12,27,60,98,105)
avg_table = [element for element in table if isinstance(element, (int, float))]
if sum(avg_table)/len(avg_table):
    print(sum(avg_table)/len(avg_table))
else:
    print(0)    



#Q9

my_tuple = (1, 2, 3)
my_list = list(my_tuple)

my_list = [1, 2, 3]
my_tuple = tuple(my_list)

print(my_list)
print(my_tuple) 



#Q10

tuple1 = ("apple", "banana", "orange","mango", "papaya", "peach")

new_tuple1 = tuple1[0], tuple1[-1]

print(new_tuple1)
