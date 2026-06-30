
principal_amount = float(input("Enter your principal amount: "))
rate = float(input("Enter your rate of interest (per year, in %): "))
time = float(input("Enter your time (in years): "))

si = (principal_amount * rate * time) / 100
amount = principal_amount + si

print(f"Simple Interest is ₹{si:.2f}")
print(f"Total Amount is ₹{amount:.2f}")