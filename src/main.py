import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import cv2
from PIL import ImageTk, Image
import face_recognition
import numpy as np



class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.parent = parent
        self.pack()
        App()
    # frm = root.Frame(root, padding=10)
    # btn = tk.Button(frm, text="hi").pack()


class labels:
    varFont = "Helvetica bold"
    fontSize = 40
    varFG = "#7676EE"

    def __init__(self, parent, name, varText):
        self.parent = parent
        self.name = name
        self.varText = varText

        self.label = tk.Label(
            parent,
            fg=self.varFG,
            text=varText,
            font=(self.varFont, self.fontSize)
        )

    def place(self, **kwargs):
        self.label.place(kwargs)


def uploadImage(event=None):
    # image = face_recognition.load_image_file("images/barackObama.jpg")
    fileName = filedialog.askopenfilename(title="Select file",
                                          filetypes=(("jpg", "*.jpg"), ("png", "*.png")))
    image = face_recognition.load_image_file(fileName)
<<<<<<< HEAD
=======

    while True:
        # Face Detection
        # Face Recognition
        image = face_recognition.load_image_file("images/barackObama.jpg")
        unknown_image = face_recognition.load_image_file(fileName)
        face_locations = face_recognition.face_locations(unknown_image)

        for (top, right, bottom, left) in face_locations:
            # Draw a box around the face
            cv2.rectangle(unknown_image, (left, top), (right, bottom), (0, 255, 0), 2)

        cv2.imshow("Image", cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        image_encoding = face_recognition.face_encodings(image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        results = face_recognition.compare_faces([image_encoding], unknown_encoding)

        cv2.putText(unknown_image, f'Barack Obama: {results[0]}', (25, 75), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        # cv2.imshow("Barack Obama", cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        cv2.imshow("Unknown", cv2.cvtColor(unknown_image, cv2.COLOR_BGR2RGB))
        cv2.waitKey(1)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
    print("done")
    cv2.destroyAllWindows()

def liveFacialRecognition():
    # Load a sample picture and learn how to recognize it.
    obama_image = face_recognition.load_image_file("barackObama.jpg")
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
>>>>>>> e50c82c37d890bdf12783f6675c762da1ae3f4f9

    while True:
        # Face Detection
        # Face Recognition
        image = face_recognition.load_image_file("images/barackObama.jpg")
        unknown_image = face_recognition.load_image_file(fileName)
        face_locations = face_recognition.face_locations(unknown_image)

        for (top, right, bottom, left) in face_locations:
            # Draw a box around the face
            cv2.rectangle(unknown_image, (left, top), (right, bottom), (0, 255, 0), 2)

        cv2.imshow("Image", cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

<<<<<<< HEAD
        image_encoding = face_recognition.face_encodings(image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        results = face_recognition.compare_faces([image_encoding], unknown_encoding)

        cv2.putText(unknown_image, f'Barack Obama: {results[0]}', (25, 75), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        # cv2.imshow("Barack Obama", cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        cv2.imshow("Unknown", cv2.cvtColor(unknown_image, cv2.COLOR_BGR2RGB))
        cv2.waitKey(1)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
    print("done")
    cv2.destroyAllWindows()


def liveFacialRecognition():
    # Load a sample picture and learn how to recognize it.
    obama_image = face_recognition.load_image_file("images/barackObama.jpg")
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

    # Load a second sample picture and learn how to recognize it.
    elon_image = face_recognition.load_image_file("images/elonMusk.jpg")
    elon_face_encoding = face_recognition.face_encodings(elon_image)[0]

    Thomas_image = face_recognition.load_image_file("images/Pic1.png")
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

=======
>>>>>>> e50c82c37d890bdf12783f6675c762da1ae3f4f9
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

root.iconphoto(False, tk.PhotoImage(file='images/logoimage.png'))
img = tk.PhotoImage(file='images/bodyimage.png')
ttk.Label(image=img).pack()


tk.Button(root, text="Obama Recognition", command=liveFacialRecognition).place(x=650, y=300)
tk.Button(root, text="Import Image", command=uploadImage).place(x=650, y=400)

root.mainloop()
