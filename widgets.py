import tkinter
from tkinter import Menu,Frame, Label, Entry, LabelFrame, Button
from tkinter import messagebox
from tkinter import StringVar
import json
import settings


class MainMenu(Menu):
    def __init__(self,root):
        Menu.__init__(self,root)
        person_menu=Menu(self,tearoff=0)
        person_menu.add_command(label='Все клиенты')
        person_menu.add_command(label='Добавить клиента')
        person_menu.add_command(label='Изменить данные клиента')
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

    def pack_button(self):
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
        self.head=HeadLabel(self, 'Добавить клиента')


        self.name=StringVar()
        self.surname = StringVar()
        self.date_birthday = StringVar()
        self.email = StringVar()
        self.phone = StringVar()

        self.fr=LabelFrame(self)

        conf=(
            ('Имя: ',  self.name),
            ('Фамилия: ', self.surname),
            ('Дата рождения(ДД.ММ.ГГГГ): ', self.date_birthday),
            ('Email: ', self.email),
            ('Телефон: ', self.phone),
        )
        self.list_frame = [InputFrame(self.fr, text, var) for (text,var) in conf]

        for frame in self.list_frame:
            frame.pack_frame()

        self.but=InputButton(self, 'Добавить', command=self.get_input_data)


    def pack_frame(self):
        self.head.pack()
        self.fr.pack(anchor='w', fill='x')
        self.but.pack_button()
        self.pack(padx=20, pady=20, fill='both',expand="YES")

    def get_input_data(self):
        data={
            'name':self.name.get(),
            'surname':self.surname.get(),
            'date_birthday':self.date_birthday.get(),
            'email':self.email.get(),
            'phone':self.phone.get()
        }

        for frame in self.list_frame:
            frame.clean()
        messagebox.showinfo('Успех', 'Пользователь успешно добавлен!')
        return json.dumps(data)



class ChangePersonFrame(AddPersonFrame):
    def __init__(self, root):
        AddPersonFrame.__init__(self, root)

        self.fr_old = LabelFrame(self,text='Старые')
        self.fr['text'] = 'Новые'

        self.old_name = StringVar()
        self.old_surname = StringVar()
        self.id = StringVar()

        conf = (
            ('Имя: ', self.old_name),
            ('Фамилия: ', self.old_surname),
            ('Идентификатор: ', self.id),
        )
        self.list_frame = [InputFrame(self.fr_old, text, var) for (text, var) in conf]

        for frame in self.list_frame:
            frame.pack_frame()
        self.but_search = InputButton(self, 'Поиск', command=self.search_client())
        self.head=HeadLabel(self, 'Изменить данные клиента')
        self.but=InputButton(self, 'Изменить', command=self.change_input_data)

    def pack_frame(self):
        self.head.pack()
        self.fr_old.pack(anchor='w', fill='x',pady=10)
        self.but_search.pack_button()
        self.fr.pack(anchor='w', fill='x')
        self.but.pack_button()
        self.pack(padx=20, pady=20, fill='both', expand="YES")

    def search_client(self):
        data = {
            'name': self.old_name.get(),
            'surname': self.old_surname.get(),
            'id': self.id.get(),
        }
        return data

    def change_input_data(self):
        new_data=self.get_input_data()
        print(new_data)


