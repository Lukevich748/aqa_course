# 1
def average_word_length(sentence):
    words = sentence.split()
    total_chars = sum(len(word) for word in words)
    return total_chars / len(words) if len(words) > 0 else 0


# 2
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Функция будет выполнена сейчас.")
        func(*args, **kwargs)
    return wrapper


# 3
def longest_word(words_list: list):
    return max(words_list, key=len)


# 4
def most_common_element(elements_list: list):
    return max(elements_list, key=elements_list.count)


# 5
def palindrome(string: str):
    return "Palindrome" if string == string[::-1].lower() else "No Palindrome"
