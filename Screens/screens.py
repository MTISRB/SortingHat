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


class BeginWindow(Window):
    root: tk.Tk

    def __init__(self, root):
        super().__init__(root, "[Title here!]")
        self.root = root
        # add title, width, height etc.

    def init_components(self):
        super().init_components()
        # override this function in child classes


class EndWindow(Window):
    root: tk.Tk

    def __init__(self, root):
        super().__init__(root, "[Title here!]")
        self.root = root
        # add title, width, height etc.

    def init_components(self):
        super().init_components()
        # override this function in child classes


class QuestionWindow(Window):
    root: tk.Tk

    def __init__(self, root):
        super().__init__(root, "[Title here!]")
        self.root = root
        # add title, width, height etc.

    def init_components(self):
        super().init_components()
        # override this function in child classes

    def correct(self) -> bool:
        pass
