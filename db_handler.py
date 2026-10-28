
import sqlite3
from pathlib import Path
from datetime import datetime, timezone


# Database location
DATABASE_PATH = (
    Path(__file__).resolve().parent / "willow.db"
)


# --------------------------------------------------
# DATABASE INITIALIZATION
# --------------------------------------------------

def initialize_database():

    connection = sqlite3.connect(DATABASE_PATH)

    try:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS predictions (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                batch_id TEXT,

                source TEXT NOT NULL,

                prediction TEXT NOT NULL,

                model_score REAL,

                created_at TEXT NOT NULL

            )
        """)

        connection.commit()

    finally:
        connection.close()

    print("Willow database initialized successfully.")


# --------------------------------------------------
# SAVE PREDICTION
# --------------------------------------------------

def save_prediction(
    prediction,
    model_score,
    source,
    batch_id=None
):

    connection = sqlite3.connect(DATABASE_PATH)

    try:
        cursor = connection.cursor()

        created_at = datetime.now(
            timezone.utc
        ).isoformat()

        cursor.execute("""
            INSERT INTO predictions (
                batch_id,
                source,
                prediction,
                model_score,
                created_at
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            batch_id,
            source,
            prediction,
            model_score,
            created_at
        ))

        connection.commit()

        return cursor.lastrowid

    finally:
        connection.close()


# --------------------------------------------------
# RETRIEVE PREDICTION HISTORY
# --------------------------------------------------

def get_prediction_history(limit=100):

    connection = sqlite3.connect(DATABASE_PATH)

    try:
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                id,
                batch_id,
                source,
                prediction,
                model_score,
                created_at
            FROM predictions
            ORDER BY id DESC
            LIMIT ?
        """, (limit,))

        records = cursor.fetchall()

        return [dict(record) for record in records]

    finally:
        connection.close()


# --------------------------------------------------
# COUNT PREDICTIONS
# --------------------------------------------------

def get_prediction_count():

    connection = sqlite3.connect(DATABASE_PATH)

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT COUNT(*) FROM predictions
        """)

        return cursor.fetchone()[0]

    finally:
        connection.close()
