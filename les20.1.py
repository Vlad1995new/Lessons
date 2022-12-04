# Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.
filename = "les20.1.txt"
spisok = list()
n = int(input("Введите количество строк вводимого текста: "))
for i in range(n):
    stroka = input("Введите строку " + str(i + 1) + ": ")
    spisok.append(stroka + "\n")
with open(filename, "w", encoding='utf-8') as file:
    for stroka in spisok:
        file.write(stroka)
