numbers = [1, 4, 7, 10, 13, 16, 19]
new_list = []
for num in numbers:
    if num %2  != 0:
        new_list.append(num * 2)
    print(new_list)

numbers = [1, 4, 7, 10, 13, 16, 19]
new_list = [num * 2 for num in numbers if num % 2 != 0 ]
print(new_list)

numbers = [2,4,6,9,2,34,12]
new_list = [num for num in numbers if num / 3 != 0]
print(new_list)
numbers = [4,5,2,12,15,26,37]
new_list = [num * 2 for num in numbers if num % 2 != 0]
print(new_list)

words = ['apple', 'banana', 'cat', 'elephant', 'dog', 'grapefruit']
new_words = []
for char in words:
    if len(char) >= 5:
        new_words.append(char)
    print(new_words)

words = ['apple', 'banana', 'cat', 'elephant', 'dog', 'grapefruit']
new_words = [char for char in words if len(char) >= 5]
new_words.append(char)
print(new_words)


nums = list(range(1, 21))
squares = []
for n in nums :
    squares.append(nums ** 2)
print(squares)

nums = list(range(1, 21))
squares = [n ** 2 for n in nums ]
print(squares)


mixed = [2, 5, 8, 11, 14, 17, 20]
numr = [num for num in mixed if num % 2 == 0]
print(numr)
numrs =[num for num in mixed if num % 2 != 0]
print(numrs)

animals = ['tiger', 'lion', 'zebra', 'elephant', 'giraffe']
first_letters = []
for animal in animals:
    first_letters.append(animal[0])
print(first_letters)  

animals = ['tiger', 'lion', 'zebra', 'elephant', 'giraffe']
first_letters = [animal[0] for animal in animals]
print(first_letters) 

animals = ['tiger', 'lion', 'zebra', 'elephant', 'giraffe']
e = [animal for animal in animals if animal.startswith('e')]
print(e)  


my_list = [5, 10, 15]
try:
    print(my_list[5])
except IndexError:
    print("error")

