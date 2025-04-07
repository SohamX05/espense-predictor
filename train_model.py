import sqlite3
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

# ✅ Connect to Database
conn = sqlite3.connect("expenses.db")

# ✅ Load Data from Database
query = "SELECT budget, food, rent, transport, entertainment, shopping, savings FROM expenses"
df = pd.read_sql_query(query, conn)
conn.close()

# ✅ Check if Data Exists
if df.empty:
    print("⚠️ No data found! Store some expense data first.")
    exit()

# ✅ Features (X) & Target (Y)
X = df[['budget']]
Y = df[['food', 'rent', 'transport', 'entertainment', 'shopping', 'savings']]

# ✅ Train Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, Y)

# ✅ Save Model
with open("budget_predictor.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ AI Model Trained Successfully!")
