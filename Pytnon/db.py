import sqlite3

class Database():
    def __init__(self):
        self.db = sqlite3.connect('botDB.sqlite3')
        self.cur = self.db.cursor()



class EnterCalendar(Database):
    def __init__(self):
        super().__init__()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS enterCalendar(
                                                                            id INTEGER PRIMARY KEY,
                                                                            form TEXT,
                                                                            date TEXT,
                                                                            description TEXT
                                                                            )
                                """)
        self.db.commit()

    def get_budget(self):
        data = self.cur.execute("SELECT date, description  FROM enterCalendar WHERE form=?", ("buget", )).fetchall()
        return data

    def get_contract(self):
        data = self.cur.execute("SELECT date, description  FROM enterCalendar WHERE form=?", ("contract", )).fetchall()
        return data

    def get_kvot(self):
        data = self.cur.execute("SELECT date, description  FROM enterCalendar WHERE form=?", ("kvot", )).fetchall()
        return data



class Institutes(Database):
    def __init__(self):
        super().__init__()
        self.cur.execute("""
                            CREATE TABLE IF NOT EXISTS "Institutes"  (
	                        "id"	INTEGER NOT NULL,
	                        "Name"	TEXT,
	                        "Description"	TEXT,
	                        PRIMARY KEY("id" AUTOINCREMENT)
                            );""")
        self.db.commit()


    def get_names(self):
        data = self.cur.execute("SELECT Name FROM Institutes").fetchall()
        return data

    def get_ids(self):
        data = self.cur.execute("SELECT id FROM Institutes").fetchall()
        return data

    def get_all_institutes_by_id(self, institute_id):
        data = self.cur.execute("SELECT * FROM Institutes WHERE id=?", (institute_id,)).fetchone()
        return data


class Directions(Database):
    def __init__(self):
        super().__init__()
        self.cur.execute("""
                            CREATE TABLE IF NOT EXISTS "Directions" (
                                "id"	INTEGER NOT NULL,
                                "name"	TEXT,
                                "institute_id"	INTEGER NOT NULL,
                                "description"	INTEGER,
                                "price"	INTEGER,
                                FOREIGN KEY("institute_id") REFERENCES "Institutes"("id"),
                                PRIMARY KEY("id" AUTOINCREMENT)
                        );""")
        self.db.commit()

    def get_names_by_institute(self, institute_id):
        data = self.cur.execute("SELECT NAME FROM Directions WHERE institute_id = ?", (institute_id,)).fetchall()
        return data

    def get_ids(self):
        data = self.cur.execute("SELECT id FROM Directions").fetchall()
        return data


    def get_name_description_price_by_id(self, id):
        data = self.cur.execute("SELECT name, description, price FROM Directions WHERE id = ?", (id, )).fetchone()
        return data

    def get_all_info_by_id(self, direction_id):
        data = self.cur.execute("SELECT * FROM Directions WHERE id = ?", (direction_id)).fetchone()
        return data







class Focus(Database):
    def __init__(self):
        super().__init__()
        self.cur.execute("""
                            CREATE TABLE IF NOT EXISTS "Focus" (
                                "id"	INTEGER NOT NULL,
                                "name"	TEXT,
                                "direction_id"	TEXT NOT NULL,
                                "description"	TEXT,
                                "specification"	TEXT,
                                "learning_plan"	TEXT,
                                "calendar_schedule"	TEXT,
                                "documents"	TEXT,
                                "passing_points"	INT,
                                "subjects" TEXT,
                                FOREIGN KEY("direction_id") REFERENCES "Directions"("id"),
                                PRIMARY KEY("id" AUTOINCREMENT)
                            );""")
        self.db.commit()


    def get_names_by_direction(self, direction_id):
        data = self.cur.execute("SELECT name, id FROM Focus WHERE direction_id = ?", (direction_id, )).fetchall()
        return data

    def get_all_ids(self):
        data = self.cur.execute('SELECT id FROM Focus').fetchall()
        return data

    def get_all_info(self, passing_points):
        data = self.cur.execute(f"SELECT name, direction_id, description, passing_points_och, subjects FROM Focus WHERE passing_points_och < {passing_points}").fetchall()
        return data

    def get_info_by_id(self, focus_id):
        focus_info = self.cur.execute("SELECT * FROM Focus WHERE id = ?", (focus_id, )).fetchone()
        directionDB = Directions()
        direction_info = directionDB.get_all_info_by_id(focus_info[2])
        instituteDB = Institutes()
        institute_info = instituteDB.get_all_institutes_by_id(direction_info[2])
        return {
                'direction': direction_info[3],
                'focus': focus_info[1],
                'institute': institute_info[1],
                'passing_points': focus_info[8],
                'passing_points_contract': focus_info[9],
                'subjects': focus_info[-1],
                'price': direction_info[-1],
                'specification': focus_info[4],
                'learning_plan': focus_info[5],
                'calendar_chedule': focus_info[6],
                'documents': focus_info[7]
        }



