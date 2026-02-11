
# Part A: Variables & Data Types

print("----- Part A -----")

# Q1
name = "Abdur Rehman"
print("Q1:", name)

# Q2
age = 20
height = 5.8
print("Q2: Age =", age, ", Height =", height)

# Q3
num = 10
print("Q3: Data type of num =", type(num))

# Q4
is_student = True
print("Q4:", is_student)

# Q5
number = input("Q5: Enter a number: ")
print("You entered:", number)

# Part B: Operators & Conditional Statements

print("\n----- Part B -----")

# Q6
num1 = int(input("Q6: Enter first number: "))
num2 = int(input("Q6: Enter second number: "))
print("Sum =", num1 + num2)

# Q7
num1 = int(input("Q7: Enter first number: "))
num2 = int(input("Q7: Enter second number: "))

if num1 > num2:
    print(num1, "is greater")
else:
    print(num2, "is greater")

# Q8
num = int(input("Q8: Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Q9
marks = int(input("Q9: 65: ") or 0)

if marks >= 50:
    print("Pass")
else:
    print("Fail")

# Q10
num = int(input("Q10:12 ") or 0)

if num < 10:
    print("Less than 10")
elif num == 10:
    print("Equal to 10")
else:
    print("Greater than 10")
# Mini Project

print("\n----- Mini Project: Positive or Negative -----")

num = int(input("Enter a number: "))

if num >= 0:
    print("Positive number")
else:
    print("Negative number")
