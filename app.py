import random
import tkinter as tk

import customtkinter as ctk

from custom_frames import MyFrame, MyTabView


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
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.sidebar_frame, self.logo_label = self.create_sidebar_frame()
        self.add_column_button = self.create_sidebar_button(
            text='Add Column', row=1, col=0
        )
        self.add_card_button = self.create_sidebar_button(
            text='Add Card', row=2, col=0
        )
        self.save_current_board = self.create_sidebar_button(
            text='Save Board', row=3, col=0
        )
        self.save_current_board = self.create_sidebar_button(
            text='Load Board', row=4, col=0
        )
        self.create_new_board = self.create_sidebar_button(
            text='Create New Board', row=5, col=0
        )
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
        self.tabviews = []
        self.create_default_tabviews(
            ['To Do', 'Currently Doing', 'Testing', 'Done']
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

    def create_sidebar_button(self, text, row, col):
        sidebar_button = ctk.CTkButton(
            self.sidebar_frame, 
            command=self.sidebar_button_event, 
            text=text,
        )
        sidebar_button.grid(row=row, column=col, padx=20, pady=5, sticky='n')
        return sidebar_button

    def create_tabview(self, row, col, title):
            border_color = '#' + ''.join(
                random.choices('0123456789ABCDEF', k=6)
            )
            tabview = MyTabView(
                self.frame, width=280, border_color=border_color,
                fg_color='#626567',
                corner_radius=10, border_width=3,
                segmented_button_selected_hover_color=border_color
            )
            tabview.grid(
                row=row, column=col, padx=(20, 0),
                pady=(20, 40), sticky='news',
            )
            tabview.add(title)
            tabview.tab(title).grid_columnconfigure(0, weight=1)
            return tabview

    def create_default_tabviews(self, default_cols):
        for i, col_title in enumerate(default_cols):
            self.tabviews.append(
                self.create_tabview(
                    row=0, col=i + 1, title=col_title
                    )
            )

    def change_dark_mode(self):
        ctk.set_appearance_mode(self.check_var.get())
    
    def add_new_card(self, index, text):
        col_title = self.tabviews[index]._current_name
        textbox = ctk.CTkTextbox(
            self.tabviews[index].tab(col_title),
            wrap='word',
            border_spacing=2,
            width=250,
            height=100,
            border_color=self.tabviews[index]._border_color,
            border_width=2,
            font=('Verdana', 12),
        )
        textbox.insert('0.0', text)
        textbox.configure(state='disabled')
        textbox.grid(
            row=len(self.tabviews[index].textboxes), column=0,
            pady=(0, 20)
        )
        move_card_button = ctk.CTkButton(
            master=self.tabviews[index].tab(col_title), text='→', 
            command=lambda: print('hi'),
            width=5,
            fg_color=self.tabviews[index]._border_color
        )
        move_card_button.grid(
            row=len(self.tabviews[index].textboxes), column=1,
            pady=(0, 20), padx=(3, 0), sticky='n'
        )
        edit_card_button = ctk.CTkButton(
            master=self.tabviews[index].tab(col_title), text='✎', 
            command=lambda: print('hi'),
            width=5,
            fg_color=self.tabviews[index]._border_color
        )
        edit_card_button.grid(
            row=len(self.tabviews[index].textboxes), column=1,
            pady=(0, 20), padx=(3, 0)
        )
        remove_card_button = ctk.CTkButton(
            master=self.tabviews[index].tab(col_title), text='✖', 
            command=lambda: print('hi'),
            width=5,
            fg_color=self.tabviews[index]._border_color
        )
        remove_card_button.grid(
            row=len(self.tabviews[index].textboxes), column=1,
            pady=(0, 20), padx=(3, 0), sticky='s'
        )
        self.tabviews[index].textboxes.append(textbox)

    def add_new_column(self, column_name):
        ...
    
    def remove_card(self, card):
        ...

    def edit_card(self, card):
        ...

    def sidebar_button_event(self):
        print('click!')
        ...
