from PySimpleGUI import PySimpleGUI as sg

#tema da janela
sg.theme('Reddit')

#layout da janela
layout = [
    [sg.Text('Usuário'), sg.Input(key='Usuário', size=(20, 1))],
    [sg.Text('Senha'), sg.Input(key='Senha', password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar login?')],
    [sg.Checkbox('Junior'), sg.Checkbox('Sênior'), sg.Checkbox('Pleno')],
    [sg.Button('Entrar')]
]
#janela
janela = sg.Window('janela de login', layout)

#ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['Usuário'] == 'matheus' and valores['Senha'] == '12345':
            print('Bem vindo')
        else:
            print('acesso negado')