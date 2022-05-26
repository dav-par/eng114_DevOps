class Passenger():

    def __init__(self):
        self._first_name = ""
        self._last_name = ""
        self._passport_number = int()

    def set_passenger(self, first, last, pass_num):
        self._first_name = first
        self._last_name = last
        self._passport_number = pass_num

    def get_passenger_details(self):
        return [self._first_name, self._last_name, self._passport_number]

