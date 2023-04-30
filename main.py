from tkinter import *
import tkinter.messagebox as tkMessageBox
import tkinter.ttk as ttk
import csv
import os
import tkinter.messagebox
from tkinter.constants import SUNKEN
from PIL import Image,ImageTk

#ICON FOR ALL WINDOWS
root = Tk()
root.title("Pharmacy Management System")
image=Image.open("img.jpeg")
photo=ImageTk.PhotoImage(image)
root.iconphoto(True,photo)

#CANVAS FOR BG

def open___window():
    pycharm = Toplevel()
    pycharm.geometry("626x417")
    pycharm.resizable(0,0)
    pycharm.title("Feedback form")
    bg = ImageTk.PhotoImage(file='pharmpic.jpeg')

    camvas1 = Canvas(pycharm, width=626, height=417, bd=0, highlightthickness=0)
    camvas1.pack(fill='both', expand=True)
    camvas1.create_image(0, 0, image=bg, anchor='nw')

    form_entry = Entry(pycharm, font=('Times', 16), width=30, fg="black", bd=0)
    form_entry.pack()

    camvas1.create_window(40, 170, anchor='nw', window=form_entry)

    def kiki():
        xx= form_entry.get()
        if xx=="" :
            tkinter.messagebox.showerror("Not working?","Please leave a review")
        else:
            with open("review.txt","a") as f:
                f.write(f"{xx} \n")
                f.close()
            tkinter.messagebox.showinfo("Goodbye","Your response have been recorded \n Thank you~ ")

    camvas1.create_text(150, 100, text="FEEDBACK FORM ˙ᵕ˙", font=("Times",20,'underline'))
    camvas1.create_text(180, 130, text="tell us about your experience!", font=("Times",20))


    sub_btn =Button(pycharm, font=("Times", 16), text="Submit", width=8,fg="navy",command=kiki, bg='cadetblue', activebackground="deeppink", activeforeground="White")
    sub_btn_window = camvas1.create_window(230,350, anchor='nw', window=sub_btn)

    pycharm.mainloop()

#BUTTON FOR FORM IN MAIN WINDOW

btt=Button(root,bg="paleturquoise2",relief=SUNKEN,fg='navy blue',font=("Times",16 ),text="FORM", command=open___window)
btt.place(x=5,y=495,width=320)

#DESCRIPTION WINDOW


def open__window():
    root1 = Tk()
    root1.geometry("1500x1500")
    root1.title("Description Window")
    root1.resizable(0,0)


    ff = Frame(root1, bg="navy")
    ff.place(x=1, y=150, width=1500, height=450)

    def bts():
       er1=er.get()
       with open("pharmacy.csv","r") as fr:
           er_reader = csv.reader(fr)
           for line in er_reader:
               if er1==line[0]:
                   MedicineName = line[0]
                   Description = line[4]
                   tree1.insert("", 0, values=(MedicineName, Description))



    b1 = Button(root1, bg='lightblue2', fg='navy',text="DESCRIPTION", font=("Algerian", 35,'underline'), bd=20, command=bts, activebackground="steelblue", activeforeground="black")
    b1.pack(fill=X, side=TOP)
    bb2 = Button(root1, bg="paleturquoise", fg="navy", text="Cost calculator", font=("Times", 20), command=cc)
    bb2.place(x=800, y=680)

    scrollbary1 = Scrollbar(ff, orient=VERTICAL)
    scrollbarx1 = Scrollbar(ff, orient=HORIZONTAL)
    tree1 = ttk.Treeview(ff,
                         columns=("MedicineName", "Description"),
                         selectmode="extended", height=50, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)


    scrollbary1.config(command=tree1.yview)
    scrollbary1.pack(side=RIGHT, fill=Y)
    scrollbarx1.config(command=tree1.xview)
    scrollbarx1.pack(side=BOTTOM, fill=X)

    tree1.heading("#0", text="", anchor=W)
    tree1.heading('MedicineName', text="MedicineName")
    tree1.heading('Description', text="Description")
    tree1.column('#0', stretch=NO, width=0, anchor=W)
    tree1.column('MedicineName', stretch=NO, minwidth=150, width=150, anchor=W)
    tree1.column("Description", stretch=YES, minwidth=150, width=800, anchor=W)
    er=Entry(ff, width=100,font=("Times",16),bg="lightpink", fg='navy')
    er.pack(ipadx=10, padx= 10, pady=10)
    tree1.pack()

