# Создайте класс на тему животных. В классе должен присутствовать конструктор не менее трёх методов.
class Animal:
    def __init__(self, name, age, who):
        self.name = name
        self.age = age
        self.who = who

    def otvet(self):
        if int(self.age[0:2]) >= 10:
            print(
                self.name + ", с Вами уже " + self.age + ". Советуем пройти бессплатный профилактический медосмотр в нашей клинике!")
        else:
            print(
                self.name + ", с Вами уже " + self.age + ". Советуем кормить 6 раз в день не большими порциями и выгуливать минимум 1 раз в день")


# В класс из предыдущего урока добавьте три класса-наследника на ваше усмотрение.
class Sex(Animal):
    def __init__(self, name, age, who, sex):
        super().__init__(name, age, who)
        self.sex = sex

    def kabinet(self):
        if str(self.sex) == "мальчик":
            print("За консультацией обратитесь в 807 кабинет")
        else:
            print("За консультацией обратитесь в 808 кабинет")


class Weight(Animal):
    def __init__(self, name, age, who, weight):
        super().__init__(name, age, who)
        self.weight = weight

    def kabinet2(self):
        if str(self.who) == "кот" and int(self.weight) > 5 or str(self.who) == "кошка" and int(self.weight) > 5:
            print("У вашего питомца лишний вес, обратитесь в 805")
        elif str(self.who) == "пёс" and int(self.weight) > 10 or str(self.who) == "сабака" and int(self.weight) > 10:
            print("У вашего питомца лишний вес, обратитесь в 804")
        else:
            print("У вашего питомца нет лишнего веса")


class Eat(Animal):
    def __init__(self, name, age, who, eat):
        super().__init__(name, age, who)
        self.eat = 'питание'

    def num(self):
        print("Для получения дополнительной информации о рационе своего питомца позвоните по номеру +374 хх ххх хх хх")
