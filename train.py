from tkinter import * 
from tkinter import ttk, messagebox 
from PIL import Image, ImageTk, ImageFilter # type: ignore 
import mysql.connector 
import cv2 
import os 
import numpy as np 

class Train: 
    def __init__(self, root): 
        self.root = root 
        self.root.geometry("1530x790+0+0") 
        self.root.title("Face Recognition System") 
       
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("Times New Roman", 29, "bold"), bg="White", fg="Black") 
        title_lbl.place(x=0, y=0, width=1300, height=45) 

        img_top = Image.open(r"Images\Train Data BG.JPEG") # Provide the correct path 
        img_top = img_top.resize((1300, 250), Image.Resampling.LANCZOS) 
        self.photoimg_top=ImageTk.PhotoImage(img_top) 
        
        f_lbl = Label(self.root,image=self.photoimg_top) 
        f_lbl.place(x=0, y=45,width=1300, height=250) 
        
        img_bottom=Image.open(r"Images\faces.webp") # Provide the correct path 
        img_bottom=img_bottom.resize((1300, 330), Image.Resampling.LANCZOS) 
        img_bottom = img_bottom.filter(ImageFilter.GaussianBlur(radius=2)) # Apply blur filter 
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom) 
        
        f_lbl = Label(self.root,image=self.photoimg_bottom) 
        f_lbl.place(x=0, y=320,width=1300, height=330) 

        #button# 
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",20,"bold"),bg="Blue",fg="White") 
        b1_1.place(x=0,y=245,width=1300,height=70) 
        
    def train_classifier(self): 
        data_dir = ("Data")# Path to your training data directory 
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)] 
        
        faces = [] 
        ids = [] 
        
        for image in path:
            img = Image.open(image).convert('L') # Convert image to grayscale 
            imageNp = np.array(img, 'uint8') 
            id = int(os.path.split(image)[1].split('.')[1]) 
                
            faces.append(imageNp) 
            ids.append(id) 
            cv2.imshow("Training", imageNp) 
            cv2.waitKey(1) == 13 
        ids = np.array(ids) 
            
        # Train the classifier 
        clf = cv2.face.LBPHFaceRecognizer_create(radius=1, neighbors=8, grid_x=8, grid_y=8) 
        clf.train(faces, ids) 
        clf.write("classifier.xml") 
        cv2.destroyAllWindows() 
        messagebox.showinfo("Result", "Training datasets completed!", parent=self.root) 


if __name__ == "__main__":
    root = Tk() 
    obj = Train(root) 
    root.mainloop()