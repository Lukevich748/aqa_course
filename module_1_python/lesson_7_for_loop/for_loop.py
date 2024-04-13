# 1
numbers = []
for number in range(0, 101):
    numbers.append(number)

# 2
while len(numbers) > 51:
    numbers.pop()

# 3
number = 1
while number <= 100:
    if number % 7 == 0:
        print("Первое число, которое делится на 7:", number)
        break
    number += 1