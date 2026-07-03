
import  time

id = 1000
student_record = []


def student_name():
    while True:
        name = input("\nEnter Student Name: ")

        if name.strip() == "":
            print("Student Name cannot be empty")
        elif name.replace(" ", "").isalpha() == False:
            print("Student Name cannot contain numbers or special characters")
        else:
            return name

def student_age():
    minimum_age = 16
    maximum_age = 22
    while True:
        age = input("Enter student age : ")

        if age.isdigit() == False:
            print("Invalid Age")
        elif int(age) < minimum_age or int(age) > maximum_age:
            print("Student Age must be between 17 and 22")
        else:
            return age

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
            return gender

def student_phone():
    while True:
        phone = input("Enter student phone number: ")

        if phone.isdigit() == False and len(phone) == 10:
            print("Invalid Phone number")
        else:
            return phone

def student_email():
    while True:
        email = input("Enter Student email: ")

        if email.strip() == "":
            print("Student email cannot be empty")
        elif "@gmail.com" not in email or " " in email:
            print("Invalid Student email")
        else:
            return email

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
            return course

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
            return branch

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

        name = student_name()
        age = student_age()
        gender = student_gender()
        phone = student_phone()
        email = student_email()
        course = student_course()
        branch = student_branch()

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
                    continue


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
                    update_choice = input("Enter the choice to update (1-7): ")

                    if update_choice.isdigit() == False or int(update_choice) not in range(1, 8):
                        print("Choice cannot be empty, any alphabet, special character or outside of range (1-7)")
                    else:
                        update_choice = int(update_choice)

                    if update_choice == 1:
                        name = student_name()
                        i.update({"name": name})
                    elif update_choice == 2:
                        age = student_age()
                        i.update({"age": age})
                    elif update_choice == 3:
                        gender = student_gender()
                        i.update({"gender": gender})
                    elif update_choice == 4:
                        phone = student_phone()
                        i.update({"phone": phone})
                    elif update_choice == 5:
                        email = student_email()
                        i.update({"email": email})
                    elif update_choice == 6:
                        course = student_course()
                        i.update({"course": course})
                    elif update_choice == 7:
                        branch = student_branch()
                        i.update({"branch": branch})


# ========== DELETE STUDENT ==========
    elif choice == 6:
        id = input("Enter Student ID: ")

        if id.isdigit() == False:
            print("Invalid ID")
        else:
            id = int(id)

            for i in student_record:
                if i.get("id") == id:
                    student_record.remove(i)
                else:
                    continue


# ========== DELETE STUDENT ==========
    elif choice == 7:
        print("Exiting the program. Goodbye!")
        break


    else:
        continue


