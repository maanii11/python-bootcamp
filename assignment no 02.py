# Q1.
print("Q1:")
for i in range(1, 11):
    print(i)

# Q2. 
print("\nQ2:")
for i in range(2, 21, 2):
    print(i)

# Q3. 
print("\nQ3:")
for char in "Python":
    print(char)

# Q4. 
print("\nQ4:")
for i in range(5, 0, -1):
    print(i)

# Q5. 
print("\nQ5:")
num = 1
while num <= 5:
    print(num)
    num += 1
    # Q6. 
def say_hello():
    print("Hello Python")

# Q7. 
def print_number(n):
    print(n)

# Q8.
def print_sum(a, b):
    print(a + b)

# Q9. 
def check_even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

# Q10. 
def print_one_to_five():
    for i in range(1, 6):
        print(i)

# Task:
def generate_table(number):
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

# Example 
print("\nMini Project (Table of 3):")
generate_table(3)
