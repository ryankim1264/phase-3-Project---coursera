from lib import CURSOR, CONN

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
        sql ="""INSERT INTO courses(title , type) VALUES(?, ?)
               
        """  
        CURSOR.execute(sql, (self.title , self.type))
        CONN.commit()
    
    @classmethod
    def all(cls):
        sql = "SELECT * FROM courses;"
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls(id=row[0], name=row[1]) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM courses WHERE id = ?"
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()
        return cls(id=row[0], name=row[1]) if row else None

    def update(self):
        sql = "UPDATE courses SET name = ? WHERE id = ?"
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM courses WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()