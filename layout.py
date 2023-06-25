import customtkinter as ctk


class Layout(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color='transparent')

        TextOptionPanel(self)
        TextOptionPanel(self)

        self.place(relx=.5, rely=.5, anchor='center')


class TextOptionPanel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color='grey')

        self.rowconfigure(0, weight=1)
        self.columnconfigure((0,1,2), weight=1, uniform='a')
        
        ctk.CTkEntry(self, height=70, font=('Helvetica', 60)).grid(row=0, column=0, columnspan=2, sticky='ew', padx=5)
        ctk.CTkOptionMenu(self, values=['Test']).grid(row=0, column=2, sticky='ew')

        self.pack(pady=5, padx=5, ipady=10, ipadx=10)