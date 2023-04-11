#\*************************/#
#\*******Te3K@_PaynE*******/#
#\**79811131773@yandex.ru**/#
#\*************************/#

'''
 На столе лежат n монеток.
 Некоторые из них лежат вверх решкой, а некоторые – гербом.
 Определите минимальное число монеток, которые нужно перевернуть,
 чтобы все монетки были повернуты вверх одной и той же стороной.
 Выведите минимальное количество монет, которые нужно перевернуть
'''
import random

# Функция вывода автора программы
def author():
    print('Программа создана:')
    print('Илья "Te3K@_PaynE" Новичихин')
    print('79811131773@yandex.ru')


print("Программа запрашивает количество монет на столе.")
print("После программа случайным образом задаёт, сколько монет лежат решкой (0) или орлом (1)")
print("Программа показывает, какое количество монет нужно перевернуть, чтобы все они лежали одноай стороной.")

_number_coins = int(input("Введите количество монет на столе: "))
_reshka = 0
_orel = 0
_str_coins = ""

for i in range(_number_coins):
    _coins = random.randint(0, 1)
    if (_coins == 0):
        _reshka += 1
    else:
        _orel += 1
    _str_coins += str(_coins) + " " 

print(_str_coins)
if (_reshka > _orel):
    print(f"Нужно перевернуть монеты с орлом в количество {_orel} штук")
else:
    print(f"Нужно перевернуть монеты с решкой в количество {_reshka} штук")

author()