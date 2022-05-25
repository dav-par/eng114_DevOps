class BudgetItem():

    def __init__(self):
        self.budget_items = {}

    def add_budget_item(self, item, value):
        self.budget_items[item] = value

    def return_budget_item_value(self, key):
        try:
            return self.budget_items[key]
        except KeyError:
            print("The key was not found")
            raise


    def delete_budget_item(self, item):
        try:
            del self.budget_items[item]
        except KeyError:
            print("The key was not found")
            raise

    def print_budget_items(self):
        print(self.budget_items)

budget = BudgetItem()

budget.add_budget_item("lunch", 10)
budget.print_budget_items()
budget.return_budget_item_value("dinner")

