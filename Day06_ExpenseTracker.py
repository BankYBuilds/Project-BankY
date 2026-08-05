# EXPENSE TRACKER

expenses = {
    "Food": 3500,
    "Transport": 1200,
    "Data": 2500,
    "Books": 5000,
    "Snacks": 800
}

total = sum(expenses.values())
mostExpensive = max(expenses.values())
cheapest = min(expenses.values())
avg = total/len(expenses)

for item, price in expenses.items():
    print(f'{item}: {price}')

highest_category = max(expenses, key=expenses.get)
lowest_category = min(expenses, key=expenses.get)

print(f"Most expensive: {highest_category} (₦{expenses[highest_category]})")
print(f"Cheapest: {lowest_category} (₦{expenses[lowest_category]})")
print("The total expense is:₦",total)
print("The average expense is:₦",avg)

if total <= 15000:
    print("Great job staying under budget!")

else:
    print("You exceeded your budget.")