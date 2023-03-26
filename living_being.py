class LivingBeing:
    def __init__(self, life_point, point_of_attack):
        self.life_point = life_point
        self.point_of_attack = point_of_attack 
        self.ouro = 0

    def attack(self, target):
        target.life_point -= self.point_of_attack
        print(f' ataque realizado, causou {target.point_of_attack} pontos de danos') 