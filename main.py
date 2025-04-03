from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student_detail import Student_mamagement_system

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x600")
        self.root.title("Face Recognition System")

        # #1.Top image 
        # print("Loading background image...")
        # img = Image.open(r"C:\Users\AASHIMA\OneDrive\Desktop\Face Recognition System\images\background image.jpg")
        # img = img.resize((400,130))
        # self.photoimg = ImageTk.PhotoImage(img)

        # f_lbl = Label(self.root, image=self.photoimg)
        # f_lbl.place(x=0, y=0, width=400, height=130)

        # #2. Top image 
        # print("Loading second image...")
        # img1 = Image.open(r"C:\Users\AASHIMA\OneDrive\Desktop\Face Recognition System\images\Img_2.jpg")
        # img1 = img1.resize((800,130))
        # self.photoimg1 = ImageTk.PhotoImage(img1)

        # f_lbl = Label(self.root, image=self.photoimg1)
        # f_lbl.place(x=400, y=0, width=800, height=130)

        # #3. Top image 
        # print("Loading third image...")
        # img2 = Image.open(r"C:\Users\AASHIMA\OneDrive\Desktop\Face Recognition System\images\Img_7.jpg")
        # img2 = img2.resize((500,130))
        # self.photoimg2 = ImageTk.PhotoImage(img2)

        # f_lbl = Label(self.root, image=self.photoimg2)
        # f_lbl.place(x=1200, y=0, width=500, height=130) 

        #4. Background image
        print("Loading background image...")
        img3 = Image.open(r"C:\Users\AASHIMA\OneDrive\Desktop\Face Recognition System\images\Img_6_blurred.jpg")
        img3 = img3.resize((1600,830))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1600, height=830)

        #lable title
        title_lbl = Label(bg_img, text="FACE RECOGNITION SYSTEM SOFTWARE", font=("arial 20 bold", 40, "bold"), bg="sky blue", fg="white")
        title_lbl.place(x=-2, y=-5, width=1600, height=80)
# arial rounded mt bold
        #student details
        print("Loading student details image...")
        img4 = Image.open(r"C:\Users\AASHIMA\OneDrive\Desktop\Face Recognition System\images\student details.jpg")
        img4 = img4.resize((220,220))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, command=self.student_detail, cursor="hand2")
        b1.place(x=150, y=150, width=220, height=220)

        b1_1 = Button(bg_img, text="STUDENT'S DETAIL", command=self.student_detail, cursor="hand2", font=("arial 20 bold", 10, "bold"), bg="dark blue", fg="white")
        b1_1.place(x=150, y=350, width=220, height=40)

        #face detection
        print("Loading face detection image...")
        img5 = Image.open(r"C:\Users\AASHIMA\OneDrive\Desktop\Face Recognition System\images\face recognition system.jpg")
        img5 = img5.resize((220,220))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b1.place(x=520, y=150, width=220, height=220)

        b1_1 = Button(bg_img, text="FACE DETECTION", cursor="hand2", font=("arial 20 bold", 10, "bold"), bg="dark blue", fg="white")
        b1_1.place(x=520, y=350, width=220, height=40)

        #Attendance
        print("Loading attendance image...")
        img6 = Image.open(r"C:\Users\AASHIMA\OneDrive\Desktop\Face Recognition System\images\Img_9.jpg")
        img6 = img6.resize((220,220))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b1.place(x=900, y=150, width=220, height=220)

        b1_1 = Button(bg_img, text="ATTENDANCE", cursor="hand2", font=("arial 20 bold", 10, "bold"), bg="dark blue", fg="white")
        b1_1.place(x=900, y=350, width=220, height=40)

        #help desk
        print("Loading help desk image...")
        img7 = Image.open(r"C:\Users\AASHIMA\OneDrive\Desktop\Face Recognition System\images\Img_12.jpg")
        img7 = img7.resize((220,220))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b1.place(x=1300, y=150, width=220, height=220)

        b1_1 = Button(bg_img, text="HELP DESK", cursor="hand2", font=("arial 20 bold", 10, "bold"), bg="dark blue", fg="white")
        b1_1.place(x=1300, y=350, width=220, height=40)

        #train data
        print("Loading train data image...")
        img8 = Image.open(r"C:\Users\AASHIMA\OneDrive\Desktop\Face Recognition System\images\img_8.jpg")
        img8 = img8.resize((220,220))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2")
        b1.place(x=150, y=470, width=220, height=220)

        b1_1 = Button(bg_img, text="TRAIN DATA", cursor="hand2", font=("arial 20 bold", 10, "bold"), bg="dark blue", fg="white")
        b1_1.place(x=150, y=670, width=220, height=40)

        #photos
        print("Loading photos image...")
        img9 = Image.open(r"C:\Users\AASHIMA\OneDrive\Desktop\Face Recognition System\images\Img_5.jpg")
        img9 = img9.resize((220,220))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2")
        b1.place(x=520, y=470, width=220, height=220)

        b1_1 = Button(bg_img, text="PHOTOS", cursor="hand2", font=("arial 20 bold", 10, "bold"), bg="dark blue", fg="white")
        b1_1.place(x=520, y=670, width=220, height=40)

        #developer
        print("Loading developer image...")
        img10 = Image.open(r"C:\Users\AASHIMA\OneDrive\Desktop\Face Recognition System\images\Img_4.jpg")
        img10 = img10.resize((220,220))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b1.place(x=900, y=470, width=220, height=220)

        b1_1 = Button(bg_img, text="DEVELOPER", cursor="hand2", font=("arial 20 bold", 10, "bold"), bg="dark blue", fg="white")
        b1_1.place(x=900, y=670, width=220, height=40)

        #exit
        print("Loading exit image...")
        img11 = Image.open(r"C:\Users\AASHIMA\OneDrive\Desktop\Face Recognition System\images\Img_3.jpg")
        img11 = img11.resize((220,220))
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        b1.place(x=1300, y=470, width=220, height=220)

        b1_1 = Button(bg_img, text="EXIT", cursor="hand2", font=("arial 20 bold", 10, "bold"), bg="dark blue", fg="white")
        b1_1.place(x=1300, y=670, width=220, height=40)


    #function calling
    def student_detail(self):
        self.new_window = Toplevel(self.root)
        self.app = Student_mamagement_system(self.new_window)
        print("Student's details clicked!")

#main function
if __name__ == "__main__":  
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
    
