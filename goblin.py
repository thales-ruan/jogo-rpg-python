from monster import Monster

class Goblin(Monster):
    def __init__(self, life_point, point_of_attack, type, intelligence):
        super().__init__(life_point, point_of_attack, type)
        self.intelligence = intelligence