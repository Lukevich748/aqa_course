# 1
def get_sum_two_numbers(a, b):
    return a + b


def get_max_number_in_list(numbers: list):
    return max(numbers)


def greeting(name):
    return print(f"Hello {name}")


# 2
def get_movie_ticket(full_name: str, age: int, adult=False):
    if age >= 18:
        print(f"{full_name}, Билет продан")
    elif adult:
        print(f"{full_name}, Билет продан под присмотром взрослого")
    else:
        print(f"{full_name}, Нельзя продать билет")


# 3
def get_square_list(numbers: list):
    square_list = [number ** 2 for number in numbers]
    return square_list
