# 1
num = int(input("Введите число: "))

if num > 0:
    print(f"Число {num} положительное")
else:
    print(f"Число {num} отрицательное")

if num < 0:
    print(f"Число {num} отрицательное")
elif num == 0:
    print(f"Число равно {num}")
elif 0 < num < 10:
    print(f"Число от 1 до 9")
else:
    print(f"Число 10 и больше")

# 2
is_raining = False
is_sunny = True

if is_raining and is_sunny:
    print("Двойка вариантов, проверьте погоду!")
elif is_raining or is_sunny:
    print("У нас хорошая погода!")
elif not is_raining:
    print("У нас солнечная погода!")