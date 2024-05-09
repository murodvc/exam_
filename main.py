# ALMAMATOV JAVLONBEK
# 1-misol
# Postgresql bazaga python yordamida ulaning . Product nomli jadval yarating (id,name,price, color,image) .

# db = product
# user = postgres
# password = 12345jn
# port = 5432
# host = localhost

import psycopg2
# def connect(db, user, password, port, host):
#     try:
#         conn = psycopg2.connect(
#             dbname=db,
#             user=user,
#             password=password,
#             port=port,
#             host=host
#         )
#         cur = conn.cursor()
#         print("Ma'lumotlar bazasiga muvaffaqiyatli ulandi!")
#         return conn, cur
#     except Exception as e:
#         print(f"Ma'lumotlar bazasiga ulanishda xato: {e}")
#         return None, None
#
# def create_table(cur):
#     try:
#         create_table_query = """CREATE TABLE product(
#                                 id serial primary key,
#                                 name varchar(50) not null,
#                                 price int,
#                                 color varchar(50),
#                                 image text ) ;"""
#         cur.execute(create_table_query)
#         conn.commit()
#         print(f"Jadval product muvaffaqiyatli yaratildi!")
#
#     except Exception as e:
#         print(f"Jadval yaratishda xato: {e}")
#
#
# dbname = input("Ma'lumotlar bazasi nomini kiriting: ")
# username = input("Foydalanuvchi nomini kiriting: ")
# password = input("Parolni kiriting: ")
# port = input("Port raqamini kiriting: ")
# host = input("Host manzilini kiriting: ")
#
# conn, cur = connect(db=dbname, user=username, password=password, port=port, host=host)
# create_table(cur)

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
# 2 - misol
# 2.Insert_product , select_all_products , update_product,delete_product nomli funksiyalar yarating.

# def insert_tables(cur):
#     try:
#         cur.execute(F"INSERT INTO product (name,price,color,image) VALUES ('olma',10.000,'qizil','olma.png');")
#         conn.commit()
#         print("Ma'lumotlar kiritildi !!!")
#     except Exception as e:
#         print(f"Jadvallarni ro'yxatga olishda xato: {e}")
#
# def select_all_product(cur):
#     cur.execute(f"select * from product;")
#     for product in cur.fetchall():
#         print(product)
#
#
#
# def update_product(cur,name,price,color,image,id):
#     update_query = """update product set name = %s, price = %s, color = %s, image = %s  where id = %s;"""
#     data = (cur,name,price,color,image,id)
#     cur.execute(update_query, data)
#     conn.commit()
#     cur.close()
#     conn.close()
#
#
# def delete_ptoduct(cur,id):
#     delete_product = """
#         DELETE FROM product WHERE id = %s;
#
#     """
#     cur.execute(delete_product,id)
#     conn.commit()
#
#
# insert_tables(cur)
# select_all_product(cur)
#
# update_product(cur,"......","......",".......","......",1)
#
# delete_ptoduct(cur,1)

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
# 3 - misol
# .Alphabet nomli class yozing .
# class obyektlarini iteratsiya qilish imkoni  bo’lsin (iterator).
# obyektni for sikli orqali iteratsiya qilinsa 26 ta alifbo xarflari chiqsin

# class Alphabet:
#     def __init__(self):
#         self.letters = 'abcdefghijklmnopqrstuvwxyz'
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.letters):
#             letter = self.letters[self.index]
#             self.index += 1
#             return letter
#         else:
#             raise StopIteration
#
# alphabet = Alphabet()
#
# for letter in alphabet:
#     print(letter, end=" ")


# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

#  4 - misol
# print_numbers va print_leters nomli funksiyalar yarating.
# prit_numbers funksiyasi (1,5) gacha bo’lgan sonlarni , print_letters esa  ‘’ABCDE” belgilarni loop da bitta dan time sleep(1) qo’yib ,
# parallel 2ta thread yarating.Ekranga parallel ravishda itemlar chiqsin.

# import threading
# import time
#
# def print_namber():
#     for i in range(1,6):
#         print(i)
#
# def print_leters():
#     for i in "ABCDE":
#         print(i)
#         time.sleep(1)
#
# t1 = threading.Thread(target=print_namber())
# t2 = threading.Thread(target=print_leters())
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# 5 - misol
# 5.Product nomli class yarating (1 – misoldagi Product ).
# Product classiga save() nomli object method yarating.
# Uni vazifasi object attributelari orqali bazaga saqlasin.

# class Product:
#     def __init__(self, name, price, color, image):
#         self.name = name
#         self.price = price
#         self.color = color
#         self.image = image
#
#     def save(self, cur):
#         try:
#             insert_query = """INSERT INTO product (name, price, color, image)
#                               VALUES (%s, %s, %s, %s);"""
#             cur.execute(insert_query, (self.name, self.price, self.color, self.image))
#             conn.commit()
#             print(f"Product saved successfully!")
#         except Exception as e:
#             print(f"Error saving product: {e}")
#
# product1 = Product(name="Widget", price=100, color="Blue", image="widget.jpg")
# product1.save(cur)


# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
# 6-misol
# 6.DbConnect nomli ContextManager yarating. Va uning vazifasi python orqali PostGresqlga ulanish (conn,cur)

# import psycopg2
#
# class DbConnect:
#     def __init__(self, db_params):
#         self.db_params = db_params
#         self.conn = psycopg2.connect(**self.db_params)
#
#     def __enter__(self):
#         self.cur = self.conn.cursor()
#         return self.cur
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.conn.commit()
#         self.conn.close()
#
# db_params = {
#     "dbname": input("Ma'lumotlar bazasining nomini kiriting: "),
#     "user": input("Foydalanuvchi nomini kiriting: "),
#     "password": input("Parolni kiriting: "),
#     "host": input("Hostni kiriting: "),
#     "port": input("Portni kiriting: ")
# }
# DbConnect(db_params)












