# 1
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())

# 2
with open("userinfo.txt", "a") as file:
    name = str(input("What is your name: "))
    age = int(input("How old are you: "))
    file.write(f"{name}:{age}\n")

# 3
with open("original.txt", "r") as original_file:
    content = original_file.read()

with open("copy.txt", "w") as copy_file:
    copy_file.write(content)