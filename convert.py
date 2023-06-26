import customtkinter as ctk
import darkdetect
from layout import Layout
from settings import *

class App(ctk.CTk):
    def __init__(self, dark, width=500, height=300):
        super().__init__()
        self.title('Converter App')
        self.gui_geometry(width, height)

        if dark:
            ctk.set_appearance_mode('dark')

        #variables
        self.valueA = ctk.StringVar(value=list_distance[0])
        self.entryA = ctk.StringVar(value='0')
        self.valueB = ctk.StringVar(value=list_distance[0])
        self.entryB = ctk.StringVar(value='0')

        self.entryA.trace('w', self.updateVariables)
        self.entryB.trace('w', self.updateVariables) 
        self.valueA.trace('w', self.updateVariables)
        self.valueB.trace('w', self.updateVariables)      

        #widgets
        self.layout = Layout(self, self.valueA, self.entryA, self.valueB, self.entryB)


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

    def updateVariables(self, *args):
        match args[0]:
            case 'PY_VAR0':
                self.calculate(self.valueA.get(), self.entryA.get(), self.valueB.get())
            case 'PY_VAR1':
                self.calculate(self.valueA.get(), self.entryA.get(), self.valueB.get())
            case 'PY_VAR2':
                self.calculate(self.valueA.get(), self.entryA.get(), self.valueB.get())

    def calculate(self, pLength, pValue, sLength):
        conversionValue = CONVERT_LIST[sLength][pLength]
        result = 0

        try:
            primaryValue = float(pValue)
            result = primaryValue / conversionValue

        except:
            print(f'INVALID PVALUE: {pValue}')
            self.entryB.set('Invalid')
            return

        test = result % 1 > 0
        if test > 0:
            result = round(result, 2)
        else:
            result = int(result)

        print(f'After result: {result}')

        self.entryB.set(str(result))

        print(f'pLength: {pLength} /  sLength: {sLength}  ->> conversion: {conversionValue}')
        print(f'primaryValue: {primaryValue}   Before result: {result}')


if __name__ == '__main__':
    dark = not darkdetect.isDark()
    
    app = App(dark)