import Database as f
import algorithm as a
import PySimpleGUI as sg
from Screens.screens import LoadQuestion
from Screens.screens import LoadResults
from Screens.screens import GenerateContent

# PLACE ALL YOUR CODE TO RUN/TEST HERE!
def main():
    #f.init('../Firebase key/mtisrb-firebase-adminsdk-u1zpn-0b5778f94d.json', fill=True)

    # a.Algorithm.init(data=[
    #    f.get_data("answers"),
    #    f.get_data("field_of_study"),
    #    f.get_data("question"),
    #    f.get_data("points"),
    #    f.get_data("user_answers"),
    # ])
    #
    # a.Algorithm.cs()

    #f.parse('../Firebase key/mtisrb-firebase-adminsdk-u1zpn-0b5778f94d.json')
    f.fill_fb(f.load_data("resources/Database.xlsx", "database"))

    # choose theme
    sg.theme('Default1')

#   question screen
    q_col1, q_col2 = LoadQuestion.question_layout("Hier komt de vraag", "Antwoord 1", "Antwoord 2",
                                              "Antwoord 3", "Antwoord 4")
    # end sceen
    r_col1, r_col2 = LoadResults.result_layout("Resultaat!")

    # content
    content = GenerateContent.draw_screens(q_col1, q_col2, r_col1, r_col2)

    # create the window, finalize it and start it at full screen
    window = sg.Window('Sorting Experience', content, element_justification='c',
                       icon="resources/img/sorting_hat.ico").finalize()
    window.Maximize()

    # creates the main window, finalizes it and makes it start in full screen mode

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "-beginExperience-":
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
                GenerateContent.switchcontent(window, "-welcome-", "-questions-")

        elif event == "-EnterQuestion-":
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
            GenerateContent.switchcontent(window, "-questions-", '-end-')
        elif event == "-close-":
                window.close()
        else:
            window.close()


if __name__ == '__main__':
    main()
