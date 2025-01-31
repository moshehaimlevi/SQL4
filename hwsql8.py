############################# SECTION NUMBER 1:

import sqlite3

def update_query(cursor, conn, query, params):
    cursor.execute(query, params)
    conn.commit()

def read_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


conn = sqlite3.connect('SQLiteHW8.db')
conn.row_factory = sqlite3.Row

cursor = conn.cursor()


create_table_query = '''
CREATE TABLE IF NOT EXISTS garage (
    fix_id INTEGER PRIMARY KEY AUTOINCREMENT,
    car_number TEXT UNIQUE NOT NULL,
    car_problem TEXT NOT NULL,
    fixed BOOLEAN DEFAULT FALSE,
    owner_ph TEXT NOT NULL
);
'''
cursor.execute(create_table_query)
conn.commit()


new_garage_car_number = str(input("What's the car number? "))
new_garage_car_problem = str(input('Enter the car problem: '))
new_garage_fixed = input('Is the car fixed? (false / true): ')
new_garage_owner_ph = str(input("Enter the owner's phone number: "))


update_query(cursor, conn, "INSERT INTO garage (car_number, car_problem, fixed, owner_ph) VALUES (?, ?, ?, ?)",
             (new_garage_car_number, new_garage_car_problem, new_garage_fixed, new_garage_owner_ph))

car_problem = read_query(cursor, "SELECT * FROM garage")
for item in car_problem:
    print(f"Fix ID: {item['fix_id']}, Car Number: {item['car_number']}, Problem: {item['car_problem']}, "
          f"Fixed: {item['fixed']}, Owner's Phone: {item['owner_ph']}")

conn.close()

########################################## SECTION NUMBER 2:

import sqlite3

def update_query(cursor, conn, query, params):
    cursor.execute(query, params)
    conn.commit()

def read_query(cursor, query, params=None):
    cursor.execute(query, params or [])
    return cursor.fetchall()

conn = sqlite3.connect('SQLiteHW8.db')
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

car_number = int(input("Enter the license number of the vehicle: "))

vehicle_check_query = "SELECT * FROM garage WHERE car_number = ?"
vehicle_data = read_query(cursor, vehicle_check_query, (car_number,))

if not vehicle_data:
    print("The vehicle is not in the garage.")
else:
    fixed_status = vehicle_data[0]['fixed']
    if fixed_status == 1:
        print("The vehicle has already been fixed. The repair tip has already ended.")
    else:
        update_query(cursor, conn, "UPDATE garage SET fixed = 1 WHERE car_number = ?", (car_number,))
        print("The vehicle has been marked as fixed.")

conn.close()

################################## SECTION NUMBER 4:

import sqlite3

def read_query(cursor, query, params=None):
    cursor.execute(query, params or [])
    return cursor.fetchall()

conn = sqlite3.connect('SQLiteHW8.db')
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

broken_down_count_query = "SELECT COUNT(*) FROM garage WHERE fixed = 0"

broken_down_vehicles = read_query(cursor, broken_down_count_query)

count = broken_down_vehicles[0][0] if broken_down_vehicles else 0

print(f"Number of vehicles waiting for treatment: {count}")

conn.close()












