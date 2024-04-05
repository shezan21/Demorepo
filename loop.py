# Q1: Print the first 10 natural number using while loop.
# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1



# Q2: Calculate the sum of all numbers from 1 to a given number

# num = int(input("Enter number"))
# sum = 0
# for i in range(1, num + 1):
#     sum += i
#     i = i + 1
# print("Sum is:", sum)


# Q3: Write a program ro find those number which are divisible by 7 and multiple of 5 between 1500 and 2700.
# for i in range (1500, 2700):
#     if i %7 ==0 and i %5 ==0:
#         print(i)

# Q4: Write a program to print multiplication table of a given number.

# num = int(input("Enter number"))
# for i in range(1,11):
#     product = num * i
#     i = i + 1
#     print(product)

'''
Q5: Write a program to display only those no. [12,75,150,180,145,525,50] from a list that satisfy the following conditions.
    a) If the no. is greater than 500, then stop the loop.
    b) If the no. is greater than 150, then skip it and move to the next no.
    c) The no. must be divisible by 5.
     
'''  

# num = [12, 75,150,180,145,525,50]

# for item in num:
#     if item > 500:
#         break
#     elif item > 150:
#         continue
#     elif item % 5 == 0:
#         print(item)

# Q6: Write a program to count the total number of 7586978 in a no. using while loop
        
# num = 7586978
# count = 0
# while num!= 0:
#     num = num // 10
#     count = count + 1
# print("Total digits are :", count)



# WAP and print triangles.
for i in range(1,11):
    for j in range(1, i+1):
        print("*", end= " ")
    print()







for i in range(10,0, -1):
    for j in range(1, i+1):
        print("*", end= " ")
    print()