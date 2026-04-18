import json
import os
from datetime import datetime

DATA_FILE = 'data.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def save_data(expenses):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category (e.g., Food, Travel, Rent): ")
    description = input("Enter description: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    expense = {
        "date": date,
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses = load_data()
    expenses.append(expense)
    save_data(expenses)
    print("\n Expense added successfully!")

def view_expenses():
    expenses = load_data()
    if not expenses:
        print("\nEmpty list. No expenses recorded yet.")
        return

    print("\n--- Your Expenses ---")
    print(f"{'Date':<20} | {'Category':<12} | {'Amount':<10} | {'Description'}")
    print("-" * 60)
    for exp in expenses:
        print(f"{exp['date']:<20} | {exp['category']:<12} | {exp['amount']:<10} | {exp['description']}")

def main():
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
