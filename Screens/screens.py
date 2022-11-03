import tkinter as tk
import tkinter.constants as tk_cons
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
