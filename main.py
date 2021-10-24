from tkinter import Tk
import settings
from widgets import MainMenu,AboutBankFrame,AddPersonFrame, ChangePersonFrame

root = Tk()
root.title(settings.NAME)
root.geometry(settings.GEOMETRY)
MainMenu(root)
ChangePersonFrame(root).pack_frame()

if __name__ == '__main__':
    root.mainloop()


