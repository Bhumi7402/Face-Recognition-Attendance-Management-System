from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk # type: ignore
import mysql.connector
import cv2


class Student:
    def __init__(self, root):  
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #Variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar() 
        self.var_phone=StringVar() 
        self.var_address=StringVar() 
        self.var_teacher=StringVar() 
        

        
        
        
     
        # First image
         
        img = Image.open(r"E:\FRAMS\Images\Faces3.JPEG")
        img = img.resize((380, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
    
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=380, height=130)
            
    
        
        # Second image
        
        img1 = Image.open(r"E:\FRAMS\Images\Faces.JPG")
        img1 = img1.resize((440, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=380, y=0, width=440, height=130)
        
            
        
        
        # Third image
           
        img2 = Image.open(r"E:\FRAMS\Images\faces9.JPEG")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
    
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=820, y=0, width=500, height=130)
            

        # Background image
        img3 = Image.open(r"E:\FRAMS\Images\Background Image.JPG")  # Provide the correct path
        img3 = img3.resize((1300, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

    
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1300, height=710)
    
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("Arial Black", 29, "bold"), bg="White", fg="Black")
        title_lbl.place(x=0, y=0, width=1300, height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=15, y=50, width=1250, height=468)
    


        # Left label frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=8, y=0, width=610, height=460)
        

        img_left = Image.open(r"E:\FRAMS\Images\faces5.JPEG")  # Provide the correct path
        img_left = img_left.resize((602, 100), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
    
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=2, y=0, width=602, height=100)
        

        # Current Course Information
        current_course_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=100, width=600, height=100)

        # Department Label and Combo Box
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 10, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=20, pady=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman", 9, "bold"), width=17, state="readonly")
        dep_combo['values'] = ("Select Department", "Computer", "IT", "Mechanical", "Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Empty Grid Cell to increase spacing
        empty_label = Label(current_course_frame)
        empty_label.grid(row=0, column=2, padx=50, pady=10, sticky=W)  # Adjust padx to increase spacing

        # Course Label and Combo Box
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 10, "bold"), bg="white")
        course_label.grid(row=0, column=3, padx=20, pady=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman", 9, "bold"), width=17, state="readonly")
        course_combo['values'] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=4, padx=10, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 10, "bold"),bg="White")
        year_label.grid(row=1, column=0, padx=20, pady=2, sticky=W)
    
        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman", 9, "bold"), width=17, state="readonly")
        year_combo['values'] = ("Select Year", "2023-24", "2024-25", "2025-26", "2026-27")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=2, sticky=W)

        # Empty Grid Cell to increase spacing
        empty_label = Label(current_course_frame)
        empty_label.grid(row=0, column=2, padx=50, pady=10, sticky=W)  # Adjust padx to increase spacing
    
        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 10, "bold"),bg="White")
        semester_label.grid(row=1, column=3, padx=20, pady=2, sticky=W)
    
        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman", 9, "bold"), width=17, state="readonly")
        semester_combo['values'] = ("Select Semester", "Sem 1", "Sem 2", "Sem 3", "Sem 4")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=4, padx=10, pady=2, sticky=W)

        # Class Student Information
        class_student_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=200, width=600, height=237)

        # Student ID
        student_id_label = Label(class_student_frame, text="Student ID", font=("times new roman", 10, "bold"), bg="white")
        student_id_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
    
        student_id_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=17, font=("times new roman", 9, "bold"))
        student_id_entry.grid(row=0, column=1, padx=20, pady=10, sticky=W)

        # Empty Grid Cell to increase spacing
        empty_label = Label(class_student_frame)
        empty_label.grid(row=0, column=2, padx=30, pady=10, sticky=W)  # Adjust padx to increase spacing
    
        # Student Name
        student_name_label = Label(class_student_frame, text="Student Name", font=("times new roman", 10, "bold"), bg="white")
        student_name_label.grid(row=0, column=3, padx=20, pady=10, sticky=W)
    
        student_name_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=17, font=("times new roman", 9, "bold"))
        student_name_entry.grid(row=0, column=4, padx=10, pady=10, sticky=W)

        # Class Division
        class_division_label = Label(class_student_frame, text="Class Division", font=("times new roman", 10, "bold"), bg="white")
        class_division_label.grid(row=1, column=0, padx=10, pady=2, sticky=W)
    
        class_division_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman", 9, "bold"), width=14, state="readonly")
        class_division_combo['values'] = ("A", "B", "C")
        class_division_combo.current(0)
        class_division_combo.grid(row=1, column=1, padx=20, pady=2, sticky=W)

        # Empty Grid Cell to increase spacing
        empty_label = Label(class_student_frame)
        empty_label.grid(row=1, column=2, padx=30, pady=2, sticky=W)  # Adjust padx to increase spacing
    
        # Roll No
        roll_no_label = Label(class_student_frame, text="Roll No.", font=("times new roman", 10, "bold"), bg="white")
        roll_no_label.grid(row=1, column=3, padx=20, pady=2, sticky=W)
    
        roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll,width=17, font=("times new roman", 9, "bold"))
        roll_no_entry.grid(row=1, column=4, padx=10, pady=2, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, text="Gender", font=("times new roman", 10, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=2, sticky=W)
        
        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman", 9, "bold"), width=14, state="readonly")
        gender_combo['values'] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=20, pady=10, sticky=W)


        # Empty Grid Cell to increase spacing
        empty_label = Label(class_student_frame)
        empty_label.grid(row=2, column=2, padx=30, pady=2, sticky=W)  # Adjust padx to increase spacing
    
        # Date of Birth
        dob_label = Label(class_student_frame, text="Date Of Birth", font=("times new roman", 10, "bold"), bg="white")
        dob_label.grid(row=2, column=3, padx=20, pady=2, sticky=W)
    
        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob,width=17, font=("times new roman", 9, "bold"))
        dob_entry.grid(row=2, column=4, padx=10, pady=2, sticky=W)

        # Email
        email_label = Label(class_student_frame, text="Email", font=("times new roman", 10, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=2, sticky=W)
    
        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width=17, font=("times new roman", 9, "bold"))
        email_entry.grid(row=3, column=1, padx=20, pady=2, sticky=W)

        # Empty Grid Cell to increase spacing
        empty_label = Label(class_student_frame)
        empty_label.grid(row=3, column=2, padx=30, pady=2, sticky=W)  # Adjust padx to increase spacing
    
        # Contact No
        contact_no_label = Label(class_student_frame, text="Contact No.", font=("times new roman", 10, "bold"), bg="white")
        contact_no_label.grid(row=3, column=3, padx=20, pady=2, sticky=W)
    
        contact_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone, width=17, font=("times new roman", 9, "bold"))
        contact_no_entry.grid(row=3, column=4, padx=10, pady=2, sticky=W)

        # Address
        address_label = Label(class_student_frame, text="Address", font=("times new roman", 10, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=2, sticky=W)
    
        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address,width=17, font=("times new roman", 9, "bold"))
        address_entry.grid(row=4, column=1, padx=20, pady=2, sticky=W)

        # Empty Grid Cell to increase spacing
        empty_label = Label(class_student_frame)
        empty_label.grid(row=4, column=2, padx=30, pady=2, sticky=W)  # Adjust padx to increase spacing
    
        # Teacher Name
        teacher_label = Label(class_student_frame, text="Teacher Name", font=("times new roman", 10, "bold"), bg="white")
        teacher_label.grid(row=4, column=3, padx=20, pady=2, sticky=W)
    
        teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=17, font=("times new roman", 9, "bold"))
        teacher_entry.grid(row=4, column=4, padx=10, pady=2, sticky=W)

        # Buttons Frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.grid(row=5, column=0,columnspan=8,padx=0, pady=0, sticky=W+E)  # Using grid with columnspan

        # Disable frame resizing based on children
        btn_frame.grid_propagate(False)

        # Set a specific height and width
        btn_frame.config(width=0, height=55)

        # Configure column weights to avoid extra space
        for i in range(6):
            btn_frame.grid_columnconfigure(i, weight=1)

        # Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1 = ttk.Radiobutton(btn_frame,variable=self.var_radio1, text="Take Photo Sample", value="Yes",width=25)
        radiobtn1.grid(row=0, column=0, padx=5, pady=2,sticky='w')

        
        radiobtn2 = ttk.Radiobutton(btn_frame,variable=self.var_radio1, text="No Photo Sample", value="No",width=23)
        radiobtn2.grid(row=0, column=2, padx=5, pady=2, sticky='w')

        # Button options
        button_options = {
            'font': ("times new roman", 10, "bold"),
            'padx': 2,
            'pady': 0,
        }

        # Buttons
        save_btn = Button(btn_frame, text="Save",command=self.add_data,width=20, bg="Green", fg="white", **button_options)
        save_btn.grid(row=1, column=3, padx=5, pady=0, sticky='w')

        update_btn = Button(btn_frame, text="Update", width=20,command=self.update_data,bg="yellow", fg="Black", **button_options)
        update_btn.grid(row=1, column=4, padx=2, pady=0, sticky='w')

        delete_btn = Button(btn_frame, text="Delete", width=20,command=self.delete_data, bg="Red", fg="white", **button_options)
        delete_btn.grid(row=1, column=5, padx=2, pady=0, sticky='w')

        reset_btn = Button(btn_frame, text="Reset", width=8, command=self.reset_data, bg="Blue", fg="white", **button_options)
        reset_btn.grid(row=1, column=6, padx=2, pady=0, sticky='w')

        take_photo_btn = Button(btn_frame, text="Take Photo Sample",command=self.take_photo, width=35, bg="orange", fg="white", **button_options)
        take_photo_btn.grid(row=1, column=0, padx=5, pady=0, sticky='w')

        update_photo_btn = Button(btn_frame, text="Update Photo Sample", width=35, bg="orange", fg="white", **button_options)
        update_photo_btn.grid(row=1, column=2, padx=5, pady=0, sticky='w')

        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=628, y=0, width=610, height=460)

        img_right = Image.open(r"Images\faces8.JPEG")  #  Corrected Path # Provide the correct path
        img_right = img_right.resize((602, 100), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
    
        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=2, y=0, width=602, height=100)

        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=100, width=600, height=62)
    
        search_label = Label(search_frame, text="Search By", font=("times new roman", 12, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 10, "bold"), width=17, state="readonly")
        search_combo['values'] = ("Select", "Roll No.", "Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=5, sticky=W)
    
        search_entry = ttk.Entry(search_frame, width=17, font=("times new roman", 10, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)
    
        search_btn = Button(search_frame, text="Search", width=13, font=("times new roman", 10, "bold"), bg="Blue", fg="white")
        search_btn.grid(row=0, column=3, padx=3, pady=5, sticky=W)

        show_all_btn = Button(search_frame, text="Show All", width=13, font=("times new roman", 10, "bold"), bg="orange", fg="white")
        show_all_btn.grid(row=0, column=4, padx=3, pady=5, sticky=W)

        # Table Frame
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=162, width=600, height=275)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
    
        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "contact", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
    
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No.")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("contact", text="Contact")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo Status")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("contact", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)
    
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    #Function Declaration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Mandatory",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="SQLBhu26@",database="face_recognizer", auth_plugin="mysql_native_password")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(), 
                                                                                                                self.var_year.get(), 
                                                                                                                self.var_semester.get(), 
                                                                                                                self.var_std_id.get(), 
                                                                                                                self.var_std_name.get(), 
                                                                                                                self.var_div.get(), 
                                                                                                                self.var_roll.get(), 
                                                                                                                self.var_gender.get(), 
                                                                                                                self.var_dob.get(), 
                                                                                                                self.var_email.get(), 
                                                                                                                self.var_phone.get(), 
                                                                                                                self.var_address.get(), 
                                                                                                                self.var_teacher.get(), 
                                                                                                                self.var_radio1.get()
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added successfully.", parent=self.root)
            except Exception as es:
                 messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    #Fetch Data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="SQLBhu26@",database="face_recognizer", auth_plugin="mysql_native_password")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()           

        if len(data)!=0:
             self.student_table.delete(*self.student_table.get_children())
             for i in data:
                  self.student_table.insert("",END,values=i)
             conn.commit()
        conn.close()  

