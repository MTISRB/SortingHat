import Database as f
import algorithm as a
import PySimpleGUI as sg
from Screens.screens import LoadQuestion


# function that reads the placeholder dictionary and generates a question for each entry


# function to close the current content frame and open the next one
def switchcontent(activewindow, currentc, nextc):
    """
    :param activewindow: The window in which the content is placed
    :param currentc: The current key of the content-frame that has to disappear
    :param nextc: The key of the content-frame you want to display next
    :return:
    """
    activewindow[currentc].update(visible=False)
    activewindow[nextc].update(visible=True)
    activewindow.refresh()

# PLACE ALL YOUR CODE TO RUN/TEST HERE!
def main():

    f.init('../Firebase key/mtisrb-firebase-adminsdk-u1zpn-13e20fa0ad.json', fill=True)
    # for i in range(15):
    #     f.upload("user_answers", i, f"Hello world {i}")
    #a.Algorithm.init(data=[
    #    f.get_data("answers"),
    #    f.get_data("field_of_study"),
    #    f.get_data("question"),
    #    f.get_data("points"),
    #    f.get_data("user_answers"),
    #])

    #a.Algorithm.cs()

    #COMMENTED OUT BECAUSE IT CAUSED ERRORS AT JASON"S PC
    #f.parse('../Firebase key/mtisrb-firebase-adminsdk-u1zpn-13e20fa0ad.json')
    #f.fill_fb(f.load_data("resources/Database.xlsx", "database"))

    # choose theme
    sg.theme('Default1')

    col1, col2 = LoadQuestion.questionlayout(LoadQuestion,"Hier komt de vraag", "Antwoord 1", "Antwoord 2",
                                             "Antwoord 3", "Antwoord 4")

    # The different screens, put into frames
    screens = [[
        sg.Frame('', [
            [sg.Image('resources/img/sorting_hat.png')],
            [sg.Text('Welkom bij de Sorting Experience! Voer hieronder je naam in!')],
            [sg.Input(key="-name-")],
            [sg.Button("Begin de Sorting Experience!", key="-beginExperience-")]],
                 visible=True, border_width=0, element_justification='c', key="-welcome-"),

        sg.Frame('', [
            [sg.Column(col1, element_justification='c'),
             sg.Column(col2, element_justification='c')]],
                 visible=False, border_width=0, element_justification='c', key="-questions-"),

        sg.Frame('', [
            [sg.Text('Je resultaat is binnen!')],
            [sg.Text('Jou aanbevolen specialisatie is:'), sg.InputText()],
            [sg.Button('Sluiten', key="-close-")],
            [sg.Image('resources/img/sorting_hat.png')]],
                 visible=False, border_width=0, element_justification='c', key="-end-")

    ]
    ]

    # create the window, finalize it and start it at full screen
    window = sg.Window('Sorting Experience', screens, element_justification='c', icon="resources/img/sorting_hat.ico").finalize()

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

        match event:
            case sg.WIN_CLOSED:
                break
            case "-beginExperience-":
                # Harry Potter easter egg 1
                if values["-name-"] == "Harry Potter":
                    sg.popup(
                        'Harry Potter!? Wil je geen schouwer meer zijn? \n'
                        'Achja, de IT-wereld verwelkomt je met beide armen!',
                        title="The boy who lived...",
                        icon="resources/img/sorting_hat.ico")

                    enteredname = ""
                elif values["-name-"] == "":
                    sg.popup("Je moet een geldige naam invoeren",
                             title="Stupify!",
                             icon="resources/img/sorting_hat.ico")

                    enteredname = ""
                else:
                    enteredname = values["-name-"]

                if enteredname != "":
                    switchcontent(window, "-welcome-", "-questions-")

            case "-EnterQuestion-":
                # dit gedeelte wordt geactiveerd wanneer er op de verder knop gedrukt wordt bij het vragen scherm,
                # en je kan hier zien welk van de vier keuzes gekozen is
                if values["-Antwoord1-"]:
                    # Geeft aan in de terminal dat het eerste antwoord gekozen is
                    print("Gekozen antwoord is 1")
                elif values["-Antwoord2-"]:
                    # Geeft aan in de terminal dat het tweede antwoord gekozen is
                    print("Gekozen antwoord is 2")
                elif values["-Antwoord3-"]:
                    # Geeft aan in de terminal dat het derde antwoord gekozen is
                    print("Gekozen antwoord is 3")
                elif values["-Antwoord4-"]:
                    # Geeft aan in de terminal dat het vierde antwoord gekozen is
                    print("Gekozen antwoord is 4")
                switchcontent(window, "-questions-", '-end-')
            case "-close-":
                window.close()

    window.close()


if __name__ == '__main__':
    main()
