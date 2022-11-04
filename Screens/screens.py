import PySimpleGUI as sg


class LoadQuestion:
    counter: int = 0

    def __init__(self):
        pass

    @staticmethod
    def question_layout(id, question, ant1, ant2, ant3, ant4):
        LoadQuestion.counter += 1
        font = ("Helvetica", 25)
        font_s = ("Helvetica", 15)

        col1 = [[sg.Image('resources/img/sorting_hat-3.png')]]
        col2 = [[sg.Text(question, key='-text-', font=font)],
                [sg.Radio(ant1, "RADIO1", key=f"-Antwoord{id}-", font=font_s)],
                [sg.Radio(ant2, "RADIO1", key=f"-Antwoord{id+1}-", font=font_s)],
                [sg.Radio(ant3, "RADIO1", key=f"-Antwoord{id+2}-", font=font_s)],
                [sg.Radio(ant4, "RADIO1", key=f"-Antwoord{id+3}-", font=font_s)],
                [sg.Button('Verder >', font=font_s, size=7, key="-Next-")]]

        return col1, col2


class LoadResults:
    def __init__(self):
        pass

    @staticmethod
    def result_layout(result):
        font = ("Helvetica", 25)
        font_s = ("Helvetica", 15)

        col1 = [[sg.Image("resources/img/sorting_hat-2.png")]]
        col2 = [[sg.Text('Hmmmm... Ja... Als je dat wilt..', font=font)],
                [sg.Text('Jij past bij:', font=font_s, key="-SPECRES-"), sg.Text(result, font=font_s)],
                [sg.Button('Sluiten', key="-close-")]]

        return col1, col2


class Content:
    index: int = 0

    def __init__(self):
        pass

    @staticmethod
    def draw_screens(q_col1, q_col2, r_col1, r_col2):
        screens = [[
            sg.Frame('', [
                [sg.Image('resources/img/sorting_hat-2.png')],
                [sg.Text('Welkom bij de Sorting Experience! Voer hieronder je naam in!')],
                [sg.Input(key="-name-")],
                [sg.Button("Begin de Sorting Experience!", key="-beginExperience-")]],
                     visible=True, border_width=0, element_justification='c', key="-welcome-"),

            sg.Frame('', [
                [sg.VPush()],
                [sg.Push(), sg.Column(q_col1[0]), sg.Column(q_col2[0]), sg.Push()],
                [sg.VPush()]],
                     visible=False, border_width=0, element_justification='c', key="-questions_1-"),

            sg.Frame('', [
                [sg.VPush()],
                [sg.Push(), sg.Column(q_col1[1]), sg.Column(q_col2[1]), sg.Push()],
                [sg.VPush()]],
                     visible=False, border_width=0, element_justification='c', key="-questions_2-"),

            sg.Frame('', [
                [sg.VPush()],
                [sg.Push(), sg.Column(q_col1[2]), sg.Column(q_col2[2]), sg.Push()],
                [sg.VPush()]],
                     visible=False, border_width=0, element_justification='c', key="-questions_3-"),

            sg.Frame('', [
                [sg.VPush()],
                [sg.Push(), sg.Column(q_col1[3]), sg.Column(q_col2[3]), sg.Push()],
                [sg.VPush()]],
                     visible=False, border_width=0, element_justification='c', key="-questions_4-"),

            sg.Frame('', [
                [sg.VPush()],
                [sg.Push(), sg.Column(q_col1[4]), sg.Column(q_col2[4]), sg.Push()],
                [sg.VPush()]],
                     visible=False, border_width=0, element_justification='c', key="-questions_5-"),

            sg.Frame('', [
                [sg.VPush()],
                [sg.Push(), sg.Column(q_col1[5]), sg.Column(q_col2[5]), sg.Push()],
                [sg.VPush()]],
                     visible=False, border_width=0, element_justification='c', key="-questions_6-"),

            sg.Frame('', [
                [sg.VPush()],
                [sg.Push(), sg.Column(q_col1[6]), sg.Column(q_col2[6]), sg.Push()],
                [sg.VPush()]],
                     visible=False, border_width=0, element_justification='c', key="-questions_7-"),

            sg.Frame('', [
                [sg.VPush()],
                [sg.Push(), sg.Column(q_col1[7]), sg.Column(q_col2[7]), sg.Push()],
                [sg.VPush()]],
                     visible=False, border_width=0, element_justification='c', key="-questions_8-"),

            sg.Frame('', [
                [sg.VPush()],
                [sg.Push(), sg.Column(q_col1[8]), sg.Column(q_col2[8]), sg.Push()],
                [sg.VPush()]],
                     visible=False, border_width=0, element_justification='c', key="-questions_9-"),

            sg.Frame('', [
                [sg.VPush()],
                [sg.Push(), sg.Column(q_col1[9]), sg.Column(q_col2[9]), sg.Push()],
                [sg.VPush()]],
                     visible=False, border_width=0, element_justification='c', key="-questions_10-"),

            sg.Frame('', [
                [sg.VPush()],
                [sg.Push(), sg.Column(q_col1[10]), sg.Column(q_col2[10]), sg.Push()],
                [sg.VPush()]],
                     visible=False, border_width=0, element_justification='c', key="-questions_11-"),

            sg.Frame('', [
                [sg.VPush()],
                [sg.Push(), sg.Column(q_col1[11]), sg.Column(q_col2[11]), sg.Push()],
                [sg.VPush()]],
                     visible=False, border_width=0, element_justification='c', key="-questions_12-"),

            sg.Frame('', [
                [sg.VPush()],
                [sg.Push(), sg.Column(q_col1[12]), sg.Column(q_col2[12]), sg.Push()],
                [sg.VPush()]],
                     visible=False, border_width=0, element_justification='c', key="-questions_13-"),

            sg.Frame('', [
                [sg.VPush()],
                [sg.Push(), sg.Column(q_col1[13]), sg.Column(q_col2[13]), sg.Push()],
                [sg.VPush()]],
                     visible=False, border_width=0, element_justification='c', key="-questions_14-"),

            sg.Frame('', [
                [sg.VPush()],
                [sg.Push(), sg.Column(q_col1[14]), sg.Column(q_col2[14]), sg.Push()],
                [sg.VPush()]],
                     visible=False, border_width=0, element_justification='c', key="-questions_15-"),

            sg.Frame('', [
                [sg.VPush()],
                [sg.Push(), sg.Column(r_col1), sg.Column(r_col2), sg.Push()],
                [sg.VPush()]],
                     visible=False, border_width=0, element_justification='c', key="-end-")
        ]]

        return screens

    @staticmethod
    def switch_content(activewindow, currentc, nextc):
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