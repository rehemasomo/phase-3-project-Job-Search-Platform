
from config import get_db_connection

class SavedSearch:
    @staticmethod
    def create(user_id, search_query):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO saved_searches (user_id, search_query) VALUES (?, ?)", 
                       (user_id, search_query))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(saved_search_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM saved_searches WHERE id = ?", (saved_search_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def update(saved_search_id, search_query):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE saved_searches SET search_query = ? WHERE id = ?", 
                       (search_query, saved_search_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get(saved_search_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM saved_searches WHERE id = ?", (saved_search_id,))
        saved_search = cursor.fetchone()
        conn.close()
        return saved_search

    @staticmethod
    def list():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM saved_searches")
        saved_searches = cursor.fetchall()
        conn.close()
        return saved_searches