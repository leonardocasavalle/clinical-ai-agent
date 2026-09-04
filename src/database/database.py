import sqlite3
from pathlib import Path


class ClinicalDatabase:
    """
    SQLite database layer for the Clinical AI Agent.

    Uses synthetic demo data only.
    """

    def __init__(self, database_path="src/data/clinical.db"):
        self.database_path = Path(database_path)

    def connect(self):
        """
        Create and return a SQLite database connection.
        """
        self.database_path.parent.mkdir(parents=True, exist_ok=True)

        return sqlite3.connect(self.database_path)

    def initialize(self):
        """
        Create the database tables if they do not exist.
        """
        with self.connect() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS patients (
                    patient_id INTEGER PRIMARY KEY,
                    age INTEGER NOT NULL,
                    sex TEXT NOT NULL
                )
                """
            )

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS lab_results (
                    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    patient_id INTEGER NOT NULL,
                    test_name TEXT NOT NULL,
                    result_value REAL NOT NULL,
                    unit TEXT NOT NULL,
                    result_date TEXT NOT NULL,
                    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
                )
                """
            )

            connection.commit()

    def seed_demo_data(self):
        """
        Insert synthetic clinical data for demonstration purposes.
        """
        with self.connect() as connection:
            cursor = connection.cursor()

            cursor.execute("DELETE FROM lab_results")
            cursor.execute("DELETE FROM patients")

            patients = [
                (1001, 45, "F"),
                (1002, 52, "M"),
                (1003, 38, "F"),
            ]

            lab_results = [
                (1001, "Glucose", 98.0, "mg/dL", "2026-08-20"),
                (1001, "Cholesterol", 185.0, "mg/dL", "2026-08-20"),
                (1002, "Glucose", 112.0, "mg/dL", "2026-08-22"),
                (1002, "Cholesterol", 210.0, "mg/dL", "2026-08-22"),
                (1003, "Glucose", 91.0, "mg/dL", "2026-08-25"),
                (1003, "Cholesterol", 172.0, "mg/dL", "2026-08-25"),
            ]

            cursor.executemany(
                """
                INSERT INTO patients (patient_id, age, sex)
                VALUES (?, ?, ?)
                """,
                patients,
            )

            cursor.executemany(
                """
                INSERT INTO lab_results (
                    patient_id,
                    test_name,
                    result_value,
                    unit,
                    result_date
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                lab_results,
            )

            connection.commit()

    def get_patient_by_id(self, patient_id):
        """
        Retrieve a patient by ID.
        """
        with self.connect() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT patient_id, age, sex
                FROM patients
                WHERE patient_id = ?
                """,
                (patient_id,),
            )

            return cursor.fetchone()

    def get_recent_lab_results(self, patient_id):
        """
        Retrieve laboratory results for a patient.
        """
        with self.connect() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT test_name, result_value, unit, result_date
                FROM lab_results
                WHERE patient_id = ?
                ORDER BY result_date DESC
                """,
                (patient_id,),
            )

            return cursor.fetchall()