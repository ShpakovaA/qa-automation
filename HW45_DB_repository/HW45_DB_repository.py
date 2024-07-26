import sqlite3


class Teacher:

    def __init__(self, name, subject, experience_years, salary):
        self.name = name
        self.subject = str(subject).capitalize()
        self.experience_years = experience_years
        self.salary = salary

    def __repr__(self):
        return f"Teacher({self.name}, {self.subject}, {self.experience_years}, {self.salary})"


class TeachersRepository:

    def __init__(self, db_path):
        self._connection = sqlite3.connect(db_path, isolation_level=None)
        self._cursor = self._connection.cursor()
        self._cursor_execute = self._cursor.execute("CREATE TABLE IF NOT EXISTS Teachers(id INTEGER PRIMARY KEY, name TEXT, subject TEXT, experience_years INTEGER, salary REAL);")

    # adds one record by passed object into methods;
    def add_teacher(self, teacher: Teacher):
        return self._cursor.execute(f"INSERT INTO Teachers(name, subject, experience_years, salary) VALUES('{teacher.name}', '{teacher.subject}', {teacher.experience_years}, {teacher.salary});")

    # add several records by passed objects into methods;
    def add_teachers(self, *teachers):
        for teacher in teachers:
            self.add_teacher(teacher)

    # obtains all records as list of objects of user defined classes;
    def get_all(self):
        self._cursor.execute(f"SELECT * FROM Teachers")
        return TeachersRepository._rows_to_objects(self._cursor.fetchall())

    # obtaining records by condition
    def get_teacher_by_subject(self, subject: str):
        subject = subject.capitalize()
        self._cursor.execute("SELECT * FROM Teachers WHERE subject=?;", (subject,))
        return TeachersRepository._rows_to_objects(self._cursor.fetchall())

    # deletes records by condition
    def delete_teachers_with_no_experience(self):
        return self._cursor.execute("DELETE FROM Teachers WHERE experience_years=0;")

    def delete_teacher(self, name):
        return self._cursor.execute("DELETE FROM Teachers WHERE name=?;", (name,))

    # updates a record/records by condition
    def update_teacher_experience(self, name: str, experience: int):
        return self._cursor.execute("UPDATE Teachers SET experience_years=? where name=?;", (experience, name))

    def change_salary(self, name, new_salary):
        return self._cursor.execute("UPDATE Teachers SET salary=? where name=?;", (new_salary, name))

    @staticmethod
    def _row_to_obj(row):
        return Teacher(*row[1:])

    @staticmethod
    def _rows_to_objects(rows):
        objects = []
        for row in rows:
            objects.append(TeachersRepository._row_to_obj(row))
        return objects

    def close(self):
        if self._connection:
            self._cursor.close()
            self._connection.close()


