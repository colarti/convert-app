import customtkinter as ctk
import darkdetect
from layout import Layout
from settings import *

class App(ctk.CTk):
    def __init__(self, dark, width=WIDTH, height=HEIGHT):
        super().__init__()
        self.title('Converter App')
        self.gui_geometry(width, height)

        if dark:
            ctk.set_appearance_mode('dark')


        #widgets
        self.layout = Layout(self)


        self.bind('<Shift-Escape>', quit)
        self.mainloop()
    
    def gui_geometry(self, width, height):
        pWidth = width
        pHeight = height
        sWidth = self.winfo_screenwidth()
        sHeight = self.winfo_screenheight()
        mWidth = sWidth//2 - pWidth//2
        mHeight = sHeight//2 - pHeight//2

        self.geometry(f'{pWidth}x{pHeight}+{mWidth}+{mHeight}')


if __name__ == '__main__':
    dark = not darkdetect.isDark()
    
    app = App(dark)