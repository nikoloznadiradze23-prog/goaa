start = int(input("enter start number:"))
end = int(input("enter end number:"))
if end < start:
    print("არასწორი შუალედი")
else:
    print("რიცხვები:", list(range(start, end + 1)))
    print("ჯამი:", sum(range(start, end + 1)))

num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
num3 = int(input("enter third number:"))
print("min number:", min(num1,num2,num3))

num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
num3 = int(input("enter third number:"))
num4 = int(input("enter fourth number:"))
print("max number:", max(num1,num2,num3,num4))


list = [12, 32, 54, 56 ,65, 88, 78]
print(len(list))

math1 = float(input("enter your math num: "))
import math
math = math.pow(math1, 2)
print("result:", math)

math1 = int(input("enter your math num: "))
import math
math = math.sqrt(math1)
print("result:", math)

num = float(input("enter your math num: "))
import math
math345 = math.floor(num)
print("result:", math345)
math2 = math.ceil(num)
print("result:", math2)


import random
num = [random.randint(1,50) for nums in range(5)]
print(num)
print(max(num))

import random
import math
num = [random.randint(1, 100) for nums in range(3)]
print("random nums:", num)
for numr in num:
    sqrt = math.sqrt(numr)
    print("result:", sqrt)

import random
randoms = [random.randint(1, 100) for nums in range(5)]
print("random nums:", randoms)
length = len(randoms)
print("length:", length)
total = sum(randoms)
print("nums sum", total)

num1 = int(input("first: "))
num2 = int(input("second: "))
max_nums = max(num1, num2)
print("maxs:", max_nums)


first = int(input("first: "))
second = int(input("second: "))
third = int(input("third: "))
min_value = min(first, second, third)
max_value = max(first, second, third)
print("min:", min_value)
print("max:", max_value)

import math
num = float(input("enter num: "))
cube = math.pow(num, 3)
print("cube:", cube)


