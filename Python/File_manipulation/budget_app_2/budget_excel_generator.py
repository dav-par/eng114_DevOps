from openpyxl import Workbook

class BudgetExcelGenerator:

    def __init__(self):
        self.workbook = Workbook()
        self.worksheet1 = self.workbook.active
        self.worksheet1["A1"] = "Item"
        self.worksheet1["B1"] = "Value"

    def add_values_to_cell(self, cell, value):
        self.worksheet1[cell] = value

    def create_budget_list(self, budget_item_dict):

        cell_marker = 2

        for item_key in budget_item_dict:
            value = budget_item_dict.get(item_key)

            self.add_values_to_cell("A" + str(cell_marker), item_key)
            self.add_values_to_cell("B" + str(cell_marker), value)
            cell_marker += 1

    def save_file_as(self, name):
        self.workbook.save(name + ".xlsx")

'''
excel_gen = BudgetExcelGenerator()
budget_items ={"book": 5.50, "games": 20}
excel_gen.create_budget_list(budget_items)
excel_gen.save_file_as()
'''