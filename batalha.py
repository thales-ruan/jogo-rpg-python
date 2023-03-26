
from character import Character
from monster import Monster
from goblin import Goblin
from loja import Loja

tubarao_vermelho = Character(life_point = 100, point_of_attack = 17, name = "Tubarão Vermelho")
goblin_venenoso = Goblin(life_point = 70, point_of_attack = 13, type = "Goblin Venenoso", intelligence = 100)
superman = Character(life_point = 140, point_of_attack = 23, name = "Super-Man")

item_loja = Loja()


def batalha(atacante, defensor, item_loja=None):

    print('\n Apresentando lutadores')
    print(f'Personagem: {atacante.name} , Sua vida é: {atacante.life_point} e seu ponto de ataque é: {atacante.point_of_attack}')
    print('############### VS ###############')
    if isinstance(defensor, Monster):
        print(f'Personagem do tipo: {defensor.type} , Sua vida é: {defensor.life_point} e seu ponto de ataque é: {defensor.point_of_attack} Inteligencia: {defensor.intelligence}')
    else:
        print(f'Personagem: {defensor.name} , Sua vida é: {defensor.life_point} e seu ponto de ataque é: {defensor.point_of_attack}')

    while atacante.life_point > 0 and defensor.life_point > 0:
        atacante.attack(defensor)
        if defensor.life_point <= 0:
            print(f"{atacante.name} Venceu a batalha!\n")
            if item_loja:
                atacante.ouro += 60
            break

        defensor.attack(atacante)
        if atacante.life_point <= 0:
            print(f"{defensor.name} Venceu a batalha!\n")
            if item_loja:
                defensor.ouro += 60
            break

    if item_loja and atacante.life_point > 0:
        item_loja.comprar_item("Espada Ouro", atacante)
        atacante.point_of_attack += 10

batalha(tubarao_vermelho, goblin_venenoso,item_loja)
batalha(tubarao_vermelho, superman)
