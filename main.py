import Database as f
import PySimpleGUI as sg



# PLACE ALL YOUR CODE TO RUN/TEST HERE!
def main():
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
