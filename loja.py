class Loja:
    def __init__(self):
        self.items = {
            "Espada Ourop": {"preco": 50, "dano": 10},
            "Machado de Batalha": {"preco": 75, "dano": 15},
            "Espada Diamante": {"preco": 90, "dano": 31},
        }

    def listar_itens(self):
        print("Itens disponíveis:")
        for i, nome_do_item in enumerate(self.items):
            item = self.items[nome_do_item]
            print(f"{i+1}. {nome_do_item} - Preço: {item['preco']}")

    def comprar_item(self, nome_do_item, personagem):
        if nome_do_item in self.itens:
            item = self.itens[nome_do_item]
            if personagem.ouro >= item["preco"]:
                personagem.ouro -= item["preco"]
                tipo_do_item = nome_do_item.split()[0] 
                if tipo_do_item == "Espada" or tipo_do_item == "Machado":
                    personagem.ponto_de_ataque += item["dano"]
                    personagem.arma = nome_do_item
                print(f"{personagem.nome} comprou {nome_do_item}!")
            else:
                print("Você não tem ouro suficiente para comprar este item.")
        else:
            print("Este item não está disponível na loja.")