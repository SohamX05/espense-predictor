from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

EXPENSES_FILE = "expenses.json"

# Load stored expenses
def load_expenses():
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, "r") as file:
            return json.load(file)
    return []

# Save expenses
def save_expenses(data):
    with open(EXPENSES_FILE, "w") as file:
        json.dump(data, file, indent=4)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/store", methods=["POST"])
def store():
    data = request.json  
    expenses = load_expenses()
    expenses.append(data)  
    save_expenses(expenses)  
    return jsonify({"message": "Data stored successfully!"})

@app.route("/get_data", methods=["GET"])
def get_data():
    return jsonify(load_expenses())

@app.route("/suggest", methods=["POST"])
def suggest():
    budget = int(request.json.get("budget", 0))

    fractions = {
        "Food": 0.3,
        "Rent": 0.4,
        "Transport": 0.1,
        "Entertainment": 0.1,
        "Shopping": 0.05,
        "Savings": 0.05
    }

    suggestion = {k: round(budget * v, 2) for k, v in fractions.items()}
    return jsonify(suggestion)

if __name__ == "__main__":
    app.run(debug=True)
