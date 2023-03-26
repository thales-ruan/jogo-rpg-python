
from personagem import Personagem
from monstro import Monstro
from goblin import Goblin
from loja import Loja

tubarao_vermelho = Personagem(pontos_de_vida = 100, pontos_de_ataque = 17, nome = "Tubarão Vermelho")
goblin_venenoso = Goblin(pontos_de_vida = 70, pontos_de_ataque = 13, tipo = "Goblin Venenoso", inteligencia = 100)
superman = Personagem(pontos_de_vida = 140, pontos_de_ataque = 23, nome = "Super-Man")

item_loja = Loja()


def batalha(atacante, defensor, item_loja=None):

    print('\n Apresentando lutadores')
    print(f'Personagem: {atacante.nome} , Sua vida é: {atacante.pontos_de_vida} e seu ponto de ataque é: {atacante.pontos_de_ataque}')
    print('############### VS ###############')
    if isinstance(defensor, Monstro):
        print(f'Personagem do tipo: {defensor.tipo} , Sua vida é: {defensor.pontos_de_vida} e seu ponto de ataque é: {defensor.pontos_de_ataque} Inteligencia: {defensor.inteligencia}')
    else:
        print(f'Personagem: {defensor.nome} , Sua vida é: {defensor.pontos_de_vida} e seu ponto de ataque é: {defensor.pontos_de_ataque}')

    while atacante.pontos_de_vida > 0 and defensor.pontos_de_vida > 0:
        atacante.ataque(defensor)
        if defensor.pontos_de_vida <= 0:
            print(f"{atacante.nome} Venceu a batalha!\n")
            if item_loja:
                atacante.ouro += 60
            break

        defensor.ataque(atacante)
        if atacante.pontos_de_vida <= 0:
            print(f"{defensor.nome} Venceu a batalha!\n")
            if item_loja:
                defensor.ouro += 60
            break

    if item_loja and atacante.pontos_de_vida > 0:
        item_loja.comprar_item("Espada Ouro", atacante)
        atacante.pontos_de_ataque += 10

batalha(tubarao_vermelho, goblin_venenoso,item_loja)
batalha(tubarao_vermelho, superman)
