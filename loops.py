# for loop
for i in range(5):
    if i == 3:
        continue
    print(i)
# for loop with else
for i in range(5):
    if i == 3:
        continue
    print(i)
# list of fruits
fruits = ["apple", "banana", "cherry", "date"]
# for loop with list
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)
# for loop with range and list
for i in range(len(fruits)):
    if fruits[i] == "banana":
        continue
    print(fruits[i])
