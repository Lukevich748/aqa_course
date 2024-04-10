# 1
numbers = [1, 2, 3, 4, 5]
print(numbers[2])
numbers.insert(5, 10)
numbers.remove(2)
print(numbers)

# 2
fruits = ["apple", "orange", "banana"]
combined = numbers + fruits
len(combined)
print(combined[-1])
combined_new = combined[1:4]

# 3
combined_copy = combined[:]
combined_copy[0] = "Яблоко"
print(combined, combined_copy)
