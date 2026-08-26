# product = {
#     "apple":[12,5, "2027-05-12"],
#     "cherry":[27,5, "2027-05-12"],
# }

# new_products= filter(lambda key: product[key][0] > 20,product)
# print(list(new_products))


# data = [("A", 2, 3), ("b", 3, 2), ("c", 1, 1)]
# print(sorted(data, key= lambda x: x[1]))


# def mult(n):
#     return lambda a: a * n

# tr = mult(5)
# db = tr(5)
# print(db)

# x = mult(5)
# y = x(5)

# print(y)

def func1():
    print("welcome")
def func2(func):
    return func
x = func2(func1)
print(x)

def func1():
    print(".......")
def func2(func):
    def wrapper():
        print("fnc")
        y = func()
        return y
    return wrapper
x = func2(func1)
print(x)