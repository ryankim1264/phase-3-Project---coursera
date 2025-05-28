from __init__ import CURSOR, CONN 

class Enrollment:
    def __init__(self, student_id , course_id , id=None):
        self.id = id 
        self.student_id = student_id
        self.course_id = course_id
    @classmethod   
    def create_table(cls):
        sql ="""CREATE TABLE IF NOT EXISTS enrollments(
            id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY(students_id)
        REFERENCE students(id),
            FOREIGN KEY(course_id)
        REFERENCE courses(id)    
        )
       
        """   
        CURSOR.execute(sql)
        CONN.commit()
        
        
    def save(self):
        sql = """
        INSERT INTO enrollments(student_id , course_id) VALUES(?, ?)
        
        """
        CURSOR.execute(sql, (self.student_id, self.course_id))
        CONN.commit()