import sqlite3

def dict_factory(cursor, row):
    fields = []

    for column in cursor.description:
        fields.append(column[0])
    
    result_dict = {}
    for i in range(len(fields)):
        result_dict[fields[i]] = row[i]

    return result_dict

class EntryDB:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()

    def get_entries(self):
        self.cursor.execute("SELECT * FROM entries")
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()