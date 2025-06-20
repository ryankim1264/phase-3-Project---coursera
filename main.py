from lib.seed import seed_data

from lib.seed import seed_data
from models.student import Student
from models.course import Course
from models.enrollment import Enrollment

def show_menu():
    print("\n=== Coursera CLI ===")
    print("1. --------List all students")
    print("2. --------List all courses")
    print("3. --------Add a student")
    print("4. --------Add a course")
    print("5. --------Enroll a student in a course")
    print("6. --------View a student's courses")
    print("7. ........Update student")
    print("8. ........Delete course")
    print("0. Exit")

def run_cli():
    while True:
        show_menu()
        choice = input("SELECT AN OPTION: ").strip()

        if choice == "1":
            for s in Student.get_all():
                print(f"{s.id}. {s.name} (Mark: {s.mark})")

        elif choice == "2":
            for c in Course.get_all():
                print(f"{c.id}. {c.title} ({c.type})")

        elif choice == "3":
            name = input("Enter student name: ")
            mark = input("Enter student mark: ")
            student = Student(name=name, mark=str(mark))
            student.save()
            print("✅ The student has been added!!!!!!!!!!!!!!!!!!")

        elif choice == "4":
            title = input("Enter course title: ")
            course_type = input("Enter course type: ")
            course = Course(title=title, type=course_type)
            course.save()
            print("The course has been added!!!!!!!!!!!!!!!!.")

        elif choice == "5":
            sid = input("Student ID: ")
            cid = input("Course ID: ")
            enrollment = Enrollment(student_id=int(sid), course_id=int(cid))
            enrollment.save()
            print("The student has been enrolled to the course !!!!!!!")

        elif choice == "6":
            sid = input("Enter student ID: ")
            courses = Enrollment.get_courses_for_student(int(sid))
            print(f"Courses for Student {sid}:")
            for c in courses:
                print(f"- {c.title}")
        
        elif choice == "7":
            sid = input("Enter student ID to update: ")
            new_mark = input("Enter new mark: ")
            student = Student.get_by_id(int(sid))
            if student:
                student.mark = str(new_mark)
                student.save()
                print("Student updated successfully!")
            else:
                print("Student not found!")
                
        elif choice == "8":
            sid = input("Enter student ID to delete: ")
            student = Student.get_by_id(int(sid))
            if student:
                student.delete()
                print(" Student deleted successfully!")
            else:
                print("Student not found!")
                
            
        elif choice == "0":
            print("BADAEE!!!!!!!!!!!!!!!!!!. THANKS FOR VISITING COURSERA. BYEEE!!")
            break

        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!! Invalid choice , Try again!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

if __name__ == "__main__":
    run_cli()

student1, student2 = seed_data()


if __name__ == "__main__":
    seed_data()