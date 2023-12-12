# Задача №1 (Декоратор времени работы)

# from datetime import time, datetime
#
#
# def working_hours_only(function):
#     def rabota():
#         if 9.00 <= int(datetime.now().strftime('%H')) <= 18.00:
#             function()
#         else:
#             print("Работать нельзя!")
#     return rabota
#
# @working_hours_only
# def work():
#     print("Работаем")
#     return

# work()


# Задача №2(Декоратор проверка типа данных)

def type_check(correct_type):
    def proverka(func):
        def wrapper(object):
            if type(object) == correct_type:
                print(func(object))
            else:
                print("Bad type!")
        return wrapper
    return proverka

@type_check(int)
def times2(num):
    return num*2

@type_check(str)
def first_letter(word):
    return word[0]

@type_check(bool)
def bool_nformation(arg):
    return arg

@type_check(float)
def float_information(inf):
    return inf

times2(15)
times2("2")

first_letter("Hello world")
first_letter(False)

bool_nformation(True)
bool_nformation(1)

float_information(2.5)
float_information(2)