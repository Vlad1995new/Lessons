# В текстовый файл построчно записаны фамилия и имя каждого учащегося класса и их оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов, и посчитать средний балл по классу.
scores = 0
n = 0
scores_all = 0
with open("les20.txt", "r", encoding="utf-8") as text:
    for line in text:
        scores = int(line.replace('\n', '')[-1])
        scores_all += scores
        n += 1
        if scores < 3:
            print("оценка меньше 3 баллов: ", line)
print("Средний балл учащихся: ", scores_all / n)
