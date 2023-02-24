import customtkinter as ctk
from tktooltip import ToolTip


class PopupCard(ctk.CTkToplevel):
    def __init__(self, card, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fgcolor = kwargs.get('fg_color')
        self.overrideredirect(True)
        self.geometry(f'240x130')
        self.card = card
        self.bind('<B1-Motion>', self._mouse_motion)  # Hold the left mouse button and drag events
        self.bind('<Button-1>', self._mouse_press)  # The left mouse button press event, long calculate by only once
        self.x = 0
        self.y = 0
        self.create_widgets()
        

    def create_widgets(self):
        self.close_button = ctk.CTkButton(
            self,
            command=self._close_popup,
            text='✖',
            width=25, height=5,
            bg_color=self.fgcolor,
            border_color='#000000',
            border_width=1,
        )
        self.close_button.grid(row=0, column=1, sticky='ne', pady=(5, 0), padx=(0, 10))
        self.always_on_top_button = ctk.CTkButton(
            self,
            command=self._lock_on_top,
            text='🔓',
            width=25, height=5,
            bg_color=self.fgcolor,
            border_color='#000000',
            border_width=1,
        )
        self.always_on_top_button.grid(row=1, column=1, sticky='ne', pady=(5, 0), padx=(0, 10))
        ToolTip(
            self.always_on_top_button, 'Keep this card always on top',
            delay=0, fg="#ffffff", bg="#1c1c1c",
            padx=10, pady=10, font=('Verdana', 9),
        )
        self.text = ctk.CTkTextbox(
            self,
            wrap='word',
            width=190, height=100, 
            border_width=2,
            border_color=self.fgcolor,
            corner_radius=8,
        )
        self.text.insert('0.0', self.card.get('0.0', 'end'))
        self.text.grid(row=0, column=0, padx=(10, 2), pady=10, sticky='nw', rowspan=10)

    def _close_popup(self, event=None):
        self.card.has_popup = False
        self.destroy()

    def _lock_on_top(self, event=None):
        text = ['🔒', '🔓'][self.always_on_top_button.cget('text') == '🔒']
        if self.always_on_top_button.cget('text') == '🔒':
            text = '🔓'
            self.wm_attributes('-topmost', 0)
        else:
            text = '🔒'
            self.wm_attributes('-topmost', 1)
        self.always_on_top_button.configure(text=text)

    def _mouse_motion(self, event):
        offset_x, offset_y = event.x - self.x, event.y - self.y  
        new_x = self.winfo_x() + offset_x
        new_y = self.winfo_y() + offset_y
        new_geometry = f'+{new_x}+{new_y}'
        self.geometry(new_geometry)

    def _mouse_press(self, event):
        self.x, self.y = event.x, event.y
