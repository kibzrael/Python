import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='kibzrael', database='sql_store'
)

cursor = db.cursor(dictionary=True)

cursor.execute(
    'SELECT DISTINCT customer_id, first_name, birth_date FROM customers WHERE phone IS NULL ORDER BY first_name DESC, customer_id ASC')

print(cursor.fetchall())
