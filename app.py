import random
import tkinter as tk

import customtkinter as ctk

from custom_frames import ColumnFrame, MyFrame


class App(ctk.CTk):
    def __init__(self, width, height):
        super().__init__()
        self.title('KBBoard')
        self.geometry(f'{width}x{height}')
        self.resizable(False, False)
        self.grid_rowconfigure(0, weight=1)
        self.frame = MyFrame(
            self, width=width - 260, height=height - 30,
            orientation='horizontal', corner_radius=15,
        )
        self.frame.grid(row=0, column=1, padx=10, pady=10, columnspan=10)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.sidebar_frame, self.logo_label = self.create_sidebar_frame()
        self.create_sidebar_buttons()
        self.check_var = tk.StringVar(value='Dark')
        self.dark_mode_optionmenu = ctk.CTkCheckBox(
            self.sidebar_frame,
            text='Dark Mode', variable=self.check_var,
            onvalue='Dark', offvalue='Light',
            command=self.change_dark_mode
        )
        self.dark_mode_optionmenu.grid(
            row=8, column=0, padx=20, pady=(10, 10), sticky='s'
        )
        self.create_default_columns(
            ['To Do', 'Currently Doing', 'Testing', 'Done']
        )

    def create_sidebar_buttons(self):
        self.create_button(
            text='Add Column', row=1, col=0, state='disabled'
        )
        self.create_button(
            text='Add Card', row=2, col=0, command=self.add_new_card
        )
        self.create_button(
            text='Save Board', row=3, col=0, state='disabled'
        )
        self.create_button(
            text='Load Board', row=4, col=0, state='disabled'
        )
        self.create_button(
            text='Create New Board', row=5, col=0, state='disabled'
        )

    def create_sidebar_frame(self):
        sidebar_frame = ctk.CTkFrame(
            self, width=140, corner_radius=15
        )
        sidebar_frame.grid(
            row=0, column=0, sticky='news', padx=10, pady=10
        )
        sidebar_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 8), weight=1)
        logo_label = ctk.CTkLabel(
            sidebar_frame, text='KBBoard', font=ctk.CTkFont(
                size=20, weight='bold'
            )
        )
        logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        return sidebar_frame, logo_label

    def create_button(self, text, row, col, command=None, state='normal'):
        sidebar_button = ctk.CTkButton(
            self.sidebar_frame, 
            command=command, 
            text=text,
            state=state,
        )
        sidebar_button.grid(row=row, column=col, padx=20, pady=5, sticky='n')
        return sidebar_button

    def create_new_column(self, row, col, title, index):
            border_color = '#' + ''.join(
                random.choices('0123456789ABCDEF', k=6)
            )
            new_column = ColumnFrame(
                self.frame, width=260, border_color=border_color,
                fg_color='#626567',
                corner_radius=10, border_width=3,
                name=title,
                id=index,
            )
            new_column.grid(
                row=row, column=col, padx=(20, 0),
                pady=(5, 40), sticky='news',
            )
            return new_column

    def create_default_columns(self, default_cols):
        for i, col_title in enumerate(default_cols):
            self.frame.columns.append(
                self.create_new_column(
                    row=1, col=i + 1, title=col_title, index=i
                )
            )
            label_frame = ctk.CTkFrame(
                master=self.frame,
                width=260,
                border_width=1,
                border_color=self.frame.columns[-1].column_color,
                bg_color=self.frame.columns[-1].column_color,
                fg_color='#3B3B3B',
            )
            label_frame.grid(row=0, column=i + 1, pady=0, padx=(20, 0))
            label = ctk.CTkLabel(
                master=label_frame,
                text=col_title,
                text_color=self.frame.columns[-1].column_color,
            )
            label.grid(row=0, column=0, padx=25)
            if i > 0:
                self.frame.columns[-2].next = self.frame.columns[-1]

    def change_dark_mode(self):
        ctk.set_appearance_mode(self.check_var.get())
    
    def add_new_card(self, column=None, text='New Card...'):
        column_obj = self.frame.columns[column or 0]
        column_obj.add_card(text)

    def add_new_column(self, column_name):
        ...
    
    def edit_card(self, card, button):
        card.flip_entry_state()
        text = ['✎', '✓'][(button._text == '✎')]
        button.configure(text=text)

    def sidebar_button_event(self):
        print('click!')
        ...
