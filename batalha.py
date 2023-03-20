
from character import Character
from goblin import Goblin

tubarao_vermelho = Character(life_point = 100, point_of_attack = 17, name = "Tubarão Vermelho")
goblin_venenoso = Goblin(life_point = 70, point_of_attack = 13, type = "Goblin Venenoso", intelligence = 100)

print('*******Que começe a grande batalha*******')
print('Apresentando lutadores')

print(f'Personagem: {tubarao_vermelho.name} , Sua vida é: {tubarao_vermelho.life_point} e seu ponto de ataque é: {tubarao_vermelho.point_of_attack}')
print('############### VS ###############')
print(f'Personagem do tipo: {goblin_venenoso.type} , Sua vida é: {goblin_venenoso.life_point} e seu ponto de ataque é: {goblin_venenoso.point_of_attack} Inteligencia: {goblin_venenoso.intelligence}')

goblin_venenoso.attack(tubarao_vermelho)
tubarao_vermelho.attack(goblin_venenoso)

print(f'Pós ataque {tubarao_vermelho.name} sua vida é {tubarao_vermelho.life_point}')
print(f'Pós ataque {goblin_venenoso.type} sua vida é {goblin_venenoso.life_point}')


