import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rajdarji@3456",
    database="food_blog_ai"
)

cursor = db.cursor(dictionary=True)