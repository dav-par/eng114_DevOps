from budget_item_manager import BudgetItem

budget = BudgetItem()

budget.add_budget_item("dinner", 30)
budget.add_budget_item("lunch", 20)

budget.save_budget_items()