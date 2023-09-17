student_data = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78},
    {'name': 'David', 'score': 95},
]

#Структурная парадигма
def calculate_average(students):
    total_score = sum(student['score'] for student in students)
    return total_score / len(students)

def find_above_average_students(students, average):
    return [student['name'] for student in students if student['score'] > average]

average = calculate_average(student_data)
above_average_students = find_above_average_students(student_data, average)

print(f"Средний балл: {average}")
print(f"Студенты с баллом выше среднего: {above_average_students}")

#Процедурная парадигма
def calculate_average_and_find_above_average_students(students):
    total_score = 0
    num_students = 0
    above_average_students = []

    for student in students:
        total_score += student['score']
        num_students += 1

    average = total_score / num_students

    for student in students:
        if student['score'] > average:
            above_average_students.append(student['name'])

    return average, above_average_students

average, above_average_students = calculate_average_and_find_above_average_students(student_data)

print(f"Средний балл: {average}")
print(f"Студенты с баллом выше среднего: {above_average_students}")
