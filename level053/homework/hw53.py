def numbers(*args):
    return sum(args)
print(1,2,3,4,3,2,1)

def argrr(*args):
    return "".join(args)
print("hello","whats good")

def info(**kwargs):
    print(f"name: {kwargs.get('name')}, age: {kwargs.get('age')}")

def car(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def decorator(func):
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return wrapper


def multi(*args):
    result = 1
    for num in args:
        result *= num
    return result
print(multi(2, 3, 4))


def minmax(*args):
    return min(args), max(args)
print(minmax(-5, 4, -3, 2, -1))
