#\*************************/#
#\*******Te3K@_PaynE*******/#
#\**79811131773@yandex.ru**/#
#\*************************/#

'''
Петя и Катя – брат и сестра.
Петя – студент, а Катя – школьница.
Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
'''

# Функция вывода автора программы
def author():
    print('Программа создана:')
    print('Илья "Te3K@_PaynE" Новичихин')
    print('79811131773@yandex.ru')

# Проверка на введение корректного числа.
def correct_number(string):
    _number = int(input(string))
    while (_number > 1000) or (_number <= 0):
        _number = int(input("Введено неверное число! Введите заново: "))
    return _number

print("Программа запрашивает на ввод два положительных натуральных числа.")
print("Показывает два других числа, сумма которых составляет первое введённое число, а произведение - второе")
print("При условии, что такие числа существуют")

_sum_number = correct_number("Введите сумму чисел: ")
_mul_number = correct_number("Введите произведение чисел: ")
for x in range (1, 501):
    y = _sum_number - x
    if (x * y == _mul_number):
        print(f"При сумме чисел {_sum_number} и произведении {_mul_number}")
        print(f"загаданными числами будут: {x} и {y}")
        break
else:
    print(f"При сумме чисел {_sum_number} и произведении {_mul_number}")
    print("Числа не найдены")

author()