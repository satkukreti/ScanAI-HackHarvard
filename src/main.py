import tkinter as tk
from tkinter import filedialog
class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.parent = parent
        self.pack()
        root = App()
    # frm = root.Frame(root, padding=10)
    # btn = tk.Button(frm, text="hi").pack()

class labels():

    varFont = "Helvetical bold"
    fontSize = 40
    varFG = "#F2F2F2"

    def __init__(self, parent, name, varText):
        self.parent = parent
        self.name = name
        self.varText = varText

        self.label = tk.Label(
            parent,
            fg = self.varFG,
            text = varText,
            font = (self.varFont, self.fontSize)
            )
    def place(self, **kwargs):
        self.label.place(kwargs)

def uploadImage(event=None):
    fileName = filedialog.askopenfilename()

root = tk.Tk()
root.geometry("1920x1080")

startMsg = labels(root, "Header", "Hello User!")
startMsg.place(x=620, y=200)

liveBtn = tk.Button(root, text="Use Live View").place(x=650, y=300)
picBtn = tk.Button(root, text="Submit Image", command=uploadImage).place(x=650, y=400)

root.mainloop()
