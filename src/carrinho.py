FRETE = 20.00
LIMITE_FRETE_GRATIS = 150.00


class Carrinho:
    """Gerencia itens de compra e calcula o total com frete."""

    def __init__(self):
        # dict preserva a ordem de inserção
        self._itens = {}

    def adicionar_item(self, nome, preco, quantidade=1):
        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        if quantidade < 1:
            raise ValueError("A quantidade deve ser maior ou igual a 1.")

        if nome in self._itens:
            self._itens[nome]["quantidade"] += quantidade
        else:
            self._itens[nome] = {"nome": nome, "preco": preco, "quantidade": quantidade}

    def remover_item(self, nome):
        if nome not in self._itens:
            raise ValueError(f"Item '{nome}' não está no carrinho.")
        del self._itens[nome]

    def show(self):
        return [dict(item) for item in self._itens.values()]

    def subtotal(self):
        return round(sum(i["preco"] * i["quantidade"] for i in self._itens.values()), 2)

    def frete(self):
        subtotal = self.subtotal()
        if subtotal == 0 or subtotal >= LIMITE_FRETE_GRATIS:
            return 0.00
        return FRETE

    def total(self):
        if not self._itens:
            return 0.00
        return round(self.subtotal() + self.frete(), 2)
