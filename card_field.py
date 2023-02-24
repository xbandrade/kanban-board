import customtkinter as ctk

from popup_card import PopupCard


class CardField(ctk.CTkTextbox):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.id = -1
        self.entry_states = ['normal', 'disabled']
        self.entry_disabled = False
        self.has_popup = False
        self.move_card_button = self.create_move_card_button()
        self.popup_button = self.create_popup_button()
        self.remove_card_button = self.create_remove_card_button()
        self.grid_buttons(row=len(self.master.cards))
        self.configure(cursor='pencil')

    def asdict(self):
        return {
            'id': self.id,
            'text': self.get('0.0', 'end').strip(),
        }

    def grid_buttons(self, row, col = 1):
        self.move_card_button.grid(
            row=row, column=col,
            pady=(0, 20), padx=(3, 0), sticky='n'
        )
        self.popup_button.grid(
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
        )
        
    def create_popup_button(self):
        return ctk.CTkButton(
            master=self.master, text='↑', 
            command=self.popup_card,
            width=28,
        )
    
    def create_remove_card_button(self):
        return ctk.CTkButton(
            master=self.master, text='✖', 
            command=self.remove_card,
            width=5,
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

    def popup_card(self):
        if not self.has_popup:
            self.has_popup = True
            PopupCard(
                card=self,
                fg_color=self.master.column_color,
                highlightthickness=4, 
                highlightbackground='black',
            )   

    def remove_card(self):
        self.master.cards[self.id] = None
        self.move_card_button.destroy()
        self.popup_button.destroy()
        self.remove_card_button.destroy()
        self.destroy()

    def flip_entry_state(self):
        self.entry_disabled = not self.entry_disabled
        self.configure(state=self.entry_states[self.entry_disabled])
