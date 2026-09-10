
def calculate_average_and_status(student_data):
    student_result = {}

    for name, data in student_data.items():
        average = data["marks"] / data["total_subjects"]

        student_result[name] = {
            "average" : average, 
            "status" : "Pass" if average >= 60 else "Fail"
        }

    return student_result