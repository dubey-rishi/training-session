# day2.py: Collections and simple i/o

# 1. Lists and dictionary
students = ['Alice', 'Bob', 'Charlie']
scores = {'Alice': 90, 'Bob': 82, 'Charlie': 77}

for student in students:
    print(student, 'score is', scores[student])

# 2. Tuple and set
point = (4, 5)
unique = set([1, 2, 2, 3, 3, 3])
print('point:', point)
print('unique set:', unique)

# 3. File writing & reading
with open('day2_data.txt', 'w') as f:
    f.write('Hello from day2\n')

with open('day2_data.txt', 'r') as f:
    print('file content:', f.read())

# 4. Exception handling
try:
    print(scores['David'])
except KeyError:
    print('David not found in scores')
