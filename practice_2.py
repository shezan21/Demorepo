# Q1
print("Python"[:3])

# Q2
print("Programming"[9:11])

#Q3
print("HelloWorld"[2:6])

#Q4
print("Education"[1::2])

#Q5
print("Hello"[::-1])

#Q6
print("JavaScript"[0] + "JavaScript"[-1])


#Q7
if "Python" in "I love Python Programming":
    print("Yes 'Python is a substring of' I love Python Programming'")
else:
    print("No 'Python is not a substring of' I love Python Programming'")


#Q8
x = "Welcome to Python"
print(x.split())

#Q9
s  = "Coding is Fun"
print(s.replace("o", "a"))


#Q10
print("HelloWorld"[-6:-3])

#Q11
x = "HelloWorld"
for char in reversed(x):
    print(char)


#Q12
text = "Python Programming"
words = text.split()
for i in words:
    first_word = i[:2]
    last_word = i[-2:]
    print(first_word + last_word, end=" ")




#Q13
g = "racecar"
l = g[::-1]

if g == l:
    print("l is a plaindrome character")
else:
    print("l is not a plaindrome character")
