from aircraft_class import Aircraft


class Aeroplane(Aircraft):

    def __init__(self):
        super().__init__()
        self._has_wings = True
        self._plane_no = int()
        self._no_of_seat = int()
        self._plane_unique_id = str()

    def set_aeroplane(self, plane_no, seats: int, u_id):
        self._plane_unique_id = u_id
        self._plane_no = plane_no
        self._no_of_seat = seats

    def check_plane_unique_id(self):
        return self._plane_unique_id
