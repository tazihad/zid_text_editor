from tkinter import Tk, Menu, filedialog, END, messagebox
from tkinter.scrolledtext import ScrolledText


# Root for main window
root = Tk(className=" Zid Text Editor")
textArea = ScrolledText(root, width=100, height=80)

#
# Functions
#


def openfile():
    file = filedialog.askopenfile(parent=root, title='Select a text file', filetypes=(("Text file", "*.*"), ("All files", "*.*")))

    if file != None:
        contents = file.read()
        textArea.insert('1.0', contents)
        file.close()


def saveFile():
    file = filedialog.asksaveasfile(mode='w')

    if file != None:

        data = textArea.get('1.0', END+'-1c')
        file.write(data)
        file.close()


def about():
    label = messagebox.showinfo("About", "A python alternative to Notepad!")


def exitRoot():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        root.destroy()






# Menu Options


menu = Menu(root)
root.config(menu=menu)
fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open", command=openfile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="Print")
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command=exitRoot)

helpMenu = Menu(menu)
menu.add_cascade(label="Help")
menu.add_cascade(label="About", command=about)

textArea.pack()

# Keep window open
root.mainloop()