#STYLING SECOND TREEVIEW

    style1=ttk.Style(tree1)
    style1.theme_use('default')
    style1.configure('Treeview',font=('Times', 15),
                background='lightcyan1',
                foreground='navy blue',
                rowheight=25,
                fieldbackground='lightcyan',
                )

    style1.configure('Treeview.Heading', font=("Times", 14),
                    background='lightcyan2',
                    foreground='black',
                    rowheight=20)
    style1.map('Treeview',
              background=[('selected', 'deeppink')])


#BUTTON FOR DESCRIPTION IN FIRST WINDOW

btn0 = Button(root,bg="paleturquoise2",fg='navy blue', text="   Description   ",relief=SUNKEN,font=("Times",16
                                                                         ), command=open__window)
btn0.place(x=377,y=495,width=320)


#CALCULATOR WINDOW
def cc():
    m = Tk()
    m.geometry("1000x720")
    m.resizable(0, 0)
    l1 = Label(m, text=":COST CALCULATOR:", bg="paleturquoise3", fg="black", font="Times 60 bold", borderwidth=20, relief=SUNKEN)
    l1.pack(side=TOP, fill=X)
    f1 = Frame(m, bg="lightskyblue1")
    f1.place(x=1, y=130, width=600, height=600)

#CREATING LISTBOX

    with open("pharmacy.csv", "r") as file:
        y = file.readlines()
        x = []
        for i in y:
            x.append(i)
        x.pop(0)
        print(x)
        y = []
        for i in x:
            k = i.split(",")
            print(k)
            y.append(k[0]+ "   price   :  " + k[1])


    def select():
        f = Frame(f1)
        f.pack()
        my_label = Label(f, bg="cadetblue1", fg="navy",font="Times 15 bold")
        my_label.pack(side=TOP)
        my_label.config(text=my_list.get(ANCHOR))

    my_list = Listbox(f1, width=100, bg="slategray1",fg="navy",font=("Times",16), selectbackground="deeppink")
    for i in y:
        my_list.insert(END, i)
    my_list.pack(side=TOP)

#BUTTON FOR SELECTING AN ITEM FROM LISTBOX

    btn = Button(f1, command=select, text="SELECT", bg="lightcyan2", fg="dodgerblue4", activebackground="deeppink",activeforeground="white" , font=("Times",16))
    btn.pack(pady=20,padx=10)
    f2 = Frame(m, bg="black")
    f2.place(x=600, y=130, width=385, height=900)

#ENTRY BOX FOR CALCULATOR
    entry = Entry(master=f2, relief=RAISED, borderwidth=3, width=45, font="Times 12 bold", bg="Azure", fg='navy')
    entry.grid(row=0, column=0, columnspan=6, ipady=12, pady=2, padx=2)

    def myclick(number):
        entry.insert(END, number)

    def equal():
        try:
            y = str(eval(entry.get()))
            entry.delete(0, END)
            entry.insert(0, y)
        except:
            tkinter.messagebox.showinfo("Error", "Syntax Error")
        finally:
            tkinter.messagebox.showinfo("Tata", "Your total bill is {}".format(y))

    def clear():
        entry.delete(0, END)

