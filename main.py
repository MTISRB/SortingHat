import Database as f
import algorithm as a
import PySimpleGUI as sg
import utils

from Screens.screens import LoadQuestion
from Screens.screens import LoadResults
from Screens.screens import Content


# PLACE ALL YOUR CODE TO RUN/TEST HERE!
def main():
    f.init('../Firebase key/mtisrb-firebase-adminsdk-u1zpn-13e20fa0ad.json', fill=False)

    # f.upload("user_answers", 0, 1)
    # f.upload("user_answers", 1, 0)
    # f.upload("user_answers", 2, 2)
    # f.upload("user_answers", 3, 3)
    # f.upload("user_answers", 4, 2)
    # f.upload("user_answers", 5, 0)
    # f.upload("user_answers", 6, 1)
    # f.upload("user_answers", 7, 3)
    # f.upload("user_answers", 8, 3)
    # f.upload("user_answers", 9, 0)
    # f.upload("user_answers", 10, 3)
    # f.upload("user_answers", 11, 2)
    # f.upload("user_answers", 12, 1)
    # f.upload("user_answers", 13, 2)
    # f.upload("user_answers", 14, 3)

    # a.Algorithm.init(data=[
    #    f.get_data("answers"),
    #    f.get_data("field_of_study"),
    #    f.get_data("question"),
    #    f.get_data("points"),
    #    f.get_data("user_answers"),
    # ])
    #
    # print(a.Algorithm.cs())

    # choose theme

    q_screen = []
    for _ in range(15):
        q_screen.append(LoadQuestion)

    sorted_questions = utils.sort(f.get_data("question"), "question", "question_id")
    sorted_answers = utils.sort(f.get_data("answers"), "answers", "answers_id")

    sg.theme('Default1')

