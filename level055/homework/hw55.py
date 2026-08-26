# class Mathutilis():
#     @staticmethod
#     def add(a, b):
#         return a+b

class UserCounter:
    total_users = 0

    @classmethod
    def create_user(cls):
        cls.total_users += 1


class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    def show_balance(self):
        print(self._balance)


class SecureData:
    def __init__(self, password):
        self.__password = password
    def check_password(self, pwd):
        return self.__password == pwd
    

class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    

class Library:
    def __init__(self, books, secret_code):
        self._books = books
        self.__secretCode = secret_code
    @staticmethod
    def calculate_fine(days_late, rate_per_day):
        return days_late * rate_per_day
lib = Library(["Book1", "Book2"], "XYZ123")
print(Library.calculate_fine(5, 2))