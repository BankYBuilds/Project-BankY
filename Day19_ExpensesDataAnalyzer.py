#Expense Data Analyzer


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("expenses.csv")


total_expenses = data["Amount"].sum()
avg_expenses = data["Amount"].mean()
max_expense = data["Amount"].max()


housing = data[data["Expense Category"] == "Housing"]
groceries = data[data["Expense Category"] == "Groceries"]
transportation = data[data["Expense Category"] == "Transportation"]
utilities = data[data["Expense Category"] == "Utilities"]
dining = data[data["Expense Category"] == "Dining"]
entertainment = data[data["Expense Category"] == "Entertainment"]
health = data[data["Expense Category"] == "Health"]
shopping = data[data["Expense Category"] == "Shopping"]

avg_housing = housing["Amount"].mean()
avg_groceries = groceries["Amount"].mean()
avg_transportation = transportation["Amount"].mean()
avg_utilities = utilities["Amount"].mean()
avg_dining = dining["Amount"].mean()
avg_entertainment = entertainment["Amount"].mean()
avg_health = health["Amount"].mean()
avg_shopping = shopping["Amount"].mean()


print(f"The total amount spent is ₦{total_expenses:,.2f}")
print(f"The average expense is ₦{avg_expenses:,.2f}")
print(f"The highest single expense is ₦{max_expense:,.2f}")
print(f"The average amount spent on Housing is ₦{avg_housing:,.2f}")
print(f"The average amount spent on Groceries is ₦{avg_groceries:,.2f}")
print(f"The average amount spent on Transportation is ₦{avg_transportation:,.2f}")
print(f"The average amount spent on Utilities is ₦{avg_utilities:,.2f}")
print(f"The average amount spent on Dining is ₦{avg_dining:,.2f}")
print(f"The average amount spent on Entertainment is ₦{avg_entertainment:,.2f}")
print(f"The average amount spent on Health is ₦{avg_health:,.2f}")
print(f"The average amount spent on Shopping is ₦{avg_shopping:,.2f}")

category_expenses = data.groupby("Expense Category")["Amount"].sum()
plt.figure(figsize=(10, 6))

plt.bar(category_expenses.index, category_expenses.values)

plt.xlabel("Category")
plt.ylabel("Amount Spent")
plt.title("Expenses by Category")

plt.show()


data["Date"] = pd.to_datetime(data["Date"])
daily_expenses = data.groupby("Date")["Amount"].sum()
plt.figure(figsize=(12, 6))

plt.plot(daily_expenses.index, daily_expenses.values, marker="o")

plt.xlabel("Date")
plt.ylabel("Amount Spent")
plt.title("Daily Expenses")

plt.show()
