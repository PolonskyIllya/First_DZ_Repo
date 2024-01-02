# Задача №1(Итератор)
# class CardDeck:
#     def __init__(self):
#         self.length = 52
#         self.index = 0
#         self.__SUITS = ['Пик', 'Бубей', 'Червей', 'Крестей']
#         self.__RANKS = [*range(2, 11), 'J', 'Q', 'K', 'A']
#
#     def __next__(self):
#         if self.index < self.length:
#             s = self.__SUITS[self.index // len(self.__RANKS)]
#             r = self.__RANKS[self.index % len(self.__RANKS)]
#             self.index += 1
#             return (f'{r} {s}')
#         else:
#             raise StopIteration
#
# deck = CardDeck()
# while True:
#     print(next(deck))


# Задача №2(Генератор)

def fib(n):
    num1, num2 = 1, 1
    for i in range(n):
        num1, num2 = num2, num1 + num2
        yield num1


print(list(fib(int(input("Введите число")))))
