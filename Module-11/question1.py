"""
Zachary Anderson, Angela Vargas, Cameron Mendez, Tevyah Hanley
Equipment Sales vs Rentals Report
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

print("Equipment Sales vs Rentals")
print("=" * 55)

query = """
SELECT 
    CONCAT(UPPER(LEFT(transaction_type, 1)), LOWER(SUBSTRING(transaction_type, 2))) AS transaction_type, 
    COUNT(*) AS total_transactions,
    SUM(e.price) AS total_revenue
FROM Transaction_Details t
JOIN Equipment e ON t.equipment_id = e.equipment_id
GROUP BY transaction_type;
"""

cursor.execute(query)
results = cursor.fetchall()

print("Transaction Type | Total Transactions | Total Revenue")
print("-" * 55)

for row in results:
    print(f"{row[0]:<16} | {row[1]:<18} | ${row[2]:.2f}")

print("-" * 55)

cursor.close()
conn.close()
