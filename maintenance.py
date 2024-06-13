import sqlite3

class Maintenance:
    def __init__(self, maintenance_id, car_vin, maintenance_type, description, date_performed):
        self.maintenance_id = maintenance_id
        self.car_vin = car_vin
        self.maintenance_type = maintenance_type
        self.description = description
        self.date_performed = date_performed

    def save(self):
        conn = sqlite3.connect("car_management.db")
        cursor = conn.cursor()
        
        # Fetch the existing record to compare
        cursor.execute("SELECT * FROM maintenance WHERE maintenance_id=?", (self.maintenance_id,))
        existing_record = cursor.fetchone()
        
        # Compare fields to decide between INSERT or UPDATE
        if existing_record:
            # Update existing record
            cursor.execute("""
                UPDATE maintenance SET car_vin=?, maintenance_type=?, description=?, date_performed=?
                WHERE maintenance_id=?
            """, (self.car_vin, self.maintenance_type, self.description, self.date_performed, self.maintenance_id))
        else:
            # Insert new record
            cursor.execute("""
                INSERT INTO maintenance (maintenance_id, car_vin, maintenance_type, description, date_performed)
                VALUES (?,?,?,?,?)
            """, (self.maintenance_id, self.car_vin, self.maintenance_type, self.description, self.date_performed))
        
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect("car_management.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM maintenance")
        maintenances = cursor.fetchall()
        conn.close()
        return maintenances

    @classmethod
    def find_by_id(cls, maintenance_id):
        conn = sqlite3.connect("car_management.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM maintenance WHERE maintenance_id=?", (maintenance_id,))
        maintenance_tuple = cursor.fetchone()
        conn.close()
        if maintenance_tuple:
            return cls(*maintenance_tuple)
        else:
            return None

    def delete(self):
        conn = sqlite3.connect("car_management.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM maintenance WHERE maintenance_id=?", (self.maintenance_id,))
        conn.commit()
        conn.close()