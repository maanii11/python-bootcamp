# week 3 assignment
# Python Programming Bootcamp:
# Topics: Sets, Tuples, Lists, Dictionaries
# --- SET QUESTIONS ---
print("--- 1. Set Operations ---")
# Create a set of 5 favorite fruits
fruits = {"Mango", "Banana", "Cherry", "Apple", "Elderberry"}
fruits.add("Dragonfruit")  
fruits.remove("Apple")     
print(f"Final fruit set: {fruits}\n")

print("--- 2. Union and Intersection ---")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}\n")


# --- TUPLE QUESTIONS ---
print("--- 3. Tuple Indexing ---")
numbers_tuple = (10, 20, 30, 40, 50)
print(f"First number: {numbers_tuple[0]}")
print(f"Last number: {numbers_tuple[-1]}\n")

print("--- 4. Sum of Tuple ---")
print(f"Sum of elements: {sum(numbers_tuple)}\n")

print("--- 5. Tuple Immutability ---")
# Attempting to change an element in (1, 2, 3)
try:
    t = (1, 2, 3)
    t[1] = 5
except TypeError as e:
    print(f"Error observed: {e}")
    print("Explanation: Tuples are immutable, meaning their elements cannot be changed after creation.\n")


# --- LIST QUESTIONS ---
print("--- 6. List Modification ---")
cities = ["Tokyo", "Paris", "New York", "London", "Berlin"]
cities.append("Sydney")      
cities.insert(1, "Dubai")    
print(f"Updated city list: {cities}\n")

print("--- 7. Doubling List Elements ---")
nums_list = [2, 4, 6, 8, 10]
for i in range(len(nums_list)):
    nums_list[i] = nums_list[i] * 2
print(f"Doubled list: {nums_list}\n")


# --- DICTIONARY QUESTIONS ---
print("--- 8 & 9. Dictionary Updates ---")
student_marks = {"Math": 85, "Science": 92, "English": 78}
print(f"Science Mark: {student_marks['Science']}")

student_marks["Math"] = 95       # Update marks
student_marks["History"] = 88    # Add new subject
print(f"Updated Dictionary: {student_marks}\n")

print("--- 10. Dictionary Loop ---")
for subject, marks in student_marks.items():
    print(f"{subject}: {marks}")
print("\n")


# --- MINI PROJECT (Week 3): Student Result Manager ---
print("--- Mini Project: Student Result Manager ---")
results = {}
subjects = ["Math", "Science", "English"]

# Take input for 3 subjects
for sub in subjects:
    score = float(input(f"Enter marks for {sub}: "))
    results[sub] = score

# Calculations
total_marks = sum(results.values())
avg_marks = total_marks / len(results)

# Determine Grade
if avg_marks >= 80:
    grade = "Grade A"
elif avg_marks >= 60:
    grade = "Grade B"
else:
    grade = "Grade C"

print(f"\nResults Summary:")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {avg_marks:.2f}")
print(f"Final Status: {grade}")