
# Jogo de escolha
# MISSÃO: criar um programa que simule um jogo simples de escolha com tela

import PySimpleGUI as sg


class Aventura:

    def __init__(self):

        self.escolha = None

    def Iniciar(self):

        #LAYOUT
        
        layout = [
            [sg.Text('Você está em sua casa e seu objetivo é chegar até a escola!\n Você prefere ir de ônibus(1),bicicleta(2) ou andando(3)?')],
            [sg.Button("1",size = (15,2) ) , sg.Button('2',size = (15,2)) , sg.Button('3',size = (15,2)) ],
            [sg.Button('SAIR')]
                
        ]

        #JANELA
        self.janela = sg.Window('Jogo de aventura!', layout=layout)

        
        self.continuar = True
        while self.continuar ==  True:
                
            # OS VALORES

            self.eventos , self.valores = self.janela.Read()

# ESCOLHA ÔNIBUS:

            # O QUE FAZER COM ESSES VALORES

            if self.eventos == 'SAIR' or self.eventos == sg.WINDOW_CLOSED:
                break

            elif self.eventos == '1':
                
                self.janela.close()
                

                # Layout Onibus
                layout_Onibus = [
                    [sg.Text('Você quer pegar o ônibus 433(1),587(2) ou 990(3) ?')],
                    [sg.Button("1",size = (15,2)), sg.Button('2',size = (15,2)), sg.Button('3',size = (15,2))],
                    [sg.Button('SAIR')]
                    
                ]

                # JANELA
                self.janela_Onibus = sg.Window('Jogo de aventura!', layout=layout_Onibus)

                self.continuar_Onibus = True
                while self.continuar_Onibus ==  True:

                    # OS VALORES

                    self.eventos_onibus , self.valores_onibus = self.janela_Onibus.Read()

                     # O QUE FAZER COM ESSES VALORES

                    if self.eventos_onibus == 'SAIR' or self.eventos_onibus == sg.WINDOW_CLOSED:

                        break


                    elif self.eventos_onibus == '1':

                        self.janela_Onibus.close()

                        #LAYOUT

                        layout_Onibus_433 = [
                            [sg.Text('Você chegou numa perfumaria')],
                            [sg.Text('FIM DE JOGO!')],
                            [sg.Button('SAIR')]


                        ]

                         #JANELA

                        self.janela_Onibus_433 = sg.Window('Jogo de aventura!', layout=layout_Onibus_433)

        
                        self.continuar_Onibus_433 = True
                        while self.continuar_Onibus_433 ==  True:
                            # OS VALORES

                            self.eventos_Onibus_433 , self.valores_Onibus_433 = self.janela_Onibus_433.Read()

                            if self.eventos_Onibus_433 == 'SAIR' or self.eventos_Onibus_433 == sg.WINDOW_CLOSED:
                                break

                    elif self.eventos_onibus == '2':

                        self.janela_Onibus.close()

                        #LAYOUT

                        layout_Onibus_587 = [
                            [sg.Text('Você chegou num cemitério')],
                            [sg.Text('FIM DE JOGO!')],
                            [sg.Button('SAIR')]


                        ]

                         #JANELA

                        self.janela_Onibus_587 = sg.Window('Jogo de aventura!', layout=layout_Onibus_587)

        
                        self.continuar_Onibus_587 = True
                        while self.continuar_Onibus_587 ==  True:
                            # OS VALORES

                            self.eventos_Onibus_587 , self.valores_Onibus_587 = self.janela_Onibus_587.Read()

                            if self.eventos_Onibus_587 == 'SAIR' or self.eventos_Onibus_587 == sg.WINDOW_CLOSED:
                                break

                    else:

                        self.janela_Onibus.close()

                        #LAYOUT

                        layout_Onibus_990 = [
                            [sg.Text('Você chegou num shopping')],
                            [sg.Text('FIM DE JOGO!')],
                            [sg.Button('SAIR')]

                        ]

                         #JANELA

                        self.janela_Onibus_990 = sg.Window('Jogo de aventura!', layout=layout_Onibus_990)

        
                        self.continuar_Onibus_990 = True
                        while self.continuar_Onibus_990 ==  True:
                            # OS VALORES

                            self.eventos_Onibus_990 , self.valores_Onibus_990 = self.janela_Onibus_990.Read()

                            if self.eventos_Onibus_990 == 'SAIR' or self.eventos_Onibus_990 == sg.WINDOW_CLOSED:
                                break


                
