def add_grades(name, grade):
    if name not in grades_dict.keys():
        grades_dict[name] = [grade]
    else:
        grades_dict[name].append(grade)


pairs = int(input())
grades_dict = {}
for i in range(pairs):
    student = input()
    grade = float(input())
    add_grades(student, grade)

for student, grades in grades_dict.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f'{student} -> {average_grade:.2f}')

