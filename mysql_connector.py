import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "salar",
    password = "salar09128668568",
    database = "mydatabase"
)



mycursor = mydb.cursor()


mycursor.execute("CREATE DATABASE mydatabase")


mycursor.execute("CREATE table mytable (firse_name VARCHAR(255), last_name VARCHAR(255))")

print(mydb)

