'''
Created on Aug 21, 2014

@author: miguel
'''

from Tkinter import *
import ScrolledText
import tkFileDialog
import tkMessageBox
import ttk

if __name__ == '__main__':
    
    def openFile(*args):
        file = tkFileDialog.askopenfile(mode='r', title='Select File')
        if file != None:
            textField.insert('1.0', file.read())
            file.close()
    
    def new(*args):
        textField.delete('0.0', END)
        
    def save(*args):
        answer = tkFileDialog.asksaveasfilename()
        file = open(answer+'.txt', 'w+')
        file.write(textField.get('0.0', END))
        file.close()
        
    def exit(*args):
        if tkMessageBox.askokcancel('Exit NotePad', 'Are you sure you want to exit ?'):
            root.destroy()
        
    def about():
        tkMessageBox._show('About NotePad', 'Just a run of the mill notepad.')
    
    def createMenu():
        menu = Menu(root)
        root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='New      Ctrl-N', command=new)
        filemenu.add_command(label='Open...      Ctrl-O', command=openFile)
        filemenu.add_command(label='Save      Ctrl-S', command=save)
        filemenu.add_command(label='Highlight Text      Ctrl-L', command=highlight_pattern)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=exit)
        helpmenu = Menu(menu)
        menu.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='About...', command=about)
    
    def highlight_pattern(*args):
        firstIndex = textField.search('if', '0.0', END)
        offset = '+%dc' % len('if')
        # if
        while firstIndex:
            lastIndex = firstIndex+offset
            textField.tag_config('redFilter', foreground='red')
            textField.tag_add('redFilter', firstIndex, lastIndex)
            firstIndex = textField.search('if', lastIndex, END)
        # elif
        firstIndex = textField.search('if', '0.0', END)
        offset = '+%dc' % len('elif')
        while firstIndex:
            lastIndex = firstIndex+offset
            textField.tag_config('redFilter', foreground='red')
            textField.tag_add('redFilter', firstIndex, lastIndex)
            firstIndex = textField.search('elif', lastIndex, END)
        # else
        firstIndex = textField.search('if', '0.0', END)
        offset = '+%dc' % len('else')
        while firstIndex:
            lastIndex = firstIndex+offset
            textField.tag_config('redFilter', foreground='red')
            textField.tag_add('redFilter', firstIndex, lastIndex)
            firstIndex = textField.search('else', lastIndex, END)
        # def
        firstIndex = textField.search('def', '0.0', END)
        offset = '+%dc' % len('def')
        while firstIndex:
            lastIndex = firstIndex + offset
            textField.tag_config('greenFilter', foreground='green')
            textField.tag_add('greenFilter', firstIndex, lastIndex)
            firstIndex = textField.search('def', lastIndex, END)
        # imports
        firstIndex = textField.search('import', '0.0', END)
        offset = '+%dc' % len('import')
        while firstIndex:
            lastIndex = firstIndex + offset
            textField.tag_config('orangeFilter', foreground='orange')
            textField.tag_add('orangeFilter', firstIndex, lastIndex)
            firstIndex = textField.search('import', lastIndex, END)
        # comments
        firstIndex = textField.search('#', '0.0', END)
        while firstIndex:
            offset = '+%dc' % len(textField.get(firstIndex, textField.search('\n', firstIndex, END)))
            lastIndex = firstIndex + offset
            textField.tag_config('purpleFilter', foreground='purple')
            textField.tag_add('purpleFilter', firstIndex, lastIndex)
            firstIndex = textField.search('#', lastIndex, END)
        
        # this is a comment
        
    root = Tk()
    root.title('NotePad')
    mainframe = ttk.Frame(root, padding=(3,3,12,12))
    textField = ScrolledText.ScrolledText(root, height=128, width=200)
    textField.config(font=('courier', 15, 'normal'))
    textField.pack()
    createMenu()
    root.bind('<Control-s>', save)
    root.bind('<Control-n>', new)
    root.bind('<Control-o>', openFile)
    root.bind('<Control-l>', highlight_pattern)
    textField.focus()
    
    root.mainloop()