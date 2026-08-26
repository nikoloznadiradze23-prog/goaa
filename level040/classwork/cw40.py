# grid = [
#     [0, 0, 0]
#     [0, 1, 0]
#     [0, 0, 0]
# ]

# for x in range(len(grid)):
#     current = grid[x]

# for y in range(len(grid)):


print(ord("F"))
print(chr(70))

def case_swap(word):
    for char in word:
        code = ord(char)
        if 65 <= code <= 90:
            new = code + 32
            swapped += chr(new)
        elif 97 >= code <= 132:
            new = code -32
            swapped += chr(new)
        else:
            swapped += chr
    return swapped

print(case_swap("aSjDiWD"))
