class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print("ცხოველი ხმას გამოსცემს")


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def accelerate(self):
        self.speed += 10

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    def info(self):
        print(self.username, self.email)

class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    

class Person:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def spend(self, amount):
        if self.balance >= amount:
            self.balance -= amount


class Logger:
    def log(self, message):
        print("LOG:", message)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def raise_salary(self, percent):
        self.salary += self.salary * (percent / 100)


class Team:
    def __init__(self):
        self.players = []
    def add_player(self, name):
        self.players.append(name)


class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    def is_long(self):
        return self.pages > 300
    


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def transfer(self, other, amount):
        if self.balance >= amount:
            self.balance -= amount
            other.balance += amount


class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
    def average(self):
        return sum(self.scores) / len(self.scores)
    

