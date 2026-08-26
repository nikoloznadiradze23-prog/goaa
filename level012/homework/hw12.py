# 2) გააკეთეთ 5-5 მაგალითი თთოეულ შედარების ოპერატორზე (>, >=, <, <=, ==, !=), გვერდზე კომენტარის საშვალებით მიუთითეთ თუ რომელ boolean მნიშვნელობას გამოიტანას, აიღეთ მრავალფეროვანი კომბინაციები, შეეცადეთ გქონდეთ ყველა ვარიანტი
print(5 > 2)  # true
print(35 < 44)# true
print(423 > 442)# false
print(89 > 97)# false
print(24 < 43)# true

print(9 >= 8)# true
print(54 >= 23)# true
print(23 >= 55)# false
print(43 >= 76)# false
print(4556>= 865)# true

print(3 < 25)# true
print(744 < 3466)# true
print(23 < 7)# false
print("html" < "py")# true
print(43 < 55)# true

print(89 <= 95)# true
print(409 <= -87)# false
print(12 <= 75)# true
print(-756 <= 34)# false
print(43 <= 55)# true

print(3 == 25)# false
print("Goa" == "best_academy") # true
print(23 == 75)# false
print(45 == 45)# true
print(43 == 55)# false


print(-39 != 5)# true
print(45 != -90)# true
print(85 != 85)# false
print("step it" != "best_academy") # true
print(-84 != 85)# true


#  შექმენით 5 ცვლადი, რომლებშიც შეინახავთ განსხვავებულ ლოგიკურ და შედარების ოპერაციათა შედეგებს (უნდა იყოს შედარების და ლოგიკური ოპერატორები ერთად მაგალითად temperature > 30 and not cloudy), გვერდზე კომენტარის საშვალებით მიუწერეთ ეს შედეგი (boolean მნიშვნელობა) აიღეთ მრავალფეროვანი კომბინაციები
speed = 330
limit = 120
license = False
night = True
school = True
rain = False
cpu = True
gpu = False
pcomp = True
monitor = False

result = speed > limit and night # true

result2 = speed < limit # true

result3 = school < night and rain # false

pc = cpu and gpu # false

setup = pcomp and monitor # false

for num in range (80, 91, 1):
    print (num)

for num in range (90, 79, -1):
    print (num)

for num in range (78, 95, 2):
    print (num)



# **6) Bonus დავალება**  
# შექმენით პროგრამა, რომელიც განსაზღვრავს `productive` ცვლადის მნიშვნელობას შემდეგი პირობების მიხედვით:
# 1. `read_pages` ცვლადში ინახება წაკითხული გვერდების რაოდენობა (მთლიანი რიცხვი).  
# 2. `free_time` ცვლადში ინახება boolean მნიშვნელობა (True/False), რომელიც გვიჩვენებს, ჰქონდა თუ არა თავისუფალი დრო.  
# 3. `productive` ცვლადი იქნება ჭეშმარიტი (True), თუ მოსწავლემ წაიკითხა მინიმუმ 20 გვერდი **და** თავისუფალი დრო ჰქონდა.  

# **მაგალითი:**
# - თუ `read_pages = 25` და `free_time = True`, მაშინ `productive = True` 
# - თუ `read_pages = 15` და `free_time = True`, მაშინ `productive = False`
# - თუ `read_pages = 30` და `free_time = False`, მაშინ `productive = False`



read_pages = 40
free_time = True
productive = read_pages >= 40 and free_time
print("was that productive?", productive)