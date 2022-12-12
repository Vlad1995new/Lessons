from abc import abstractmethod


class Animal:
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def age(self):
        pass

    @abstractmethod
    def height(self):
        pass

    @abstractmethod
    def weight(self):
        pass

    @abstractmethod
    def country(self):
        pass


class Tiger(Animal):
    @abstractmethod
    def __init__(self, type1="Амурский", age1="8 лет", height1="1.2", weight1="180", country1="Россия"):
        self.age1 = age1
        self.type1 = type1
        self.height1 = height1
        self.weight1 = weight1
        self.country1 = country1

    @abstractmethod
    def type(self):
        print(self.type1 + " тигр")

    @abstractmethod
    def age(self):
        print("Возраст:  " + self.age1)

    @abstractmethod
    def height(self):
        print("Рост в метрах: " + self.height1)

    @abstractmethod
    def weight(self):
        print("Вес: " + self.weight1 + " кг")

    @abstractmethod
    def country(self):
        print("Страна обитания: " + self.country1)


tiger1 = Tiger()
tiger1.type()
tiger1.age()
tiger1.weight()
tiger1.height()
tiger1.country()
