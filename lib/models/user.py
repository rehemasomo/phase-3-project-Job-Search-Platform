
from config import get_db_connection

class User:
    @staticmethod
    def create(username, password, email):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", 
                       (username, password, email))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(username):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE username = ?", (username,))
        conn.commit()
        conn.close()

    @staticmethod
    def update(username, password, email):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET password = ?, email = ? WHERE username = ?", 
                       (password, email, username))
        conn.commit()
        conn.close()

    @staticmethod
    def get(username):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()
        return user

    @staticmethod
    def list():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        conn.close()
        return users
