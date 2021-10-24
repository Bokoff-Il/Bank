from tkinter import Tk
import settings
from widgets import MainMenu

root = Tk()
root.title(settings.NAME)
root.geometry('800x600')
MainMenu(root)


if __name__ == '__main__':
    root.mainloop()


