from classes import *

lst_imobiliarias = []

#opção 1
def adc_imobiliaria():
    nome = input('Digite o nome da imobiliaria:\n').upper()
    fone = input('Digite o telefone da imobiliaria\n')
    imob = Imobiliaria(nome, fone)
    # imob.set_adc_telefone(fone)
    lst_imobiliarias.append(imob)
    teste_na_lista()
    # pega_telefone_imob()


def teste_na_lista():
    for imobiliaria in lst_imobiliarias:
        print(imobiliaria.get_nome_imob(), imobiliaria.get_telefones_imob())


def teste_telefone():
    for imobiliaria in lst_imobiliarias:
        print(imobiliaria.get_telefones_imob())


#opção 2
def adc_imovel():
    nome = input('digite o nome da imobiliaria ').upper()
    for imobiliaria in lst_imobiliarias:
        if imobiliaria.get_nome_imob() == nome:
            type = input('Digite o tipo de imovel ').upper()
            adress = input('Digite o endereço do imovel ').upper()
            status = int(input('Digite o status\n1 ALUGADO\n0 DISPONÍVEL '))
            imovel = Imovel(type, adress)
            imovel.set_status_imovel(status)
            imobiliaria.set_adc_imoveis_lst(imovel)


#opção 3
def relatorio_imobiliarias():
    imob_escolhida = input('Digite o nome da imobiliária para gerar relatório\n').upper()
    for imobiliaria in lst_imobiliarias:
        if imob_escolhida == imobiliaria.get_nome_imob():
            print(imobiliaria.itera_lista_imoveis())
            # print("Nome Imobiliaria: ",imobiliaria.get_nome_imob(),'\n')
            # print("Lista de telefones ",imobiliaria.get_telefones_imob(),'\n')
            # print("Imóveis: ",imobiliaria.itera_lista_imoveis(),'\n')


#opção 4
def altera_status():
    imobiliaria_escolhida = input('Informe a imobiliária\n').upper()
    for x, imobiliaria in enumerate(lst_imobiliarias):
        if imobiliaria_escolhida == imobiliaria.get_nome_imob():
            print(f"Imobiliária encontrada na posição {x} da lista")
            print(imobiliaria.itera_lista_imoveis())
            imovel_esc = input('Digite o endereço de um dos imóveis acima ').upper()
            for y, imovel in enumerate(imobiliaria.get_lst_imoveis()):
                if imovel_esc == imovel.get_endereco_imovel():
                    print(f"Endereço encontrado na posição {y}")
                    print(imovel.get_status())
                    status_atual = int(input('Digite 1 para alugado e 0 para disponível '))
                    imovel.set_status_imovel(status_atual)
                else:
                    continue
        else:
            continue


def deduplicar_imobiliaria(imob_texto):
    if lst_imobiliarias:
        for imobiliaria in lst_imobiliarias:
            if imobiliaria.get_nome_imob() == imob_texto.get_nome_imob():
                return False
    return True


def salva_texto():
    arquivo = open("imoveis.txt", "w")
    for imobiliaria in lst_imobiliarias:
        for imovel in imobiliaria.get_lst_imoveis():
            imob_txt = imobiliaria.get_nome_imob()
            fone_txt = imobiliaria.get_telefones_imob()
            tipo_txt = imovel.get_tipo_imovel()
            endereco_txt = imovel.get_endereco_imovel()
            status_txt = imovel.get_status()
            arquivo.write(str(imob_txt) +";"+ str(fone_txt)+";"+str(tipo_txt)+";"+str(endereco_txt)+";"+str(status_txt)+"\n")
    arquivo.close()



menu_principal =  """
  ================================
  --------------MENU--------------
  ================================
  0- Finalizar o Programa
  1- Adicionar Imobiliaria
  2- Adicionar Imovel
  3- Relatório Imobiliarias
  4- Alterar Status de Imovel
  ================================
  Escolha: """


def main():
    teclado = input(menu_principal)
    if teclado == "0":
        salva_texto()
        print('Programa encerrado')
    elif teclado == "1": adc_imobiliaria()
    elif teclado == "2": adc_imovel()
    elif teclado == "3": relatorio_imobiliarias()
    elif teclado == "4": altera_status()
    main()


arquivo = open("imoveis.txt", "r")
for linha in arquivo:
    status_txt = 0
    lista = linha.strip().split(";")
    imob_txt = Imobiliaria(lista[0], lista[1])
    # imob_txt.set_adc_telefone(lista[1])
    if deduplicar_imobiliaria(imob_txt):
        lst_imobiliarias.append(imob_txt)
    if str(lista[4]) == 'ALUGADO':
        status_txt = 1
    elif str(lista[4]) == 'DISPONIVEL':
        status_txt = 0
    imovel_txt = Imovel(lista[2], lista[3])
    imovel_txt.set_status_imovel(status_txt)
    for imobiliaria in lst_imobiliarias:
        if imobiliaria.get_nome_imob() == lista[0]:
            imobiliaria.set_adc_imoveis_lst(imovel_txt)
arquivo.close()

main()
