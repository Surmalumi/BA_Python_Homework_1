# 1. Написать цикл для выведения на экран каждой буквы своего ФИО.

#без цикла
#fio = input()
#print(*list(fio), sep='\n')

fio = input()
for letter in fio:
    print(letter)