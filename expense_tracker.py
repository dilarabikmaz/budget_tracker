from entry import Entry

def main():
    print(f"🎯 Running Expense Tracker!")
    file_path = "expense.csv"
    actions = [
        "Add income",
        "Add expense",
        "See current balance",
    ]

    while True:
        # Print each possible action
        for i, action in enumerate(actions):
            print(f" {i + 1}. {action}")
        
        # Try converting the index to int
        try:
            selected_index = int(input("Enter action number: "))
        except Exception: 
            print("Invalid action type. Please try again!")

        # Proceed based on the index of action selected
        if selected_index == 1:
            # Get user input to create income
            income = get_income_from_user()

            # Write their income to a file
            save_expense_income(income, file_path, "i")
        elif selected_index == 2:
            # Get user input to create expense
            expense = get_expense_from_user()

            # Write their expense to a file
            save_expense_income(expense, file_path, "e")

            # Read file to summarize expenses
            summarize_expenses(file_path)
        elif selected_index == 3:
            # Read file to summarize expenses
            summarize_expenses(file_path)
        else:
            print("Invalid action")
        break

def get_income_from_user():
    income_budget_types = [
        "💻 Yale Computer Society", 
        "🌎 International Students' Organization", 
        "💃 Yale Modern Dance Collective",
    ]

    income_categories = []

    while True:
        # Prompt the user to select which budget they want to add to
        print("Select the budget you want to add an income to: ")
        for i, budget_type_name in enumerate(income_budget_types):
            print(f" {i + 1}. {budget_type_name}")
        
        try:
            selected_index = int(input("Enter a budget type number: "))
        except Exception: 
            print("Invalid budget type. Please try again!")

        # Initialize potential income categories based on the index of the budget type provided
        if selected_index - 1 in range(len(income_budget_types)):
            if selected_index == 1:
                income_categories = [
                    "Balance from previous academic year",
                    "UOFC Grant",
                    "Event ticket sale",
                    "Sponsorship",
                ]
            elif selected_index == 2:
                income_categories = [
                    "Balance from pervious academic year",
                    "UOFC Grant",
                    "Fundraising",
                    "Event ticket sale",
                    "Donations",
                ]
            elif selected_index == 3:
                income_categories = [
                    "UOFC Grant",
                    "Arts Discretionary Fund",
                    "Creative and Performing Arts Grant",
                    "Balance from pervious academic year",
                ]
            budget_type = income_budget_types[selected_index - 1]
            break
        else:
            print("Invalid budget type. Please try again!")

    income_name = input("Income Name: ")
    income_amount = float(input("Income Amount: "))
    income_category = []

    # Prompt the user to select a category based on the budget type the have chosen
    while True:
        for i, category_name in enumerate(income_categories):
            print(f" {i + 1}. {category_name}")

        try:
            selected_index = int(input(f"Enter a category number: "))
        except Exception:
            print("Invalid category. Please try again!")
        
        if selected_index - 1 in range(len(income_categories)):
            income_category = income_categories[selected_index - 1]
            break
        else:
            print("Invalid category. Please try again!")

    # Create an instance of the Entry class using the provided parameters      
    new_income = Entry(
        budget_type=budget_type, name=income_name, category=income_category, amount=income_amount
    )
    return new_income

def get_expense_from_user():
    expense_budget_types = [
        "💻 Yale Computer Society", 
        "🌎 International Students' Organization", 
        "💃 Yale Modern Dance Collective",
    ]

    expense_categories = []

    # Prompt the user to select which budget they want to add to
    while True:
        print("Select the budget you want to add an expense to: ")
        for i, budget_type_name in enumerate(expense_budget_types):
            print(f" {i + 1}. {budget_type_name}")
        
        try:
            selected_index = int(input("Enter a budget type number: "))
        except Exception: 
            print("Invalid budget type. Please try again!")

        # Based on the budget type provided, initialize the possible expense categories
        if selected_index - 1 in range(len(expense_budget_types)):
            if selected_index == 1:
                expense_categories = [
                    "y/cs Events",
                    "Projects",
                    "Publicity",
                    "Internal Events",
                ]
            elif selected_index == 2:
                expense_categories = [
                    "Sociocultural Council Events",
                    "External Affairs Projects",
                    "Publicity",
                    "Internal Events/Team Building",
                ]
            elif selected_index == 3:
                expense_categories = [
                    "Costumes/props",
                    "Photoshoots/Publicity",
                    "Company events",
                    "Initiation",
                ]
            budget_type = expense_budget_types[selected_index - 1]
            break
        else:
            print("Invalid budget type. Please try again!")

    # Prompt the user for the other variables needed
    expense_name = input("Expense Name: ")
    expense_amount = float(input("Expense Amount: "))
    expense_category = []

    # Prompt the user to select a category based on the budget type the have chosen
    while True:
        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}. {category_name}")

        try:
            selected_index = int(input(f"Enter a category number: "))
        except Exception:
            print("Invalid category. Please try again!")
        
        if selected_index - 1 in range(len(expense_categories)):
            expense_category = expense_categories[selected_index - 1]
            break
        else:
            print("Invalid category. Please try again!")
            
    # Create an instance of the Entry class using the provided parameters      
    new_expense = Entry(
        budget_type=budget_type, name=expense_name, category=expense_category, amount=expense_amount
    )
    return new_expense


def save_expense_income(expense_or_income, file_path, type):
    if type == 'e':
        # If the entry is an expense, convert amount to negative
        expense_or_income.amount = float(expense_or_income.amount) * -1
        print(f"🎯 Saving user expense: {expense_or_income} to {file_path}")
    else:
        print(f"🎯 Saving user income: {expense_or_income} to {file_path}")
    with open(file_path, "a") as f:
        # Add expense/income to file
        f.write(f"{expense_or_income.budget_type}, {expense_or_income.name}, {expense_or_income.amount}, {expense_or_income.category}\n")

def summarize_expenses(expense_file_path):
    print(f"🎯 Sumarizing User Expenses:")
    entries = []

    # Print each line of the file, add each entry to the entries list
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            budget_type, expense_name, expense_amount, expense_category = stripped_line.split(",")
            print(budget_type, expense_name, expense_amount, expense_category)
            line_expense = Entry(
                budget_type=budget_type, name=expense_name, amount=float(expense_amount), category=expense_category
            )
            entries.append(line_expense)

    amount_by_budget = {}

    for entry in entries:
        key = entry.budget_type
        if key in amount_by_budget:
            amount_by_budget[key] += entry.amount
        else:
            amount_by_budget[key] = entry.amount
    
    print("\n-----------")
    
    for key, amount in amount_by_budget.items():
        print(f"{key}: ${amount}")
    
    print("\n")

if __name__ == "__main__":
    main()