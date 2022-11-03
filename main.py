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
    kop = ("Helvetica", 25)
    platte_tekst = ("Helvetica", 15)

    col1 = [[sg.Image('resources/img/sorting_hat-3.png')]]
    col2 = [[sg.Text("Hier komt de vraag", key='-text-', font=kop)],
            [sg.Radio('Antwoord 1', "RADIO1", font=platte_tekst)],
            [sg.Radio('Antwoord 2', "RADIO1", font=platte_tekst)],
            [sg.Radio('Antwoord 3', "RADIO1", font=platte_tekst)],
            [sg.Radio('Antwoord 4', "RADIO1", font=platte_tekst)],
            [sg.Button('< Terug', font=platte_tekst, size=7), sg.Button('Verder >', font=platte_tekst, size=7)]]

    layoutVragen = [[sg.VPush()],
                    [sg.Push(), sg.Column(col1), sg.Column(col2), sg.Push()],
                    [sg.VPush()]]

    windowVragen = sg.Window('The Sorting Experience', layoutVragen, element_justification='c',
                             size=(1600, 900)).Finalize()
    windowVragen.Maximize()
    #EIND CODE ELISE

    #CODE LESLIE
    sg.theme("LightGreen")

    kop_text = ('Helvetica', 25)
    platte_text = ('Helvectica', 15)

    col1 = [sg.Image(r'C:\Users\leslie2k4\PycharmProjects\sorting testing\sorting_hat-2.png')],
    col2 = [sg.Text('Je resultaat is binnen', font=kop_text)], \
           [sg.Text('Jij past bij:', font=platte_text), sg.Text('*result*', font=platte_text)],
    col3 = [sg.Text("")], \
           [sg.Button('opnieuw')]

    layoutEind = [[sg.VPush()],
                  [sg.Push(), sg.Column(col1), sg.Column(col2), sg.Column(col3), sg.Push()],
                  [sg.VPush()]]

    windowEind = sg.Window("The Sorting Experience", layoutEind, size=(1920, 1080))
    event, values = windowEind.read()

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
