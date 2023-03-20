from living_being import LivingBeing

class Character(LivingBeing):
    def __init__(self, life_point, point_of_attack, name):
        super().__init__(life_point, point_of_attack)
        self.name = name


