import customtkinter as ctk
from _tkinter import TclError


class CardField(ctk.CTkTextbox):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.id = -1
        self.entry_states = ['normal', 'disabled']
        self.entry_disabled = True
        self.move_card_button = self.create_move_card_button()
        self.edit_card_button = self.create_edit_card_button()
        self.remove_card_button = self.create_remove_card_button()
        self.grid_buttons(row=len(self.master.cards))

    def asdict(self):
        return {
            'id': self.id,
            'text': self.get('0.0', 'end'),
        }


    def grid_buttons(self, row, col = 1):
        self.move_card_button.grid(
            row=row, column=col,
            pady=(0, 20), padx=(3, 0), sticky='n'
        )
        self.edit_card_button.grid(
            row=row, column=col,
            pady=(0, 20), padx=(3, 0)
        )
        self.remove_card_button.grid(
            row=row, column=col,
            pady=(0, 20), padx=(3, 0), sticky='s'
        )

    def create_move_card_button(self):
        return ctk.CTkButton(
            master=self.master, text='→', 
            command=self.move_card,
            width=5,
            fg_color=self.master.column_color,
        )
        
    def create_edit_card_button(self):
        return ctk.CTkButton(
            master=self.master, text='✎', 
            command=self.edit_card,
            width=5,
            fg_color=self.master.column_color,
        )
    
    def create_remove_card_button(self):
        return ctk.CTkButton(
            master=self.master, text='✖', 
            command=self.remove_card,
            width=5,
            fg_color=self.master.column_color,
        )

    def move_card(self):
        if self.master.next:
            self.master.next.add_card(self.get('0.0', 'end'))
            self.remove_card()
        else:
            print('No columns to move this card')

    def _fix_cards_ids(self):
        for card in self.master.cards[self.id:]:
            card.id -= 1

    def edit_card(self):
        self.flip_entry_state()
        text = ['✎', '✓'][(self.edit_card_button._text == '✎')]
        self.edit_card_button.configure(text=text)

    def remove_card(self):
        self.master.cards[self.id] = None
        self.move_card_button.destroy()
        self.edit_card_button.destroy()
        self.remove_card_button.destroy()
        self.destroy()

    def flip_entry_state(self):
        self.entry_disabled = not self.entry_disabled
        self.configure(state=self.entry_states[self.entry_disabled])
