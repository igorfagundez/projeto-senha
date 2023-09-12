import random
import PySimpleGUI as sg
import os 

class PassGen: 
    #Layout
    def __init__(self):
        sg.theme('Black')
        layout = [  
            [sg.Text('Site/Software', size=(10,1)),
             sg.Input(key='site', size=(20,1))],
             [sg.Text('E-mail/Usuario', size=(10,1), sg.input(key='usuario', size=(20,1)))],
             [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(range(30)), key='total_chars', default_value=1, size=(3,1))],
             [sg.Output(size=(32,5))],
             [sg.Button('Gerar Senha')]
        ]
    #Declarar Janela
    self.janela = sg.Window('Password Generator', layout)
    def iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            
    def salvar_senha(self):
        pass

gen = PassGen()
gen.iniciar