#BUTTONS FOR CALCULATOR
    button_1 = Button(master=f2, text='1', font=15, borderwidth=2, relief=RAISED, height=2, padx=15, pady=5, width=10,bg="darkslategray4",fg="navy",
                      command=lambda: myclick(1))
    button_1.grid(row=1, column=0, pady=2, padx=5)
    button_2 = Button(master=f2, text='2', padx=15, font=15, borderwidth=2, relief=RAISED, height=2, pady=5, width=10,bg="darkslategray4",fg="navy",
                      command=lambda: myclick(2))
    button_2.grid(row=1, column=1, pady=2, padx=5)
    button_3 = Button(master=f2, text='3', padx=15, pady=5, width=10, font=15, borderwidth=2, relief=RAISED, height=2,bg="darkslategray4",fg="navy",
                      command=lambda: myclick(3))
    button_3.grid(row=1, column=2, pady=2, padx=5)
    button_4 = Button(master=f2, text='4', padx=15, relief=RAISED, height=2, pady=5, font=15, borderwidth=2, width=10,bg="darkslategray3",fg="navy",
                      command=lambda: myclick(4))
    button_4.grid(row=2, column=0, pady=2, padx=5)
    button_5 = Button(master=f2, text='5', padx=15, pady=5, width=10, relief=RAISED, font=15, borderwidth=2, height=2,bg="darkslategray3",fg="navy",
                      command=lambda: myclick(5))
    button_5.grid(row=2, column=1, pady=2, padx=5)
    button_6 = Button(master=f2, text='6', padx=15, relief=RAISED, height=2, pady=5, width=10, font=15, borderwidth=2,bg="darkslategray3",fg="navy",
                      command=lambda: myclick(6))
    button_6.grid(row=2, column=2, pady=2, padx=5)
    button_7 = Button(master=f2, text='7', font=15, borderwidth=2, padx=15, relief=RAISED, height=2, pady=5, width=10,bg="darkslategray2",fg="navy",
                      command=lambda: myclick(7))
    button_7.grid(row=3, column=0, pady=2, padx=5)
    button_8 = Button(master=f2, text='8', padx=15, pady=5, font=15, borderwidth=2, width=10, relief=RAISED, height=2,bg="darkslategray2",fg="navy",
                      command=lambda: myclick(8))
    button_8.grid(row=3, column=1, pady=2, padx=5)
    button_9 = Button(master=f2, text='9', padx=15, pady=5, width=10, font=15, borderwidth=2, relief=RAISED, height=2,bg="darkslategray2",fg="navy",
                      command=lambda: myclick(9))
    button_9.grid(row=3, column=2, pady=2, padx=5)
    button_0 = Button(master=f2, text='0', padx=15, pady=5, relief=RAISED, height=2, width=10, font=15, borderwidth=2,bg="darkslategray1",fg="navy",
                      command=lambda: myclick(0))
    button_0.grid(row=5, column=2, pady=2, padx=5)

    button_00 = Button(master=f2, text='00', padx=15, pady=5, relief=RAISED, height=2, width=10, font=15, borderwidth=2,bg="lightskyblue3",fg="navy",
                      command=lambda: myclick("00"))
    button_00.grid(row=7, column=0, pady=2, padx=5)

    button_add = Button(master=f2, text="+", padx=15, pady=5, width=10, relief=RAISED, height=2, font=15, borderwidth=2,bg="darkslategray1",fg="navy",
                        command=lambda: myclick('+'))
    button_add.grid(row=5, column=0, pady=2, padx=5)

    button_subtract = Button(master=f2, text="-", padx=15, pady=5, width=10, relief=RAISED, height=2, font=15,bg="darkslategray1",fg="navy",
                             borderwidth=2, command=lambda: myclick('-'))
    button_subtract.grid(row=5, column=1, pady=2, padx=5)

    button_multiply = Button(master=f2, text="*", padx=15, font=15, borderwidth=2, pady=5, width=10, relief=RAISED,bg="lightskyblue3",fg="navy",
                             height=2, command=lambda: myclick('*'))
    button_multiply.grid(row=7, column=2, pady=2, padx=5)

    button_div = Button(master=f2, text="/", padx=15, pady=5, width=10, font=15, borderwidth=2, relief=RAISED, height=2,bg="lightskyblue3",fg="navy",
                        command=lambda: myclick('/'))
    button_div.grid(row=6, column=0, pady=2, padx=5)

    button_clear = Button(master=f2, text="=", padx=15, pady=5, relief=RAISED, height=2, font=15, borderwidth=2,bg="lightskyblue3",fg="navy",
                          width=25, command=equal)
    button_clear.grid(row=6, column=1, columnspan=2, padx=7, pady=2)

    button_equal = Button(master=f2, text="clear", padx=15, pady=5, width=9, relief=RAISED, height=2, font=15,bg="lightskyblue2",fg="navy",
                          borderwidth=2, command=clear)
    button_equal.grid(row=7, column=0, columnspan=3, padx=5, pady=2)



btn = Button(root, width=30,text="  COST CALCULATOR",fg='navy blue',font=('Times',16), bg="paleturquoise2", relief=SUNKEN, command=cc)
btn.pack(padx=15,pady=15 ,side=BOTTOM,anchor="ne")


#DEFINING GEOMETRY OF MAIN WINDOW

width = 1130
height = 550

root.geometry('%dx%d' % (width, height))
root.resizable(0,0)


