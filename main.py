import Database as f
import algorithm as a
import PySimpleGUI as sg
from Screens.screens import LoadQuestion
from Screens.screens import LoadResults
from Screens.screens import GenerateContent

# db_replacement = [
#     {
#         "vraag_nummer": 0,
#         "vraag_tekst": "In welke richting heb je al interesse?",
#         "vraag_antwoorden": [["Forensische ICT", "FICT", 4,]
#                              ["Interactie-Technologie", "IICT", 4,]
#                              ["Software Engineering", "SE", 4,]
#                              ["Databases", "DB", 4]]
#     },
#     {
#         "vraag_nummer": 1,
#         "vraag_tekst": "Welk van deze karaktereigenschappen is je sterkste punt?",
#         "vraag_antwoorden": [["analytisch denken", "FICT", 4,]
#                              ["samenwerken", "IICT", 4,]
#                              ["problem solving", "SE", 4,]
#                              ["precies werken", "DB", 4]]
#     },
#     {
#         "vraag_nummer": 2,
#         "vraag_tekst": "Welk van deze karaktereigenschappen is je zwakste punt?",
#         "vraag_antwoorden": [["analytisch denken", "FICT", 4]
#                              ["samenwerken", "IICT", 5]
#                              ["problem solving", "SE", "4,]
#                              ["precies werken", "punten_voor_specialisatie": "DB", "4]]
#     },
#     {
#         "vraag_nummer": 3,
#         "vraag_tekst": "Welk van deze omschrijvingen zijn het beste van toepassing?",
#         "vraag_antwoorden": [["Het liefst werk ik met mensen", "FICT", 4]
#                              ["Ik kan met anderen werken als het nodig is", "IICT", 4]
#                              ["Ik kan goed samenwerken in een team", "SE", 4]
#                              ["Ik werk liever zoveel mogelijk alleen", "DB", 4]]
#     }
# ]

# function that generates a question layout for each entry

# PLACE ALL YOUR CODE TO RUN/TEST HERE!
def main():
    # f.init('../Firebase key/mtisrb-firebase-adminsdk-u1zpn-13e20fa0ad.json', fill=True)
    # for i in range(15):
    #     f.upload("user_answers", i, f"Hello world {i}")
    # a.Algorithm.init(data=[
    #    f.get_data("answers"),
    #    f.get_data("field_of_study"),
    #    f.get_data("question"),
    #    f.get_data("points"),
    #    f.get_data("user_answers"),
    # ])

    # a.Algorithm.cs()

    # COMMENTED OUT BECAUSE IT CAUSED ERRORS AT JASON"S PC
    # f.parse('../Firebase key/mtisrb-firebase-adminsdk-u1zpn-13e20fa0ad.json')
    # f.fill_fb(f.load_data("resources/Database.xlsx", "database"))

    # choose theme
    sg.theme('Default1')

    q_col1, q_col2 = LoadQuestion.question_layout("Hier komt de vraag", "Antwoord 1", "Antwoord 2",
                                              "Antwoord 3", "Antwoord 4")
    r_col1, r_col2 = LoadResults.result_layout("Resultaat!")

    content = GenerateContent.draw_screens(q_col1, q_col2, r_col1, r_col2)

    # create the window, finalize it and start it at full screen
    window = sg.Window('Sorting Experience', content, element_justification='c',
                       icon="resources/img/sorting_hat.ico").finalize()
    window.Maximize()

    # creates the main window, finalizes it and makes it start in full screen mode

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
                    GenerateContent.switchcontent(window, "-welcome-", "-questions-")

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
                GenerateContent.switchcontent(window, "-questions-", '-end-')
            case "-close-":
                window.close()

    window.close()


if __name__ == '__main__':
    main()
