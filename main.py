import Database as f
import algorithm as a
import PySimpleGUI as sg


# PLACE ALL YOUR CODE TO RUN/TEST HERE!
def main():

    f.init('../Firebase key/mtisrb-firebase-adminsdk-u1zpn-13e20fa0ad.json', fill=True)
    # for i in range(15):
    #     f.upload("user_answers", i, f"Hello world {i}")
    a.Algorithm.init(data=[
        f.get_data("answers"),
        f.get_data("field_of_study"),
        f.get_data("question"),
        f.get_data("points"),
        f.get_data("user_answers"),
    ])

    a.Algorithm.cs()

    #COMMENTED OUT BECAUSE IT CAUSED ERRORS AT JASON"S PC
    #f.parse('../Firebase key/mtisrb-firebase-adminsdk-u1zpn-13e20fa0ad.json')
    #f.fill_fb(f.load_data("resources/Database.xlsx", "database"))

    # choose theme
    sg.theme('Default1')

    # de widgets die in de het main window moeten komen
    layoutWelcome = [
        [sg.Image('resources/img/sorting_hat.png')],
        [sg.Text('Welkom bij de Sorting Experience! Voer hieronder je naam in!')],
        [sg.Input()],
        [sg.Button("Begin de Sorting Experience!")]
    ]


    #CODE ELISE
    col1 = [[sg.Image('resources/img/sorting_hat.png', size=(300, 300))]]
    col2 = [[sg.Text("Hier komt de vraag")],
            [sg.Radio('Antwoord 1', "RADIO1")],
            [sg.Radio('Antwoord 2', "RADIO1")],
            [sg.Radio('Antwoord 3', "RADIO1")],
            [sg.Radio('Antwoord 4', "RADIO1")],
            [sg.Button('Terug'), sg.Button('Verder')]]

    layoutVragen = [[sg.Column(col1, element_justification='c'),
                    sg.Column(col2, element_justification='c')]]

    windowVragen = sg.Window('The Sorting Experience', layoutVragen, element_justification='c', size=(800, 600)).Finalize()
    windowVragen.Maximize()
    while True:
        event, values = windowVragen.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break

    windowVragen.close()
    #EIND CODE ELISE

    #CODE LESLIE
    layoutEind = [[sg.Text('Je resultaat is binnen!')],
              [sg.Text('Jou aanbevolen specialisatie is:'), sg.InputText()],
              [sg.Button('verder'), sg.Button('opnieuw')],
              [sg.Image('/Users/leslie2k4/pythonProject/sorting testing/the_sorting_hat.png')]]

    windowEind = sg.Window('resultaat', layoutEind, size=(800, 600), element_justification="c")

    while True:
        event, values = windowEind.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

    windowEind.close()
    #EIND LESLIE



    # creates the main window, finalizes it and makes it start in full screen mode
    window = sg.Window('Sorting Experience', layoutWelcome, element_justification='c').finalize()
    window.Maximize()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Begin de Sorting Experience!":
            if values[1] == "Harry Potter":
                sg.popup(
                    'Harry Potter!? Wil je geen schouwer meer zijn? \n'
                    'Achja, de IT-wereld verwelkomt je met beide armen!',
                    no_titlebar=True)

    window.close()

if __name__ == '__main__':
    main()
