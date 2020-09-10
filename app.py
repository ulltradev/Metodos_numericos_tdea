import PySimpleGUI as sg      

sg.theme('DarkAmber')    # Keep things interesting for your users

layout = [[sg.Text('Persistent window')],
          [sg.Text("-- dada la funcion  math.pow(x,3) + 2*math.pow(x,2) - 3*x - 1")],
          [sg.Text("-- y basado en el siguiente input de ejemplo")],
          [sg.Text("-- Input de ejemplo: regulaFalsi(1, 2, 0.0004, 100)")],      
          [sg.Input(key='-IN-')],      
          [sg.Button('Read'), sg.Exit()]]      

window = sg.Window('Regla Falsa', layout)      

while True:                             # The Event Loop
    event, values = window.read() 
    print(event, values)       
    if event == sg.WIN_CLOSED or event == 'Exit':
        break      

window.close()