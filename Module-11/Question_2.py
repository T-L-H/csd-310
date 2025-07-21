"""
Zachary Anderson, Angela Vargas, Tevyah Hanley, Cameron Mendez
Booking Trends Report
"""
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='TLHarts19!',
    database='outland_adventures'
)
cursor = conn.cursor()

print("Booking Trends by Region")
print("=" * 55)

query = """
SELECT 
    t.region,
    YEAR(b.booking_date) AS year,
    COUNT(*) AS total_bookings
FROM Booking b
JOIN Trip t ON b.trip_id = t.trip_id
GROUP BY t.region, year
ORDER BY t.region, year;
"""

cursor.execute(query)
results = cursor.fetchall()

print("Region            | Year | Total Bookings")
print("-" * 55)

for row in results:
    print(f"{row[0]:<16} | {row[1]}  | {row[2]}")

print("-" * 55)

cursor.close()
conn.close()
