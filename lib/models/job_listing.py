from config import get_db_connection

class JobListing:
    @staticmethod
    def create(title, description, company):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO job_listings (title, description, company) VALUES (?, ?, ?)", 
                       (title, description, company))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(job_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM job_listings WHERE id = ?", (job_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def update(job_id, title, description, company):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE job_listings SET title = ?, description = ?, company = ? WHERE id = ?", 
                       (title, description, company, job_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get(job_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM job_listings WHERE id = ?", (job_id,))
        job = cursor.fetchone()
        conn.close()
        return job

    @staticmethod
    def list():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM job_listings")
        jobs = cursor.fetchall()
        conn.close()
        return jobs