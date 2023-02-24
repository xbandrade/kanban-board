import json
import random
import tkinter as tk
from turtle import title

import customtkinter as ctk
from tktooltip import ToolTip

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
        add_column_button = self.create_button(
            text='Add Column', row=1, col=0, command=self.add_new_column
        )
        ToolTip(
            add_column_button, 'Insert a new column to the board',
            delay=0, fg="#ffffff", bg="#1c1c1c", 
            padx=10, pady=10, font=('Verdana', 10)
        )
        add_card_button = self.create_button(
            text='Add Card', row=2, col=0, command=self.add_new_card
        )
        ToolTip(
            add_card_button, 'Insert a new card to the first column',
            delay=0, fg="#ffffff", bg="#1c1c1c",
            padx=10, pady=10, font=('Verdana', 10)
        )
        save_board_button = self.create_button(
            text='Save Board', row=3, col=0, command=self.save_board
        )
        ToolTip(
            save_board_button, 'Save the current board',
            delay=0, fg="#ffffff", bg="#1c1c1c",
            padx=10, pady=10, font=('Verdana', 10)
        )
        load_board_button = self.create_button(
            text='Load Board', row=4, col=0, command=self.load_board
        )
        ToolTip(
            load_board_button, 'Load a saved board',
            delay=0, fg="#ffffff", bg="#1c1c1c",
            padx=10, pady=10, font=('Verdana', 10)
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

    def create_new_column(self, row, col, title, index, color=None):
            border_color = color or '#' + ''.join(
                random.choices('0123456789ABCDEF', k=6)
            )
            new_column = ColumnFrame(
                self.frame, width=260, border_color=border_color,
                fg_color='#626567',
                corner_radius=10, border_width=3,
                name=title, id=index,
                scrollbar_button_color=border_color,
            )
            new_column.grid(
                row=row, column=col, padx=(20, 0),
                pady=(5, 40), sticky='news',
            )            
            label_frame = ctk.CTkFrame(
                master=self.frame,
                width=260,
                border_width=1,
                border_color=new_column.column_color,
                bg_color=new_column.column_color,
                fg_color='#626567',
            )
            label_frame.grid(row=0, column=index + 1, pady=0, padx=(20, 0))
            new_column.label = ctk.CTkLabel(
                master=label_frame,
                text=title,
                text_color='#c9c9c9',
                font=('Verdana', 12),
            )
            new_column.label.grid(row=0, column=0, padx=25)
            new_column.label.bind(
                '<Button-1>', command=new_column.edit_column_name
            )
            if index > 0:
                self.frame.columns[-1].next = new_column
            return new_column

    def create_default_columns(self, default_cols):
        for i, col_title in enumerate(default_cols):
            self.frame.columns.append(
                self.create_new_column(
                    row=1, col=i + 1, title=col_title, index=i
                )
            )
        self.add_new_card(0, 'Write something here')

    def change_dark_mode(self):
        ctk.set_appearance_mode(self.check_var.get())
    
    def add_new_card(self, column=0, text='New Card...'):
        column_obj = self.frame.columns[min(column, len(self.frame.columns) - 1)]
        column_obj.add_card(text)

    def add_new_column(self, column_name='', index=-1, color=None):
        if not column_name:
            dialog = ctk.CTkInputDialog(
                text='Enter a name for the new column', title='New Column'
            )
        new_text = column_name or dialog.get_input()
        if new_text:
            index = len(self.frame.columns) if index < 0 else index
            self.frame.columns.append(
                self.create_new_column(
                    row=1, col=index + 1, title=column_name, index=index,
                    color=color,
                )
            )
            self.frame.columns[-1].label.configure(text=new_text)
        
    
    def edit_card(self, card, button):
        card.flip_entry_state()
        text = ['✎', '✓'][(button._text == '✎')]
        button.configure(text=text)


    def save_board(self):    
        with open('json/data.json', 'w') as f:
            f.write(
                json.dumps(
                    {col.id: col.asdict() for col in self.frame.columns},
                    indent=4
                )
            )

    def load_board(self):
        self.clear_frame()
        with open('json/data.json', 'r') as f:
            columns = json.loads(f.read())
            for col in columns:
                self.deserialize_obj(columns[col])
        for i in range(1, len(self.frame.columns)):
            self.frame.columns[i - 1].next = self.frame.columns[i]
        

    def clear_frame(self):
        for col in self.frame.columns:
            for card in col.cards:
                if card:
                    card.remove_card()
            col.cards = []
        self.frame.columns = []
        for widget in self.frame.winfo_children():
            for child in widget.winfo_children():
                child.destroy()
            widget.destroy()

    def deserialize_obj(self, obj):
        self.add_new_column(
            column_name=obj.get('name', ''),
            index=obj.get('id', -1),
            color=obj.get('column_color', ''),
        )
        new_col = self.frame.columns[-1]
        cards = obj.get('cards', [])
        for card in cards:
            new_col.add_card(
                text=cards[card].get('text', '').strip(),
            )


