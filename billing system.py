from tkinter import *
from tkinter import ttk
import random
from datetime import datetime
from tkinter import messagebox
import sys

def main():
    win=Tk()
    app=LoginPage(win)
    win.mainloop()

class LoginPage:
    def __init__(self,win):
        self.win=win
        self.win.geometry("1350x750+0+0")
        self.win.title("Billing System")

        self.title_label = Label(self.win,text="Billing System",font=('Arial',35,'bold'),bg="pink",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)

        self.main_frame= Frame(self.win,bg="pink",bd=6,relief=GROOVE)
        self.main_frame.place(x=250,y=150,width=800,height=450)

        self.login_lbl= Label(self.main_frame,text="Login",bd=6,relief=GROOVE,anchor=CENTER,bg="powderblue",font=("times new roman",25,"bold"))
        self.login_lbl.pack(side=TOP,fill=X)

        self.entry_frame= LabelFrame(self.main_frame,text="Enter details",bd=6,relief=GROOVE,bg="powderblue",font=("times newroman",18))
        self.entry_frame.pack(fill=BOTH,expand=TRUE)

        self.entus_lbl= Label(self.entry_frame,text="Enter username:",bg="powderblue",font=("times new roman",15))
        self.entus_lbl.grid(row=0,column=0,padx=2,pady=2)

        #==========varaibles==========
        username=StringVar()
        password=StringVar()
        #============================
        self.entus_ent=Entry(self.entry_frame,font=('times new roman',15),bd=6,textvariable=username)
        self.entus_ent.grid(row=0,column=1,padx=2,pady=2)

        self.entus_lbl= Label(self.entry_frame,text="Enter password:",bg="powderblue",font=("times new roman",15))
        self.entus_lbl.grid(row=1,column=0,padx=2,pady=2)

        self.entus_ent=Entry(self.entry_frame,font=("times new roman",15),bd=6,textvariable=password)
        self.entus_ent.grid(row=1,column=1,padx=2,pady=2)
        #==========functions==========

        def check_login():
            '''this function will check login'''
            if username.get()=="suhani"and password.get()=="187":
                self.billing_btn.config(state="normal")
            else:
                pass #----->message box

        def reset():
            username.set("")
            password.set("")

        def billing_sect():
            self.newwindow=Toplevel(self.win)
            self.app= Window2(self.newwindow)


        #==========buttons============

        self.button_frame=LabelFrame(self.entry_frame,text="Options",font=("arial,15"),bg="powderblue",bd=7,relief=GROOVE)
        self.button_frame.place(x=20,y=100,width=730,height=85)

        self.login_btn=Button(self.button_frame,text="Login",font=("arial",15),bd=5,width=15,command=check_login)
        self.login_btn.grid(row=0,column=0,padx=20,pady=2)

        self.billing_btn=Button(self.button_frame,text="Billing",font=("arial",15),bd=5,width=15,command=billing_sect)
        self.billing_btn.grid(row=0,column=1,padx=20,pady=2)
        self.billing_btn.config(state="disabled")

        self.reset_btn=Button(self.button_frame,text="Reset",font=("arial",15),bd=5,width=15,command=reset)
        self.reset_btn.grid(row=0,column=2,padx=20,pady=2)

