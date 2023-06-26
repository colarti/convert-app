import customtkinter as ctk
from settings import *

class Layout(ctk.CTkFrame):
    def __init__(self, parent, valueA, entryA, valueB, entryB):
        super().__init__(parent, fg_color='transparent')

        TextOptionPanel(self, valueA, entryA, 'normal')
        TextOptionPanel(self, valueB, entryB, 'disabled')

        self.place(relx=.5, rely=.5, anchor='center', relwidth=1)

class TextOptionPanel(ctk.CTkFrame):
    def __init__(self, parent, options, entry, state):
        super().__init__(parent, fg_color='grey')

        self.rowconfigure(0, weight=1)
        self.columnconfigure((0,1,2), weight=1, uniform='a')

        self.optionMenu = options
        self.entry = entry
        
        ctk.CTkEntry(self, textvariable=self.entry, justify='right', state=state, height=70, font=('Helvetica', 60)).grid(row=0, column=0, columnspan=2, sticky='ew', padx=5)
        ctk.CTkOptionMenu(self, variable=self.optionMenu, values=list_distance).grid(row=0, column=2, sticky='ew')


        self.pack(pady=5, padx=5, ipady=10, ipadx=10)
