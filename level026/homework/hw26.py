word = input("enter word:")
print(word.lower())

word1 = input("first word:")
word2 = input("second word:")
print(word1.lower() == word2.lower())

countries = ["georgia", "armenia", "greece", "norway", "denmark"]
for country in countries:
    print(country.lower())

word = input("enter word:")
print(word.upper())

countries = ["georgia", "armenia", "greece", "norway", "denmark"]

for country in countries:
    print(country.upper())

word = input("enter word:")
print(word.isupper())

word = input("enter word: ")
print(word.capitalize())

word = "gEoRGia"
print(word.capitalize())

countries = ["geOrgia", "aRMeNIA", "tUrKey"]

for country in countries:
    print(country.lower().capitalize())
def greetings():
    print("hello")
greetings()


def repeat_word(number, word):
    for i in range(number):
        print(word)

from turtle import *

def draw_square(x, y):
    penup()
    goto(x, y)
    pendown()
    for i in range(4):
        forward(100)
        right(90)
draw_square(0, 0)
done()

def calculate_area(length, width):
    return length * width
area = calculate_area(5, 10)
print("area", area)

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(factorial(5))