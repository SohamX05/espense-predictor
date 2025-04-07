document.addEventListener("DOMContentLoaded", function () {
    loadStoredData(); // Load stored expenses on page load
});

document.getElementById("store-form")?.addEventListener("submit", function (e) {
    e.preventDefault();

    let budget = document.getElementById("budget").value;
    let food = document.getElementById("food").value;
    let rent = document.getElementById("rent").value;
    let transport = document.getElementById("transport").value;
    let entertainment = document.getElementById("entertainment").value;
    let shopping = document.getElementById("shopping").value;
    let savings = document.getElementById("savings").value;

    let expenseData = { budget, food, rent, transport, entertainment, shopping, savings };

    let expenses = JSON.parse(localStorage.getItem("expenses")) || [];
    expenses.push(expenseData);
    localStorage.setItem("expenses", JSON.stringify(expenses));

    loadStoredData();
    document.getElementById("store-form").reset();
});

function loadStoredData() {
    let expenses = JSON.parse(localStorage.getItem("expenses")) || [];
    let tableBody = document.querySelector("#expense-table tbody");
    if (tableBody) {
        tableBody.innerHTML = "";
        expenses.forEach(expense => {
            let row = `<tr>
                <td>${expense.budget}</td>
                <td>${expense.food}</td>
                <td>${expense.rent}</td>
                <td>${expense.transport}</td>
                <td>${expense.entertainment}</td>
                <td>${expense.shopping}</td>
                <td>${expense.savings}</td>
            </tr>`;
            tableBody.innerHTML += row;
        });
    }
}

// Budget Suggestion Logic
function predictBudget() {
    let budget = document.getElementById("budgetInput").value;
    if (!budget) return;

    let food = (budget * 0.3).toFixed(2);
    let rent = (budget * 0.25).toFixed(2);
    let transport = (budget * 0.15).toFixed(2);
    let entertainment = (budget * 0.1).toFixed(2);
    let shopping = (budget * 0.1).toFixed(2);
    let savings = (budget * 0.1).toFixed(2);

    let suggestTable = document.querySelector("#suggest-table tbody");
    suggestTable.innerHTML = `
        <tr><td>Food</td><td>${food}</td></tr>
        <tr><td>Rent</td><td>${rent}</td></tr>
        <tr><td>Transport</td><td>${transport}</td></tr>
        <tr><td>Entertainment</td><td>${entertainment}</td></tr>
        <tr><td>Shopping</td><td>${shopping}</td></tr>
        <tr><td>Savings</td><td>${savings}</td></tr>
    `;
}
