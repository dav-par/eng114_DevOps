from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tounge = True
        self.cold_blooded = True
        self.venom = None
        self.limbs = False

    def use_tounge_to_smell(self):
        print("smelling throught my tounge")