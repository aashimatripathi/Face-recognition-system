from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student_mamagement_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x600")
        self.root.title("Student Management System")


        #variables
        self.var_dep = StringVar()
        self.var_gender = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_email = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_dob = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_photo = StringVar()

        


    # #1.Top image 
    #     print("Loading background image...")
    #     img = Image.open(r"C:\Users\AASHIMA\OneDrive\Desktop\Face Recognition System\images\Img_8.jpg")
    #     img = img.resize((500,130))
    #     self.photoimg = ImageTk.PhotoImage(img)

    #     f_lbl = Label(self.root, image=self.photoimg)
    #     f_lbl.place(x=0, y=0, width=500, height=130)

    #     #2. Top image 
    #     print("Loading second image...")
    #     img1 = Image.open(r"C:\Users\AASHIMA\OneDrive\Desktop\Face Recognition System\images\student details.jpg")
    #     img1 = img1.resize((660,130))
    #     self.photoimg1 = ImageTk.PhotoImage(img1)

    #     f_lbl = Label(self.root, image=self.photoimg1)
    #     f_lbl.place(x=500, y=0, width=660, height=130)

    #     #3. Top image 
    #     print("Loading third image...")
    #     img2 = Image.open(r"C:\Users\AASHIMA\OneDrive\Desktop\Face Recognition System\images\Img_6.jpg")
    #     img2 = img2.resize((550,130))
    #     self.photoimg2 = ImageTk.PhotoImage(img2)

    #     f_lbl = Label(self.root, image=self.photoimg2)
    #     f_lbl.place(x=1100, y=0, width=550, height=130) 


        #4. Background image
        print("Loading background image...")
        img3 = Image.open(r"C:\Users\AASHIMA\OneDrive\Desktop\Face Recognition System\images\Img_14_blurred.jpg")
        img3 = img3.resize((1600,1000))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1600, height=1000)
        

        #lable title
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("algerian", 40), bg="light blue", fg="dark blue")
        title_lbl.place(x=-2, y=-2, width=1600, height=70)


        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=100, width=1550, height=630)


        #left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=5, y=0, width=750, height=610)


        img_left = Image.open(r"C:\Users\AASHIMA\OneDrive\Desktop\Face Recognition System\images\Img_13.jpg")
        img_left = img_left.resize((700,130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=20, y=0, width=700, height=130) 

        #------------------------------------------------------------------------------------------------------------#

        #current course
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Details", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=20, y=135, width=700, height=120)

        #Department Details
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 14, "bold"), bg="white", )
        dep_label.grid(row=0, column=0, padx=10, sticky=W)
        
        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=("times new roman", 14, "bold"), width=17)
        dep_combo["value"] = ("Select Department", "Computer Science", "Information Technology", "Electronics", "Mechanical", "Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        #Course Details
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 14, "bold"), bg="white", )
        course_label.grid(row=0, column=2, padx=30, sticky=W)
        
        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("times new roman", 14, "bold"), width=17)
        course_combo["value"] = ("Select Courses", "Computer science and engg.", "Aerospace engg.", "Robotics engg.", "Civil engg.", "Electrical engg.", "Mechanical engg.")    
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        #Year Details
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 14, "bold"), bg="white", )
        year_label.grid(row=1, column=0, padx=10, sticky=W)
        
        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("times new roman", 14, "bold"), width=17)
        year_combo["value"] = ("Select Year", "2021-22", "2022-23", "2023-24", "2024-25")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        #Semester Details
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 14, "bold"), bg="white", )
        semester_label.grid(row=1, column=2, padx=30, sticky=W)
        
        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_sem, font=("times new roman", 14, "bold"), width=17)
        semester_combo["value"] = ("Select Semester", "I", "II", "III", "IV", "V", "VI", "VII", "VIII")    
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        #--------------------------------------------------------------------------------------------------#

        #Class Student details
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=20, y=260, width=700, height=320)


        #student id
        studentID_label = Label(class_student_frame, text="Student ID:", font=("times new roman", 13, "bold"), bg="white", )
        studentID_label.grid(row=0, column=0, padx=10,pady=5, sticky=W)

        studentID_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id, width=20, font=("times new roman", 13, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10,pady=5, sticky=W)


        #student name
        studentName_label = Label(class_student_frame, text="Student Name:", font=("times new roman", 13, "bold"), bg="white", )
        studentName_label.grid(row=0, column=2, padx=10,pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=20, font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)


        #Class division
        studentDiv_label = Label(class_student_frame, text="Class Division:", font=("times new roman", 13, "bold"), bg="white", )
        studentDiv_label.grid(row=1, column=0, padx=10,pady=5, sticky=W)

        student_Div_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div, font=("times new roman", 12), width=20)
        student_Div_combo["value"] = ("Select Division", "A", "B", "C", "D")
        student_Div_combo.current(0)
        student_Div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)


        #Roll no.
        roll_no_label = Label(class_student_frame, text="Roll no.:", font=("times new roman", 13, "bold"), bg="white", )
        roll_no_label.grid(row=1, column=2, padx=10,pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20, font=("times new roman", 13, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)


        #Email
        email_label = Label(class_student_frame, text="Email:", font=("times new roman", 13, "bold"), bg="white", )
        email_label.grid(row=3, column=0, padx=10,pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=("times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)


        #phone no.
        phone_no_label = Label(class_student_frame, text="Phone no.:", font=("times new roman", 13, "bold"), bg="white", )
        phone_no_label.grid(row=3, column=2, padx=10,pady=5, sticky=W)

        phone_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=("times new roman", 13, "bold"))
        phone_no_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)


        #Address
        address_label = Label(class_student_frame, text="Address:", font=("times new roman", 13, "bold"), bg="white", )
        address_label.grid(row=4, column=0, padx=10,pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)


        #Teacher names
        teacher_name_label = Label(class_student_frame, text="Teacher name:", font=("times new roman", 13, "bold"), bg="white", )
        teacher_name_label.grid(row=4, column=2, padx=10,pady=5, sticky=W)

        teacher_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=20, font=("times new roman", 13, "bold"))
        teacher_name_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)


        #Gender
        gender_label = Label(class_student_frame, text="Gender:", font=("times new roman", 13, "bold"), bg="white")
        gender_label.grid(row=5, column=0, padx=10,pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender, font=("times new roman", 12), width=20)
        gender_combo["value"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=5, column=1, padx=10, pady=5, sticky=W)


        #Date of Birth
        dob_label = Label(class_student_frame, text="D.O.B:", font=("times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=5, column=2, padx=10,pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=("times new roman", 13, "bold"))
        dob_entry.grid(row=5, column=3, padx=10, pady=5, sticky=W)


        #RADIO BUTTON
        radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_photo, text="Take Photo Sample", value="yes")
        radiobtn1.grid(row=6, column=0, padx=10, pady=5)

        radiobtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_photo, text="No Photo Sample", value="no")
        radiobtn2.grid(row=6, column=1, padx=10, pady=5)


        #Buttons frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=7, y=200, width=680, height=45)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, font=("times new roman", 13, "bold"),width=14, bg="light blue", fg="dark blue")
        save_btn.grid(row=0, column=0, padx=10, pady=5)
         
        update_btn = Button(btn_frame, text="Update", command=self.update_data, font=("times new roman", 13, "bold"), width=14, bg="light blue", fg="dark blue")
        update_btn.grid(row=0, column=1, padx=10, pady=5)

        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data,font=("times new roman", 13, "bold"),width=14, bg="light blue", fg="dark blue")
        delete_btn.grid(row=0, column=2, padx=10, pady=5)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset,font=("times new roman", 13, "bold"),width=14, bg="light blue", fg="dark blue")
        reset_btn.grid(row=0, column=3, padx=10, pady=5)


        #------------------------------------------------------------------------------------------------------------#

        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=7, y=250, width=680, height=45)

        take_photo_btn = Button(btn_frame1,  text="Take photo sample",command=self.generate_dataset,font=("times new roman", 13, "bold"),width=30, bg="light blue", fg="dark blue")
        take_photo_btn.grid(row=0, column=0, padx=10, pady=5)

        Update_photo_btn = Button(btn_frame1, text="Update photo sample",font=("times new roman", 13, "bold"),width=30, bg="light blue", fg="dark blue")
        Update_photo_btn.grid(row=0, column=1, padx=10, pady=5)


        #------------------------------------------------------------------------------------------------------------#


        #Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=770, y=0, width=760, height=610)

        img_right = Image.open(r"C:\Users\AASHIMA\OneDrive\Desktop\Face Recognition System\images\Img_15.jpeg")
        img_right = img_right.resize((710,130))
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=20, y=0, width=710, height=130) 


        #------------------------------------------------------------------------------------------------------------#

        #Search System
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=20, y=135, width=710, height=70)

        search_label = Label(search_frame, text="Search bar", font=("times new roman", 11, "bold"), bg="white")
        search_label.grid(row=0, column=0, padx=10,pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 11, "bold"), width=17)
        search_combo["value"] = ("Select", "Roll no.", "Phone no.")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, width=20, font=("times new roman", 11, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search",font=("times new roman", 11, "bold"),width=11, bg="light blue", fg="dark blue")
        search_btn.grid(row=0, column=3, padx=10, pady=5)

        show_all_btn = Button(search_frame, text="Show All",font=("times new roman", 11, "bold"),width=11, bg="light blue", fg="dark blue")
        show_all_btn.grid(row=0, column=4, padx=10, pady=5)

        
        #------------------------------------------------------------------------------------------------------------#
        #Table Frame
        
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=20, y=210, width=710, height=370)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div","dob", "roll","gender", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No.")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="D.O.B.")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No.")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher Name")
        self.student_table.heading("photo", text="Photo sample status")
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
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)


        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()

        #------------------------------------------------------------------------------------------------------------#
    #function declaration
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required" , parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
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
                    self.var_photo.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Data has been inserted successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)


        #------------------------------------------------------------------------------------------------------------

    #fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    #------------------------------------------------------------------------------------------------------------#
    #get cursor
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_photo.set(data[14])


    #------------------------------------------------------------------------------------------------------------#
    #update function
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if Update:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = """UPDATE student SET 
                    dep=%s, course=%s, `year`=%s, semester=%s, student_name=%s, `div`=%s, 
                    roll_no=%s, gender=%s, dob=%s, email=%s, phone_no=%s, 
                    address=%s, teacher=%s, photo_sample=%s 
                    WHERE student_id=%s"""
                    
                    values = (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_photo.get(),
                        self.var_std_id.get(),
                    )

                    my_cursor.execute(sql, values)
                    conn.commit()
                    messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)  
                    self.fetch_data()  # Refresh data after updating
                    conn.close()
                else:
                    if not Update:
                        return      
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    #---------------------------------------------------------------------------------------------------------------#
    #delete function
    def delete_data(self):
        if not self.var_std_id.get():
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM student WHERE student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                    conn.commit()
                    conn.close()
                    self.fetch_data()
                    messagebox.showinfo("Delete", "Student details deleted successfully", parent=self.root)
                else:
                    if not delete:
                        return    
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    #---------------------------------------------------------------------------------------------------------------#
    #reset function
    def reset(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_photo.set("")

    #---------------------------------------------------------------------------------------------------------------#
    #generate dataset or take photo sample
    def generate_dataset(self):
        if self.var_dep.get("Select Department") or self.var_std_name.get()=="" or self.var_std_id().get()=="" :
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                my_result = my_cursor.fetchall()
                id = 0
                for i in my_result:
                    id += 1
                my_cursor.execute("update student set Dep = %s, Course = %s, Year = %s, Semester = %s, Name = %s, Division = %s, Roll_no = %s, Gender =%s, Dob =%s, Email =%s, Phone_no = %s, Address = %s, Teacher = %s, Photo_sample =%s where student_id = %s",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_photo.get(),
                    self.var_std_id.get() == id+1,
                ))
                conn.commit()
                self.fetch_data()
                self.reset()
                conn.close()

                #---------------------------------------------------------------------------------------------------------------#
                # load predefined data on face frontals from opencv
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                    
                cap = cv2.VdeoCapture(0)
                img_id = 0
                while True:
                    ret, myframe = cap.read()
                    if face_cropped(myframe) is not False:
                        img_id += 1
                    face = cv2.resize(face_cropped(myframe), (450,450)) 
                    face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)   
                    file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path, face)
                    cv2.putText(face,str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) ==100:
                        break

                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result","Generating data sets completed successfully....")
            except Exception as e:
                messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root)





if __name__ == "__main__":  
    root = Tk()
    obj = Student_mamagement_system(root)
    root.mainloop()
    




