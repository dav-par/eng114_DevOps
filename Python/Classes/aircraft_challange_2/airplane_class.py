from aircraft_class import Aircraft


class Aeroplane(Aircraft):

    def __init__(self):
        super().__init__()
        self._has_wings = True
        self._plane_no = int()
        self._no_of_seat = int()

    def set_aeroplane(self, plane_no, seats: int):
        self._plane_no = plane_no
        self._no_of_seat = seats



