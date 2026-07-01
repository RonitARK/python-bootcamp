
temp = float(input("Enter your temperature: "))
unit = input("Enter temperature unit (C, F, K): ")
desired_unit = input("Enter desired temperature unit (C, F, K): ")
if unit == "C":
    if desired_unit == "F":
        result = print(f"{temp}°C is {(temp * (9 / 5))+ 32}°F")
    else:
        result = print(f"{temp}°C is {(temp + 273.15)}°K")

elif unit == "F":
    if desired_unit == "C":
        result = print(f"{temp}°F is {(temp - 32) * (5 / 9)}°C")
    else:
        result = print(f"{temp}°F is {(temp - 32 ) * (5 / 9) + 273.15}°K")
elif unit == "K":
    if desired_unit == "C":
        result = print(f"{temp}°K is {temp - 273.15}°C")
    else:
        result = print(f"{temp}°K is {(temp - 273.15) * (9 / 5) + 35 }°F")




