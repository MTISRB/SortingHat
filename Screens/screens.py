import PySimpleGUI as sg


class LoadQuestion:
    def __init__(self):
        pass

    @staticmethod
    def question_layout(question, ant1, ant2, ant3, ant4):
        font = ("Helvetica", 25)
        font_s = ("Helvetica", 15)

        col1 = [[sg.Image('resources/img/sorting_hat-3.png')]]
        col2 = [[sg.Text(question, key='-text-', font=font)],
                [sg.Radio(ant1, "RADIO1", key="-Antwoord1-", font=font_s)],
                [sg.Radio(ant2, "RADIO1", key="-Antwoord2-", font=font_s)],
                [sg.Radio(ant3, "RADIO1", key="-Antwoord3-", font=font_s)],
                [sg.Radio(ant4, "RADIO1", key="-Antwoord4-", font=font_s)],
                [sg.Button('< Terug', font=font_s, size=7),
                 sg.Button('Verder >', font=font_s, size=7, key="-EnterQuestion-")]]

        return col1, col2


class LoadResults:
    def __init__(self):
        pass

    @staticmethod
    def result_layout(result):
        font = ("Helvetica", 25)
        font_s = ("Helvetica", 15)

        col1 = [[sg.Image("resources/img/sorting_hat-2.png")]]
        col2 = [[sg.Text('Je resultaat is binnen', font=font)],
                [sg.Text('Jij past bij:', font=font_s), sg.Text(result, font=font_s)],
                [sg.Button('Sluiten', key="-close-")]]

        return col1, col2


class GenerateContent:
    def __init__(self):
        pass

    @staticmethod
    def draw_screens(q_col1, q_col2, r_col1, r_col2):
        screens = [[
            sg.Frame('', [
                [sg.Image('resources/img/sorting_hat.png')],
                [sg.Text('Welkom bij de Sorting Experience! Voer hieronder je naam in!')],
                [sg.Input(key="-name-")],
                [sg.Button("Begin de Sorting Experience!", key="-beginExperience-")]],
                     visible=True, border_width=0, element_justification='c', key="-welcome-"),

            sg.Frame('', [
                [sg.VPush()],
                [sg.Push(), sg.Column(q_col1), sg.Column(q_col2), sg.Push()],
                [sg.VPush()]],
                     visible=False, border_width=0, element_justification='c', key="-questions-"),

            sg.Frame('', [
                [sg.VPush()],
                [sg.Push(), sg.Column(r_col1), sg.Column(r_col2), sg.Push()],
                [sg.VPush()]],
                     visible=False, border_width=0, element_justification='c', key="-end-")
        ]
        ]
        return screens

    @staticmethod
    def switchcontent(activewindow, currentc, nextc):
        """
        # Changes the showing content
        :param activewindow: The window in which the content is placed
        :param currentc: The current key of the content-frame that has to disappear
        :param nextc: The key of the content-frame you want to display next
        :return:
        """
        activewindow[currentc].update(visible=False)
        activewindow[nextc].update(visible=True)
        activewindow.refresh()