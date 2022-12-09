# Написать функцию, которая просит ввести имя и выводит на экран "Привет и введённое имя".
# Далее написать к функции декоратор, который изменяет функцию и переводит имя в заглавные буквы.
def decorator(func):
    def wrapper(peremen):
        name_up = func(peremen.upper() + "!!")
        return name_up

    return wrapper


@decorator
def hello(name):
    return "Привет " + name + "!"


print(hello(input("Введите имя: ")))