def additem():
    e1 = entry1.get()
    e3 = entry3.get()
    e2 = entry2.get()
    e4 = entry4.get()
    e5 = entry5.get()
    e6 = entry6.get()
    if entry1.get() == "" and entry2.get() == "" and entry3.get() == "" and entry4.get() == "" and entry5.get() == "" and entry6.get() == "":

        print("Error")
        tkMessageBox.showerror("error", "there is issue with some information")

    else:
        result = tkMessageBox.askquestion("Submit", "You are about to enter following details\n" + e1 + "\n"
                                          + e2 + "\n" + e3 + "\n" + e4 + "\n" + e5 + "\n" + e6)
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)
        if (result == "yes"):
            with open("pharmacy.csv", 'a') as csvfile:
                csvfile.write('{0}, {1}, {2}, {3},{4},{5}\n'.format(str(e1), e2, e3, str(e4), str(e5), e6))

            csvfile.close()
        else:
            entry1.set("")
            entry2.set("")
            entry3.set("")
            entry4.set("")
            entry5.set("")
            entry6.set("")


def deleteitem():

    e1 = entry1.get()
    e2 = entry2.get()
    e3 = entry3.get()
    e4 = entry4.get()
    e5 = entry5.get()
    e6 = entry6.get()
    if entry1.get() == "" and entry2.get() == "" and entry3.get() == "" and entry4.get() == "" and entry5.get() == "" and entry6.get() == "":
        print("Error")
        tkMessageBox.showerror("error", "there is issue with some information")
    else:
        result = tkMessageBox.askquestion("Submit",
                                          "You are about to delete following details\n" + e1 + "\n" + e2 + "\n" + e3 + "\n" + e4 + "\n" + e5 + "\n" + e6)

        if (result == "yes"):
            print("here")
            with open("pharmacy.csv", 'r') as f, open("pharmacy1.csv", "w") as w1:
                for line in f:
                    if e1 not in line:
                        w1.write(line)
            os.remove("pharmacy.csv")
            os.rename("pharmacy1.csv", "pharmacy.csv")
            f.close()
            w1.close()

            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry6.delete(0, END)


def updateitem():
    e1 = entry1.get()
    e2 = entry2.get()
    e3 = entry3.get()
    e4 = entry4.get()
    e5 = entry5.get()
    e6 = entry6.get()
    if entry1.get() == "" and entry2.get() == "" and entry3.get() == "" and entry4.get() == "" and entry5.get() == "" and entry6.get() == "":

        print("Error")
        tkMessageBox.showerror("error", "there is issue with some information")
    else:
        result = tkMessageBox.askquestion("Submit",
                                          "You are about to update following details\n" + e1 + "\n" + e2 + "\n" + e3 + "\n" + e4 + "\n" + e5 + "\n" + e6)

        if (result == "yes"):
            print("here")
            with open("pharmacy.csv", "r") as f1, open("pharmacy1.csv", "w") as working:
                for line in f1:
                    if str(e1) not in line:
                        working.write(line)
                    else:
                        working.write('{0}, {1}, {2}, {3},{4} ,{5}\n'.format(str(e1), e2, e3, str(e4), str(e5), e6))
            os.remove("pharmacy.csv")
            os.rename("pharmacy1.csv", "pharmacy.csv")
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry6.delete(0, END)


def viewitem():
    tree.delete(*tree.get_children())
    with open('pharmacy.csv', "r") as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            MedicineName = row['MedicineName']
            MedicinePrice = row['MedicinePrice']
            Quantity = row['Quantity']
            Category = row['Category']
            Discount = row['Discount']
            tree.insert("", 0, values=(MedicineName, MedicinePrice, Quantity, Category, Discount))
    f.close()
    txt_result.config(text="Successfully read the data from database", fg="navy", font=("Times",12))


def clearitem():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)


MedicineName = StringVar()
MedicinePrice = StringVar()
Quantity = StringVar()
Category = StringVar()
Description = StringVar()
Discount = StringVar()

#FRAMES

Top = Frame(root, width=900, height=50, bd=8, relief="groove",bg='deeppink')
Top.pack(side=TOP)
Left = Frame(root, width=200, height=500, bd=8, relief="raise", bg='steel blue')
Left.pack(side=LEFT)
Right = Frame(root, width=500, height=500, relief="raise", bg='steel blue')
Right.pack(side=RIGHT, anchor=NW)
Forms = Frame(Left, width=300, height=450,bg='Azure')
Forms.pack(side=TOP)
Buttons = Frame(Left, width=300, height=320, bd=8, relief="raise", bg='steel blue')
Buttons.pack(side=BOTTOM,anchor="e")

txt_title = Label(Top, width=900, font=('Algerian', 24), fg='Navy blue',bg='paleturquoise', text="Pharmacy Management System +")
txt_title.pack()

