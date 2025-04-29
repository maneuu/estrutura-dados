class Pais:
    def __init__(self,nome:str,capital:str,dimensao:float,fronteira:list):
        self.__nome = nome
        self.__capital = capital
        self.__dimensao = dimensao
        self.__fronteira = fronteira
    
    @property
    def nome(self):
        return self.__nome
    @property
    def capital(self):
        return self.__capital
    @property
    def dimensao(self):
        return self.__dimensao
    @property
    def fronteira(self):
        return self.__fronteira
        
    
    def add_fronteira(self,nova_fronteira):
        if nova_fronteira not in self.__fronteira:
            self.__fronteira.append(nova_fronteira)

    def __str__(self):
        #  Agora as fronteiras são instâncias de outros países, então chamamos __str__ neles
        fronteiras = ", ".join([pais.nome for pais in self.__fronteira]) if self.__fronteira else "Nenhuma"
        return (
            f"🌍\tPaís: {self.__nome}\n"
            f"🏛️\tCapital: {self.__capital}\n"
            f"📏\tDimensão: {self.__dimensao:.2f} km²\n"
            f"🌐\tFaz fronteira com: {fronteiras}\n"
        )


# Instâncias dos países
brasil = Pais("Brasil", "Brasília", 8515767, [])
argentina = Pais("Argentina", "Buenos Aires", 2780400, [])
bolivia = Pais("Bolívia", "Sucre", 1098581, [])
peru = Pais("Peru", "Lima", 1285216, [])

# Definindo as fronteiras para o Brasil
brasil.add_fronteira(argentina)
brasil.add_fronteira(bolivia)
brasil.add_fronteira(peru)

# Definindo as fronteiras para a Argentina
argentina.add_fronteira(brasil)
argentina.add_fronteira(bolivia)

# Definindo as fronteiras para a Bolívia
bolivia.add_fronteira(brasil)
bolivia.add_fronteira(argentina)

# Definindo as fronteiras para o Peru
peru.add_fronteira(brasil)

# Lista de países
paises = [brasil, argentina, bolivia, peru]

# Exibindo todos os países e suas fronteiras
for pais in paises:
    print(pais)
    print("-" * 50)  # Linha separadora
