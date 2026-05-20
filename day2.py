#1)
name = input("Enter the name of the Student: ")
s_class = int(input("Enter the class of the Student: "))
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks of subject {i}: "))
    marks.append(mark)
    total_marks = sum(marks)
    percentage = (total_marks / 500) * 100
print(f"Name of the Student is: {name}, class : {s_class} and percentage is: {percentage}")
#2.
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
result = str1 + " " + str2
combined = result
print("\nCombined String:", combined)
print("\nlower() :", combined.lower())
print("upper() :", combined.upper())
print("title() :", combined.title())
print("swapcase() :", combined.swapcase())
print("capitalize() :", combined.capitalize())
print("casefold() :", combined.casefold())
print("center(50) :", combined.center(50))
print("count('a') :", combined.count('a'))
print("endswith('a') :", combined.endswith('a'))
print("find('a') :", combined.find('a'))
print("isalnum() :", combined.isalnum())
print("isdigit() :", combined.isdigit())
print("isnumeric() :", combined.isnumeric())
print("isspace() :", combined.isspace())
print("replace('a', '@') :", combined.replace('a', '@'))
#3.
a = 10
b = 5
print("Initial value of a:", a)
print("initial value of b:",b)
a += b
print("After a += b :", a)
a -= b
print("After a -= b :", a)
a *= b
print("After a *= b :", a)
#4.
if percentage >= 60:
    print("Grade A")
elif percentage >= 50 and percentage < 60:
    print("Grade B")
elif percentage >= 40 and percentage < 50:
    print("Grade C")
elif percentage >= 33 and percentage < 40:
    print("Grade D")
else:
    print("Fail")
