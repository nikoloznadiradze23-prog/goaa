# def rect(lenght,width):
#     area  = lenght * width
#     perimeter = 2 * (lenght * width)
#     return area,perimeter


# def hello(name):
#     print("wellcome"+ name)








rgb = ("red","green","blue","red")

def manual_count(sequence,target):
    count = 0
    for target in sequence:
        count += 1
        return count

rgb = manual_count(rgb,"red")
print (rgb)