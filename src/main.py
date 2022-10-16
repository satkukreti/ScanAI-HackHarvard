import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import cv2
from PIL import ImageTk, Image
import face_recognition
import numpy as np
import os
import Object_Detection.yolov5.detect as dtc



class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.parent = parent
        #self.pack()
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
        global left
        fileName = filedialog.askopenfilename(title="Select Image",
                                              filetypes=(("jpg", "*.jpg"), ("png", "*.png")))
        image = face_recognition.load_image_file(fileName)

        obama = face_recognition.load_image_file("src/images/barackObama.jpg")
        face_locations = face_recognition.face_locations(image)

        # for (top, right, bottom, left) in face_locations:
        #     # Draw a box around the face
        #     cv2.rectangle(unknown_image, (left, top), (right, bottom), (0, 255, 0), 2)

        image_encoding = face_recognition.face_encodings(obama)[0]
        faces = face_recognition.face_encodings(image)
        if len(faces) <= 0:
            root = tk.Tk()
            tk.messagebox.showerror(title="Error", message="No faces were found.")
            # print("error")
            cv2.destroyAllWindows()
            root.destroy()
        else:
            unknown_encoding = face_recognition.face_encodings(image)[0]
            results = face_recognition.compare_faces([image_encoding], unknown_encoding)

            cv2.putText(image, f'Is this Barack Obama? {results[0]}', (25, 75), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (255, 255, 255), 2)
            # cv2.imshow("Barack Obama", cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            print(face_locations)
            print(face_locations[0][3])
            if results[0]==False:
                cv2.rectangle(image, (face_locations[0][3], face_locations[0][2] - 35), (face_locations[0][1], face_locations[0][2]), (255, 0, 0 ), cv2.FILLED)
                print("SHOULD BE RED")

            else:
                unknown_encoding = face_recognition.face_encodings(image)
                #print(unknown_encoding)
                results=[]
                x = 0
                for i in range(len(unknown_encoding)):
                    #print(i)
                    #print(face_recognition.compare_faces([image_encoding], unknown_encoding[x]))
                    results.append(face_recognition.compare_faces([image_encoding], unknown_encoding[x]))
                    x+=1
                cv2.putText(image, f'Is this Barack Obama? {results[0]}', (25, 75), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (255, 255, 255), 2)
                # cv2.imshow("Barack Obama", cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
                #print(face_locations)
                #print(face_locations[0][3])
                if results[0]==False:
                    cv2.rectangle(image, (face_locations[0][3], face_locations[0][2] - 35), (face_locations[0][1], face_locations[0][2]), (255, 0, 0 ), cv2.FILLED)
                    #print("SHOULD BE RED")

                else:
                    cv2.rectangle(image, (face_locations[0][3], face_locations[0][2] - 35), (face_locations[0][1], face_locations[0][2]), (0, 255, 0 ), cv2.FILLED)
                    #print("Should be green")

                counter = 0
                for (top, right, bottom, left) in face_locations:
                    if results[counter][0]==True:
                        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
                        cv2.rectangle(image, (left, bottom - 35), (right, bottom), (0, 255, 0 ), cv2.FILLED)
                    elif results[counter][0]==False:
                        cv2.rectangle(image, (left, top), (right, bottom), (255, 0, 0), 2)
                        cv2.rectangle(image, (left, bottom - 35), (right, bottom), (255, 0, 0 ), cv2.FILLED)
                    counter+=1

            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.imshow("Unknown", cv2.cvtColor(image, cv2.COLOR_BGR2RGB))


    def liveFacialRecognition():
        # Load a sample picture and learn how to recognize it.
        obama_image = face_recognition.load_image_file("src/images/barackObama.jpg")
        obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

        # Load a second sample picture and learn how to recognize it.
        elon_image = face_recognition.load_image_file("src/images/elonMusk.jpg")
        elon_face_encoding = face_recognition.face_encodings(elon_image)[0]

        Thomas_image = face_recognition.load_image_file("src/images/Pic1.png")
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
                cv2.putText(frame, name, (left, bottom - 4), font, 1, (255, 255, 255), 2)

            # Display the resulting image
            cv2.imshow('Image', frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def weapon_finder():
        dtc.run(weights='src/best.pt', source=0)
    
    def weapon_image():
        fileName = filedialog.askopenfilename(title="Select Image",
                                              filetypes=(("jpg", "*.jpg"), ("png", "*.png")))
        dtc.run(weights='src/best.pt', source=fileName, view_img=True)



    print(os.getcwd())


    root = tk.Tk()
    root.title("SCAN ai")
    root.geometry("1920x1080")
    root.configure(bg="#ffffff")
    root.iconphoto(False, tk.PhotoImage(file='src/images/logoimage.png'))

    frame = tk.LabelFrame(root, font="Helvetica, 20", text="  Thomas, Winston, Tina, & Satvik present  ", padx=100, pady=10, labelanchor="n")
    frame.configure(bg="#ffffff")

    my_img = ImageTk.PhotoImage(Image.open('src/images/bodyimage.png'))
    my_label = tk.Label(image=my_img, padx=20, pady=20)
    tk.Label(text="   ", bg="#ffffff").pack()
    my_label.pack()
    tk.Label(text="   ", bg="#ffffff").pack()


    #root.iconphoto(False, tk.PhotoImage(file='images/logoimage.png'))
    #img = tk.PhotoImage(file='images/bodyimage.png')
    #ttk.Label(image=img).pack()


    frame.pack(padx=100, pady=10, fill="both")

    tk.Label(frame,text="   ", bg="#ffffff").pack()
    tk.Button(frame, font="Arial, 20",text="Are You Obama?", command=liveFacialRecognition, pady=10).pack(fill="x")
    tk.Label(frame,text="   ", bg="#ffffff").pack()
    tk.Label(frame,text="   ", bg="#ffffff").pack()
    tk.Button(frame, font="Arial, 20",text="Import Image", command=uploadImage, pady=10).pack(fill="x")
    tk.Label(frame,text="   ", bg="#ffffff").pack()
    tk.Label(frame,text="   ", bg="#ffffff").pack()
    tk.Button(frame, font="Arial, 20", text="Live Weapon Detection", command=weapon_finder, pady=10).pack(fill="x")
    tk.Label(frame,text="   ", bg="#ffffff").pack()
    tk.Label(frame,text="   ", bg="#ffffff").pack()
    tk.Button(frame, font="Arial, 20", text="Image Weapon Detection", command=weapon_image, pady=10).pack(fill="x")
    tk.Label(frame,text="   ", bg="#ffffff").pack()

    root.mainloop()
