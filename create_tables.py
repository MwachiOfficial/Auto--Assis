import sqlite3

CONN = sqlite3.connect("car_management.db")
CURSOR = CONN.cursor()

CREATE_CARS_TABLE_QUERY = """
CREATE TABLE cars (
    vin TEXT PRIMARY KEY,
    make TEXT,
    model TEXT,
    year INTEGER
);
"""

CREATE_MAINTENANCE_TABLE_QUERY = """
  CREATE TABLE maintenance (
            id INTEGER PRIMARY KEY,
            car_vin TEXT NOT NULL,
            maintenance_type TEXT NOT NULL,
            description TEXT NOT NULL,
            date_performed DATE NOT NULL
        )
    
"""

CREATE_COMMENT_TABLE_QUERY = """
CREATE TABLE comment (
    id INTEGER PRIMARY KEY,
    maintenance_id INTEGER,
    comment TEXT,
    FOREIGN KEY (maintenance_id) REFERENCES maintenance (id)
);
"""
with sqlite3.connect("car_management.db") as conn:
    conn.execute(CREATE_CARS_TABLE_QUERY)
    conn.execute(CREATE_MAINTENANCE_TABLE_QUERY)
    conn.execute(CREATE_COMMENT_TABLE_QUERY)