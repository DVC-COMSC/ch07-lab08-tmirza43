# ******************************
# Make your Code
# ******************************

numbers = input("Enter 5 int in ascending order: ").split()
numbers = list(map(int, numbers))
new = int(input("Enter another value: "))

for i in range(5):
  if numbers[i] > new:
    numbers.insert(i, new)
    break

print(numbers)