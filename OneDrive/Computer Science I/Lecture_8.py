groceries = []
groceries.append("milk")
print(groceries)
groceries.append("eggs")
print(groceries)
groceries.append("bread")
print(groceries)

numbers = [10, 30, 40]
numbers.insert(1, 20)
numbers.insert(0, 5)
numbers.append(50)
numbers.extend([60, 70, 80])
print(numbers)

# Case 1:
a = [1, 2]
a.append([3, 4])
# What is a? [1, 2, [3, 4]]
# Case 2:
b = [1, 2]
b.extend([3, 4])
# What is b? [1, 2, 3, 4]
# Case 3:
c = [1, 2]
c.append("hi")
# What is c? [1, 2, "hi"]
# Case 4:
d = [1, 2]
d.extend("hi")
# What is d? [1, 2, "h", "i"]
print(a)
print(b)
print(c)
print(d)

#Extend adds each individual letter in a word

animals = ["cat", "dog", "bird", "dog", "fish"]
animals.remove("bird")
print(animals)
print(animals.pop())
print(animals)
del animals[0]
print(animals)

queue = ["Alice", "Bob", "Charlie", "David", "Eve"]
queue.remove("David")
print(queue)
print(queue.pop(0))
print(queue)
del queue[-1]
print(queue)

scores = [85, 92, 78, 64, 95, 88]

if 100 in scores:
    scores.remove(100)
else:
    print("100 not found")
if len(scores) >= 11:
    scores.pop(10)
else:
    print("Index 10 doesn't exist")
middle = int(len(scores) / 2)
del scores[middle - 1:middle + 1]

print(scores)