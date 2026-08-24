import sqlite3

conn = sqlite3.connect("chinook.sqlite")
cursore = conn.cursor()

# вывод всех таблиц
cursore.execute("""
    SELECT name 
    FROM sqlite_master 
    WHERE type='table';
""")
tabels = cursore.fetchall()
for table in tabels:
    print(table)

cursore.execute("""
    SELECT *
    FROM 'Artist';
""")
artists = cursore.fetchall()
# print("\nИСПОЛНИТЕЛИ\n")
# for artist in artists:
#     print(artist)

# инфа по атрибутам таблицы с треками
cursore.execute("""
    PRAGMA table_info(Track);
""")
# print("\nИНФО ПО ТРЕКАМ\n")
# for col in cursore.fetchall():
#     print(col)


cursore.execute("""
    SELECT Name, UnitPrice
    FROM 'Track'
    WHERE Composer = 'Queen';
""")
tracks = cursore.fetchall()
# print("\nТРЕКИ QUEEN\n")
# for track in tracks:
#     print(track)

# инфа по атрибутам таблицы "Покупатели"
cursore.execute("""
    PRAGMA table_info(Customer);
""")
print("\nАТРИБУТЫ ТАБЛИЦЫ ПОКУПАТЕЛИ\n")
for col in cursore.fetchall():
    print(col)

# инфа по покупателям
cursore.execute("""
    SELECT FirstName, LastName, Email
    FROM Customer
    WHERE SupportRepId = 5
    ORDER BY FirstName
    LIMIT 10;
""")
customers = cursore.fetchall()
print("\nПОКУПАТЕЛИ\n")
for customer in customers:
    print(customer)