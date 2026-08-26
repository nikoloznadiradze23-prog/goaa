fruits = ["ვაშლი", "ბანანი", "ატამი", "მსხალი", "ალუბალი"]
print(fruits[2])

numbers = [10, 20, 30, 40, 50]
numbers[1] = 25
print(numbers)

colors = ['წითელი', 'მწვანე','ლურჯი', 'ყვითელი', 'იასამნისფერი']
index = int(input("enter your index:"))
print(index)
if index in [0,1,2,3,4]:
    print("your color is:", colors[index])
else:
    print("error")

animals = ['ძაღლი', 'კატა', 'სპილო', 'ვეფხვი', 'ლომი']
animals[4]=("გემი")
print(animals)

colors = ['თეთრი', 'შავი', 'ნარინჯისფერი', 'ვარდისფერი']
index=int(input("მიუითე რიცხვი:"))
new_color=input("შეიყვანე სასურველი ფერი: ")
if index in [0,1,2,3,]:
    print("new color added successfully:",colors)
else:
    print("error")