# ESCOLHA BICICLETA:

            elif self.eventos == '2':
                
                self.janela.close()
                

                # Layout bicicleta
                layout_Bicicleta = [
                    [sg.Text('Você quer ir pela ponte(1), ciclovia(2) ou estrada de terra(3) ?')],
                    [sg.Button("1",size = (15,2)), sg.Button('2',size = (15,2)), sg.Button('3',size = (15,2))],
                    [sg.Button('SAIR')]
                    
                ]

                # JANELA
                self.janela_Bicicleta = sg.Window('Jogo de aventura!', layout=layout_Bicicleta)

                self.continuar_Bicicleta = True
                while self.continuar_Bicicleta ==  True:
                
                # OS VALORES

                    self.eventos_Bicicleta , self.valores_Bicicleta = self.janela_Bicicleta.Read()
                
                # O QUE FAZER COM OS VALORES

                    if self.eventos_Bicicleta == 'SAIR' or self.eventos_Bicicleta == sg.WINDOW_CLOSED:

                        break

                    elif self.eventos_Bicicleta == '1':

                        self.janela_Bicicleta.close()

                        #LAYOUT

                        layout_Bicicleta_ponte = [
                            [sg.Text('Você chegou numa praia ')],
                            [sg.Text('FIM DE JOGO!')],
                            [sg.Button('SAIR')]


                        ]

                         #JANELA

                        self.janela_Bicicleta_ponte = sg.Window('Jogo de aventura!', layout=layout_Bicicleta_ponte)

        
                        self.continuar_Bicicleta_ponte = True
                        while self.continuar_Bicicleta_ponte ==  True:
                            # OS VALORES

                            self.eventos_Bicicleta_ponte , self.valores_Bicicleta_ponte = self.janela_Bicicleta_ponte.Read()

                            if self.eventos_Bicicleta_ponte == 'SAIR' or self.eventos_Bicicleta_ponte == sg.WINDOW_CLOSED:
                                break

                    elif self.eventos_Bicicleta == '2':

                        self.janela_Bicicleta.close()

                        #LAYOUT

                        layout_Bicicleta_ciclovia = [
                            [sg.Text(' Você chegou num estádio de futebol ')],
                            [sg.Text('FIM DE JOGO!')],
                            [sg.Button('SAIR')]


                        ]

                         #JANELA

                        self.janela_Bicicleta_ciclovia = sg.Window('Jogo de aventura!', layout=layout_Bicicleta_ciclovia)

        
                        self.continuar_Bicicleta_ciclovia = True
                        while self.continuar_Bicicleta_ciclovia ==  True:
                            # OS VALORES

                            self.eventos_Bicicleta_ciclovia , self.valores_Bicicleta_ciclovia = self.janela_Bicicleta_ciclovia.Read()

                            

                            if self.eventos_Bicicleta_ciclovia == 'SAIR' or self.eventos_Bicicleta_ciclovia == sg.WINDOW_CLOSED:
                                break

                    else:

                        self.janela_Bicicleta.close()

                        #LAYOUT

                        layout_Bicicleta_estradaterra = [
                            [sg.Text('Você chegou numa fábrica abandonada  ')],
                            [sg.Text('FIM DE JOGO!')],
                            [sg.Button('SAIR')]


                        ]

                         #JANELA

                        self.janela_Bicicleta_estradaterra = sg.Window('Jogo de aventura!', layout=layout_Bicicleta_estradaterra)

        
                        self.continuar_Bicicleta_estradaterra = True
                        while self.continuar_Bicicleta_estradaterra ==  True:
                            # OS VALORES

                            self.eventos_Bicicleta_estradaterra , self.valores_Bicicleta_estradaterra = self.janela_Bicicleta_estradaterra.Read()

                            if self.eventos_Bicicleta_estradaterra == 'SAIR' or self.eventos_Bicicleta_estradaterra == sg.WINDOW_CLOSED:
                                break


