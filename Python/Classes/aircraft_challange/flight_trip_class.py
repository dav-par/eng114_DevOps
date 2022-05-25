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
        self._passengers = []

    def set_flight_trip(self, start, end, flight_no, date):  #need to add aeroplane to flight
        self._flight_num = flight_no
        self._flight_date = date
        self._flight_origin = start
        self._flight_destination = end

    def add_passenger(self, pass_unique_id):
        self._passengers.append(pass_unique_id)

    def add_Aeroplane(self, plane_uniquid_id):
        self._passengers.append(plane_uniquid_id)

    def get_flight_numbers(self):
        return self._flight_num

    def get_passengers(self):
        return self._passengers

    def sell_ticket(self, passenger_unique_id):
        if self._no_of_seat > 0:
            self._passengers.append(passenger_unique_id)
            self._no_of_seat -= 1

        else: print("no seats left")

    def get_flight_details(self):
        return [self._flight_origin, self._flight_destination, self._flight_date]


