import sqlite3

class DataBase:
    def __init__(self, name):
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()
    
    def create_table(self, name, columns, pk=None):
        cols = []
        for col, type_ in columns.items():
            col_def = f"{col} {type_}"
            if col == pk:
                col_def += " PRIMARY KEY AUTOINCREMENT"
            cols.append(col_def)
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {name} ({', '.join(cols)});")
        self.conn.commit()
    
    def insert_many(self, table, data_list):
        cols = ', '.join(data_list[0].keys())
        vals = ', '.join(['?' for _ in data_list[0]])
        self.cursor.executemany(f"INSERT INTO {table} ({cols}) VALUES ({vals});", 
                                [list(d.values()) for d in data_list])
        self.conn.commit()
    
    def query(self, sql, params=()):
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()
    
    def close(self):
        self.conn.close()

# --- ВАША БАЗА ЗДЕСЬ ---

db = DataBase('my_training.db')

# Создаете таблицу
db.create_table('students', 
                {'id': 'INTEGER', 'name': 'TEXT', 'score': 'INTEGER'}, 
                pk='id')

# Заполняете данными
db.insert_many('students', [
    {'name': 'Анна', 'score': 95},
    {'name': 'Борис', 'score': 85},
    {'name': 'Виктор', 'score': 90},
])

# Проверяете
print(db.query('SELECT * FROM students ORDER BY score DESC;'))

db.close()