student = {
    "name": "niga",
    "hobby": "basketball",
    "height": 2.04,
    "weight": 78,
}

print(student.get("name"))
print(student.pop("height"))
# gets - gamoaq mashi motavsebuli key
# pop - shlis masshimotavsebul key

print(student.keys())
print(student.values())
# keys gamoaqvs monacemebis sataurebi
# values gamoaqvs monacemebis mnishvnelobebi
person = {
    "name": "nig",
    "lastname": "blackson",
    "country": "africa",
}
print(person.items())

animal = {
    "color": "white",
    "type": "bear",
    "place": "antarctica",
}

print(animal.copy())
print(animal.clear())

person.update({
    "age": 14,
})
person.popitem()

numbers = [1, 4, 7, 10, 13, 16, 19]
evens = [num + 1 for num in numbers if num % 2 == 0]
print(evens)

for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print(evens)

new_evens = [num + 1 for i in numbers if num %2 == 0]
print(new_evens)



words = ['apple', 'banana', 'cat', 'elephant', 'dog', 'grapefruit']
for char in words:
    if char in words > 5 :
        print(char)