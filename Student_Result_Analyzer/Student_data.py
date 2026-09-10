import csv

def read_and_organize_student_data():
    student_data = {}

    try:
        with open("Student_Result_Analyzer/Student_Data.csv", "r") as file:
            reader = csv.DictReader(file)

            for data in reader:

                if data["name"].strip():
                    name = data["name"].strip()

                else:
                    print("Error: Missing 'name' field in the CSV data. Skipping this entry.")
                    continue

                try:
                    score = int(data["score"])

                except ValueError:
                    print(f"Error: Invalid score '{data['score']}' for student '{name}'. Skipping this entry.")
                    continue

                if name in student_data:
                    student_data[name]["marks"] += score
                    student_data[name]["total_subjects"] += 1
                else:
                    student_data[name] = {
                        "marks" : score,
                        "total_subjects" : 1
                    }

    except FileNotFoundError:
        print("Error: The file 'Student Result Analyzer/Student_Data.csv' was not found.")

    return student_data