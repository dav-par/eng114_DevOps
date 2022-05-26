from openpyxl import Workbook
from flight_trip_class import Flight_trip


class Excel(Flight_trip):

    def __init__(self):
        super().__init__()
        self.workbook = Workbook()
        self.worksheet1 = self.workbook.active
        self.worksheet1["A1"] = "flight number"
        self.worksheet1["C1"] = "Origin:"
        self.worksheet1["E1"] = "Destination:"

        self.worksheet1["A2"] = "First name"
        self.worksheet1["B2"] = "Last name"
        self.worksheet1["C2"] = "Passport number"

    def add_values_to_cell(self, cell, value):
        self.worksheet1[cell] = value

    def create_flight_list(self, flight_number, passenger_list):
        cell_marker = 3

        for value in passenger_list:
            self.add_values_to_cell("A" + str(cell_marker), value)
            cell_marker += 1
            pass

    def save_file_as(self, name):
        self.workbook.save(name + ".xlsx")


excel_gen = Excel()
excel_gen.create_flight_list(1000, ["David", "Park", 12345])
excel_gen.save_file_as("flight" + str(1000))