#get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1],)
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

#update function
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are Mandatory", parent=self.root)
        else:
          try:
            Update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
            if Update > 0:
                conn = mysql.connector.connect(host="localhost", user="root", password="SQLBhu26@", database="face_recognizer", auth_plugin="mysql_native_password")
                my_cursor = conn.cursor()
                sql = """UPDATE student 
                         SET Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, `Roll no.`=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, `Photo Sample`=%s 
                         WHERE Student_ID=%s"""
                val = (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()
                )
                my_cursor.execute(sql, val)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
            else:
                return
          except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

#Delete
    def delete_data(self):
        if self.var_std_id.get() == "":
         messagebox.showerror("Error", "Student ID is required to delete", parent=self.root)
        else:
          try:
            delete = messagebox.askyesno("Delete", "Are you sure you want to delete this student?", parent=self.root)
            if delete > 0:
                conn = mysql.connector.connect(host="localhost", user="root", password="SQLBhu26@", database="face_recognizer", auth_plugin="mysql_native_password")
                my_cursor = conn.cursor()
                sql = "delete from student where Student_ID=%s"
                val = (self.var_std_id.get(),)
                my_cursor.execute(sql, val)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Student record deleted successfully", parent=self.root)
            else:
                if not delete:
                    return
          except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

#reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

