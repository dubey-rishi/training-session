# day1.py: Basic Python fundamentals

# 1. Variables and arithmetic
x = 10
y = 5
print('x + y =', x + y)
print('x * y =', x * y)

# 2. Conditionals
if x > y:
    print('x is greater than y')
else:
    print('x is not greater than y')

# 3. Loops
for i in range(1, 6):
    print('i =', i)

# 4. Functions

def square(n):
    return n * n

print('square(7) =', square(7))

# 5. Simple list comprehension
nums = [1, 2, 3, 4, 5]
squares = [n * n for n in nums]
print('squares =', squares)
