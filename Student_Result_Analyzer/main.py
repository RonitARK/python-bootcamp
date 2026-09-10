import Student_data as sd
import Analyzer as az

student_data = sd.read_and_organize_student_data()
student_result = az.calculate_average_and_status(student_data)

print(student_result)

