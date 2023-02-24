import json

import customtkinter as ctk

from card_field import CardField


class MyFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.columns = []

class ColumnFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, name, id, **kwargs):
        super().__init__(master, **kwargs)
        self.name = name
        self.master = master
        self.id = id
        self.next = None
        self.label = None
        self.cards = []
        self.column_color = kwargs.get('border_color', '#000000')
        self._scrollbar.configure(width=7, border_spacing=1, corner_radius=100)

    def asdict(self):
        return {
            'name': self.name,
            'id': self.id,
            'cards': {i: card.asdict() for i, card in enumerate(self.cards) if card},
            'column_color': self.column_color,
        }

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
        row = len(self.cards) # if id < 0 else id
        new_card.insert('0.0', text)
        new_card.configure(state='disabled')
        new_card.grid(
            row=row, column=0,
            pady=(0, 20),
        )
        new_card.id = row
        self.cards.append(new_card)

    def edit_column_name(self, button):
        curr_text = self.label.cget('text')
        dialog = ctk.CTkInputDialog(
            text='Enter a new name for the column', title='Edit Column'
        )
        self.label.configure(text=dialog.get_input().strip() or curr_text)
        