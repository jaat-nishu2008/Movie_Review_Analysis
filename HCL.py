import csv
import os
FILENAME = "expenses.csv"
     def initialize_file():
 """Creates the CSV file with headers if it doesn't already exist."""
 if not os.path.exists(FILENAME):
 with open(FILENAME, "w", newline="") as file:
 writer = csv.writer(file)
 writer.writerow(["Date", "Category", "Amount"])
 def add_expense(date, category, amount):
 """Appends a new expense row to the CSV file."""
 with open(FILENAME, "a", newline="") as file:
 writer = csv.writer(file)
 writer.writerow([date, category, amount])
 print(f"Saved: {category} - ₹{amount}")
   def view_summary():
 """Reads all expenses and calculates total spending."""
 total = 0
 print("\n--- Expense Report ---") 
 try:
 with open(FILENAME, "r") as file:
 reader = csv.DictReader(file)
 for row in reader:
 print(f"{row['Date']} | {row['Category']}: ₹{row['Amount']}")
 total += float(row["Amount"])
 print(f"----------------------\nTotal Spent: ₹{total:.2f}")
 except FileNotFoundError:
 print("No expenses recorded yet!")
# --- Running the Program ---
  initialize_file()
 add_expense("2026-11-19", "Groceries", 450)
add_expense("2026-11-19", "Internet Bill", 899)
add_expense("2026-11-20", "Coffee", 180)
