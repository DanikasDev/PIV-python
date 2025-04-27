"""As minhas Lareiras"""

class Lareira:
    """
    Implementação de uma Lareira Genérica
    """

    def __init__(self):
        """ inicializa uma lareira apagada."""
        self.acesa = False

    def acender(self):
        """Acende a lareira."""
        if not self.acesa:
            self.acesa = True
            print("A lareira está agora acesa.")
        else:
            print("A lareira já está acesa.")

    def apagar(self):
        """Apaga a lareira."""
        if self.acesa:
            self.acesa = False
            print("A lareira foi apagada.")
        else:
            print("A lareira já está apagada.")

    def __str__(self):
        """Retorna uma representação em string
        da lareira."""
        if self.acesa:
            status = "acesa"
        else:
            status = "apagada"
        return f"Lareira está {status} "

class LareiraInicializada:
    """
    Implementação de uma Lareira Genérica
    """

    def __init__(self, nome="Lareira Inicializada"):
        """ inicializa uma lareira apagada."""
        self.acesa = False
        self.nome = nome

    def acender(self):
        """Acende a lareira."""
        if not self.acesa:
            self.acesa = True
            print(f"A lareira {self.nome} está agora acesa.")
        else:
            print(f"A lareira {self.nome} já está acesa.")

    def apagar(self):
        """Apaga a lareira."""
        if self.acesa:
            self.acesa = False
            print(f"A lareira {self.nome} foi apagada.")
        else:
            print(f"A lareira {self.nome} já está apagada.")

    def __str__(self):
        """Retorna uma representação em string
        da lareira."""
        if self.acesa:
            status = "acesa"
        else:
            status = "apagada"

        return f"Lareira {self.nome} está {status}!"

class LareiraGrandeAcesa(LareiraInicializada):
    """
    Implementação de uma Lareira Específica
    """

    def __init__(self):
        """ Upgrade Lareira """
        super().__init__(nome = "Minha Grande e quentinha Lareira")

    def __str__(self):
        if self.acesa:
            status = "Nacesa"
        else:
            status = "Napagada"
        return f"Lareira {self.nome} está {status} "

    def novo_metodo(self):
        """Método Novo"""
        return "Sabe bem no inverno!"

lareira5 = LareiraGrandeAcesa()
print(lareira5.novo_metodo())
