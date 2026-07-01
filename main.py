from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #Head Image
        img=Image.open(r"E:\FRAMS\Images\Head Image.jpg")
        img=img.resize((1300, 130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1300,height=130)

        #Background Image
        img1=Image.open(r"E:\FRAMS\Images\Background Image.JPG")
        img1=img1.resize((1300, 710),Image.Resampling.LANCZOS)
        img1 = img1.filter(ImageFilter.GaussianBlur(radius=4))  # Apply blur filter
        self.photoimg1=ImageTk.PhotoImage(img1)

        bg_image=Label(self.root,image=self.photoimg1)
        bg_image.place(x=0,y=130,width=1300,height=710)

        #Add title
        title_lbl=Label(bg_image,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("Arial Black",29,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1300,height=40)

        #Student Button
        img2=Image.open(r"E:\FRAMS\Images\Student Pannel.JPG")
        img2=img2.resize((130, 130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Button(bg_image,image=self.photoimg2,command=self.student_details,cursor="hand2")
        b1.place(x=250,y=90,width=130,height=130)

        b1_1=Button(bg_image,text="Student Panel",command=self.student_details,cursor="hand2",font=("times new roman",12,"bold"),bg="white",fg="black")
        b1_1.place(x=250,y=220,width=130,height=40)

        #Detect Face Button
        img3=Image.open(r"E:\FRAMS\Images\Face Detector.JPG")
        img3=img3.resize((130, 130),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b1=Button(bg_image,image=self.photoimg3,command=self.face_data,cursor="hand2")
        b1.place(x=470,y=90,width=130,height=130)

        b1_1=Button(bg_image,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",12,"bold"),bg="white",fg="black")
        b1_1.place(x=470,y=220,width=130,height=40)

        #Attendance Button
        img4=Image.open(r"E:\FRAMS\Images\Attendance.JPEG")
        img4=img4.resize((130, 130),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_image,image=self.photoimg4,cursor="hand2")
        b1.place(x=690,y=90,width=130,height=130)

        b1_1=Button(bg_image,text="Attendance",cursor="hand2",font=("times new roman",12,"bold"),bg="white",fg="black")
        b1_1.place(x=690,y=220,width=130,height=40)
        
        #Help Desk Button
        img5=Image.open(r"E:\FRAMS\Images\Help Support.JPEG")
        img5=img5.resize((130, 130),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_image,image=self.photoimg5,cursor="hand2")
        b1.place(x=910,y=90,width=130,height=130)

        b1_1=Button(bg_image,text="Help Desk",cursor="hand2",font=("times new roman",12,"bold"),bg="white",fg="black")
        b1_1.place(x=910,y=220,width=130,height=40)

        #Data Train Button
        img6=Image.open(r"E:\FRAMS\Images\Data Train.JPG")
        img6=img6.resize((130, 130),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_image,image=self.photoimg6,command=self.train_data,cursor="hand2",)
        b1.place(x=250,y=320,width=130,height=130)

        b1_1=Button(bg_image,text="Data Train",command=self.train_data,cursor="hand2",font=("times new roman",12,"bold"),bg="white",fg="black")
        b1_1.place(x=250,y=450,width=130,height=40)

        #Dataset Button
        img7=Image.open(r"E:\FRAMS\Images\\Dataset.PNG")
        img7=img7.resize((130, 130),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_image,image=self.photoimg7,command=self.open_img,cursor="hand2")
        b1.place(x=470,y=320,width=130,height=130)

        b1_1=Button(bg_image,text="Dataset",command=self.open_img,cursor="hand2",font=("times new roman",12,"bold"),bg="white",fg="black")
        b1_1.place(x=470,y=450,width=130,height=40)
    
        #Developer Button
        img8=Image.open(r"E:\FRAMS\Images\Developer.JPG")
        img8=img8.resize((130, 130),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_image,image=self.photoimg8,cursor="hand2")
        b1.place(x=690,y=320,width=130,height=130)

        b1_1=Button(bg_image,text="Developer",cursor="hand2",font=("times new roman",12,"bold"),bg="white",fg="black")
        b1_1.place(x=690,y=450,width=130,height=40)
    
        #Exit Button
        img9=Image.open(r"Images\Exit.JPEG")
        img9=img9.resize((130, 130),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_image,image=self.photoimg9,cursor="hand2")
        b1.place(x=910,y=320,width=130,height=130)

        b1_1=Button(bg_image,text="Exit",cursor="hand2",font=("times new roman",12,"bold"),bg="white",fg="black")
        b1_1.place(x=910,y=450,width=130,height=40)

    def open_img(self):
        os.startfile("Data")

        #Function Buttons. 
    def student_details(self):
        # Create a new window for the Student panel
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        # Create a new window for the Student panel
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        # Create a new window for the Student panel
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()