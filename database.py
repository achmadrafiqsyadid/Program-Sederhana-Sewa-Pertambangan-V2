import mysql.connector
from mysql.connector import Error

def connect_db():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pertambangan",
            port=3306
        )

        if not db.is_connected():
            raise Error("Koneksi ke database gagal.")

        return db

    except Error as e:
        from PySide6.QtWidgets import QMessageBox
        QMessageBox.critical(
            None,
            "Database Error",
            f"Gagal terhubung ke database MySQL:\n{e}"
        )
        return None
