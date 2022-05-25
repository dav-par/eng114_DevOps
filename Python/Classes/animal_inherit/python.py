from snake import Snake

class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_pray(self):
        print("I've eaten large pray")

    def constrict(self):
        print("Squeeze")

    def climb(self):
        print("Up we go")

    def shed_skin(self):
        print("I'm growing new skin")


