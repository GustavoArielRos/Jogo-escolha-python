# Jogo de escolha
# MISSÃO: criar um programa que simule um jogo simples de escolha.


class Aventura:

    def __init__(self):

        self.escolha = None

# Função da primeira escolha
    def Lista_Escolhas(self):

        self.primeira_lista = ['ônibus','bicicleta','andando']

# Função das escolhas de ônibus
    def Escolhas_Onibus(self):

        self.onibus_lista = ['433','587','990']

        self.onibus_433 = 'Você chegou numa perfumaria\n FIM DE JOGO!!!'
        self.onibus_587 = 'Você chegou num cemitério\n FIM DE JOGO!!!'
        self.onibus_990 = 'Você chegou num shopping\n FIM DE JOGO!!!'

# Função das escolhas de bicicleta
    def Escolhas_Bicicleta(self):

        self.bicicleta_lista = ['ponte','ciclovia','estrada de terra']

        self.bicicleta_ponte = ' Você chegou numa praia\n FIM DE JOGO!!!' 
        self.bicicleta_ciclovia = ' Você chegou num estádio de futebol\n FIM DE JOGO!!!'
        self.bicicleta_estrada_de_terra = 'Você chegou numa fábrica abandonada\n FIM DE JOGO!!!'

# Função das escolhas de andando
    def Escolhas_Andando(self):

        self.andando_lista = ['floresta fechada', 'velha ponte de madeira num rio cheio de crocodilos',
                              'um campo florido']

        self.andando_floresta = 'Você chegou numa cachoeira\n FIM DE JOGO!!!'
        self.andando_velha_ponte = 'Você chegou na escola\n PARABÉNS, VOCÊ GANHOU O JOGO'
        self.campo_florido = 'Você chegou numa igreja\n FIM DE JOGO!!!'



# Função iniciar
    def Iniciar(self):

        self.Lista_Escolhas()

        print('Você está em sua casa e seu objetivo é chegar até a escola!\n'
              'Você prefere ir de ',self.primeira_lista[0],',',
               self.primeira_lista[1],'ou', self.primeira_lista[2],'?')
        
        try:
            
            self.escolha = input('Escolha uma dessas 3 opções: ')

            if self.escolha == self.primeira_lista[0]:

                self.Escolhas_Onibus()
                print('Você quer pegar o ônibus',self.onibus_lista[0],',',self.onibus_lista[1],'ou',
                self.onibus_lista[2],'?')
                self.escolha_onibus_1 = input('Escolha a opção: ')

                if self.escolha_onibus_1 == self.onibus_lista[0]:
                    print(self.onibus_433)

                elif self.escolha_onibus_1 == self.onibus_lista[1]:
                    print(self.onibus_587)

                elif self.escolha_onibus_1 == self.onibus_lista[2]:
                    print(self.onibus_990)

                else:
                    print('Erro no programa! Opção inválida,as opções são somente as palavras',self.onibus_lista[0],',',self.onibus_lista[1],'ou',self.onibus_lista[2])
                    
                    



            elif self.escolha == self.primeira_lista[1]:
                
                self.Escolhas_Bicicleta()
                print('Você quer',self.bicicleta_lista[0],',',self.bicicleta_lista[1],'ou',self.bicicleta_lista[2],'?')
                self.escolha_bicicleta_1 = input('Escolha a opção: ')

                if self.escolha_bicicleta_1 == self.bicicleta_lista[0]:
                    print(self.bicicleta_ponte)

                elif self.escolha_bicicleta_1 == self.bicicleta_lista[1]:
                    print(self.bicicleta_ciclovia)

                elif self.escolha_bicicleta_1 == self.bicicleta_lista[2]:
                    print(self.bicicleta_estrada_de_terra)

                else:
                    print('Erro no programa! Opção inválida,as opções são somente as palavras',self.bicicleta_lista[0],',',self.bicicleta_lista[1],'ou',self.bicicleta_lista[2])
                    
                    

            elif self.escolha == self.primeira_lista[2]:

                self.Escolhas_Andando()
                print('Você quer passar por uma ',self.andando_lista[0],',',self.andando_lista[1],'ou',self.andando_lista[2],'?')
                self.escolha_andando_1 = input('Escolha a opção: ')

                if self.escolha_andando_1 == self.andando_lista[0]:
                    print(self.andando_floresta)

                elif self.escolha_andando_1 == self.andando_lista[1]:
                    print(self.andando_velha_ponte)

                elif self.escolha_andando_1 == self.andando_lista[2]:
                    print(self.campo_florido)

                else:
                    print('Erro no programa! Opção inválida,as opções são somente as palavras',self.andando_lista[0],',',self.andando_lista[1],'ou',self.andando_lista[2])

            else:
                print('Opção inválidade, as opções são somente as palavras',self.primeira_lista[0],',',self.primeira_lista[1],'ou',self.primeira_lista[2])
                
                self.Iniciar()

        except:
            print('Opção Inválida!')
            self.Iniciar()

simular = Aventura()
simular.Iniciar()