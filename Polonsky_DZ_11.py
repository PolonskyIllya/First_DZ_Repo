# Задача №1

# class Publication:
#     def __init__(self, title, author, year, public_forbes):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.public_forbes = public_forbes
#     def imya(self):
#         print(f'Имя издательства: {self.public_forbes}')
#     def display(self):
#         print(f' Заголовок: {self.title}\n Автор: {self.author}\n Год выпуска: {self.year}')
#
# class Book(Publication):
#     def __init__(self, title, author, year, public_forbes, isbn):
#         super().__init__(title, author, year, public_forbes)
#         self.isbn = isbn
#
#     def imya(self):
#         super().imya()
#
#     def display(self):
#         super().display()
#         print(f'isbn: {self.isbn}')
#
# class Magazine(Publication):
#     def __init__(self, title, author, year, public_forbes, issue_number):
#         super().__init__(title, author, year, public_forbes)
#         self.issue_number = issue_number
#
#     def imya(self):
#         super().imya()
#
#     def display(self):
#         super().display()
#         print(f'issue_number: {self.issue_number}')
#
# seven_days = Book('Begin', 'DJ Smash', 2023, 'Lost', isbn=23)
# seven_days.imya()
# seven_days.display()
# seven_days = Magazine('Moon', 'Frank Yuss', 1898, 'Cosmic show', 77)
# seven_days.imya()
# seven_days.display()

# Задача №2

class BankAccount:
    def __init__(self, balance, interest_rate,transactoins):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append({amount})
        print(f"Зачислено на депозит: {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append({amount})
        print(f"Списано с депозита: {self.balance}")

    def add_interest(self):
        percent = self.balance*self.interest_rate/100
        self.balance += percent
        self.transactions.append({self.balance})
        print(f"Процент по депозиту: {self.balance}")

    def history(self):
        for transactions in self.transactions:
            print(transactions)

account = BankAccount(100000, 0.5, 0)
account.deposit(15000)
account.withdraw(7500)
account.add_interest()
account.history()
print(f"Баланс:{account.balance}")