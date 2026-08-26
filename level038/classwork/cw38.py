


# my_car = {
#     "brand": "range rover",
#     "type":"suv",
#     "year":2014,
#     "price":50000,
#     "hp":540,
#     "sold": False
# }
# print(my_car["hp"])

# my_car.update({
#     "price":55000,
#     "color":"black"
# })

# print(my_car)

# new_car=my_car.copy




# person = {
#     "name":"name",
#     "last name":"lname",
#     "age":17,
#     "height":1.84,
#     "hobby":"reading",
#     "weight":78,
#     "isfree": False,
# }
# print(person("name"))

# person.clear()
# print(person)
# person.update({
#     "age":18
# })
# person.pop("hobby")
# person.popitem()
# print(person.key())
# print(person.items())
# print(person.keys())
# persons = person.copy()



# for key,value in person.items():
#     print(f"key: {key}, value: {value}")



nums = [54, 25, 24, 26, 63, 45, 16, 37]
evens = [num + 1 for num in nums if num % 2 == 0]
print(evens)

for num in nums:
    if num % 2 == 0:
        evens.append(num)
print(evens)

new_evens = [num + 1 for i in nums if num % 2 == 0]
print(new_evens)

numr = [num + 4 for i in range(1,11) if num % 4 == 0]
print(numr)
numbr = [num +3 for i in range(1,11) if num % 3 == 0]
print(numbr)