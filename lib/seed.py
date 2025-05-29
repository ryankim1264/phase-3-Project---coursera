from lib import CONN, CURSOR
from models.student import Student
from models.course import Course
from models.enrollment import Enrollment

def seed_data():
    Student.create_table()
    Course.create_table()
    Enrollment.create_table()
    
    student1 = Student(name="Jess" , mark= "A")
    student1.save()
     
    student2 = Student(name="Winfrey" , mark="B")
    student2.save()
    course1 = Course("Computer science" , "IT" )
    course1.save()
    course2 = Course("BBIT " , "BUISNESS & IT")
    course2.save()

    enroll1 = Enrollment(student_id=student1.id, course_id=course1.id)
    enroll1.save()
    enroll2 = Enrollment(student_id=student2.id, course_id=course2.id)
    enroll2.save()
    return student1, student2

print("Data Seeded")

    