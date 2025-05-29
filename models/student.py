from lib import CURSOR, CONN

class Student:
    def __init__(self, name, mark, id=None):
        self.id = id
        self.name = name
        self.mark = mark

    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY, 
            name TEXT,
            mark TEXT
        )"""
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = "INSERT INTO students(name, mark) VALUES (?, ?)"
        CURSOR.execute(sql, (self.name, self.mark))
        self.id = CURSOR.lastrowid
        CONN.commit()

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM students")
        rows = CURSOR.fetchall()
        return [cls(id=row[0], name=row[1], mark=row[2]) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM students WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        return cls(id=row[0], name=row[1], mark=row[2]) if row else None

    def update(self):
        sql = "UPDATE students SET name = ?, mark = ? WHERE id = ?"
        CURSOR.execute(sql, (self.name, self.mark, self.id))
        CONN.commit()

    def delete(self):
        CURSOR.execute("DELETE FROM students WHERE id = ?", (self.id,))
        CONN.commit()
