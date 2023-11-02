class Cliente:
    def __init__(self, nome, fone):
        self._nome = nome
        self.telefone = fone

    # método get
    def get_nome(self):
        return self._nome

    # método set
    def set_nome(self, nome):
        self.nome = nome
