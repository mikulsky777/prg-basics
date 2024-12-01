categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

most_expensive = expenses.index(max(expenses))

category = categories[most_expensive]
expense = expenses[most_expensive]

print(f'The most expensive category is {category} with expenses of {expense}')