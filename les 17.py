str1 = input('введите любую строку: ')
str2 = []
for i in range(len(str1)):
    if str1[i] not in str2:
        str2 += (str1[i],)
print(str2)
str2 = tuple(str2)
print(str2)
