# Unit 1
# Beginner

rgb_color = (255, 128, 0)
print(rgb_color[0])
print(rgb_color[1])
print(rgb_color[2])
palette = [rgb_color]
print(palette)

# Intermediate

record_1 = ("Alice", 9, 14)
record_2 = ("Bob", 11, 17)
record_3 = ("Charlotte", 12, 18)

classroom = [record_1, record_2, record_3]
print(classroom[1][0])
name = classroom[0][0]
grade = classroom[0][1]
age = classroom[0][2]

print(f"Name:  {name}")
print(f"Grade: {grade}")
print(f"Age: {age}")


# Advanced

student_report = ("George", [70, 90, 80], 80)
student_report[1].append(100)
updated_report = ("George", [70, 90, 80, 100], 85)
print(student_report)
print(updated_report)

# Unit 2
# Beginner

grades = [80, 85, 90]
date = (4, 23, 2026)

def boost_grades(grades):
    for i in range(len(grades)):
        grades[i]+=5


boost_grades(grades)
print(grades)
# The grades need to be changed, so we use a list. The date does not need to change, so we use a tuple.

# Intermediate

def find_range(*scores):
    minimum_value = scores[0]
    maximum_value = scores[0]
    for i in range(len(scores)):
        if scores[i] < minimum_value:
            minimum_value = scores[i]
        elif scores [i] > maximum_value:
            maximum_value = scores[i] 
    return (minimum_value, maximum_value)

test_scores = [78, 92, 85, 88, 91]
print(find_range(80, 75, 90))
print(find_range(95, 68, 83, 70, 93, 88, 75))
print(find_range(*test_scores))
    
# Advanced

def calculate_statistics(*stats):
    count = len(stats)
    total = sum(stats)
    average = total/count
    return (count, total, average)

print(calculate_statistics(12, 5, 7))
    

# Unit 3
#Beginner

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(grid)
print(grid[1][1])

for row in grid:
    print(row)

grades = [45, 78, 92, 61, 88, 73, 55, 90, 82]

passing_grades = [i for i in grades if i >= 60]
letter_grades = ["A" if j >= 90 else "B" if j >= 80 else "C" if j >= 70 else "D" for j in passing_grades]
print(passing_grades)
print(letter_grades)

# Advanced

mult_table = [[i for i in range(1, 5)] for i in range(1, 5)]
for row in mult_table:
    print(row)

def sum_diagonal(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    
    return sum

print(sum_diagonal(mult_table))

evens = (i for j in mult_table for i in j if i % 2 == 0)
evens = list(evens)
for i in range(5):
    print(evens[i])
