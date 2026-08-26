def process(word, callback):
    return callback(word)
def to_upper(text):
    return text.upper()
result = process("hello", to_upper)
print(result)

def greet():
    return "Hello World"
def goodbye():
    return "See you next time"
def higher_func(func):
    print(func())
higher_func(greet)
higher_func(goodbye)

words = ["hello", "world"]
upper = list(map(lambda w: w.upper(), words))
print(upper)

nums = [2, 4, 6, 8, 10]
result = list(filter(lambda x: x % 4 == 0, nums))
print(result)

nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 3, nums))
print(result)

data = [("B", 22, 1), ("A", 12, 3), ("C", 14, 2)]
sorted = sorted(data, key=lambda x: x[1])
print(sorted)

def total(price, count):
    return price * count
total_lambda = lambda price, count: price * count
print(total(5, 3))
print(total_lambda(5, 3))