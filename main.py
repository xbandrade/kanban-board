import random

import customtkinter as ctk

from app import App

ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('dark-blue')

random.seed(323)


def add_test_cards(app):
    app.add_new_card(0, 'Something I have to do tomorrow')
    app.add_new_card(0, 'Something else I have to do this week')
    app.add_new_card(1, 'This is what I am currently working on')
    app.add_new_card(1, 'I am also working on this')
    app.add_new_card(2, 'This is ready for testing')
    app.add_new_card(3, 'This is already done!')
  

if __name__ == '__main__':
    app = App(1200, 600)
    add_test_cards(app)
    app.mainloop()
