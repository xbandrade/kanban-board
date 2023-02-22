import customtkinter as ctk


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
        if self.master.next:  # FIXME: FIX THIS (?)
            text = self.get('0.0', 'end')
            self.remove_card()
            self.master.next.add_card(
                text=text,
            )
        else:
            print('No columns to move this card')

    def edit_card(self):
        self.flip_entry_state()
        text = ['✎', '✓'][(self.edit_card_button._text == '✎')]
        self.edit_card_button.configure(text=text)

    def remove_card(self):
        self.move_card_button.destroy()
        self.edit_card_button.destroy()
        self.remove_card_button.destroy()
        del self.master.cards[self.id]
        for card in self.master.cards[self.id:]:
            card.id -= 1
        self.destroy()

    def flip_entry_state(self):
        self.entry_disabled = not self.entry_disabled
        self.configure(state=self.entry_states[self.entry_disabled])
