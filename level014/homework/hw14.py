# CONTROL FLOW იღებს გადაწყვეტილებას თუ რომელი კოდის ბლოკირება უნდა მოხდეს
# და loop ანუ ციკლი ამეორებს მოქმედებას


for num in range (0, 31, 1):
    print (num)

for num in range (15, 31, 1):
    print (num)

for num in range (15, 81, 1):
    print (num)

for num in range (0, 89, 1):
    print (num)

for num in range (0, 51, 3):
    print (num)

num1= int(input("put in num1:"))
num2= int(input("put in num2:"))
for num in range(num1, num2, 1):
    print (num)

for num in range (0, 101, 2):
    print(num)

num3=0
for num in range(20, 41, 1):
    num3 += num
    print(num3)

num4=0
for num in range(0, 101, 3):
    num4 += num
    print(num4)

num5=0
for num in range(0, 101, 3):
    num5 += num
    print(num5)

num5=7
v=1
for i in range(1, num5 + 1):
    v*=num5
    print(num5)

num = 0
while num <20: 
    num += 1
    print(num)  

num1 = 9
while num1 <30: 
    num1 += 1
    print(num1)  

num2 = 14
while num2 <80: 
    num2 += 1
    print(num2)  

num3 = 50
while num3 >0: 
    num3 -= 1
    print(num3)  

num4 = 0
while num4 <48: 
    num4 += 3
    print(num4)  

num5 = 0
while num5 <50: 
    num5 += 2
    print(num5)

num6 = 103
while num6 >2: 
    num6 -= 3
    print(num6)  

code = input("enter your pin code:")
while (code != "goabest123"):
    code = input("enter pin code:")
print("autorized")
