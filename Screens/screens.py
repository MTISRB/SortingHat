import tkinter as tk
import tkinter.constants as tk_cons
import PySimpleGUI as sg


class LoadQuestion:

    def questionlayout(self, vraag, ant1, ant2, ant3, ant4):
        col1 = [[sg.Image('resources/img/sorting_hat.png', size=(300, 300))]]
        col2 = [[sg.Text(vraag)],
                [sg.Radio(ant1, "RADIO1", key="-Antwoord1-")],
                [sg.Radio(ant2, "RADIO1", key="-Antwoord2-")],
                [sg.Radio(ant3, "RADIO1", key="-Antwoord3-")],
                [sg.Radio(ant4, "RADIO1", key="-Antwoord4-")],
                [sg.Button('Terug'), sg.Button('Verder', key="-EnterQuestion-")]]

        return col1, col2

