import customtkinter as ctk

from card_field import CardField


class MyFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.columns = []


class ColumnFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, name, id, **kwargs):
        super().__init__(master, **kwargs)
        self.cards = []
        self.name = name
        self.master = master
        self.id = id
        self.next = None
        self.column_color = kwargs.get('border_color', '#000000')

    def add_card(self, text):
        new_card = CardField(
            self,
            wrap='word',
            border_spacing=2,
            width=225,
            height=100,
            border_width=2,
            font=('Verdana', 12),
            border_color=self.column_color,
        )
        row = len(self.cards)
        new_card.insert('0.0', text)
        new_card.configure(state='disabled')
        new_card.grid(
            row=row, column=0,
            pady=(0, 20),
        )
        new_card.move_card_button.grid(
            row=row, column=1,
            pady=(0, 20), padx=(3, 0), sticky='n'
        )
        new_card.edit_card_button.grid(
            row=row, column=1,
            pady=(0, 20), padx=(3, 0)
        )
        new_card.remove_card_button.grid(
            row=row, column=1,
            pady=(0, 20), padx=(3, 0), sticky='s'
        )
        new_card.id = row
        self.cards.append(new_card)

