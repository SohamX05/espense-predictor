import sqlite3

# Connect to the database
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Create the `expenses` table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        budget INTEGER,
        food INTEGER,
        rent INTEGER,
        transport INTEGER,
        entertainment INTEGER,
        shopping INTEGER,
        savings INTEGER
    )
''')

conn.commit()
conn.close()

print("✅ Table 'expenses' created successfully!")