#Generate data set or Take photo sample
    def take_photo(self):
        self.add_data()
        if self.var_std_id.get() == "":
         messagebox.showerror("Error", "Student ID is required for taking a photo sample", parent=self.root)
        else:
         try:
            conn = mysql.connector.connect(host="localhost", user="root", password="SQLBhu26@", database="face_recognizer", auth_plugin="mysql_native_password")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student")
            myresult = my_cursor.fetchall()
            id = 0
            for x in myresult:
                id += 1
            my_cursor.execute("UPDATE student SET `Photo_Sample`='Yes' WHERE Student_ID=" + str(self.var_std_id.get()))
            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()
         
            # OpenCV Code for Generating Dataset
            face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            
            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cropped_face = img[y:y + h, x:x + w]
                    return cropped_face
                return None

            cap = cv2.VideoCapture(0)
            img_id = 0
            while True:
                ret, frame = cap.read()
                if face_cropped(frame) is not None:
                    img_id += 1
                    face = cv2.resize(face_cropped(frame), (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                    cv2.imwrite(file_name_path, face)
                    cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("Cropped Face", face)
                
                if cv2.waitKey(1) == 13 or int(img_id) == 100:  # Enter Key to Stop or 100 images
                    break

            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Generating dataset completed!")
         except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

if __name__ == "__main__":
        root = Tk()
        obj = Student(root)
        root.mainloop()