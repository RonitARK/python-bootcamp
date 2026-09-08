import csv
import json

with open("sample_file.csv", "r") as file:
    reader = csv.DictReader(file)

    new_records = []

    for i in reader:
        record = i
        if int(record['score']) >= 60:
            new_records.append({
                "name": record["name"],
                "score": int(record["score"])
            })
    print(new_records)

    with open("passed_students.json", "w") as f:
        json.dump(new_records, f)


