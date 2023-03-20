from living_being import LivingBeing

class Monster(LivingBeing):
    def __init__(self, life_point, point_of_attack, type):
        super().__init__(life_point, point_of_attack)
        self.type = type

    def attack(self, target):
        super().attack(target)