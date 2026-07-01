
term = int(input("Enter the fibonacci term (except 0): "))

f_0 = 0
f_1 = 1

if term == 1:
    print(f"{term}st term is {f_0}")
elif term == 2:
    print(f"Fibonacci series is: {f_0},{f_1}")
    print(f"{term}th term is {f_1}")
else:
    print(f"Fibonacci series is: {f_0},{f_1},",end="")
    for i in range(2, term):
        f_2 = f_0 + f_1
        f_0 = f_1
        f_1 = f_2
        print(f_2,end=",")
    print(f"\n{term}th term is {f_2}")
