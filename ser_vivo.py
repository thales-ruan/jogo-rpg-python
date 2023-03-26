class SerVivo:
    def __init__(self, pontos_de_vida, pontos_de_ataque):
        self.pontos_de_vida = pontos_de_vida
        self.pontos_de_ataque = pontos_de_ataque 
        self.ouro = 0

    def ataque(self, alvo):
        alvo.pontos_de_vida -= self.pontos_de_ataque
        print(f' ataque realizado, causou {alvo.pontos_de_ataque} pontos de danos') 