#LABELS

label0 = Label(Forms, text="Medicine Name:", fg='Navy blue', font=('Monotype Corsiva', 16,'underline'), bg='Azure',bd=15)
label0.grid(row=0, stick="e")
label1 = Label(Forms, text="Medicine Price:", fg='Navy blue', font=('Monotype Corsiva', 16,"underline"), bd=15,bg='Azure')
label1.grid(row=1, stick="e")
label2 = Label(Forms, text="Quantity:", fg='Navy blue', font=('Monotype Corsiva', 16,"underline"), bd=15,bg='Azure')
label2.grid(row=2, stick="e")
label3 = Label(Forms, text="Category:", fg='Navy blue', font=('Monotype Corsiva', 16,"underline"), bd=15,bg='Azure')
label3.grid(row=3, stick="e")
label4 = Label(Forms, text="Description:", fg='Navy blue', font=('Monotype Corsiva', 16,"underline"), bd=15,bg='Azure')
label4.grid(row=4, stick="e")
label5 = Label(Forms, text="Discount:", font=('Monotype Corsiva', 16,"underline"), bd=16,bg='Azure',fg='Navy Blue')
label5.grid(row=5, stick="e")
txt_result = Label(Buttons,bg='Azure')
txt_result.pack(side=TOP)

#ENTRIES

entry1 = Entry(Forms, textvariable=MedicineName, width=30,bg="grey92",font="Times")
entry1.grid(row=0, column=1)
entry2 = Entry(Forms, textvariable=MedicinePrice, width=30,bg="grey92",font="Times")
entry2.grid(row=1, column=1)
entry3 = Entry(Forms, textvariable=Quantity, width=30,bg="grey92",font="Times")
entry3.grid(row=2, column=1)
entry4 = Entry(Forms, textvariable=Category, width=30,bg="grey92",font="Times")
entry4.grid(row=3, column=1)
entry5 = Entry(Forms, textvariable=Description, width=30,bg="grey92",font="Times")
entry5.grid(row=4, column=1)
entry6 = Entry(Forms, textvariable=Discount, width=30,bg="grey92",font="Times")
entry6.grid(row=5, column=1)

btn_add = Button(Buttons, width=10, text="ADD", command=additem, bg="Azure",fg='navy', font=("Times",12))
btn_add.pack(side=LEFT)
btn_delete = Button(Buttons, width=10, text="Delete", command=deleteitem,bg="Azure",fg='navy', font=("Times",12))
btn_delete.pack(side=LEFT)
btn_update = Button(Buttons, width=10, text="UPDATE", command=updateitem,bg="Azure",fg='navy', font=("Times",12))
btn_update.pack(side=LEFT)
btn_view = Button(Buttons, width=10, text="View", command=viewitem,bg="Azure",fg='navy', font=("Times",12))
btn_view.pack(side=LEFT)
btn_clear = Button(Buttons, width=10, text="CLEAR", command=clearitem,bg="Azure",fg='navy', font=("Times",12))
btn_clear.pack(side=LEFT)

#STUPID SCROLLBARS

scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
tree = ttk.Treeview(Right, columns=("MedicineName", "MedicinePrice", "Quantity", "Category", "Discount"),
                    height=400, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)

#DEFINING FIRST TREEVIEW

tree.heading("#0", text='', anchor=W)
tree.heading('MedicineName', text="MedicineName", anchor=W)
tree.heading('MedicinePrice', text="MedicinePrice", anchor=W)
tree.heading('Quantity', text="Quantity", anchor=W)
tree.heading('Category', text="Category", anchor=W)
tree.heading('Discount', text="Discount", anchor=W)
tree.column('#0', stretch=NO, width=0)
tree.column('MedicineName', stretch=YES, minwidth=0, width=120)
tree.column('MedicinePrice', stretch=YES, minwidth=0, width=120)
tree.column('Quantity', stretch=YES, minwidth=0, width=120)
tree.column('Category', stretch=YES, minwidth=0, width=120)
tree.column('Discount', stretch=YES, minwidth=0, width=120)

#STYLING FIRST TREEVIEW

style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", font=('Times', 15),
                background='lightcyan1',
                foreground='navy blue',
                rowheight=25,
                fieldbackground='lightcyan',
                )
style.configure('Treeview.Heading', font=("Times",14),
                background='lightcyan2',
                foreground='black',
                rowheight=20)
style.map('Treeview',
          background=[('selected','deeppink')])

tree.pack()

root.mainloop()
