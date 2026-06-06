# PYTHON FUNDAMENTALS - PART 2
# Topics: Conditionals, Loops, Functions, Lambda, Recursion

# ============================================
# 1. Conditional Statements
# ============================================
age = 18
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# ============================================
# 2. Practice Examples (Conditionals)
# ============================================
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# ============================================
# 3. Odd or Even
# ============================================
num = 7
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# ============================================
# 4. Nesting
# ============================================
x = 15
if x > 10:
    if x > 20:
        print("x is greater than 20")
    else:
        print("x is between 10 and 20")

# ============================================
# 5. Match Case in Python
# ============================================
day = "Monday"
match day:
    case "Monday":
        print("Start of work week")
    case "Friday":
        print("End of work week")
    case "Saturday" | "Sunday":
        print("Weekend!")
    case _:
        print("Midweek")

# ============================================
# 6. Loops using While
# ============================================
i = 1
while i <= 5:
    print(f"While loop: {i}")
    i += 1

# ============================================
# 7. Practice Examples (Loops)
# ============================================
# Sum of first N numbers using while
n = 10
total = 0
count = 1
while count <= n:
    total += count
    count += 1
print(f"Sum of 1 to {n} = {total}")

# ============================================
# 8. Multiplication Table of N
# ============================================
n = 5
i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1

# ============================================
# 9. Break and Continue
# ============================================
# Break example
for i in range(1, 10):
    if i == 5:
        break
    print(f"Break example: {i}")

# Continue example
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(f"Continue example (odd): {i}")

# ============================================
# 10. Loops using For
# ============================================
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# ============================================
# 11. Vowel Count
# ============================================
string = "Hello World"
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1
print(f"Vowel count in '{string}': {count}")

# ============================================
# 12. range() Function
# ============================================
# range(stop)
for i in range(5):
    print(i, end=" ")
print()

# range(start, stop)
for i in range(2, 8):
    print(i, end=" ")
print()

# range(start, stop, step)
for i in range(0, 20, 4):
    print(i, end=" ")
print()

# ============================================
# 13. Sum of N Numbers
# ============================================
n = 100
total = sum(range(1, n + 1))
print(f"Sum of 1 to {n} = {total}")

# ============================================
# 14. Functions in Python
# ============================================
def greet(name):
    return f"Hello, {name}!"

print(greet("Nishant"))

# ============================================
# 15. Practice Examples (Functions)
# ============================================
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"Is 17 prime? {is_prime(17)}")
print(f"Is 20 prime? {is_prime(20)}")

def find_max(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

print(f"Max of [3,1,9,4,7]: {find_max([3,1,9,4,7])}")

# ============================================
# 16. Types of Functions
# ============================================
# No argument, no return
def say_hello():
    print("Hello!")

# With argument, no return
def print_square(n):
    print(f"Square of {n} = {n**2}")

# With argument, with return
def add(a, b):
    return a + b

# Default argument
def power(base, exp=2):
    return base ** exp

say_hello()
print_square(4)
print(add(3, 5))
print(power(3))      # 9
print(power(3, 3))   # 27

# ============================================
# 17. Lambda Function
# ============================================
square = lambda x: x ** 2
multiply = lambda x, y: x * y
is_even = lambda x: x % 2 == 0

print(f"Square of 5: {square(5)}")
print(f"3 x 4 = {multiply(3, 4)}")
print(f"Is 8 even? {is_even(8)}")

# Lambda with map and filter
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"Squares: {squares}")
print(f"Evens: {evens}")

