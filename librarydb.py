import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

db = mysql.connector.connect(
    host = os.getenv('dbhost'),
    user = os.getenv('dbuser'),
    password = os.getenv('dbpassword'),
    database = os.getenv('dbname')
)
# dbcursor = db.cursor()
# dbcursor.execute('select * from books')
# result = dbcursor.fetchall()

class Users:
    def sign_up(self,username,password):
        db.ping(reconnect=True)
        cursor = db.cursor(dictionary=True,buffered=True)
        value = 'insert into admins(username,passwd) values(%s,%s)'
        cursor.execute(value,(username,password))
        db.commit()
        cursor.close()

    def get_username(self,username):
        db.ping(reconnect=True)
        cursor = db.cursor(dictionary=True,buffered=True)
        querry = 'select * from admins where username = %s'
        cursor.execute(querry,(username,))
        result = cursor.fetchone()
        cursor.close()
        return result

class Operate(Users):
    def view(self):
        db.ping(reconnect=True)
        cursor = db.cursor(dictionary=True,buffered=True)
        querry = 'select * from books'
        cursor.execute(querry)
        result = cursor.fetchall()
        cursor.close()
        return result
    def available(self):
        db.ping(reconnect=True)
        cursor = db.cursor(dictionary=True,buffered=True)
        querry = 'select * from books where status = "available"'
        cursor.execute(querry)
        result = cursor.fetchall()
        cursor.close()
        return result
    def borrowed(self):
        db.ping(reconnect=True)
        cursor = db.cursor(dictionary=True,buffered=True)
        querry = 'select * from books where status = "borrowed"'
        cursor.execute(querry)
        result = cursor.fetchall()
        cursor.close()
        return result

    def add_books(self,title,author):
        db.ping(reconnect=True)
        cursor = db.cursor()
        querry = 'insert into books (title,author) values (%s,%s)'
        result = cursor.execute(querry,(title,author,))
        db.commit()
        db.close()
        cursor.close()
        return result

class Actions(Operate):
    def delete(self,id):
        db.ping(reconnect=True)
        cursor = db.cursor(dictionary=True,buffered=True)
        querry = 'delete from books where book_id = %s'
        result = cursor.execute(querry,(id,))
        db.commit()
        cursor.close()
        db.close()
        return result
    def update_to_available(self,book_id):
        db.ping(reconnect=True)
        cursor = db.cursor(dictionary=True,buffered=True)
        querry = 'update books set status = "available" where book_id = %s'
        result = cursor.execute(querry,(book_id,))
        db.commit()
        cursor.close()
        db.close()
        return result
    def update_to_borrowed(self,book_id):
        db.ping(reconnect=True)
        cursor = db.cursor(dictionary=True,buffered=True)
        querry = 'update books set status = "borrowed" where book_id = %s'
        result = cursor.execute(querry,(book_id,))
        db.commit()
        cursor.close()
        db.close()
        return result
    def book_available(self,book_id):
        db.ping(reconnect=True)
        cursor = db.cursor(dictionary=True,buffered=True)
        querry = 'select * from books where status = "available" and book_id = %s'
        cursor.execute(querry,(book_id,))
        result = cursor.fetchone()
        cursor.close()
        return result
    def book_borrowed(self,book_id):
        db.ping(reconnect=True)
        cursor = db.cursor(dictionary=True,buffered=True)
        querry = 'select * from books where status = "borrowed" and book_id = %s'
        cursor.execute(querry,(book_id,))
        result = cursor.fetchone()
        cursor.close()
        return result