#   question screen
    q_col1, q_col2 = LoadQuestion.question_layout(1, sorted_questions[0][0], sorted_answers[0][0], sorted_answers[0][1], sorted_answers[0][2], sorted_answers[0][3])
    q_col3, q_col4 = LoadQuestion.question_layout(5, sorted_questions[1][0], sorted_answers[1][0], sorted_answers[1][1], sorted_answers[1][2], sorted_answers[1][3])
    q_col5, q_col6 = LoadQuestion.question_layout(9, sorted_questions[2][0], sorted_answers[2][0], sorted_answers[2][1], sorted_answers[2][2], sorted_answers[2][3])
    q_col7, q_col8 = LoadQuestion.question_layout(13, sorted_questions[3][0], sorted_answers[3][0], sorted_answers[3][1], sorted_answers[3][2], sorted_answers[3][3])
    q_col9, q_col10 = LoadQuestion.question_layout(17, sorted_questions[4][0], sorted_answers[4][0], sorted_answers[4][1], sorted_answers[4][2], sorted_answers[4][3])
    q_col11, q_col12 = LoadQuestion.question_layout(21, sorted_questions[5][0], sorted_answers[5][0], sorted_answers[5][1], sorted_answers[5][2], sorted_answers[5][3])
    q_col13, q_col14 = LoadQuestion.question_layout(25, sorted_questions[6][0], sorted_answers[6][0], sorted_answers[6][1], sorted_answers[6][2], sorted_answers[6][3])
    q_col15, q_col16 = LoadQuestion.question_layout(29, sorted_questions[7][0], sorted_answers[7][0], sorted_answers[7][1], sorted_answers[7][2], sorted_answers[7][3])
    q_col17, q_col18 = LoadQuestion.question_layout(33, sorted_questions[8][0], sorted_answers[8][0], sorted_answers[8][1], sorted_answers[8][2], sorted_answers[8][3])
    q_col19, q_col20 = LoadQuestion.question_layout(37, sorted_questions[9][0], sorted_answers[9][0], sorted_answers[9][1], sorted_answers[9][2], sorted_answers[9][3])
    q_col21, q_col22 = LoadQuestion.question_layout(41, sorted_questions[10][0], sorted_answers[10][0], sorted_answers[10][1], sorted_answers[10][2], sorted_answers[10][3])
    q_col23, q_col24 = LoadQuestion.question_layout(45, sorted_questions[11][0], sorted_answers[11][0], sorted_answers[11][1], sorted_answers[11][2], sorted_answers[11][3])
    q_col25, q_col26 = LoadQuestion.question_layout(49, sorted_questions[12][0], sorted_answers[12][0], sorted_answers[12][1], sorted_answers[12][2], sorted_answers[12][3])
    q_col27, q_col28 = LoadQuestion.question_layout(53, sorted_questions[13][0], sorted_answers[13][0], sorted_answers[13][1], sorted_answers[13][2], sorted_answers[13][3])
    q_col29, q_col30 = LoadQuestion.question_layout(57, sorted_questions[14][0], sorted_answers[14][0], sorted_answers[14][1], sorted_answers[14][2], sorted_answers[14][3])

    # end sceen
    r_col1, r_col2 = LoadResults.result_layout("Resultaat!")

    # content
    content = Content.draw_screens(
        (
            q_col1, q_col3, q_col5,
            q_col7, q_col9, q_col11,
            q_col13, q_col15, q_col17,
            q_col19, q_col21, q_col23,
            q_col25, q_col27, q_col29,
        ),
        (
            q_col2, q_col4, q_col6,
            q_col8, q_col10, q_col12,
            q_col14, q_col16, q_col18,
            q_col20, q_col22, q_col24,
            q_col26, q_col28, q_col30,
        ),
        r_col1, r_col2)

    # create the window, finalize it and start it at full screen
    window = sg.Window('Sorting Experience', content, element_justification='c',
                       icon="resources/img/sorting_hat.ico", resizable=True).finalize()
    window.Maximize()

    # creates the main window, finalizes it and makes it start in full screen mode
    while True:
        event, values = window.read()
        index = 1

        print(values, event)

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

                entered_name = ""
            elif values["-name-"] == "":
                sg.popup("Je moet een geldige naam invoeren",
                         title="Stupify!",
                         icon="resources/img/sorting_hat.ico")

                entered_name = ""
            else:
                entered_name = values["-name-"]

            if entered_name != "":
                Content.switch_content(window, "-welcome-", "-questions_1-")
        elif "Next" in event:
            # dit gedeelte wordt geactiveerd wanneer er op de verder knop gedrukt wordt bij het vragen scherm,
            # en je kan hier zien welk van de vier keuzes gekozen is
            print(True, Content.index)
            temp = values.copy()
            temp.pop("-name-", None)
            # index = 1
            for val in temp:
                if values[f"-Antwoord{index}-"]:
                    f.upload("user_answers", Content.index, 0)
                    break
                else:
                    index += 1
                if values[f"-Antwoord{index}-"]:
                    f.upload("user_answers", Content.index, 1)
                    break
                else:
                    index += 1
                if values[f"-Antwoord{index}-"]:
                    f.upload("user_answers", Content.index, 2)
                    break
                else:
                    index += 1
                if values[f"-Antwoord{index}-"]:
                    f.upload("user_answers", Content.index, 3)
                    break
                else:
                    index += 1

            Content.index += 1
            if Content.index == 1:
                Content.switch_content(window, "-questions_1-", '-questions_2-')
            elif Content.index == 2:
                Content.switch_content(window, "-questions_2-", '-questions_3-')
            elif Content.index == 3:
                Content.switch_content(window, "-questions_3-", '-questions_4-')
            elif Content.index == 4:
                Content.switch_content(window, "-questions_4-", '-questions_5-')
            elif Content.index == 5:
                Content.switch_content(window, "-questions_5-", '-questions_6-')
            elif Content.index == 6:
                Content.switch_content(window, "-questions_6-", '-questions_7-')
            elif Content.index == 7:
                Content.switch_content(window, "-questions_7-", '-questions_8-')
            elif Content.index == 8:
                Content.switch_content(window, "-questions_8-", '-questions_9-')
            elif Content.index == 9:
                Content.switch_content(window, "-questions_9-", '-questions_10-')
            elif Content.index == 10:
                Content.switch_content(window, "-questions_10-", '-questions_11-')
            elif Content.index == 11:
                Content.switch_content(window, "-questions_11-", '-questions_12-')
            elif Content.index == 12:
                Content.switch_content(window, "-questions_12-", '-questions_13-')
            elif Content.index == 13:
                Content.switch_content(window, "-questions_13-", '-questions_14-')
            elif Content.index == 14:
                Content.switch_content(window, "-questions_14-", '-questions_15-')
            elif Content.index == 15:
                a.Algorithm.init(data=[
                   f.get_data("answers"),
                   f.get_data("field_of_study"),
                   f.get_data("question"),
                   f.get_data("points"),
                   f.get_data("user_answers"),
                ])

                result = a.Algorithm.cs()
                
                Content.switch_content(window, "-questions_15-", '-end-')
        elif event == "-close-":
            window.close()
        else:
            window.close()
        values.clear()


if __name__ == '__main__':
    main()
