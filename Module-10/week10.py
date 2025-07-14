import mysql.connector
"""
Zachary Anderson, Tevyah Hanley, Angela Vargas
Bravo Team
7/8/25
Module 9-10 Milestone#2 Python Script 
*Warning- If you uncomment the database creation line it will create the database with all the info, don't forget to fill in your password when running the code.
"""
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='TLHarts19!'  # Replace with your MySQL password
)
cursor = conn.cursor()

# Uncomment to create the database once
cursor.execute("CREATE DATABASE IF NOT EXISTS outland_adventures")
cursor.execute("USE outland_adventures")

# ------------------ TABLE CREATION ------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS Customer (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    date_joined DATE NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Guide (
    guide_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Trip (
    trip_id INT PRIMARY KEY AUTO_INCREMENT,
    destination VARCHAR(100) NOT NULL,
    region VARCHAR(50) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    visa_required BOOLEAN NOT NULL
)
""")

# New junction table for many-to-many Trip-Guide
cursor.execute("""
CREATE TABLE IF NOT EXISTS TripGuide (
    trip_id INT,
    guide_id INT,
    PRIMARY KEY (trip_id, guide_id),
    FOREIGN KEY (trip_id) REFERENCES Trip(trip_id),
    FOREIGN KEY (guide_id) REFERENCES Guide(guide_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Booking (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    trip_id INT,
    booking_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (trip_id) REFERENCES Trip(trip_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Equipment (
    equipment_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    type VARCHAR(100) NOT NULL,
    equipment_condition VARCHAR(50),
    status VARCHAR(50),
    purchase_date DATE,
    price DECIMAL(10,2)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Employee (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Transaction_Details (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    equipment_id INT,
    employee_id INT,
    transaction_type VARCHAR(20),
    transaction_date DATE,
    return_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (equipment_id) REFERENCES Equipment(equipment_id),
    FOREIGN KEY (employee_id) REFERENCES Employee(employee_id)
)
""")

conn.commit()

# ------------------ DATA INSERTION ------------------

# Employees
employees = [
    ('Blythe Timmerson', 'Owner', 'blythe@outland.com', '555-1001'),
    ('Jim Ford', 'Owner', 'jim@outland.com', '555-1002'),
    ('Anita Gallegos', 'Marketing', 'anita@outland.com', '555-1003'),
    ('Dimitrios Stravopolous', 'Inventory Manager', 'dimitrios@outland.com', '555-1004'),
    ('Mei Wong', 'Ecommerce Developer', 'mei@outland.com', '555-1005')
]
cursor.executemany("INSERT INTO Employee (name, role, email, phone) VALUES (%s, %s, %s, %s)", employees)

# Guides
guides = [
    ('John MacNell', 'john.macnell@outland.com', '555-2001'),
    ('DB Duke Marland', 'duke.marland@outland.com', '555-2002')
]
cursor.executemany("INSERT INTO Guide (name, email, phone) VALUES (%s, %s, %s)", guides)

# Customers
customers = [
    ('Zachary Anderson', 'Zachary1@example.com', '555-3001', '2023-01-15'),
    ('Angela Vargas', 'Angela1@example.com', '555-3002', '2023-02-20'),
    ('Tevyah Hanley', 'Tevyah1@example.com', '555-3003', '2023-03-10'),
    ('Clark Kent', 'solokrypto@example.com', '555-3004', '2023-04-05'),
    ('Bruce Wayne', 'bat4life@example.com', '555-3005', '2023-05-12')
]
cursor.executemany("INSERT INTO Customer (name, email, phone, date_joined) VALUES (%s, %s, %s, %s)", customers)

# Trips
trips = [
    ('Safari Adventure', 'Africa', '2024-07-01', '2024-07-14', True),
    ('Himalayan Trek', 'Asia', '2024-08-15', '2024-08-28', True),
    ('Mediterranean Hike', 'Southern Europe', '2024-09-10', '2024-09-20', False)
]
cursor.executemany("""
INSERT INTO Trip (destination, region, start_date, end_date, visa_required)
VALUES (%s, %s, %s, %s, %s)
""", trips)

# Link guides to trips (TripGuide junction table)
trip_guides = [
    (1, 1),  # Safari Adventure - John MacNell
    (2, 2),  # Himalayan Trek - DB Duke Marland
    (3, 1)   # Mediterranean Hike - John MacNell
]
cursor.executemany("INSERT INTO TripGuide (trip_id, guide_id) VALUES (%s, %s)", trip_guides)

# Equipment
equipment = [
    ('Mountain Tent', 'Tent', 'Good', 'Available', '2015-05-10', 350.00),
    ('Lightweight Backpack', 'Backpack', 'Excellent', 'Available', '2020-07-20', 120.00),
    ('Thermal Sleeping Bag', 'Sleeping Bag', 'Fair', 'Rented', '2019-11-11', 90.00),
    ('Handheld GPS', 'Gadget', 'Good', 'Available', '2018-02-15', 150.00),
    ('First Aid Kit', 'Safety', 'Excellent', 'Available', '2021-03-22', 45.00),
    ('Camping Stove', 'Cooking', 'Worn', 'Sold', '2016-12-05', 80.00)
]
cursor.executemany("""
INSERT INTO Equipment (name, type, equipment_condition, status, purchase_date, price)
VALUES (%s, %s, %s, %s, %s, %s)
""", equipment)

# Bookings
bookings = [
    (1, 1, '2024-06-01'),
    (2, 2, '2024-06-05'),
    (3, 3, '2024-06-10'),
    (1, 2, '2024-06-15'),
    (2, 3, '2024-06-20')
]
cursor.executemany("INSERT INTO Booking (customer_id, trip_id, booking_date) VALUES (%s, %s, %s)", bookings)

# Transactions (now includes employee_id)
transactions = [
    (1, 1, 1, 'rental', '2024-06-02', '2024-06-16'),
    (2, 2, 2, 'sale', '2024-06-06', None),
    (3, 3, 3, 'rental', '2024-06-12', '2024-06-22'),
    (4, 4, 4, 'sale', '2024-06-18', None),
    (5, 5, 5, 'rental', '2024-06-21', '2024-07-01')
]
cursor.executemany("""
INSERT INTO Transaction_Details (customer_id, equipment_id, employee_id, transaction_type, transaction_date, return_date)
VALUES (%s, %s, %s, %s, %s, %s)
""", transactions)

conn.commit()
cursor.close()
conn.close()

print("Database, tables, and sample data created successfully!")