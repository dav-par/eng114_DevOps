class Passenger():

    def __init__(self):
        self._first_name = ""
        self._last_name = ""
        self._passport_number = int()"

    def set_passenger(self, first, last, pass_num, uid):
        self._first_name = first
        self._last_name = last
        self._passport_number = pass_num
        self._unique_id = uid

    def get_passenger_unique_id(self):
        return self._unique_id

    def get_passenger_passport(self):
        return self._passport_number

