import tkinter
from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox

def main():
    win = Tk()
    app = LoginPage(win)
    win.mainloop()

class LoginPage:
    def __init__(self , win):
        self.win = win
        self.win.geometry("1350x750+0+0")
        self.win.title("Restaurant Management System")

        self.title_label = Label(self.win,text="Restaurant Management System",font=('Arial',35,'bold'),bg="lightblue",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)

        self.main_frame = Frame(self.win,bg="lightblue",bd=6,relief=GROOVE)
        self.main_frame.place(x=250,y=150,width=800,height=450)

        self.login_lbl = Label(self.main_frame,text="Login",bd=6,relief=GROOVE,anchor=CENTER, bg="lightblue",font=('Arial',20,'bold'))
        self.login_lbl.pack(side=TOP,fill=X)

        self.entry_frame = LabelFrame(self.main_frame,text="Enter Details",bd=6,relief=GROOVE,bg="lightblue",font=('Arial',18))
        self.entry_frame.pack(fill=BOTH,expand=True)

        self.entus_lbl = Label(self.entry_frame,text="Usernmae",bg="lightblue",font=('Arial',15))
        self.entus_lbl.grid(row=0,column=0,padx=2,pady=2)


        #________________Veriables______________________

        username = tkinter.StringVar()
        password = tkinter.StringVar()

        #_______________________________________________

        self.entus_ent = Entry(self.entry_frame,font=('Arial',15),bd=6,textvariable=username)
        self.entus_ent.grid(row=0,column=1,padx=2,pady=2)

        self.entpss_lbl = Label(self.entry_frame, text="password", bg="lightblue", font=('Arial', 15))
        self.entpss_lbl.grid(row=1, column=0, padx=2, pady=2)

        self.entpss_ent = Entry(self.entry_frame, font=('Arial', 15),bd=6,textvariable=password,show="*")
        self.entpss_ent.grid(row=1, column=1, padx=2, pady=2)

        #__________________________________________

        #_____________Function_____________________

        def check_login():

            if username.get() == "" and password.get() =="":
                self.biling_btn.config(state='normal')
            else:
                pass

        def reset():
            username.set("")
            password.set("")
            self.biling_btn.config(state="disabled")

        def biling_sect():
            self.newWindow = Toplevel(self.win)
            self.app = Window2(self.newWindow)




        #______________Button______________________

        self.button_frame = LabelFrame(self.entry_frame,text="Options",font=('Arial',15),bg="lightblue",bd=7,relief=GROOVE)
        self.button_frame.place(x=20,y=100,width=730,height=85)


        self.login_btn = Button(self.button_frame,text="Login",font=('Arial',12),bd=5,width=15,command=check_login)
        self.login_btn.grid(row=0,column=0,pady=2,padx=40)

        self.biling_btn = Button(self.button_frame, text="billing", font=('Arial', 12), bd=5, width=15,command=biling_sect)
        self.biling_btn.grid(row=0, column=1, pady=2, padx=40)
        self.biling_btn.config(state="disable")

        self.reset_btn = Button(self.button_frame, text="reset", font=('Arial', 12), bd=5, width=15,command=reset)
        self.reset_btn.grid(row=0, column=2, pady=2, padx=40)

        #___________________________________________



        class Window2:
            def __init__(self,win):
                self.win = win
                self.win.geometry("1350x750+0+0")
                self.win.title("Restaurant Management System")

                self.title_label = Label(self.win,text="Restaurant Management System",font=('Arial', 35, 'bold'),bg="lightblue", bd=8, relief=GROOVE)
                self.title_label.pack(side=TOP, fill=X)

                #____________________Veriable_________________#


                cust_nm = StringVar()
                cust_cot = StringVar()
                date_pr = StringVar()
                item_pr = StringVar()
                item_qnty = StringVar()
                cost_of = StringVar()

                date_pr.set(datetime.now())

                total_list = []
                self.grd_total = 0





                #_______________________________

                self.entry_frame = LabelFrame(self.win,text="Enter Deatails",background="lightblue",font=('Arial',20),bd=7,relief=GROOVE)
                self.entry_frame.place(x=20,y=95,width=500,height=650)

                self.bill_no_lbl = Label(self.entry_frame,text="Bill Number",font=('Arial',15),bg="lightblue")
                self.bill_no_lbl.grid(row=0,column=0,padx=2,pady=2)

                self.bill_no_ent = Entry(self.entry_frame,bd=5,textvariable=None,font=('Arial',15))
                self.bill_no_ent.grid(row=0,column=1,padx=2,pady=2)

                self.cust_nm_lgl = Label(self.entry_frame, text="Customer Name", font=('Arial', 15), bg="lightblue")
                self.cust_nm_lgl.grid(row=1, column=0, padx=2, pady=2)

                self.cust_nm_ent = Entry(self.entry_frame, bd=5, textvariable=cust_nm, font=('Arial', 15))
                self.cust_nm_ent.grid(row=1, column=1, padx=2, pady=2)

                self.cust_cot_lbl = Label(self.entry_frame, text="Customer contact", font=('Arial', 15), bg="lightblue")
                self.cust_cot_lbl.grid(row=2, column=0, padx=2, pady=2)

                self.cust_cot_ent = Entry(self.entry_frame, bd=5, textvariable=cust_cot, font=('Arial', 15))
                self.cust_cot_ent.grid(row=2, column=1, padx=2, pady=2)

                self.date_lbl = Label(self.entry_frame, text="Date", font=('Arial',15),bg="lightblue")
                self.date_lbl.grid(row=3,column=0,padx=2,pady=2)

                self.date_ent = Entry(self.entry_frame, bd=5,textvariable=date_pr,font=('Arial',15))
                self.date_ent.grid(row=3,column=1,padx=2,pady=2)

                self.item_pur_lbl = Label(self.entry_frame, text="Item purchased", font=('Arial', 15), bg="Lightblue")
                self.item_pur_lbl.grid(row=4,column=0,padx=2,pady=2)

                self.item_pur_ent = Entry(self.entry_frame, bd=5,textvariable=item_pr,font=('Arial',15))
                self.item_pur_ent.grid(row=4,column=1,padx=2,pady=2)


                self.item_qty_lbl = Label(self.entry_frame, text="Item Quantity", font=('Arial',15), bg="lightblue")
                self.item_qty_lbl.grid(row=5,column=0,padx=2,pady=2)

                self.item_Qty_ent = Entry(self.entry_frame, bd=5, textvariable=item_qnty,font=('Arial',15))
                self.item_Qty_ent.grid(row=5,column=1,padx=2,pady=2)

                self.cost_one_ldl = Label(self.entry_frame, text="Cost", font=('Arial',15), bg="Lightblue")
                self.cost_one_ldl.grid(row=6,column=0,padx=2,pady=2)

                self.cost_one_ent = Entry(self.entry_frame, bd=5, textvariable=cost_of, font=('Arial',15))
                self.cost_one_ent.grid(row=6,column=1,padx=2,pady=2)


                #_______________Function__________________


                def default_bill():
                    self.bill_text.insert(END,"\t\t\t\t        Restaurant Name")
                    self.bill_text.insert(END,"\n\t\t\t\t221,Baker Street,Londan,England")
                    self.bill_text.insert(END,"\n\t\t\t\t     Contact - 01234567891")
                    self.bill_text.insert(END,"\n===============================================================================================")


                def genbill():
                    self.bill_text.insert(END,f"Customer name: {cust_nm.get()}")
                    self.bill_text.insert(END,f"\nContact Number: {cust_cot.get()}")
                    self.bill_text.insert(END,f"\nDate: {date_pr.get()}")
                    self.bill_text.insert(END,"\n===============================================================================================")
                    self.bill_text.insert(END,"\nProduct Name\t\t      Quantity               \t\tPer Cost\t\t            Total")
                    self.bill_text.insert(END,"\n===============================================================================================")

                    self.add_btn.config(state="normal")
                    self.total_btn.config(state="normal")
                    self.save_btn.config(state="normal")



                def clear_fun():
                    cust_nm.set("")
                    cust_cot.set("")
                    item_pr.set("")
                    item_qnty.set("")
                    cost_of.set("")


                def reset_fun():
                    total_list.clear()
                    self.grd_total = 0
                    self.bill_text.delete("1.0",END)
                    default_bill()
                    self.add_btn.config(state="disabled")
                    self.total_btn.config(state="disabled")

                def add_func():
                    qnty = int(item_qnty.get())
                    cost = int(cost_of.get())
                    total =qnty*cost
                    total_list.append(total)
                    self.bill_text.insert(END,f"\n{item_pr.get()}\t\t        {item_qnty.get()}\t\t                 {cost_of.get()}\t\t               {total}")


                def total_func():
                    for item in total_list:
                        self.grd_total =self.grd_total + item
                    self.bill_text.insert(END,"\n===============================================================================================")
                    self.bill_text.insert(END,f"\t\t\t\t\t\t\t\t Grand Total: {self.grd_total}")
                    self.bill_text.insert(END,"\n===============================================================================================")










                #_________________________Button________________________________________________________

                self.button_frame = LabelFrame(self.entry_frame, font=('Arial', 15), bg="lightblue", bd=7, relief=GROOVE)
                self.button_frame.place(x=30, y=290, width=391, height=165)

                self.add_btn =Button(self.button_frame,text="Add",bd=3,font=('Arial',12),width=12,height=3,bg="lightgrey",command=add_func)
                self.add_btn.grid(row=0,column=0,pady=2,padx=3)

                self.cle_btn = Button(self.button_frame, text="Clear", bd=3, font=('Arial', 12), width=12, height=3,bg="lightgrey",command=clear_fun)
                self.cle_btn.grid(row=0, column=1, pady=2, padx=3)

                self.gener_btn = Button(self.button_frame, text="Generate", bd=3, font=('Arial', 12), width=12, height=3,bg="lightgrey",command=genbill)
                self.gener_btn.grid(row=0, column=2, pady=2, padx=3)

                self.res_btn = Button(self.button_frame, text="Reset", bd=3, font=('Arial', 12), width=12, height=3,bg="lightgrey",command=reset_fun)
                self.res_btn.grid(row=2, column=0, pady=2, padx=3)

                self.total_btn = Button(self.button_frame, text="Total", bd=3, font=('Arial', 12), width=12, height=3,bg="lightgrey",command=total_func)
                self.total_btn.grid(row=2, column=1, pady=2, padx=3)

                self.save_btn = Button(self.button_frame, text="Save Bill", bd=3, font=('Arial',12), width=12, height=3, bg="Lightgrey")
                self.save_btn.grid(row=2, column=2, pady=2, padx=3)

                self.add_btn.config(state="disabled")
                self.total_btn.config(state="disabled")
                self.save_btn.config(state="disabled")


                #________________________Calculator______________________________________________________

                self.calcu_frame = Frame(self.win,bg='Lightgrey',bd=9,relief=GROOVE)
                self.calcu_frame.place(x=540,y=95,width=800,height=295)

                self.num_cla_ent = Entry(self.calcu_frame, bd=5, textvariable=None,font=('Arial', 15),width=70)
                self.num_cla_ent.grid(row=0,column=0)


                #__________________________________Bill Area____________________________________


                self.bill_makig_frame = LabelFrame(self.win, text="Billing Area",font=('Arial',15),bd=7,relief=GROOVE)
                self.bill_makig_frame.place(x=540,y=400,width=800,height=320)

                self.y_scroll = Scrollbar(self.bill_makig_frame,orient="vertical")
                self.bill_text = Text(self.bill_makig_frame,bg="White",yscrollcommand=self.y_scroll.set)
                self.y_scroll.config(command=self.bill_text.yview)
                self.y_scroll.pack(side=RIGHT,fill=Y)
                self.bill_text.pack(fill=BOTH,expand=True)

                default_bill()


if __name__ == "__main__":
    main()