class Window2:
    def __init__(self,win):
        self.win=win
        self.win.geometry("1350x750+0+0")
        self.win.title("Billing System")

        self.title_label = Label(self.win,text="Billing System",font=('Arial',35,'bold'),bg="pink",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)

        #=======variables======
        bill_no=random.randint(100,9999)
        bill_no_tk=IntVar()
        bill_no_tk.set(bill_no)
        
        calc_var=StringVar()

        cust_nm=StringVar()
        cust_cot=StringVar()
        date_pr = StringVar()
        item_pur=StringVar()
        item_qty=StringVar()
        cone=StringVar()

        date_pr.set(datetime.now())

        #=========ENTRY=========

        self.entry_frame=LabelFrame(self.win,text="Enter Details",background="powderblue",font=("arial",20),bd=7,relief=GROOVE)
        self.entry_frame.place(x=20,y=95,width=500,height=650)

        self.bill_no_lbl=Label(self.entry_frame,text="Bill Number ",font=("arial",15),bg='powderblue')
        self.bill_no_lbl.grid(row=0,column=0,padx=2,pady=2)

        self.bill_no_ent=Entry(self.entry_frame,bd=5,font=("arial,15"),textvariable=bill_no_tk)
        self.bill_no_ent.grid(row=0,column=1,padx=2,pady=2)
        

        self.cust_nm_lbl=Label(self.entry_frame,text="Customer name",font=("arial",15),bg='powderblue')
        self.cust_nm_lbl.grid(row=1,column=0,padx=2,pady=2)

        self.cust_nm_lbl_no_ent=Entry(self.entry_frame,bd=5,textvariable=cust_nm,font=("arial,15"))
        self.cust_nm_lbl_no_ent.grid(row=1,column=1,padx=2,pady=2)

        self.cust_cont_lbl=Label(self.entry_frame,text="Customer contact  ",font=("arial",15),bg='powderblue')
        self.cust_cont_lbl.grid(row=2,column=0,padx=2,pady=2)

        self.cust_cont_lbl_no_ent=Entry(self.entry_frame,bd=5,textvariable=cust_cot,font=("arial,15"))
        self.cust_cont_lbl_no_ent.grid(row=2,column=1,padx=2,pady=2)

        self.date_lbl=Label(self.entry_frame,text="Date ",font=("arial",15),bg='powderblue')
        self.date_lbl.grid(row=3,column=0,padx=2,pady=2)

        self.date_ent=Entry(self.entry_frame,bd=5,textvariable=date_pr,font=("arial,15"))
        self.date_ent.grid(row=3,column=1,padx=2,pady=2)

        self.item_pur_lbl=Label(self.entry_frame,text="Item purchased ",font=("arial",15),bg='powderblue')
        self.item_pur_lbl.grid(row=4,column=0,padx=2,pady=2)

        self.item_pur_ent=Entry(self.entry_frame,bd=5,textvariable=item_pur,font=("arial,15"))
        self.item_pur_ent.grid(row=4,column=1,padx=2,pady=2)

        self.item_qty_lbl=Label(self.entry_frame,text="Item quantity ",font=("arial",15),bg='powderblue')
        self.item_qty_lbl.grid(row=5,column=0,padx=2,pady=2)

        self.item_qty_ent=Entry(self.entry_frame,bd=5,textvariable=item_qty,font=("arial,15"))
        self.item_qty_ent.grid(row=5,column=1,padx=2,pady=2)

        self.cost_one_lbl=Label(self.entry_frame,text="Cost of one ",font=("arial",15),bg='powderblue')
        self.cost_one_lbl.grid(row=6,column=0,padx=2,pady=2)

        self.cost_one_ent=Entry(self.entry_frame,bd=5,textvariable=cone,font=("arial,15"))
        self.cost_one_ent.grid(row=6,column=1,padx=2,pady=2)
        #==========Functions=====

        total_list= []
        self.grd_total = 0

        def default_bill():
            self.bill_txt.insert(END,"\n\t\t\t\t S.D Mart")
            self.bill_txt.insert(END,"\n\t\t\t Sector 22 Market ,Chandigarh")
            self.bill_txt.insert(END,"\n\t\t\t\t Contact - 9876543219")
            self.bill_txt.insert(END,"\n============================================================================")
            self.bill_txt.insert(END,f"\nBill Number :{bill_no_tk.get()}")

        def genbill():
            if cust_nm.get() == "" or (cust_cot.get() == "" or len(cust_cot.get()) != 10):
                messagebox.showerror("Error!,Please enter all the fields correctly.")
            else:
                self.bill_txt.insert(END,f"\nCustomer Name:{cust_nm.get()}")
                self.bill_txt.insert(END,f"\nCustomer Contact :{cust_cot.get()}")
                self.bill_txt.insert(END,f"\nDate :{date_pr.get()}")
                self.bill_txt.insert(END,"\n============================================================================")
                self.bill_txt.insert(END,"\nProduct Name\t\t      Quantity     \t\t Per Cost\t\t      Total")
                self.bill_txt.insert(END,"\n============================================================================")

                self.add_btn.config(state="normal")
                self.total_btn.config(state="normal")
                self.save_btn.config(state="normal")
                

        
        def clear_func():
            cust_nm.set("")
            cust_cot.set("")
            item_pur.set("")
            item_qty.set("")
            cone.set("")

        def reset_func():
            total_list.clear()
            self.grd_total = 0
            self.add_btn.config(state="disabled")
            self.total_btn.config(state="disabled")
            self.save_btn.config(state="disabled")
            self.bill_txt.delete("1.0",END)
            default_bill()

        def add_func():
            if item_pur.get() == ""or item_qty.get() == "":
                messagebox.showerror("Error!,Please enter all the fields correctly.",parent=self.win)
            else:
                qty=int(item_qty.get())
                cones=int(cone.get())
                total=qty*cones
                total_list.append(total)
                self.bill_txt.insert(END,f"\n{item_pur.get()}\t\t      {item_qty.get()}\t\t        RS.{cone.get()}\t\t      Rs.{total}")

        def total_func():
            for item in total_list:
                self.grd_total=self.grd_total +item
            gst_rate=0.18
            gst_amount= self.grd_total*gst_rate
            total_with_gst = self.grd_total+gst_amount
            
            self.bill_txt.insert(END,"\n===========================================================================")
            self.bill_txt.insert(END,f"\n\t\t\t\t\t\t SubTotal:{self.grd_total}")
            self.bill_txt.insert(END,f"\n\t\t\t\t\t\t GST :({gst_rate*100}%:{gst_amount}")
            self.bill_txt.insert(END,f"\n\t\t\t\t\t\t Grand Total:{total_with_gst}")
            self.bill_txt.insert(END,"\n===========================================================================")

        def save_func():
            user_choice= messagebox.askyesno ("Confirm?",f"Do you want to save the bill{bill_no_tk.get()}",parent=self.win)
            if user_choice >0:
                self.bill_content = self.bill_txt.get("1.0",END)
                try:
                 con= open(f"{sys.path[0]}/bills/"+str(bill_no_tk.get())+".txt","w")
                except Exception as e:
                    messagebox.showerror("Error!",f"Error due to {e}")
                con.write(self.bill_content)
                con.close()
                messagebox.showinfo("Success!",f"Bill{bill_no_tk.get()} has been saved successfully!",parent=self.win)
            else:
                return
                                             
        
        #==========button=======

        self.button_frame=LabelFrame(self.entry_frame,bd=5,text= "Options",bg="pink",font=("arial",15))
        self.button_frame.place(x=20,y=280,width=430,height=300)

        self.add_btn=Button(self.button_frame,bd=2,text="Add",font=("arial,12"),width=10,height=3,command=add_func)
        self.add_btn.grid(row=0,column=0,padx=4,pady=2)

        self.generate_btn=Button(self.button_frame,bd=2,text="Generate",font=("arial,12"),width=10,height=3,command=genbill)
        self.generate_btn.grid(row=0,column=1,padx=4,pady=2)

        self.clear_btn=Button(self.button_frame,bd=2,text="Clear",font=("arial,12"),width=10,height=3,command=clear_func)
        self.clear_btn.grid(row=0,column=2,padx=4,pady=2)

        self.total_btn=Button(self.button_frame,bd=2,text="Total",font=("arial,12"),width=10,height=3,command=total_func)
        self.total_btn.grid(row=1,column=0,padx=4,pady=2)

        self.reset_btn=Button(self.button_frame,bd=2,text="Reset",font=("arial,12"),width=10,height=3,command=reset_func)
        self.reset_btn.grid(row=1,column=1,padx=4,pady=2)

        self.save_btn=Button(self.button_frame,bd=2,text="Save",font=("arial,12"),width=10,height=3,command=save_func)
        self.save_btn.grid(row=1,column=2,padx=4,pady=2)

        self.add_btn.config(state="disabled")
        self.total_btn.config(state="disabled")
        self.save_btn.config(state="disabled")

        

        #========calculator frame=======
        self.calc_frame=Frame(self.win,bd=3,background="powderblue",relief=GROOVE)
        self.calc_frame.place(x=550,y=100,width=690,height=340)

        self.num_ent=Entry(self.calc_frame,bd=15,background="powderblue",textvariable=calc_var,font=("arial",15),width=61,justify="right")
        self.num_ent.grid(row=0,column=0,columnspan=11)

        def press_btn(event):
            text = event.widget.cget("text")
            if text == "=":
                if calc_var.get().isdigit():
                    value=int(calc_var.get())
                else:
                    try:
                        value=eval(self.num_ent.get())
                    except:
                        print("ERROR")
                calc_var.set(value)
                self.num_ent.update()
            elif text == "C":
                calc_var.set(" ")
                self.num_ent.update()
            else:
                calc_var.set(calc_var.get() + text)
                self.num_ent.update()

        self.btn7=Button(self.calc_frame,bg="powderblue",text="7",bd=8,width=12,height=1,font=('arial',15))
        self.btn7.grid(row=2,column=0,padx=4,pady=2)
        self.btn7.bind("<Button-1>",press_btn)

        self.btn8=Button(self.calc_frame,bg="powderblue",text="8",bd=8,width=12,height=1,font=('arial',15))
        self.btn8.grid(row=2,column=1,padx=2,pady=2)
        self.btn8.bind("<Button-1>",press_btn)


        self.btn9=Button(self.calc_frame,bg="powderblue",text="9",bd=8,width=12,height=1,font=("arial",15))
        self.btn9.grid(row=2,column=2,padx=2,pady=2)
        self.btn9.bind("<Button-1>",press_btn)


        self.btnadd=Button(self.calc_frame,bg="powderblue",text="+",bd=8,width=12,height=1,font=('arial',15))
        self.btnadd.grid(row=2,column=3,padx=2,pady=2)
        self.btnadd.bind("<Button-1>",press_btn)


        self.btn4=Button(self.calc_frame,bg="powderblue",text="4",bd=8,width=12,height=1,font=('arial',15))
        self.btn4.grid(row=3,column=0,padx=4,pady=2)
        self.btn4.bind("<Button-1>",press_btn)


        self.btn5=Button(self.calc_frame,bg="powderblue",text="5",bd=8,width=12,height=1,font=('arial',15))
        self.btn5.grid(row=3,column=1,padx=2,pady=2)
        self.btn5.bind("<Button-1>",press_btn)


        self.btn6=Button(self.calc_frame,bg="powderblue",text="6",bd=8,width=12,height=1,font=("arial",15))
        self.btn6.grid(row=3,column=2,padx=2,pady=2)
        self.btn6.bind("<Button-1>",press_btn)


        self.btnsub=Button(self.calc_frame,bg="powderblue",text="-",bd=8,width=12,height=1,font=('arial',15))
        self.btnsub.grid(row=3,column=3,padx=2,pady=2)
        self.btnsub.bind("<Button-1>",press_btn)


        self.btn1=Button(self.calc_frame,bg="powderblue",text="1",bd=8,width=12,height=1,font=('arial',15))
        self.btn1.grid(row=4,column=0,padx=4,pady=2)
        self.btn1.bind("<Button-1>",press_btn)


        self.btn2=Button(self.calc_frame,bg="powderblue",text="2",bd=8,width=12,height=1,font=('arial',15))
        self.btn2.grid(row=4,column=1,padx=2,pady=2)
        self.btn2.bind("<Button-1>",press_btn)


        self.btn3=Button(self.calc_frame,bg="powderblue",text="3",bd=8,width=12,height=1,font=("arial",15))
        self.btn3.grid(row=4,column=2,padx=2,pady=2)
        self.btn3.bind("<Button-1>",press_btn)

        self.btnmul=Button(self.calc_frame,bg="powderblue",text="*",bd=8,width=12,height=1,font=('arial',15))
        self.btnmul.grid(row=4,column=3,padx=2,pady=2)
        self.btnmul.bind("<Button-1>",press_btn)

        self.btn0=Button(self.calc_frame,bg="powderblue",text="0",bd=8,width=12,height=1,font=('arial',15))
        self.btn0.grid(row=5,column=0,padx=4,pady=2)
        self.btn0.bind("<Button-1>",press_btn)

        self.btnpoint=Button(self.calc_frame,bg="powderblue",text=".",bd=8,width=12,height=1,font=('arial',15))
        self.btnpoint.grid(row=5,column=1,padx=2,pady=2)
        self.btnpoint.bind("<Button-1>",press_btn)

        self.btnequals =Button(self.calc_frame,bg="powderblue",text="=",bd=8,width=12,height=1,font=("arial",15))
        self.btnequals.grid(row=5,column=2,padx=2,pady=2)
        self.btnequals.bind("<Button-1>",press_btn)

        self.btndiv=Button(self.calc_frame,bg="powderblue",text="/",bd=8,width=12,height=1,font=('arial',15))
        self.btndiv.grid(row=5,column=3,padx=2,pady=2)
        self.btndiv.bind("<Button-1>",press_btn)

        self.btnclear=Button(self.calc_frame,bg="powderblue",text="C",bd=8,width=12,height=1,font=('arial',15))
        self.btnclear.grid(row=1,column=3,padx=2,pady=2)
        self.btnclear.bind("<Button-1>",press_btn)


        
        #=========Bill frame=======

        self.bill_frame=LabelFrame(self.win,text="Bill Area",font=('Arial',18),background="powderblue",bd=8,relief=GROOVE)
        self.bill_frame.place(x=590,y=450,width=650,height=295)

        self.y_scroll=Scrollbar(self.bill_frame,orient="vertical")
        self.bill_txt=Text(self.bill_frame,bg='white',yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command=self.bill_txt.yview) 
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.bill_txt.pack(fill=BOTH,expand=TRUE)

        default_bill()

        









        




















        

        
        
        


        



         


        


        



    

if __name__=="__main__":
    main()
