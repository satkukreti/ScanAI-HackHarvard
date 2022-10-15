import tkinter as tk
from tkinter import filedialog
import cv2
import face_recognition
import cv2
import numpy as np

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
    varFG = "#7676EE"

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
            cam.release()
            cv2.destroyAllWindows()
            break
        cv2.namedWindow('Facial Recognition', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Facial Recognition', 500, 500)
        cv2.imshow('Facial Recognition', frame1)


def facialRecognition():
    # Load a sample picture and learn how to recognize it.
    obama_image = face_recognition.load_image_file("barackObama.jpg")
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

    # Load a second sample picture and learn how to recognize it.
    elon_image = face_recognition.load_image_file("elonMusk.jpg")
    elon_face_encoding = face_recognition.face_encodings(elon_image)[0]

    Thomas_image = face_recognition.load_image_file("Pic1.png")
    Thomas_face_encoding = face_recognition.face_encodings(Thomas_image)[0]

    # Create arrays of known face encodings and their names
    known_face_encodings = [
        obama_face_encoding,
        elon_face_encoding,
        Thomas_face_encoding
    ]
    known_face_names = [
        "Barack Obama",
        "Elon Musk",
        "Thomas"
    ]

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    capture = cv2.VideoCapture(0)

    while True:

        # Grab a single frame of video
        ret, frame = capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Not Obama"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left, bottom - 4), font, 1, (0, 0, 255), 2)

        # Display the resulting image
        cv2.imshow('Image', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    capture.release()
    cv2.destroyAllWindows()

root = tk.Tk()
root.geometry("1920x1080")

startMsg = labels(root, "Header", "Hello User!")
startMsg.place(x=620, y=200)

liveBtn = tk.Button(root, text="Obama Recognition", command=facialRecognition).place(x=650, y=300)
picBtn = tk.Button(root, text="Import Image", command=uploadImage).place(x=650, y=400)

root.mainloop()
