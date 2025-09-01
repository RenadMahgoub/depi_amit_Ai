from core.system_manager import SystemManager


# ===================== MENU =====================
def show_menu():
    """Display the main menu options."""
    print("\n" + "=" * 40)
    print(" Student & Course Management System ")
    print("=" * 40)
    print("1. Add student")
    print("2. Remove student")
    print("3. Add course")
    print("4. Remove course")
    print("5. Search courses")
    print("6. Record grade")
    print("7. Get all students")
    print("8. Get all courses")
    print("9. Enroll course")
    print("10. Exit")
    print("=" * 40)


# ===================== STUDENTS =====================
def add_student(manager):
    """Add a new student to the system."""
    name = input("Enter student name: ")
    student_id = manager.add_student(name)
    print(f"Student added with ID: {student_id}")


def remove_student(manager):
    """Remove a student by ID."""
    student_id = int(input("Enter student ID: "))
    manager.remove_student(student_id)
    print("Student removed successfully.")


def get_all_students(manager):
    """Display all students."""
    students = manager.get_all_students()
    if students:
        print("\nAll Students:")
        for student in students:
            print(f"- {student}")
    else:
        print("No students found.")


# ===================== COURSES =====================
def add_course(manager):
    """Add a new course to the system."""
    name = input("Enter course name: ")
    course_id = manager.add_course(name)
    print(f"Course added with ID: {course_id}")


def remove_course(manager):
    """Remove a course by ID."""
    course_id = int(input("Enter course ID: "))
    manager.remove_course(course_id)
    print("Course removed successfully.")


def search_courses(manager):
    """Search for courses by name."""
    search_name = input("Enter course name to search: ")
    courses = manager.search_courses(search_name)
    if courses:
        print("\nMatched Courses:")
        for course in courses:
            print(f"- {course}")
    else:
        print("No courses matched your search.")


def get_all_courses(manager):
    """Display all courses."""
    courses = manager.get_all_courses()
    if courses:
        print("\nAll Courses:")
        for course in courses:
            print(f"- {course}")
    else:
        print("No courses found.")


# ===================== GRADES & ENROLLMENT =====================
def record_grade(manager):
    """Record a grade for a student in a course."""
    student_id = int(input("Enter student ID: "))
    course_id = int(input("Enter course ID: "))
    grade = input("Enter grade: ")
    manager.record_grade(student_id, course_id, grade)
    print("Grade recorded successfully.")


def enroll_course(manager):
    """Enroll a student in a course."""
    student_id = int(input("Enter student ID: "))
    course_id = int(input("Enter course ID: "))
    manager.enroll_course(student_id, course_id)
    print("Student enrolled in course.")


# ===================== MAIN =====================
def core():
    """Main function to run the system."""
    manager = SystemManager()
    actions = {
        "1": add_student,
        "2": remove_student,
        "3": add_course,
        "4": remove_course,
        "5": search_courses,
        "6": record_grade,
        "7": get_all_students,
        "8": get_all_courses,
        "9": enroll_course,
    }

    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "10":
            print("Exiting the system. Goodbye!")
            break

        action = actions.get(choice)
        if action:
            action(manager)
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    core()
