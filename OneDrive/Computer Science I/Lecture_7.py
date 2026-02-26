colors = ["red", "blue", "yellow"]
numbers = [10, 20, 30]
print(colors)
print(numbers)

temps = [72,75,78]
temps[0] = 70
print(temps)
#word = "Hello"
#word[0] = "J"
#There is an error because strings cannot be changed

animals = ["cat", "dog", "bird", "fish", "hamster"]
print(animals[0])
print(animals[-1])
print(len(animals))

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
months[1] = "February"
print(len(months))
print(months[len(months) // 2])
print(months[-1])
print(months[len(months) -1])

data = [100, 200, 300]
empty = []
if data:
    print(data[0])
if empty:
    print(empty[0])
else:
    print("List is empty")
temp = data[0]
data[0] = data[-1]
data[-1] = temp
print(data)