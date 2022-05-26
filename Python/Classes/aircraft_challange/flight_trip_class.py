from airplane_class import Aeroplane
from passenger_class import Passenger


class Flight_trip(Aeroplane, Passenger):

    def __init__(self):
        super().__init__()
        self._flight_date = ""
        self._flight_num = int()
        self._flight_origin = ""
        self._flight_destination = ""
        self._Aeroplane = ""
        self._passenger_list = []

    def set_flight_trip(self, start, end, flight_no, date, aeroplane):
        self._flight_num = flight_no
        self._Aeroplane = aeroplane
        self._flight_date = date
        self._flight_origin = start
        self._flight_destination = end

    def add_passenger(self, passport_num):
        self._passenger_list.append(int(passport_num))
        self._no_of_seat -= 1

    def get_flight_number(self):
        return self._flight_num

    def get_flight_details(self):
        return [self._flight_num, self._flight_date, self._flight_origin, self._flight_destination]

    def get_passenger_list(self):
        return self._passenger_list