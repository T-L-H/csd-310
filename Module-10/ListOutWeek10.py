import mysql.connector


conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='TLHarts19!',
    database='outland_adventures'
)

cursor = conn.cursor()

tables = [
    "Customer",
    "Guide",
    "Trip",
    "TripGuide",
    "Booking",
    "Equipment",
    "Employee",
    "Transaction_Details"
]

for table in tables:
    print(f"\n--- {table} ---")
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

cursor.close()
conn.close()