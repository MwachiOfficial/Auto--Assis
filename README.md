
# AutoAssist
## Overview
AutoAssist is a command-line application designed to manage cars, their maintenance records, and associated comments. The system allows users to perform CRUD (Create, Read, Update, Delete) operations on cars, maintenance records, and comments.

# Features
Car Management: Add, view, update, and delete car information.
Maintenance Management: Record and manage maintenance activities for each car.
Comment Management: Add, view, update, and delete comments related to maintenance activities.
Installation
Clone the repository:


## cd Auto--Assist
## Set up the virtual environment:


python -m venv venv

Install dependencies:


pip install -r requirements.txt
## Set up the database:
Ensure car_management.db is created and the tables are set up with the required schema. You can use the following script to set up the tables:

## python

import sqlite3

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
    car_vin TEXT,
    maintenance_type TEXT,
    description TEXT,
    date_performed TEXT,
    FOREIGN KEY (car_vin) REFERENCES cars (vin)
);
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

## Usage
To start the application, run:


python main.py
Main Menu
0: Exit the program
1: Cars Menu
2: Maintenance Menu
3: Comments Menu
Cars Menu
0: Back to Main Menu
1: List all cars
2: Find car by make
3: Find car by VIN
4: Create car
5: Update car
6: Delete car
Maintenance Menu
0: Back to Main Menu
1: List all maintenances
2: Find maintenance by id
3: Create maintenance
4: Update maintenance
5: Delete maintenance
Comments Menu
0: Back to Main Menu
1: List all comments
2: Find comment by id
3: Create comment
4: Update comment
5: Delete comment
Class Information
Car Class
The Car class represents a car and includes methods to save, retrieve, and delete car records.

## Attributes
vin (str): Vehicle Identification Number, primary key.
make (str): Car make.
model (str): Car model.
year (int): Manufacturing year.
Methods
__init__(self, vin, make, model, year): Constructor to initialize a car instance.
save(self): Saves the car to the database. If the car already exists, it updates the existing record.
get_all(): Retrieves all car records from the database.
find_by_make(make): Finds cars by their make.
find_by_id(cls, vin): Finds a car by its VIN.
delete(self): Deletes the car from the database.
Maintenance Class
The Maintenance class represents maintenance records for cars and includes methods to save, retrieve, and delete maintenance records.

## Attributes
car_vin (str): VIN of the car associated with the maintenance record.
maintenance_type (str): Type of maintenance.
description (str): Description of the maintenance.
date_performed (str): Date the maintenance was performed.
Methods
__init__(self, car_vin, maintenance_type, description, date_performed): Constructor to initialize a maintenance instance.
save(self): Saves the maintenance record to the database. If the record already exists, it updates the existing record.
get_all(cls): Retrieves all maintenance records from the database.
find_by_id(cls, car_vin): Finds a maintenance record by the car's VIN.
delete(self): Deletes the maintenance record from the database.
Comment Class
The Comment class represents comments associated with maintenance records and includes methods to save, retrieve, and delete comments.

## Attributes
maintenance_id (int): ID of the maintenance record associated with the comment.
comment (str): The comment text.
Methods
__init__(self, maintenance_id, comment): Constructor to initialize a comment instance.
save(self): Saves the comment to the database.
get_all(): Retrieves all comments from the database.
find_by_id(cls, id_): Finds a comment by its ID.
delete(self): Deletes the comment from the database.
update(self, new_comment): Updates the comment text in the database.
Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
## Ryan Anzaye

