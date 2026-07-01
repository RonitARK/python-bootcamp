from datetime import datetime

today = datetime.now()
dob = input("Enter your date of birth (DD,MM,YYYY): ").split(",")
age = today.year - int(dob[2])
print(f"You are {age} years old")