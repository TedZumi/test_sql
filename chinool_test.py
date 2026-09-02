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

def get_table_info(table_name):
    print(f"\nСостав таблицы {table_name}:")
    cursore.execute(f"""
        PRAGMA table_info({table_name});
    """)
    results = cursore.fetchall()
    for result in results:
        print(result)


""" Уровень 1. Базовый SELECT + WHERE + ORDER BY + LIMIT """
# # Первые 10 треков в алфавитном порядке
# get_table_info("Track")
# print(f"\nПервые 10 треков в алфавитном порядке:")
# cursore.execute("""
#     SELECT Name, Composer, UnitPrice FROM Track
#     ORDER BY Name
#     LIMIT 10;
# """)
# for result in cursore.fetchall():
#     print(result)

# # Все клиенты из USA и Canada отсортированы по фамилии
# get_table_info("Customer")
# print(f"\nВсе клиенты из USA и Canada отсортированы по фамилии:")
# cursore.execute("""
#     SELECT * FROM Customer
#     WHERE Country = "USA" OR Country = "Canada"
#     ORDER BY LastName;
# """)
# for result in cursore.fetchall():
#     print(result)

# # 10 самых дорогих треков
# print(f"\n10 самых дорогих треков:")
# cursore.execute("""
#     SELECT Name, UnitPrice FROM Track
#     ORDER BY UnitPrice
#     LIMIT 10;
# """)
# for result in cursore.fetchall():
#     print(result)
    
# # все счета за 2025 год, отсортированные по дате (сначала свежие)
# get_table_info("Invoice")
# print(f"\nвсе счета за 2025 год, отсортированные по дате (сначала свежие):")
# cursore.execute("""
#     SELECT * FROM Invoice
#     WHERE InvoiceDate LIKE '2025%'
#     ORDER BY InvoiceDate DESC;
# """)
# for result in cursore.fetchall():
#     print(result)
    
# # 5 самых длинных треков - название, длительность (сек)
# print(f"\n5 самых длинных треков - название, длительность (сек):")
# cursore.execute("""
#     SELECT Name, Milliseconds/1000 FROM Track
#     ORDER BY Milliseconds DESC
#     LIMIT 5;
# """)
# for result in cursore.fetchall():
#     print(result)


""" Уровень 2. DISTINCT + JOIN """
# уникальные имена композиторов, у которых есть треки в базе (по алфавиту)
# get_table_info("Track")
# get_table_info("Artist")
# print(f"\nуникальные имена композиторов, у которых есть треки в базе (по алфавиту):")
# cursore.execute("""
#     SELECT DISTINCT Composer 
#     FROM Track
#     WHERE Composer IS NOT NULL
#     ORDER BY Composer;
# """)
# for result in cursore.fetchall():
#     print(result)

# треки с названиями альбомов (20)
# get_table_info("Track")
# get_table_info("Album")
# print(f"\nтреки с названиями альбомов (20):")
# cursore.execute("""
#     SELECT 
#         Track.Name AS Track_N,
#         Album.Title AS Album_N
#     FROM Track
#     LEFT JOIN Album
#         ON Track.AlbumID = Album.AlbumID
#     LIMIT 20;
# """)
# for result in cursore.fetchall():
#     print(result)

# все треки с именами исполнителей (10)
# get_table_info("Track")
# get_table_info("Album")
# get_table_info("Artist")
# print(f"\nсписок треков с названиями альбомов, в которых они находятся (20):")
# cursore.execute("""
#     SELECT 
#         Track.Name AS Track,
#         Artist.Name AS Artist
#     FROM Track
#     LEFT JOIN Album
#         ON Track.AlbumId = Album.AlbumId
#     LEFT JOIN Artist
#         ON Album.ArtistId = Artist.ArtistId
#     LIMIT 10;
# """)
# for result in cursore.fetchall():
#     print(result)

# уникальные страны клиентов, у которых есть счета (сорт по стране)
# get_table_info("Customer")
# get_table_info("Invoice")
# print(f"\nуникальные страны клиентов, у которых есть счета (сорт по стране):")
# cursore.execute("""
#     SELECT DISTINCT Customer.Country AS Country
#     FROM Customer
#     JOIN Invoice
#         ON Customer.CustomerId = Invoice.CustomerId
#     ORDER BY Country;
# """)
# for result in cursore.fetchall():
#     print(result)
    
# список треков с названиями жанров (genres) и медиатипов (media_types) 15
# get_table_info("Track")
# get_table_info("MediaType")
# get_table_info("Genre")
# print(f"\nсписок треков с названиями жанров (genres) и медиатипов (media_types) 15:")
# cursore.execute("""
#     SELECT 
#         Track.Name AS Track_N,
#         Genre.Name AS Genre_N,
#         MediaType.Name AS MediaType_N
#     FROM Track
#     LEFT JOIN Genre
#         ON Track.GenreId = Genre.GenreId
#     LEFT JOIN MediaType
#         ON Track.MediaTypeId = MediaType.MediaTypeId
#     LIMIT 15;
# """)
# for result in cursore.fetchall():
#     print(result)


