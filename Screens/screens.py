import tkinter as tk
import tkinter.constants as tk_cons


class Window:
    master: tk.Tk
    width: int = 0
    height: int = 0

    def __init__(self, master, title):
        self.master = master
        # add title, width, height etc.

    def init_components(self):
        # override this function in child classes
        pass

    def _new(self, _class):
        self.new = tk.Toplevel(self.master)
        _class(self.new)


# All classes inherit from the Window interface, extra methods can be added to these classes
class BeginWindow(Window):
    root: tk.Tk

    def __init__(self, root):
        super().__init__(root, "[Title here!]")
        self.root = root
        # add title, width, height etc.

    def init_components(self):
        super().init_components()
        # add components here


class EndWindow(Window):
    root: tk.Tk

    def __init__(self, root):
        super().__init__(root, "[Title here!]")
        self.root = root
        # add title, width, height etc.

    def init_components(self):
        super().init_components()
        # add components here


class QuestionWindow(Window):
    root: tk.Tk

    def __init__(self, root):
        super().__init__(root, "[Title here!]")
        self.root = root
        # add title, width, height etc.

    def init_components(self):
        super().init_components()
        # add components here

    def correct(self) -> bool:
        pass
