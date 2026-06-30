
num = list(input("Enter all three numbers (separated by space): ").split())

print(num)
if num[0] > num[1] and num[0] < num[2]:
    print(f"{num[0]} is largest number in {num}")
elif num[0] < num[1] and num[1] < num[2]:
    print(f"{num[2]} is largest number in {num}")
else:
    print(f"{num[1]} is largest number in {num}")
