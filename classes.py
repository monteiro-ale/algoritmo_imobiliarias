class Imobiliaria:
    def __init__(self, nome_imobiliaria, telefone):
        self.nome_imobiliaria = nome_imobiliaria
        self.telefone = telefone
        self.__lst_imoveis_alugar = []

    def get_nome_imob(self):
        return self.nome_imobiliaria

    def get_telefones_imob(self):
        return self.telefone

    def get_lst_imoveis(self):
        return self.__lst_imoveis_alugar

    def set_nome_imob(self, nome):
        self.nome_imobiliaria = nome

    def set_adc_imoveis_lst(self, objeto_imovel):
        self.__lst_imoveis_alugar.append(objeto_imovel)

    def set_adc_telefone(self, fone):
        self.telefone = fone

    def itera_lista_imoveis(self):
        for x, imovel in enumerate(self.__lst_imoveis_alugar):
            print(x, '\n', imovel.get_tipo_imovel(), '\n', imovel.get_endereco_imovel(), '\n', imovel.get_status(), '\n')

    def __str__(self):
        return f"Imobiliaria {self.get_nome_imob()}\n" \
               f"Telefones {self.get_telefones_imob()}\n" \


class Imovel:
    def __init__(self, tipo, endereco):
        self.tipo = tipo
        self.endereco = endereco
        self.alugado = None

    def get_tipo_imovel(self):
        return self.tipo

    def get_endereco_imovel(self):
        return self.endereco

    def get_status(self):
        if self.alugado is True:
            return 'ALUGADO'
        else:
            return 'DISPONIVEL'

    def set_tipo_imovel(self, tipo):
        self.tipo = tipo

    def set_endereco_imovel(self, endereco):
        self.endereco = endereco

    def set_status_imovel(self, status_atual):
        if status_atual == 1:
            self.alugado = True
        elif status_atual == 0:
            self.alugado = False

    def __str__(self):
        return f"Tipo de imóvel {self.tipo}\n" \
               f" Endereço {self.endereco}\n" \
               f" Status {self.get_status()}"
