import math

shape = (input("Enter your shape: ")).lower()

match shape:
    case "square":
        side = float(input("Enter your side (cm): "))
        print(f"The area is {side * side}cm²")
    case "rectangle":
        length = float(input("Enter your length (cm): "))
        width = float(input("Enter your width (cm): "))
        print(f"The area is {length * width}cm²")
    case "triangle":
        base = float(input("Enter your base (cm): "))
        height = float(input("Enter your height (cm): "))
        print(f"The area is {(1/2) * base * height}cm²")
    case "circle":
        radius = float(input("Enter your radius (cm): "))
        print(f"The area is {math.pi * (radius ** 2)}cm²")
    case "parallelogram":
        base = float(input("Enter your base (cm): "))
        height = float(input("Enter your height (cm): "))
        print(f"The area is {base * height}cm²")
    case "trapezium":
        side_a = float(input("Enter your side 'a' (cm): "))
        side_b = float(input("Enter your side 'b' (cm): "))
        height = float(input("Enter your height (cm): "))
        print(f"The area is {((side_a + side_b) / 2) * height}cm²")
