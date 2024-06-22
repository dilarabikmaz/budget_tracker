class Income:
    def __init__(self, budget_type, name, category, amount) -> None:
        self.budget_type = budget_type
        self.name = name
        self.category = category
        self.amount = amount

    def __repr__(self):
        return f"<Income: {self.name}, {self.budget_type}, {self.category}, {self.amount}"
    
    