import json

data = [
    {
        "name": "Adam",
        "age": 19,
        "grades": [85, 90, 95]
    },
    {
        "name": "Temir",
        "age": 19,
        "grades": [70, 75, 80]
    },
    {
        "name": "Daur",
        "age": 18,
        "grades": [100, 99, 98]
    }
]

with open('students.json', 'w') as f:
    json.dump(data, f)

#calculation
with open('students.json', 'r') as f:
    students = json.load(f)

for student in students:
    grades = student["grades"]
    if grades:
        avg = sum(grades) / len(grades)
    else:
        avg = 0
    student["average_grade"] = avg

with open('updated_students.json', 'w') as f:
    json.dump(students, f)