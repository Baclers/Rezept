
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="rezeptdatenbank"
    )

mycursor = db.cursor()

mycursor.execute("SELECT * from Art")

for x in mycursor:
    print(x)