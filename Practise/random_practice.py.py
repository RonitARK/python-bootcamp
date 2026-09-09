
# 1. Find duplicate elements in a list.

my_list = [1, 2, 3, 2, 4, 5, 1, 6, 2]

seen = set()
duplicates = set()

for item in my_list:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print(list(duplicates))

# 2. Reverse a string without slicing (`[::-1]`).

name = "Ronit"
for i in range(len(name)-1,-1,-1):
    print(name[i],end="")
print()

# 3. Count the frequency of each character in a string.

text = "Banana"
char_counts = {}

for char in text:
    char_counts[char] = char_counts.get(char, 0) + 1

print(char_counts)

# 4. Find the second-largest number in a list.

my_num = [23,32,45,76,83,99]
my_num.sort()
print(my_num[-2])

# 5. Remove duplicates while preserving order.

num = [1,2,4,3,5,1,2]
print(list(dict.fromkeys(num)))

