from les29 import Animal, Sex, Weight, Eat

print("Укажите имя, возраст и происхождение вашего домашнего животного.",
      "Если есть вопросы по поводу: веса, пола или питания введите дополнительный пункт.",
      sep='\n')
Animal1 = Animal("Кузя", "10 лет", "кот")
Animal1.otvet()
Animal2 = Animal("Тузик", "2 года", "собака")
Animal2.otvet()
Animal3 = Sex("Скалка", "3 года", "кошка", "девочка")
Animal3.otvet()
Animal3.kabinet()
Animal4 = Weight("Скалка", "3 года", "кошка", "4")
Animal4.otvet()
Animal4.kabinet2()
Animal5 = Eat("Скалка", "3 года", "кошка", "питание")
Animal5.otvet()
Animal5.num()
