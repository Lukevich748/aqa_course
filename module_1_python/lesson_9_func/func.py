# 1
def get_sum_two_numbers(a, b):
    return a + b


def get_max_number_in_list(numbers: list):
    return max(numbers)


def greeting(name):
    return f"Hello {name}!"


greeting_result = greeting(name="Artem")
print(greeting_result)


# 2
def get_movie_ticket(full_name: str, age: int, adult=False):
    if age >= 18:
        return "Билет продан."
    elif adult:
        return "Билет продан под присмотром взрослого."
    else:
        return "Нельзя продать билет."


ticket_result = get_movie_ticket(full_name="Lukevich Artem", age=17, adult=True)
print(ticket_result)


# 3
def get_square_list(numbers: list):
    square_list = [number ** 2 for number in numbers]
    return square_list

