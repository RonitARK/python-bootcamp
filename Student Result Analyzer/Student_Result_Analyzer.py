import csv

def read_and_organize_student_data():
    student_data = {}

    with open("Student Result Analyzer/Student_Data.csv", "r") as file:
        reader = csv.DictReader(file)

        for data in reader:
            name = data["name"]
            score = int(data["score"])
            if name in student_data:
                student_data[name]["marks"] += score
                student_data[name]["total_subjects"] += 1
            else:
                student_data[name] = {
                    "marks" : score,
                    "total_subjects" : 1
                }

    return student_data



def calculate_average_and_status(student_data):
    student_result = {}

    for name, data in student_data.items():
        average = data["marks"] / data["total_subjects"]

        student_result[name] = {
            "average" : average, 
            "status" : "Pass" if average >= 60 else "Fail"
        }

    return student_result


student_data = read_and_organize_student_data()
student_result = calculate_average_and_status(student_data)

print(student_result)

