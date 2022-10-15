import tkinter as tk
from tkinter import filedialog
import cv2

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

def LiveCamBtn():
    cam = cv2.VideoCapture(0)
    while cam.isOpened():
        ret, frame1 = cam.read()
        ret, frame2 = cam.read()
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            if cv2.contourArea(c) < 10000:
                continue
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        if cv2.waitKey(10) == ord('0'):
            cv2.destroyAllWindows()
            break
        cv2.imshow('Facial Recognition', frame1)

root = tk.Tk()
root.geometry("1920x1080")

startMsg = labels(root, "Header", "Hello User!")
startMsg.place(x=620, y=200)

liveBtn = tk.Button(root, text="Use Live View", command=LiveCamBtn).place(x=650, y=300)
picBtn = tk.Button(root, text="Submit Image", command=uploadImage).place(x=650, y=400)

root.mainloop()
