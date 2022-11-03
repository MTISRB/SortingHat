import tkinter as tk
import tkinter.constants as tk_cons
import PySimpleGUI as sg


class LoadQuestion:

    def questionlayout(self, vraag, ant1, ant2, ant3, ant4):
        kop = ("Helvetica", 25)
        platte_tekst = ("Helvetica", 15)

        col1 = [[sg.Image('resources/img/sorting_hat-3.png')]]
        col2 = [[sg.Text(vraag, key='-text-', font=kop)],
                [sg.Radio(ant1, "RADIO1", key="-Antwoord1-", font=platte_tekst)],
                [sg.Radio(ant2, "RADIO1", key="-Antwoord2-", font=platte_tekst)],
                [sg.Radio(ant3, "RADIO1", key="-Antwoord3-", font=platte_tekst)],
                [sg.Radio(ant4, "RADIO1", key="-Antwoord4-", font=platte_tekst)],
                [sg.Button('< Terug', font=platte_tekst, size=7),
                 sg.Button('Verder >', font=platte_tekst, size=7, key="-EnterQuestion-")]]

        return col1, col2


class LoadResults:

    def resultlayout(self, result):
        kop_text = ("Helvetica", 25)
        platte_text = ("Helvetica", 15)

        col1 = [[sg.Image("resources/img/sorting_hat-2.png")]]
        col2 = [[sg.Text('Je resultaat is binnen', font=kop_text)],
                [sg.Text('Jij past bij:', font=platte_text), sg.Text(result, font=platte_text)],
                [sg.Button('Sluiten', key="-close-")]]

        return col1, col2
