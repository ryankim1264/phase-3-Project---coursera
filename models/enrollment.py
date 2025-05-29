from lib import CURSOR, CONN 

class Enrollment:
    def __init__(self, student_id , course_id , id=None):
        self.id = id 
        self.student_id = student_id
        self.course_id = course_id
    @classmethod   
    def create_table(cls):
        sql ="""CREATE TABLE IF NOT EXISTS enrollments (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
         );
       
        """   
        CURSOR.execute(sql)
        CONN.commit()
        
        
    def save(self):
        sql = """
        INSERT INTO enrollments(student_id , course_id) VALUES(?, ?)
        
        """
        CURSOR.execute(sql, (self.student_id, self.course_id))
        self.id = CURSOR.lastrowid
        CONN.commit()
        
        
    @classmethod
    def all(cls):
        sql = "SELECT * FROM enrollments;"
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls(id=row[0], student_id=row[1], course_id=row[2]) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM enrollments WHERE id = ?"
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()
        return cls(id=row[0], student_id=row[1], course_id=row[2]) if row else None

    def update(self):
        sql = """
            UPDATE enrollments SET student_id = ?, course_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.student_id, self.course_id, self.id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM enrollments WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
    @classmethod   
    def get_courses_for_student(cls, student_id):
     sql = """
        SELECT courses.id, courses.title, courses.type
        FROM courses
        JOIN enrollments ON courses.id = enrollments.course_id
        WHERE enrollments.student_id = ?
     """
     CURSOR.execute(sql, (student_id,))
     from models.course import Course
     rows = CURSOR.fetchall()
     return [Course(id=row[0], title=row[1], type=row[2]) for row in rows]