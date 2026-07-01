
num = int(input("Enter a factorial number: "))
fact = 1

if num == 0 or num == 1:
    print("Factorial is: 1")
else:
    for i in range(num , 0, -1):
        fact *= i
print(fact)