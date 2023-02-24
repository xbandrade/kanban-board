import customtkinter as ctk


class CustomChoiceBox(ctk.CTkToplevel):
    def __init__(self, title, message, editable_option, items, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('300x130')
        self.resizable(False, False)
        self.message = message
        self.editable = editable_option
        self.title(title)
        self.items = items
        self.protocol('WM_DELETE_WINDOW', self._on_closing)
        self.after(100, self._create_widgets)
        self.lift()
        self.attributes('-topmost', True)
        self._choice = False
        self.closed = False
        self.menu_state = len(self.items) >= 1
        self.combobox_var = ctk.StringVar(value='New Board')
        self.optionmenu_var = ctk.StringVar(value='No boards' if not self.menu_state else self.items[0])
        self.bind('<Escape>', self._on_closing)
        self.grab_set()

    def _create_widgets(self):
        self.grid_columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight=1)
        self.label = ctk.CTkLabel(self, text=self.message)
        self.label.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky='ew')
        if self.editable:
            combobox = ctk.CTkComboBox(
                master=self,
                values=self.items,
                command=self._combobox_event,
                variable=self.combobox_var,
            )
        else:
            combobox = ctk.CTkOptionMenu(
                master=self,
                values=self.items,
                command=self._combobox_event,
                state=['disabled', 'normal'][self.menu_state],
                variable=self.optionmenu_var,
            )
        ok_button = ctk.CTkButton(
            self, 
            text=['Load', 'Save'][self.editable],
            command=self._load_event,
            state=['disabled', 'normal'][self.menu_state] if not self.editable else 'normal'
        )
        combobox.grid(row=1, column=0, padx=20, pady=20, sticky='ew')
        ok_button.grid(row=1, column=1, padx=20, pady=20, sticky='ew')

    def _on_closing(self, event=None):
        self.closed = True
        self.grab_release()
        self.destroy()
        
    def _combobox_event(self, event=None):
        self._choice = event

    def _load_event(self, event=None):
        self.grab_release()
        self.destroy()

    def get_input(self):
        self.master.wait_window(self)
        if self.closed:
            return None
        return self.combobox_var.get() if self.editable else self.optionmenu_var.get()


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

