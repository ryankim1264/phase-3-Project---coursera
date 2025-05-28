from __init__ import CURSOR, CONN

class Course:
    def __init__(self, title , type, id=None) :
        self.id = id
        self.title= title
        self.type = type
          
    @classmethod
    def create_table(cls):
        sql ="""CREATE TABLE IF NOT EXISTS courses(
        id INTEGER  PRIMARY KEY,
        title TEXT,
        type TEXT
        )
        """   
        CURSOR.execute(sql)
        CONN.commit()
        
    def save(self):
        sql ="""INSERT INTO courses(title , type) VALUE(?, ?)
               
        """  
        CURSOR.execute(sql, (self.title , self.type))
        CONN.commit()
          