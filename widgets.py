from tkinter import Menu


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