""" Уровень 4. Комбинированный: WHERE + GROUP BY + HAVING + ORDER BY + LIMIT + OFFSET """
""" Найти топ-5 самых продаваемых треков (по количеству продаж в invoice_items) за 2025 год. 
Вывести название трека, количество продаж и общую выручку. 
Использовать JOIN, WHERE, GROUP BY, ORDER BY, LIMIT """
# get_table_info("Track")
# get_table_info("Invoice")
# get_table_info("InvoiceLine")
# print(f"\nтоп-5 самых продаваемых треков за 2025 год:")
# cursore.execute("""
#     SELECT 
#         Track.Name AS Track_N,
#         COUNT(InvoiceLine.Quantity) AS Count_sale,
#         SUM(InvoiceLine.UnitPrice * InvoiceLine.Quantity) AS Gain
#     FROM Track
#     JOIN InvoiceLine
#         ON Track.TrackId = InvoiceLine.TrackId
#     JOIN Invoice 
#         ON InvoiceLine.InvoiceId = Invoice.InvoiceId
#     WHERE strftime('%Y', Invoice.InvoiceDate) = '2025' 
#     GROUP BY Track_N
#     ORDER BY Count_sale DESC
#     LIMIT 5;
# """)
# print("-"*150)
# print(f"{'Трек':<50} | {'Продажи':<10} | {'Выручка':<15}")
# print("-"*150)
# for Track_N, Count_sale, Gain in cursore.fetchall():
#     print(f"{Track_N:<50} | {Count_sale:<10} | {Gain:<15}")

""" Найти клиентов, которые сделали больше 5 заказов и потратили более 50 долларов. 
Вывести имя клиента, количество заказов и общую сумму. 
Использовать HAVING, JOIN, GROUP BY """
# get_table_info("Customer")
# get_table_info("Invoice")
# get_table_info("InvoiceLine")
# print(f"\nклиенты которые сделали больше 5 заказов и потратили более 50 долларов:")
# cursore.execute("""
#     SELECT 
#         Customer.FirstName AS Customer_N,
#         COUNT(DISTINCT Invoice.InvoiceId) AS OrderCount,
#         SUM(InvoiceLine.UnitPrice * InvoiceLine.Quantity) AS Gain
#     FROM Customer
#     JOIN Invoice
#         ON Customer.CustomerId = Invoice.CustomerId
#     JOIN InvoiceLine 
#         ON InvoiceLine.InvoiceId = Invoice.InvoiceId
#     GROUP BY Customer.CustomerId
#     HAVING OrderCount > 5 AND Gain > 10 
#     ORDER BY Gain DESC;
# """)
# print("-"*150)
# print(f"{'Имя клиента':<50} | {'Количество заказов':<10} | {'Общая сумма':<15}")
# print("-"*150)
# for Customer_N, OrderCount, Gain in cursore.fetchall():
#     print(f"{Customer_N:<50} | {OrderCount:<10} | {Gain:<15}")
    
""" Вывести список жанров, у которых средняя длительность трека больше 300000 мс, 
но только для треков, выпущенных до 2010 года. 
Использовать JOIN, WHERE, GROUP BY, HAVING, ORDER BY по средней длительности """
# get_table_info("Track")
# get_table_info("Genre")
# print(f"\nсписок жанров, у которых средняя длительность трека больше 300000 мс (до 2010):")
# cursore.execute("""
#     SELECT 
#         Genre.Name AS Genre_N,
#         ROUND(AVG(Track.Milliseconds), 0) AS Time,
#         COUNT(*) AS TrackCount
#     FROM Track
#     JOIN Genre
#         ON Track.GenreId = Genre.GenreId
#     GROUP BY Genre.GenreId
#     HAVING Time > 300000 
#     ORDER BY Time DESC;
# """)
# print("-"*150)
# print(f"{'Жанр':<50} | {'Среднее время':<10} | {'Треков':<15}")
# print("-"*150)
# for Genre_N, Time, TrackCount in cursore.fetchall():
#     print(f"{Genre_N:<50} | {Time:<10} | {TrackCount:<15}")

""" Вывести треки с пометкой Дорогой или Дешевый """
get_table_info("Track")
print(f"\nСписок дорогих и дешевых треков:")
cursore.execute(""" 
    SELECT 
        Name, 
        Composer, 
        UnitPrice,
        CASE
            WHEN UnitPrice > 1 THEN "Дорогой"
            ELSE "Обычный"
        END AS PriceCategory
    FROM Track
    LIMIT 50  
""")
print("-"*150)
print(f"{'Название':<50} | {'Автор':<100} | {'Цена':<15} | {'Ценовая категория':<15}")
print("-"*150)
for Name, Composer, UnitPrice, PriceCategory in cursore.fetchall():
    print(f"{Name:<50} | {Composer:<100} | {UnitPrice:<15} | {PriceCategory:<15}")
    
print("\nТреки с композитором или 'Неизвестен':")
cursore.execute(""" 
    SELECT 
        Name, 
        CASE
            WHEN Composer IS NULL THEN "Неизвестный исполнитель"
            ELSE Composer
        END AS ComposerName
    FROM Track
    LIMIT 500  
""")
print("-"*150)
print(f"{'Название':<50} | {'Автор':<100}")
print("-"*150)
for Name, ComposerName in cursore.fetchall():
    print(f"{Name:<50} | {ComposerName:<100}")


""" Расчет общей выручки с условиями:
Если цена трека меньше 0.99, считаем её как 0.99 (минимальная цена).
Если трек длинный (> 5 минут), добавляем к цене наценку 0.50 цента."""
print("\nОбщая выручка с условиями:")
cursore.execute("""
    SELECT
        SUM(
            (CASE
                WHEN Track.UnitPrice < 0.99 THEN 0.99
                ELSE Track.UnitPrice
            END
            +
            CASE
                WHEN Track.Milliseconds / 60000 > 5 THEN 0.50
                ELSE 0
            END)
            * InvoiceLine.Quantity
        ) AS TotalRevenue
    FROM Track
    JOIN InvoiceLine
        ON InvoiceLine.TrackId = Track.TrackId;
""")
total = cursore.fetchone()[0]
print(f"  Итоговая выручка с наценками: ${total:.2f}")