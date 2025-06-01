from lib import CONN, CURSOR
from models.student import Student
from models.course import Course
from models.enrollment import Enrollment

def reset_tables():
    CURSOR.execute("DROP TABLE IF EXISTS enrollments")
    CURSOR.execute("DROP TABLE IF EXISTS courses")
    CURSOR.execute("DROP TABLE IF EXISTS students")
    CONN.commit()

def seed_data():
    reset_tables()
    Student.create_table()
    Course.create_table()
    Enrollment.create_table()

    students_data = [
        {"name": "Jess", "mark": "A"},
        {"name": "Winfrey", "mark": "B"},
    ]
    students = []
    for data in students_data:
        student = Student(name=data["name"], mark=data["mark"])
        student.save()
        print(f"Saved student: {student.name} (ID: {student.id})")
        students.append(student)

    courses_data = [
        {"title": "Computer Science", "type": "IT"},
        {"title": "BBIT", "type": "Business & IT"},
    ]
    courses = []
    for data in courses_data:
        course = Course(title=data["title"], type=data["type"])
        course.save()
        print(f" Saved course: {course.title} (ID: {course.id})")
        courses.append(course)

    enrollments = [
        (students[0].id, courses[0].id),
        (students[1].id, courses[1].id),
    ]
    for student_id, course_id in enrollments:
        enrollment = Enrollment(student_id=student_id, course_id=course_id)
        enrollment.save()
        print(f"Enrolled  {student_id} in course {course_id}")

    print("Done")
    return students  


if __name__ == "__main__":
    seed_data()
