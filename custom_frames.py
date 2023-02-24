import customtkinter as ctk

from card_field import CardField


class CustomConfirmationBox(ctk.CTkToplevel):
    def __init__(self, title, message, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('300x130')
        self.resizable(False, False)
        self.message = message
        self.title(title)
        self.protocol('WM_DELETE_WINDOW', self._on_closing)
        self.after(100, self._create_widgets)
        self.lift()
        self.attributes('-topmost', True)
        self._choice = False
        self.bind('<Escape>', self._on_closing)
        self.grab_set()

    def _create_widgets(self):
        self.grid_columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight=1)
        self.label = ctk.CTkLabel(self, text=self.message)
        self.label.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky='ew')
        yes_button = ctk.CTkButton(
            self, 
            text='Yes',
            command=self._yes_event,
        )
        no_button = ctk.CTkButton(
            self, 
            text='No',
            command=self._no_event,
        )
        yes_button.grid(row=1, column=0, padx=20, pady=20, sticky='ew')
        no_button.grid(row=1, column=1, padx=20, pady=20, sticky='ew')

    def _on_closing(self, event=None):
        self.grab_release()
        self.destroy()

    def _yes_event(self, event=None):
        self._choice = True
        self.grab_release()
        self.destroy()

    def _no_event(self, event=None):
        self._choice = False
        self.grab_release()
        self.destroy()

    def get_input(self):
        self.master.wait_window(self)
        return self._choice

class MainFrame(ctk.CTkScrollableFrame):
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
        row = len(self.cards)
        new_card.insert('0.0', text)
        new_card.configure(state='disabled')
        new_card.grid(
            row=row, column=0,
            pady=(0, 20),
        )
        new_card.id = row
        self.cards.append(new_card)

    def edit_column_name(self, button=None):
        curr_text = self.label.cget('text')
        dialog = ctk.CTkInputDialog(
            text='Enter a new name for the column', title='Edit Column'
        )
        text = dialog.get_input()
        self.label.configure(text.strip() if text else curr_text)
        