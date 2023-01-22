def get_grade(student, names_list, grade_list, course_list):
    i = names_list.index(student)
    grade = grade_list[i]
    course = course_list[i]
    return (course, grade)


names = ["Ana", "John", "Denise", "Katy"]
grade = ["B", "A+", "A", "A"]
course = [2.00, 6.0001, 20.002, 9.01]
print(get_grade("Katy", names, grade, course))


# list vs dictionaries


students = {
    "Ana": (2.00, "B"),
    "John": (6.0001, "A+"),
    "Denise": (20.002, "A"),
    "Katy": (9.01, "A")
}
print(students["Katy"])
