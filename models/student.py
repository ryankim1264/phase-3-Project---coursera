from __init__ import CURSOR, CONN

class Student:
    def __init__(self, name , mark, id=None):
        self.id = id
        self.name =  name
        self.mark = mark
        
    @classmethod
    def create_table(cls):
        sql = """ 
        CREATE TABLE IF NOT EXISTS students(
            id INTERGER PRIMARY KEY, 
            name TEXT,
            mark TEXT
            )
        
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    
    def save(self):
        sql= """
        INSERT INTO students(name , mark) VALUE (?, ?)
        """    
        CURSOR.execute(sql, (self.name , self.location))
        CONN.commit()
        