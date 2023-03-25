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

