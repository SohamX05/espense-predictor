import sqlite3

# Connect to the database
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Fetch all data from the expenses table
cursor.execute("SELECT * FROM expenses")
rows = cursor.fetchall()

# Print the data
if rows:
    print("✅ Data in the expenses table:")
    for row in rows:
        print(row)
else:
    print("⚠️ No data found in the expenses table.")

conn.close()
