
import  time

def student_name():
    while True:
        name = input("\nEnter Student Name: ")

        if name.strip() == "":
            print("Student Name cannot be empty")
        elif name.replace(" ", "").isalpha() == False:
            print("Student Name cannot contain numbers or special characters")
        else:
            break

def student_age():
    while True:
        age = input("Enter student age : ")

        if age.isdigit() == False:
            print("Invalid Age")
        elif int(age) < 16 or int(age) > 22:
            print("Student Age must be between 17 and 22")
        else:
            break

def student_gender():
    while True:
        gender = input("Enter student gender (M,F): ").upper()

        if gender.strip() == "":
            print("Student gender cannot be empty")
        elif gender.replace(" ", "").isalpha() == False:
            print("Student gender cannot contain numbers or special characters")
        elif gender != "M" and gender != "F":
            print("Invalid Gender")
        else:
            break

def student_phone():
    while True:
        phone = input("Enter student phone number: ")

        if phone.isdigit() == False and len(phone) == 10:
            print("Invalid Phone number")
        else:
            break

def student_email():
    while True:
        email = input("Enter Student email: ")

        if email.strip() == "":
            print("Student email cannot be empty")
        elif "@gmail.com" not in email or " " in email:
            print("Invalid Student email")
        else:
            break

def student_course():
    while True:
        course = input("Enter student course: ").upper()

        if course.strip() == "":
            print("Student course cannot be empty")
        elif course.replace(" ", "").isalpha() == False:
            print("Student course cannot contain numbers or special characters")
        elif course not in ["BTECH", "BCA", "BBA", ]:
            print("Invalid course")
        else:
            break

def student_branch():
    while True:
        branch = input("Enter student branch: ").upper()

        if branch.strip() == "":
            print("Student branch cannot be empty")
        elif branch.replace(" ", "").isalpha() == False:
            print("Student branch cannot contain numbers or special characters")
        elif branch not in ["CSE", "ECE", "IT", ]:
            print("Invalid branch")
        else:
            break

id = 1000
name = ""
age = 0
gender = ""
phone = 0
email = ""
branch = ""
course = ""
student_record = []


while True:
    time.sleep(2)

    print("\n=====================================")
    print("===== Student Management System =====")
    print("=====================================")
    print("1. Add Student" , "2. View All Students" , "3. Search Student by ID" , "4. Search Student by Name" , "5. Update Student" , "6. Delete Student" , "7. Exit", sep="\n")

    choice = input("Enter your choice: ")

    if choice.isdigit() == False or int(choice) not in range(1,8):
        print("Choice cannot be empty, any alphabet, special character or outside of range (1-7)")
    else:
        choice = int(choice)



# ========== ADD STUDENT ==========
    if choice == 1:

        student_name()
        student_age()
        student_gender()
        student_phone()
        student_email()
        student_course()
        student_branch()

        id = id + 1
        student_info = {"id": id,
                        "name": name,
                        "age": age,
                        "gender": gender,
                        "phone": phone,
                        "email": email,
                        "course": course,
                        "branch": branch,}

        student_record.append(student_info)


# ========== VIEW ALL STUDENT ==========
    elif choice == 2:
        for i in student_record:
            print(f"\nID: {i.get('id')}" , f"Name: {i.get('name')}" , f"Age: {i.get('age')}" , f"Gender: {i.get('gender')}" , f"Phone Number: {i.get('phone')}" , f"Email: {i.get('email')}" , f"Course: {i.get('course')}" , f"Branch: {i.get('branch')}" , sep = "\n")


# ========== SEARCH BY ID ==========
    elif choice == 3:
        id = input("Enter Student ID: ")

        if id.isdigit() == False:
            print("Invalid ID")
        else:
            id = int(id)

            for i in student_record:
                if i.get("id") == id:
                    print(f"\nID: {i.get('id')}", f"Name: {i.get('name')}", f"Age: {i.get('age')}", f"Gender: {i.get('gender')}", f"Phone Number: {i.get('phone')}", f"Email: {i.get('email')}", f"Course: {i.get('course')}", f"Branch: {i.get('branch')}", sep="\n")
                else:
                    print("Invalid ID")


# ========== SEARCH BY NAME ==========
    elif choice == 4:
        name = input("Enter Student Name: ")
        for i in student_record:
            if i.get("name") == name:
                print(f"\nID: {i.get('id')}", f"Name: {i.get('name')}", f"Age: {i.get('age')}",  f"Gender: {i.get('gender')}", f"Phone Number: {i.get('phone')}", f"Email: {i.get('email')}", f"Course: {i.get('course')}", f"Branch: {i.get('branch')}", sep="\n")
            else:
                print("Invalid Name")


# ========== UPDATE STUDENT ==========
    elif choice == 5:
        id = input("Enter Student ID: ")

        if id.isdigit() == False:
            print("Invalid ID")
        else:
            id = int(id)

            for i in student_record: # no output
                if i.get("id") == id:
                    print("1. Name", "2. Age", "3. Gender", "4. Phone Number", "5. Email", "6. Course", "7. Branch", sep="\n")
                    update = input("Enter the choice to update (1-7): ")

                    if update.isdigit() == False or int(update) not in range(1, 8):
                        print("Choice cannot be empty, any alphabet, special character or outside of range (1-7)")
                    else:
                        update = int(update)

                    if update == 1:
                        student_name()
                        i.update(name)
                    elif update == 2:
                        student_age()
                        i.update(age)
                    elif update == 3:
                        student_gender()
                        i.update(gender)
                    elif update == 4:
                        student_phone()
                        i.update(phone)
                    elif update == 5:
                        student_email()
                        i.update(email)
                    elif update == 6:
                        student_course()
                        i.update(course)
                    elif update == 7:
                        student_branch()
                        i.update(branch)


# ========== DELETE STUDENT ==========
    elif choice == 6:
        id = input("Enter Student ID: ")

        if id.isdigit() == False:
            print("Invalid ID")
        else:
            id = int(id)

            for i in student_record:
                if i.get("id") == id: # not working
                    student_record.remove(i)
                else:
                    print("Invalid ID")


# ========== DELETE STUDENT ==========
    elif choice == 7:
        print("Exiting the program. Goodbye!")
        break


    else:
        continue


