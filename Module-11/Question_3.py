"""
Zachary Anderson, Angela Vargas, Tevyah Hanley, Cameron Mendez
Old Equipment Report

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

print("Equipment Older Than 5 Years")
print("=" * 55)

query = """
SELECT 
    name,
    purchase_date,
    TIMESTAMPDIFF(YEAR, purchase_date, CURDATE()) AS age_years
FROM Equipment
WHERE TIMESTAMPDIFF(YEAR, purchase_date, CURDATE()) > 5;
"""

cursor.execute(query)
results = cursor.fetchall()

print("Equipment Name       | Purchase Date | Age (Years)")
print("-" * 55)

for row in results:
    print(f"{row[0]:<20} | {row[1]}   | {row[2]}")

print("-" * 55)

cursor.close()
conn.close()
