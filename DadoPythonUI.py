import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6

        self.layout = [
            [sg.Text('Jogar o Dado?')],
            [sg.Button('sim'),sg.Button('nao')]
        ]
    
    def Iniciar(self):
        #Cria janela
        self.janela = sg.Window('Simulador de Dado',layout=self.layout)
        #Le os valores da tela
        self.eventos, self.valores = self.janela.Read()
        #Execução dos dados
        try:
            if self.eventos == 'sim':
                self.GerarValorDoDado()
            elif self.eventos == 'nao':
                print('Agradecemos a sua participaçao!')
            else:
                print('Favor digitar sim ou nao')
        except:
            print('Ocorreu um erro')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()
