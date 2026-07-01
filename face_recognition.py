from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk, ImageFilter  # type: ignore
import mysql.connector
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        img_top = Image.open(r"Images\Face_recognition_bg.JPG")  # Provide the correct path
        img_top = img_top.resize((1270, 630), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=0, width=1270, height=630)

        # Button
        b1_1 = Button(f_lbl, text="START", cursor="hand2", font=("times new roman", 18, "bold"), bg="Red", fg="White",command=self.face_recog)
        b1_1.place(x=539, y=145, width=200, height=40)

         # Face Recognition
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)
            
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", user="root", password="SQLBhu26@", database="face_recognizer",auth_plugin="mysql_native_password")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_ID=" + str(id))
                n = my_cursor.fetchone()
                name = n[0] if n else "Unknown"

                my_cursor.execute("select `Roll no.` from student where Student_ID=" + str(id))
                r = my_cursor.fetchone()
                roll_no = r[0] if r else "Unknown" 
                
                my_cursor.execute("select Dep from student where Student_ID=" + str(id))
                d = my_cursor.fetchone()
                department = d[0] if d else "Unknown" 

                if confidence > 50:  # Lower the confidence threshold for testing
                    cv2.putText(img, f"Roll No.:{roll_no}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{name}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{department}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", cv2.resize(img, (640, 480)))

            if cv2.waitKey(1) == 13:  # 13 is the Enter Key
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()