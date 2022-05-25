class BudgetItems():

    def __init__(self):
        self.budget_items = {}

    def add_budget_item(self, item, value):
        self.budget_items[item] = value

    def return_budget_item_value(self, key):
        return self.budget_items[key]

    def delete_budget_item(self, item):
        delete self.budget_items[item]

    def print_budget_items(self):
        print(self.budget_items)
