from monster import Monster

class Wolf(Monster):
    def __init__(self,life_point, point_of_attack, type, force ):
        super().__init__(life_point, point_of_attack, type)
        self.force = force