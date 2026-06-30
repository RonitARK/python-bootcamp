
height = float(input("Enter the height (in meters):"))
weight = float(input("Enter the weight (in kg):"))
bmi = round(weight / (height ** 2),2)
print(f"Height: {height}m \nWeight: {weight}kg\nBMI: {bmi}")

match bmi:
    case 1 if bmi < 18.5:
        print("Underweight")
    case 2 if bmi < 25:
        print("Normal weight")
    case 3 if bmi < 30:
        print("Overweight")
    case 4 if bmi < 35:
        print("Obesity (Class |)")
    case 5 if bmi < 40:
        print("Obesity (Class ||)")
    case 6 if bmi > 40:
        print("Obesity (Class |||)")
    case _:
        print("Invalid")