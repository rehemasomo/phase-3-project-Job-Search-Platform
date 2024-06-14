
from config import get_db_connection

class Application:
    @staticmethod
    def create(user_id, job_id, status):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO applications (user_id, job_id, status) VALUES (?, ?, ?)", 
                       (user_id, job_id, status))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(application_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM applications WHERE id = ?", (application_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def update(application_id, status):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE applications SET status = ? WHERE id = ?", 
                       (status, application_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get(application_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM applications WHERE id = ?", (application_id,))
        application = cursor.fetchone()
        conn.close()
        return application

    @staticmethod
    def list():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM applications")
        applications = cursor.fetchall()
        conn.close()
        return applications