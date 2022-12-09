# Создать класс и вызвать пять объектов этого класса.
class dog:
    def __init__(self, name, name2, height, weight, color):
        self.name = name
        self.name2 = name2
        self.height = height
        self.weight = weight
        self.color = color

    def joke(self):
        if self.height < 40 and self.weight >= 10:
            print(
                self.name + ", у Вас крассивый, " + self.color + " пес, но " + self.name2 + " слишком много ест!")
        else:
            print(self.name + ", у Вас крассивый и вполне здоровый " + self.color + " пес!")


dog1 = dog("Игорь", "Гадзила", 50, 15, "рыжий")
dog1.joke()
dog2 = dog("Варя", "Чарли", 20, 11, "белый")
dog2.joke()
dog3 = dog("Настя", "Дымок", 15, 1.5, "черный")
dog3.joke()
dog4 = dog("Влад", "Принц", 39, 10, "черный")
dog4.joke()
dog5 = dog("Максим", "Гризли", 100, 20, "черно-серый")
dog5.joke()
