from animal import Animal

class Reptile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chambers = [3, 4]
        self.amiotic_egg = None

    def seek_heat(self):
        print("It's chilly outside, where is the sun")

    def hunt(self):
        print("wait for it and pounce")

    def use_venom(self):
        if self.venom == True:
            print("if i've got it, i'll use it")

    def attract_mate_through_sent(self):
        print("I smell good")
