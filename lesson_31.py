import sqlite3
import pandas

connection = sqlite3.connect('sample.db')  # подключение

cursor = connection.cursor()  # курсор

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS products (
#     id integer PRIMARY KEY AUTOINCREMENT, name text, price real, amount integer
#     )
    # """)

# cursor.execute("""
#     INSERT INTO products ( name, price, amount)
#     VALUES (?, ?, ?)
#     """, ('яблоко', 100, 5)
# )
# products = [[f'product {i}', i *100, i] for i in range(100)]
#
# for i_product in products:
#     cursor.execute("""
#     INSERT INTO products (name, price, amount)
#     VALUES (:name, :price, :amount)
#     """, {'name': i_product[0], 'price': i_product[1], 'amount': i_product[2]}
# )

query = cursor.execute("""
    SELECT * FROM products
""")
data_frame = pandas.DataFrame(query.fetchall(), columns=['Id', 'Name', 'Price', 'Amount'])

print(data_frame)
print(data_frame.describe())

connection.commit()

connection.close()  # окончение сессии с бд
