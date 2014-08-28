'''
Created on Aug 25, 2014

@author: miguel
'''

from Tkinter import Tk, StringVar
import os, platform
import ttk


def main():
    fileWords = open('wordList.txt')
    fileWords = fileWords.read()
    fileWords = fileWords.split()
    def clear():
        os.system('cls' if platform.system() == "Windows" else "clear")
        
    def whenClicked(*args):
        prefix = pattern.get()
        labelText.set("")
        for word in fileWords:
            if word.startswith(prefix):
                labelText.set(str(labelText.get())+'\n'+word)
    
        
        
    root = Tk()
    root.title('AutoComplete')
    ttk.Label(root, text='Enter search pattern').pack()
    pattern = StringVar()
    ttk.Entry(root, textvariable=pattern).pack()
    ttk.Button(root, text='Submit', command=whenClicked).pack()
    labelText = StringVar()
    ttk.Label(root, textvariable=labelText).pack()
    root.bind('<Return>', whenClicked)
    root.mainloop()
    
if __name__ == '__main__':
    main()