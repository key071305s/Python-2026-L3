students = []
courses = []
mark = {}

def students_count():
	count_students = int(input("Enter the number of student: "))
	return count_students
def students_info():
	ID_student = int(input("Enter the ID student: "))
	NAME_student = input("Enter the name: ")
	DoB_student = input("Enter the day of birth: ")
	students.append({'Name':NAME_student, 'ID':ID_student, 'DoB':DoB_student})
def courses_count():
	count_courses = int(input("Enter the numbner of courses: "))
	return count_courses
def courses_info():
	ID_course = int(input("Enter the ID course: "))
	NAME_course = input("Enter the name of course: ")
	courses.append({'Name course': NAME_course, 'ID':ID_course})
def marks(courses, students, mark):
	
	ID_selected = int(input("Enter the course ID to input marks for: "))

	found = False
	for i in courses:
		if i['ID'] == ID_selected:
			found = True
			break

	if not found:
		print("The course not found")
		return
	if ID_selected not in mark:
		mark[ID_selected] ={}

	for s in students:
		score = float(input(f"Enter the mark for {s['Name']}: "))
		mark[ID_selected][s['ID']] = score


count_s = students_count()
for i in range(count_s):
	students_info()
	i = i+1
count_c = courses_count()
for i in range(count_c):
	courses_info()
	i = i+1


while True:
	print("--------------MENU---------------")
	print("1. INPUT THE MARK FOR EACH COURSE")
	print("2. SHOW LIST STUDENTS")
	print("3. SHOW LIST COURSES")
	print("4. SHOW STUDENT MARKS FOR COURSE")
	print("5. EXIT")

	selected = int(input("Enter your select:"))

	match selected:
		case 1:
			marks(courses, students, mark)
			
		case 2:
			print("Students: ", students)

		case 3:
			print("Courses: ", courses)
		case 4:
			print("The marks: ", mark)
		case 5:
			break
		case _:
			print("NOT EXIST")




