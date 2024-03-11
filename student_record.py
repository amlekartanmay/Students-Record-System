from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter

class LibrayManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Record System")
        self.root.geometry("1440x700+0+0")

        #========================================Variablr==================================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.title_var=StringVar()
        self.firstname_var=StringVar()
        self.middlename_var=StringVar()
        self.lastname_var=StringVar()
        self.address_var=StringVar()
        self.phno_var=StringVar()
        self.department_var=StringVar()

        lbltitle=Label(self.root,text="STUDENT RECORD SYSTEM",bg="orange",fg="black",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=14,relief=RIDGE,padx=22,bg="red")
        frame.place(x=0,y=128,width=1360,height=360)

        #===============================================DF left===================================================
        DataFrameLeft=LabelFrame(self.root,text="Student Information",bg="orange",fg="black",bd=20,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=16,y=145,width=900,height=325)

        lblMamber=Label(DataFrameLeft,text="Member Type",bg="orange",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMamber.grid(row=0, column=0, sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.member_var,width=27,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer","Non Teaching-Staff")
        comMember.grid(row=0, column=1)

        lblPRN_No=Label(DataFrameLeft,text="PRN No :",bg="orange",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.prn_var,width=29)
        txtPRN_No.grid(row=1, column=1)

        lblTitle=Label(DataFrameLeft,text="Title :",bg="orange",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.title_var,width=29)
        txtTitle.grid(row=2, column=1)

        lblFirstName=Label(DataFrameLeft,text="First Name :",bg="orange",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3, column=1)

        lbLMiddleName=Label(DataFrameLeft,text="Middle Name :",bg="orange",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbLMiddleName.grid(row=3, column=2, sticky=W)
        txLMiddleName=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.middlename_var,width=29)
        txLMiddleName.grid(row=3, column=4)

        lblLastName=Label(DataFrameLeft,text="Last Name :",bg="orange",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4, column=1)

        lblAddress=Label(DataFrameLeft,text="Address :",bg="orange",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress.grid(row=5, column=0, sticky=W)
        txtAddress=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.address_var,width=29)
        txtAddress.grid(row=5, column=1)

        lblPHno=Label(DataFrameLeft,text="PH.No :",bg="orange",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPHno.grid(row=6, column=0, sticky=W)
        txtPHno=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.phno_var,width=29)
        txtPHno.grid(row=6, column=1)
        
        lblDept=Label(DataFrameLeft,text="Department :",bg="orange",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDept.grid(row=7, column=0, sticky=W)
        txtDept=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.department_var,width=29)
        txtDept.grid(row=7, column=1)

        #==================================================DAta Frame R==============================================
        
        DataFrameRight=LabelFrame(self.root,text="Student Details",bg="orange",fg="black",bd=20,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=920,y=145,width=420,height=325)

        self.txtBox=Text(DataFrameRight,font=("times new roman",12,"bold"),width=40,height=12,padx=6,pady=6)
        self.txtBox.grid(row=0,column=2)

        '''listScrollBar=Scrollbar(DataFrameRight)
        listScrollBar.grid(row=0,column=1,sticky='ns')

        listBooks=["Applied Mathematices","Java Programming","Python Programming","Database Management System","System Programming","Artificial Inteligence"
                   ,"Theory of Computation","Operating System","HTML","DM&GT","Computer Architecture","Applied Mathematices VBD"
                   ,"Java Programming VBD","Database Management System VBD","Python Programming VBD","Theory of Computation VBD"
                   ,"Operating System VBD","Computer Architecture VBD"]
        

        listBox=Listbox(DataFrameRight,font=("times new roman",12,"bold"),width=15,height=12)
        listBox.grid(row=0,column=0,padx=4)
        listScrollBar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)'''
        
        # =================================================Button Frame=============================================
        framebutton=Frame(self.root,bd=14,relief=RIDGE,padx=22,bg="green")
        framebutton.place(x=0,y=488,width=1360,height=65)

        btnAddData=Button(framebutton,command=self.add_data,text="ADD DATA",font=("times new roman",12,"bold"),width=15,bg="yellow",fg="black",padx=35,pady=2)
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(framebutton,text="SHOW DATA",font=("times new roman",12,"bold"),command=self.showData,width=15,bg="yellow",fg="black",padx=35,pady=2)
        btnAddData.grid(row=0,column=5)

        btnAddData=Button(framebutton,text="UPDATE",font=("times new roman",12,"bold"),command=self.update,width=15,bg="yellow",fg="black",padx=35,pady=2)
        btnAddData.grid(row=0,column=10)

        btnAddData=Button(framebutton,text="DELETE",font=("times new roman",12,"bold"),command=self.delete,width=15,bg="yellow",fg="black",padx=35,pady=2)
        btnAddData.grid(row=0,column=15)

        btnAddData=Button(framebutton,text="RESET",font=("times new roman",12,"bold"),command=self.reset,width=15,bg="yellow",fg="black",padx=35,pady=2)
        btnAddData.grid(row=0,column=20)

        btnAddData=Button(framebutton,text="EXIT",font=("times new roman",12,"bold"),command=self.iExit,width=15,bg="yellow",fg="black",padx=35,pady=2)
        btnAddData.grid(row=0,column=25)



        #==================================================Info======================================================
        frameDetails=Frame(self.root,bd=14,relief=RIDGE,padx=22,bg="gray")
        frameDetails.place(x=0,y=553,width=1360,height=140)

        Table_frame=Frame(frameDetails,bd=6,relief=RIDGE,bg="gray")
        Table_frame.place(x=0,y=0,width=1300,height=130)

        xscrollbar=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscrollbar=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","middlename","lastname"
                                                            ,"address","phno","department"),xscrollcommand=xscrollbar.set,yscrollcommand=yscrollbar.set)
        xscrollbar.pack(side=BOTTOM,fill=X)
        yscrollbar.pack(side=RIGHT,fill=Y)

        xscrollbar.config(command=self.library_table.xview)
        yscrollbar.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="MEMBER TYPE")
        self.library_table.heading("prnno",text="PRN.NO")
        self.library_table.heading("title",text="TITLE OF STUDENT")
        self.library_table.heading("firstname",text="NAME")
        self.library_table.heading("middlename",text="MIDDLE NAME")
        self.library_table.heading("lastname",text="SURNAME")
        self.library_table.heading("address",text="ADDRESS")
        self.library_table.heading("phno",text="PHONE NO.")
        self.library_table.heading("department",text="DEPARTMENT")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("middlename",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address",width=100)
        self.library_table.column("phno",width=100)
        self.library_table.column("department",width=100)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Tanmay@135",database="tanmayamlekardb")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,Title=%s,Name=%s,Middle_Name=%s,Surname=%s,Address=%s,Phone_No=%s,Department=%s where PRN_No=%s",(
                                                                                                                                                            self.member_var.get(),
                                                                                                                                                            self.title_var.get(),
                                                                                                                                                            self.firstname_var.get(),
                                                                                                                                                            self.middlename_var.get(),
                                                                                                                                                            self.lastname_var.get(),
                                                                                                                                                            self.address_var.get(),
                                                                                                                                                            self.phno_var.get(),
                                                                                                                                                            self.department_var.get(),
                                                                                                                                                            self.prn_var.get(),
                                                                                                                                                      ))
        
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Updation Completed")
    
    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Tanmay@135",database="tanmayamlekardb")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                     self.member_var.get(),
                                                                                     self.prn_var.get(),
                                                                                     self.title_var.get(),
                                                                                     self.firstname_var.get(),
                                                                                     self.middlename_var.get(),
                                                                                     self.lastname_var.get(),
                                                                                     self.address_var.get(),
                                                                                     self.phno_var.get(),
                                                                                     self.department_var.get()
                                                                                   ))
        conn.commit()
        self.fatch_data()
        conn.close()

        messagebox.showinfo("Successful","Data Entered Successfully")

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Tanmay@135",database="tanmayamlekardb")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * From Library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content["values"]

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.title_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.middlename_var.set(row[4]),
        self.lastname_var.set(row[5]),
        self.address_var.set(row[6]),
        self.phno_var.set(row[7]),
        self.department_var.set(row[8])

    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END,"Prn no:\t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END,"Tiltle:\t\t"+ self.title_var.get() + "\n")
        self.txtBox.insert(END,"Name:\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"Middle Name:\t\t"+ self.middlename_var.get() + "\n")
        self.txtBox.insert(END,"Surname:\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"Address:\t\t"+ self.address_var.get() + "\n")
        self.txtBox.insert(END,"Phone no:\t\t"+ self.phno_var.get() + "\n")
        self.txtBox.insert(END,"Department:\t\t"+ self.department_var.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.title_var.set(""),
        self.firstname_var.set(""),
        self.middlename_var.set(""),
        self.lastname_var.set(""),
        self.address_var.set(""),
        self.phno_var.set(""),
        self.department_var.set("")
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to Exit")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.prn_var.get()=="":
             messagebox.showerror("Error","First Select Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Tanmay@135",database="tanmayamlekardb")
            my_cursor=conn.cursor()
            query="delete from library where PRN_No=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("success","Member is Deleted")


    

        








if __name__ == "__main__":
    root=Tk()
    obj=LibrayManagementSystem(root)
    root.mainloop()