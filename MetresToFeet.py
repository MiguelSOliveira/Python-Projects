'''
Created on Aug 20, 2014

@author: miguel
'''

from Tkinter import *
import ttk
if __name__ == '__main__':
    
    def whenClicked(*args):
        value = float(metres.get())
        feetAnswerLabel.set(value*3.2808)
        return feetAnswerLabel
    
    
    app = Tk()
    app.title("Metres to Feet")
    mainframe = ttk.Frame(app, padding=(3,3,12,12))
    mainframe.grid(column=0,row=0, sticky=(N,E,S,W))
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)
    
    metres = StringVar()
    metresTextBox = ttk.Entry(mainframe, textvariable=metres, width=7)
    metresTextBox.grid(row=0, column=1, sticky=(W,E))

    feetAnswerLabel = StringVar()
    feetAnswer = ttk.Label(mainframe, textvariable=feetAnswerLabel).grid(row=1, column=1, sticky=(E,W))
    
    feetLabelBox = ttk.Label(mainframe, text='feet').grid(row=1, column=2, sticky=(W))
    metresLabelBox = ttk.Label(mainframe, text='metres').grid(row=0, column=2, sticky=(W))
    isEqual = ttk.Label(mainframe, text='is equal to ').grid(row=1, column=0, sticky=(E))
    
    calculateButton = ttk.Button(mainframe, text='Calculate', command=whenClicked).grid(row=2, column=2, sticky=(W))
    app.bind('<Return>', whenClicked)
    metresTextBox.focus()
    
    app.mainloop()