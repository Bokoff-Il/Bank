import tkinter
from tkinter import Menu,Frame, Label, Entry, LabelFrame, Button
from tkinter import messagebox
from tkinter import StringVar
import settings


class MainMenu(Menu):
    def __init__(self,root):
        Menu.__init__(self,root)
        person_menu=Menu(self,tearoff=0)
        person_menu.add_command(label='Все клиенты')
        person_menu.add_command(label='Добавить клиента')
        person_menu.add_command(label='Удалить клиента')

        account_menu=Menu(self, tearoff=0)
        account_menu.add_command(label='Все счета')
        account_menu.add_command(label='Добавить счет')
        account_menu.add_command(label='Удалить счет')
        account_menu.add_command(label='Блокировать счет')

        card_menu = Menu(self, tearoff=0)
        card_menu.add_command(label='Все карты')
        card_menu.add_command(label='Выпустить карту')
        account_menu.add_command(label='Блокировать карту')

        transaction_menu = Menu(self, tearoff=0)
        transaction_menu.add_command(label='Пополнить счет')
        transaction_menu.add_command(label='Снять деньги со счета')
        transaction_menu.add_command(label='Перевод между счетами')

        self.add_cascade(label='Клиенты',menu=person_menu)
        self.add_cascade(label='Счета', menu=account_menu)
        self.add_cascade(label='Карты', menu=card_menu)
        self.add_cascade(label='Операции', menu=transaction_menu)

        root.config(menu=self)


class BaseFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.background_color=settings.BACKGROUND_COLOR
        self.configure(bg=self.background_color)
    def pack_frame(self):
        self.pack(padx=20, pady=20, fill='both',expand="YES")


class HeadLabel(Label):
    def __init__(self, root, text):
        Label.__init__(self,root)
        self.configure(font=settings.HEAD_FONT, text=text, bg=root.background_color)


class InfoLabel(Label):
    def __init__(self, root, text):
        Label.__init__(self,root)
        self.configure(font=settings.TEXT_FONT, text=text, bg=root.background_color)


class InputButton(Button):
   def __init__(self,root, text, command):
       Button.__init__(self,root)
       self['text']=text
       self['font']=settings.TEXT_FONT
       self['command'] = command
       self.pack(pady=5)


class InputFrame(BaseFrame):
    def __init__(self, root, text, var):
        BaseFrame.__init__(self, root)
        self.label=InfoLabel(self, text)
        self.input=Entry(self, font=settings.TEXT_FONT, textvariable=var)

    def pack_frame(self):
        self.label.pack(side='left')
        self.input.pack(side='left',expand='yes',fill='x')
        self.pack(anchor='w', fill='x')
        return self

    def clean(self):
        self.input.delete(0,tkinter.END)


class AboutBankFrame(BaseFrame):
    def __init__(self, root):
        BaseFrame.__init__(self,root)
        HeadLabel(self, 'Банк').pack()


class AddPersonFrame(BaseFrame):
    def __init__(self, root):
        BaseFrame.__init__(self, root)
        HeadLabel(self, 'Добавить пользователя').pack()

        self.name=StringVar()
        self.surname = StringVar()
        self.date_birthday = StringVar()
        self.email = StringVar()
        self.phone = StringVar()

        self.fr=LabelFrame(self)

        self.list_frame=[
            InputFrame(self.fr,'Имя: ',self.name),
            InputFrame(self.fr, 'Фамилия: ', self.surname),
            InputFrame(self.fr, 'Дата рождения: ', self.date_birthday),
            InputFrame(self.fr, 'Email: ', self.email),
            InputFrame(self.fr, 'Телефон: ', self.phone)
        ]

        for frame in self.list_frame:
            frame.pack_frame()

        self.fr.pack(anchor='w',fill='x')
        InputButton(self, 'Добавить', command=self.get_input_data)

    def get_input_data(self):
        name=self.name.get()
        surname=self.surname.get()
        date_birthday=self.date_birthday.get()
        email=self.email.get()
        phone=self.phone.get()

        for frame in self.list_frame:
            frame.clean()
        messagebox.showinfo('Успех', 'Пользователь успешно добавлен!')
        print(name,surname,date_birthday,email,phone)







