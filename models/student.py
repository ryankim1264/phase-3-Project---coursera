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
        
    @classmethod
    def get_all (cls):
        sql = """
        SELECT * FROM students""" 
        CURSOR.execute(sql) 
        rows = CURSOR.fetchall() 
        return [cls(id = row[0], name=row[1]) for row in rows]
    
    @classmethod
    def find_by_id(cls ,id):
        sql = """SELECT * FROM students WHERE id = ?"""
        CURSOR.execute(sql , (id,))
        row = CURSOR.fetchone()
        return cls(id=row[0], name=row[1]) if row else None
    
    def update(self):
        sql = """UPDATE students SET name = ? WHERE id = ?"""
        CURSOR.execute(sql , (self.name, self.id))
        CONN.commit()
        
    def delete(self):
        sql = """DELETE FROM students WHERE id = ?"""
        CURSOR.execute(sql, (self.id))
        CONN.commit()
                