from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk   #pip install pillow
import mysql.connector
from tkinter import messagebox

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")

        #variables (to store data in my sql data-base)
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_ID = StringVar()
        self.var_name = StringVar()
        self.var_section = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_mobile = StringVar()
        self.var_address = StringVar()


        #1st Image
        img_1 = Image.open(r"college_images\IIT_1.jpg")
        img_1 = img_1.resize((280,160),Image.ANTIALIAS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        self.btn_1 = Button(self.root,image=self.photoimg_1,cursor="hand2")
        self.btn_1.place(x=0,y=0,width=540,height=160)

        #2nd Image
        img_2 = Image.open(r"college_images\IIT_2.jpg")
        img_2 = img_2.resize((200,160),Image.ANTIALIAS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        self.btn_2 = Button(self.root,image=self.photoimg_2,cursor="hand2")
        self.btn_2.place(x=400,y=0,width=540,height=160)

        #3rd Image
        img_3 = Image.open(r"college_images\IIT_3.jpg")
        img_3 = img_3.resize((400,160),Image.ANTIALIAS)
        self.photoimg_3 = ImageTk.PhotoImage(img_3)

        self.btn_3 = Button(self.root,image=self.photoimg_3,cursor="hand2")
        self.btn_3.place(x=800,y=0,width=540,height=160)


        #bACKGROUND IMAGE
        img_4 = Image.open(r"college_images\university.jpg")
        img_4 = img_4.resize((1300,500), Image.ANTIALIAS)
        self.photoimg_4 = ImageTk.PhotoImage(img_4)

        bg_lbl = Label(self.root,image=self.photoimg_4,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=160,width=1300,height=500)

        lbl_title = Label(bg_lbl,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",37,"bold"),fg="gray",bg="white")
        lbl_title.place(x=0,y=0,width=1300,height=40)

        #manage_frame
        Manage_frame = Frame(bg_lbl,bd=2,relief=RIDGE,bg="white")
        Manage_frame.place(x=0,y=40,width=1300,height=500)

        #left frame
        DataLeftFrame = LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Enter Student Data",
                                   font=("times new roman",17,"bold"),fg="red",bg="white")
        DataLeftFrame.place(x=5,y=5,width=500,height=435)

        #right_frame
        DataRightFrame = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2, text="View Student Information",
                                   font=("times new roman", 17, "bold"), fg="red", bg="white")
        DataRightFrame.place(x=505, y=5, width=750, height=435)

        #Current course label frame information
        std_lbl_info_frame = LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Current Course Information",
                                   font=("times new roman",15,"bold"),fg="black",bg="white")
        std_lbl_info_frame.place(x=0,y=5,width=430,height=120)


    #labels and combobox
    #department

        lbl_dep = Label(std_lbl_info_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep = ttk.Combobox(std_lbl_info_frame,textvariable=self.var_dep,font=("arial",10,"bold"),width=13,state="readonly")
        combo_dep["value"]=("Select Deptartment","Civil","Computer Science","Electronics","Electricals","Information Technology","Mechanical")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)


    # course

        course_std = Label(std_lbl_info_frame, text="Courses:", font=("times new roman", 12, "bold"), bg="white")
        course_std.grid(row=0, column=2, padx=2,pady=10, sticky=W)

        com_txtcourse_std = ttk.Combobox(std_lbl_info_frame,textvariable=self.var_course, font=("arial", 10, "bold"), width=13, state="readonly")
        com_txtcourse_std["value"] = ("Select Course", "B.Tech", "M.Tech", "Phd", "M.Sc.", "M.A.","Internship")
        com_txtcourse_std.current(0)
        com_txtcourse_std.grid(row=0, column=3, padx=2, pady=10, sticky=W)


    # year

        current_year = Label(std_lbl_info_frame, text="Year:", font=("times new roman", 12, "bold"), bg="white")
        current_year.grid(row=1, column=0, padx=2,pady=10, sticky=W)

        com_txt_current_year = ttk.Combobox(std_lbl_info_frame,textvariable=self.var_year, font=("arial", 10, "bold"), width=13, state="readonly")
        com_txt_current_year["value"] = ("Select Year", "1st Year", "2nd year", "3rd year", "4th year", "5th year")
        com_txt_current_year.current(0)
        com_txt_current_year.grid(row=1, column=1, padx=2, sticky=W)

    # semester

        label_semester = Label(std_lbl_info_frame, text="Semester:", font=("times new roman", 12, "bold"), bg="white")
        label_semester.grid(row=1, column=2, padx=2,pady=10, sticky=W)

        com_semester = ttk.Combobox(std_lbl_info_frame,textvariable=self.var_sem, font=("arial", 10, "bold"), width=13, state="readonly")
        com_semester["value"] = ("Select Semester", "1st sem", "2nd sem", "3rd sem", "4th sem", "5th sem", "6th sem",
                             "7th sem", "8th sem")
        com_semester.current(0)
        com_semester.grid(row=1, column=3, padx=2,pady=10, sticky=W)

    # student class labelframe information (class course information)
        std_lbl_class_frame = LabelFrame(DataLeftFrame, bd=4, relief=RIDGE, padx=2, text="Personal Information",
                               font=("times new roman", 15, "bold"), fg="black", bg="white")
        std_lbl_class_frame.place(x=0, y=130, width=490, height=225)

    #labels entry
    # ID
        lbl_id = Label(std_lbl_class_frame, text="Stud-ID:", font=("times new roman", 12, "bold"), bg="white")
        lbl_id.grid(row=0, column=0, padx=2, pady=7, sticky=W)

        id_entry = ttk.Entry(std_lbl_class_frame,textvariable=self.var_ID,font=("times new roman",12),width=20)
        id_entry.grid(row=0,column=1,sticky=W,padx=2,pady=7)

    # Name
        lbl_Name = Label(std_lbl_class_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white")
        lbl_Name.grid(row=0, column=2, padx=2, pady=7, sticky=W)

        txt_name = ttk.Entry(std_lbl_class_frame,textvariable=self.var_name,font=("times new roman",12),width=20)
        txt_name.grid(row=0,column=3,sticky=W,padx=2,pady=7)

    # Section
        lbl_Section = Label(std_lbl_class_frame, text="Section:", font=("times new roman", 12, "bold"), bg="white")
        lbl_Section.grid(row=1, column=0, padx=2, pady=7, sticky=W)

        com_txt_sec = ttk.Combobox(std_lbl_class_frame,textvariable=self.var_section, font=("arial", 10, "bold"), width=20, state="readonly")
        com_txt_sec["value"] = ("Select Section","A","B","C")
        com_txt_sec.current(0)
        com_txt_sec.grid(row=1, column=1, padx=2,pady=7, sticky=W)

    # Roll no
        lbl_Roll = Label(std_lbl_class_frame, text="Roll-No:", font=("times new roman", 12, "bold"), bg="white")
        lbl_Roll.grid(row=1, column=2, padx=2, pady=7, sticky=W)

        txt_Roll = ttk.Entry(std_lbl_class_frame,textvariable=self.var_roll, font=("times new roman", 12), width=20)
        txt_Roll.grid(row=1, column=3, sticky=W, padx=2, pady=7)

    # gender
        lbl_gender = Label(std_lbl_class_frame, text="Gender:", font=("times new roman", 12, "bold"), bg="white")
        lbl_gender.grid(row=2, column=0, padx=2, pady=7, sticky=W)

        com_txt_gender = ttk.Combobox(std_lbl_class_frame,textvariable=self.var_gender, font=("arial", 10, "bold"), width=20, state="readonly")
        com_txt_gender["value"] = ("Select Gender","Male","Female","Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=2, column=1, padx=2, pady=7, sticky=W)

    # DOB
        lbl_DOB = Label(std_lbl_class_frame, text="DOB:", font=("times new roman", 12, "bold"), bg="white")
        lbl_DOB.grid(row=2, column=2, padx=2, pady=7, sticky=W)

        txt_DOB = ttk.Entry(std_lbl_class_frame,textvariable=self.var_dob, font=("times new roman", 12), width=20)
        txt_DOB.grid(row=2, column=3, sticky=W, padx=2, pady=7)


    # Email
        lbl_email = Label(std_lbl_class_frame, text="E-Mail:", font=("times new roman", 12, "bold"), bg="white")
        lbl_email.grid(row=3, column=0, padx=2, pady=7, sticky=W)

        txt_email = ttk.Entry(std_lbl_class_frame,textvariable=self.var_email, font=("times new roman", 12), width=20)
        txt_email.grid(row=3, column=1, sticky=W, padx=2, pady=7)


    # Mobile
        lbl_mobile = Label(std_lbl_class_frame, text="Mobile:", font=("times new roman", 12, "bold"), bg="white")
        lbl_mobile.grid(row=3, column=2, padx=2, pady=7, sticky=W)

        txt_mobile = ttk.Entry(std_lbl_class_frame,textvariable=self.var_mobile, font=("times new roman", 12), width=20)
        txt_mobile.grid(row=3, column=3, sticky=W, padx=2, pady=7)


    # Address
        lbl_address = Label(std_lbl_class_frame, text="Address:", font=("times new roman", 12, "bold"), bg="white")
        lbl_address.grid(row=4, column=0, padx=2, pady=7, sticky=W)

        txt_address = ttk.Entry(std_lbl_class_frame,textvariable=self.var_address, font=("times new roman", 12), width=20)
        txt_address.grid(row=4, column=1, sticky=W, padx=2, pady=7)

        #button frame
        button_frame = Frame(DataLeftFrame, bd=2, relief=RIDGE, bg="white")
        button_frame.place(x=0, y=355, width=490, height=50)

        btn_add = Button(button_frame,text="Save",command=self.add_data,font=("times new roman",13,"bold"),width=10,bg="navy blue",fg="white")
        btn_add.grid(row=0,column=0,sticky=W,padx=5)

        btn_update = Button(button_frame, text="Update",command=self.update_data, font=("times new roman", 13, "bold"), width=10, bg="navy blue",
                         fg="white")
        btn_update.grid(row=0, column=1, sticky=W, padx=5)

        btn_delete = Button(button_frame, text="Delete",command=self.delete_data, font=("times new roman", 13, "bold"), width=10, bg="navy blue",
                         fg="white")
        btn_delete.grid(row=0, column=2, sticky=W, padx=5)

        btn_reset = Button(button_frame, text="Reset",command=self.reset_data, font=("times new roman", 13, "bold"), width=10, bg="navy blue",
                         fg="white")
        btn_reset.grid(row=0, column=3, sticky=W, padx=5)



        #right_frame (View Student Details and search system)
        Search_Frame = LabelFrame(DataRightFrame, bd=4, relief=RIDGE, padx=2, text="Search Student Details",
                                   font=("times new roman", 15, "bold"), fg="black", bg="white")
        Search_Frame.place(x=15, y=5, width=710, height=80)


        search_by = Label(Search_Frame, text="Search by:", font=("times new roman", 12, "bold"), bg="red")
        search_by.grid(row=0, column=0, padx=2, pady=7, sticky=W)

        #search
        self.var_com_search = StringVar()
        com_txt_search = ttk.Combobox(Search_Frame, textvariable=self.var_com_search, font=("arial", 10, "bold"), width=20, state="readonly")
        com_txt_search["value"] = ("Select option","Roll no","Mobile","ID")
        com_txt_search.current(0)
        com_txt_search.grid(row=0, column=1, padx=5, sticky=W)

        self.var_search=StringVar()
        txt_search = ttk.Entry(Search_Frame, textvariable=self.var_search, font=("times new roman", 12), width=20)
        txt_search.grid(row=0, column=2, sticky=W, padx=2, pady=7)

        btn_search = Button(Search_Frame, command=self.search_data, text="Search", font=("times new roman", 13, "bold"), width=8, bg="navy blue",
                         fg="white")
        btn_search.grid(row=0, column=3, sticky=W, padx=5)

        btn_show_all = Button(Search_Frame,command=self.fetch_data, text="Show all", font=("times new roman", 13, "bold"), width=8, bg="navy blue",
                         fg="white")
        btn_show_all.grid(row=0, column=4, sticky=W, padx=5)

        # ==================Student Table and scroll bar============================================================

        table_frame = Frame(DataRightFrame,bd=4,relief=RIDGE)
        table_frame.place(x=4,y=100,width=730,height=300)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,columns=("Department","Course","Year","Semester","ID",
                                                               "Name","Section","Roll-No","Gender","DOB","E-Mail","Mobile",
                                                               "Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Section",text="Section")
        self.student_table.heading("Roll-No",text="Roll-No")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("E-Mail",text="E-Mail")
        self.student_table.heading("Mobile",text="Mobile")
        self.student_table.heading("Address",text="Address")

        self.student_table["show"] = "headings"

        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Section",width=100)
        self.student_table.column("Roll-No",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("E-Mail",width=100)
        self.student_table.column("Mobile",width=100)
        self.student_table.column("Address",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    # function to add data to mysql============================================================================

    def add_data(self):
        if (self.var_dep.get()==""or self.var_email.get()=="" or self.var_ID.get()=="" ):
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Saket@1965",database="mydata")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_ID.get(),
                    self.var_name.get(),
                    self.var_section.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_mobile.get(),
                    self.var_address.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student has been added!",parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent = self.root)

    #fetch function
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Saket@1965", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # get cursor
    def get_cursor(self,event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_ID.set(data[4])
        self.var_name.set(data[5])
        self.var_section.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_mobile.set(data[11])
        self.var_address.set(data[12])

    #update
    def update_data(self):
        if (self.var_dep.get()==""or self.var_email.get()=="" or self.var_ID.get()=="" ):
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure to update this data",parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Saket@1965", database="mydata")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set dep=%s, course=%s, year=%s, sem=%s, name=%s, section=%s,"
                                      " roll=%s, gender=%s, dob=%s, email=%s, mobile=%s, address=%s where ID = %s",
                    (self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_name.get(),
                    self.var_section.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_mobile.get(),
                    self.var_address.get(),
                    self.var_ID.get()  ))

                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success","Student Successfully updated",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent = self.root)

    #delete
    def delete_data(self):
        if self.var_ID.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete","Are you sure to delete this student data",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Saket@1965", database="mydata")
                    my_cursor = conn.cursor()
                    sql = "delete from student where ID = %s"
                    value = (self.var_ID.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student data has been deleted",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent = self.root)

    #reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_ID.set("")
        self.var_name.set("")
        self.var_section.set("Select Section")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_mobile.set("")
        self.var_address.set("")

    #search
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get() == "":
            messagebox.showerror("Error","Please select option")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Saket@1965",
                                               database="mydata")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student where " +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent = self.root)



if __name__ == "__main__":
    root = Tk()
    obj=Student(root)
    root.mainloop()