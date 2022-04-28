def register(course, student):
    if course not in courses:
        courses[course] = [student]
    else:
        courses[course].append(student)


def print_courses():
    for course, students in courses.items():
        registered_students = len(students)
        print(f'{course}: {registered_students}')
        for student_name in students:
            print(f'-- {student_name}')


courses = {}
while True:
    data = input()
    if data == 'end':
        break
    data = data.split(' : ')
    course_name = data[0]
    student_name = data[1]
    register(course_name, student_name)
print_courses()