# ESCOLHA ANDANDO:

            else:

                self.janela.close()
                

                # Layout andando

                layout_Andando = [
                    [sg.Text('Você quer ir pela floresta fechada(1),velha ponte de madeira num rio cheio de crocodilos(2) ou por um um campo florido(3) ?')],
                    [sg.Button("1",size = (15,2)), sg.Button('2',size = (15,2)), sg.Button('3',size = (15,2))],
                    [sg.Button('SAIR')]
                    
                ]

                # JANELA
                self.janela_Andando = sg.Window('Jogo de aventura!', layout=layout_Andando)

                self.continuar_Andando = True
                while self.continuar_Andando ==  True:
                
                # OS VALORES

                    self.eventos_Andando , self.valores_Andando = self.janela_Andando.Read()

                # O QUE FAZER COM OS VALORES

                    if self.eventos_Andando == 'SAIR' or self.eventos_Andando == sg.WINDOW_CLOSED:

                        break

                    elif self.eventos_Andando == '1':

                        self.janela_Andando.close()

                        #LAYOUT

                        layout_Andando_floresta = [
                            [sg.Text('Você chegou numa cachoeira')],
                            [sg.Text('FIM DE JOGO!')],
                            [sg.Button('SAIR')]


                        ]

                         #JANELA

                        self.janela_Andando_floresta = sg.Window('Jogo de aventura!', layout=layout_Andando_floresta)

        
                        self.continuar_Andando_floresta = True
                        while self.continuar_Andando_floresta ==  True:
                            # OS VALORES

                            self.eventos_Andando_floresta , self.valores_Andando_floresta = self.janela_Andando_floresta.Read()

                            if self.eventos_Andando_floresta == 'SAIR' or self.eventos_Andando_floresta == sg.WINDOW_CLOSED:
                                break

                    elif self.eventos_Andando == '2':

                        self.janela_Andando.close()

                        #LAYOUT

                        layout_Andando_velha_ponte = [
                            [sg.Text('Você chegou na escola.')],
                            [sg.Text('PARABÉNS!')],
                            [sg.Button('SAIR')]


                        ]

                         #JANELA

                        self.janela_Andando_velha_ponte = sg.Window('Jogo de aventura!', layout=layout_Andando_velha_ponte)

        
                        self.continuar_Andando_velha_ponte = True
                        while self.continuar_Andando_velha_ponte ==  True:
                            # OS VALORES

                            self.eventos_Andando_velha_ponte , self.valores_Andando_velha_ponte= self.janela_Andando_velha_ponte.Read()

                            if self.eventos_Andando_velha_ponte == 'SAIR' or self.eventos_Andando_velha_ponte == sg.WINDOW_CLOSED:
                                break

                    else:

                        self.janela_Andando.close()

                        #LAYOUT

                        layout_Andando_campo = [
                            [sg.Text('Você chegou numa igreja')],
                            [sg.Text('FIM DE JOGO!')],
                            [sg.Button('SAIR')]


                        ]

                         #JANELA

                        self.janela_Andando_campo = sg.Window('Jogo de aventura!', layout=layout_Andando_campo)

        
                        self.continuar_Andando_campo = True
                        while self.continuar_Andando_campo ==  True:
                            # OS VALORES

                            self.eventos_Andando_campo , self.valores_Andando_campo= self.janela_Andando_campo.Read()

                            if self.eventos_Andando_campo == 'SAIR' or self.eventos_Andando_campo == sg.WINDOW_CLOSED:
                                break


simular = Aventura()
simular.Iniciar()

