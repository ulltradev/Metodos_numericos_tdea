import PySimpleGUI as sg      
from regla_falsa import *

sg.theme('DarkAmber')    # Keep things interesting for your users

layout = [[sg.Text("-- dada la funcion  math.pow(x,3) + 2*math.pow(x,2) - 3*x - 1")],
          [sg.Text("-- y basado en el siguiente input de ejemplo")],
          [sg.Text("-- Input de ejemplo: regulaFalsi(1, 2, 0.0004, 100)")], 
          [sg.Text("indique el punto inferior, parametro poscisional 1")],      
          [sg.Input(key='a_Param')], 
          [sg.Text("indique el punto superior, parametro poscisional 2")],      
          [sg.Input(key='b_Param')], 
          [sg.Text("indique la tolerancia, parametro poscisional 3")],      
          [sg.Input(key='tol_Param')],
          [sg.Text("indique el numero maximo de iteraciones, parametro poscisional 4")],      
          [sg.Input(key='n_Param')],
          [sg.Button('Read'), sg.Exit()]]      

window = sg.Window('Regla Falsa', layout)      

while True:                             # The Event Loop
    event, values = window.read() 

    regla_falsa(int(values['a_Param']),\
                int(values['b_Param']),\
                float(values['tol_Param']),\
                int(values['n_Param']))

    if event == sg.WIN_CLOSED or event == 'Exit':
        break      

window.close()