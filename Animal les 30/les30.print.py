from les29 import Animal, Sex, Weight, _Eat

print("Укажите имя, возраст и происхождение вашего домашнего животного.",
      "Если есть вопросы по поводу: веса, пола или питания введите дополнительный пункт.",
      sep='\n')
# Animal1 = Animal("Кузя", "10 лет", "кот")
# Animal1._otvet()
# Animal2 = Animal("Тузик", "2 года", "собака")
# Animal2._otvet()
# Animal3 = Sex("Скалка", "3 года", "кошка", "девочка")
# Animal3._otvet()
# Animal3.kabinet()
# Animal4 = Weight("Скалка", "3 года", "кошка", "4")
# Animal4._otvet()
# Animal4.kabinet2()
# Animal5 = _Eat("Скалка", "3 года", "кошка", "питание")
# Animal5._otvet()
# Animal5._Eat__num()
Animal6 = Sex("Кузя")
Animal6._otvet()
Animal6.kabinet()
Animal6 = Sex("Скалка", "3 года", "кошка", "девочка")
Animal6._otvet()
Animal6.kabinet()
