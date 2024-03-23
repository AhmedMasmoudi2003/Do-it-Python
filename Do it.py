from tkinter import *
#from tkinter.tix import *
from tkinter import messagebox
from os import startfile
from pickle import *
from tkinter import ttk
from tkinter import filedialog

#===================================||  Functions  ||===========================================================================================

def add(e = None):
    global saved
    ch = task.get()
    listbox.insert(END,"==> "+task.get())
    task_entry.delete(0,END)
    saved = False
    
def edit():
    global saved
    task_entry.delete(0,END)
    task_entry.insert(0,listbox.get(ANCHOR)[4:])
    listbox.delete(ANCHOR)
    saved = False

def down():
    global saved
    if listbox.curselection():
        index = listbox.curselection()[0]
        if index < listbox.size() - 1:
            item = listbox.get(index)
            listbox.insert(index + 2, item)
            listbox.delete(index)
            listbox.select_set(index + 1)
    
    
    #element = listbox.get(ANCHOR)
    #pos = listbox.index(ANCHOR)+1
    #listbox.delete(ANCHOR)
    #listbox.insert(pos,element)
    
    saved = False

def up():
    global saved
    if listbox.curselection():
        index = listbox.curselection()[0]
        if index > 0:
            item = listbox.get(index)
            listbox.insert(index - 1, item)
            listbox.delete(index + 1)
            listbox.select_set(index - 1)
    #element = listbox.get(ANCHOR)
    #pos = listbox.index(ANCHOR)-1
    #listbox.delete(ANCHOR)
    #listbox.insert(pos,element)
    saved = False

def delete(e = None):
    listbox.delete(ANCHOR)
    
def new(e = None):
    global saved
    listbox.delete(0,END)
    task_entry.delete(0,END)
    saved = False
    
def openn(e = None):
    listbox.delete(0,END)
    global file_loc
    file_loc = filedialog.askopenfilename()
    f = open(file_loc,"r")
    for x in f:
        #if x!= "\n":
        if x.strip():
            listbox.insert(END,x)
    f.close()
        
def save(e = None):
    try:
        global saved
        f = open(file_loc,"w")
        f.write('\n'.join(listbox.get(0, END)))
        f.close()
        messagebox.showinfo("Do it!", "File Saved Successfully")
        saved = True
    except NameError:
        saveas()

def saveas():
    global file_loc
    global saved
    file_loc = filedialog.asksaveasfilename(filetypes=(("Text files", "*.txt"),("All files", "*.*")),defaultextension=".txt")#fel save ki tji temchi el 9dim ywalli fih entré zeyda************
    f = open(file_loc,"w")
    f.write('\n'.join(listbox.get(0, END)))
    f.close()
    
    f = open("last.txt","w")   #precise the last file(folder location and name) you saved so when open it will open automatically for you
    f.write(file_loc)
    f.close()
    messagebox.showinfo("Do it!", "File Saved Successfully")   
    saved = True
    
    
def on_closing(event=None):
    close()


def close(e = None):

    if listbox.get(0, END) != "" and saved==False:
        want_save = messagebox.askyesno("File not saved", "Do you want to Save?")
        if want_save:
            save()
            screen.destroy()
        else:
            screen.destroy()
    else:
        screen.destroy()
   
def contact():
    try:
        startfile("contact.txt") # Open any program, text or office document.
    except FileNotFoundError:
        pass
        
def tuto():
    try:
        startfile("tuto...txt") # Open any program, text or office document.
    except FileNotFoundError:
        pass


#==========||  window settings  ||===============
saved = True
screen = Tk()
screen.title("Do It! 1.0")
screen.geometry("800x600")
screen.resizable(False,False)

#==========||  background and icon  ||===============

bgimage=PhotoImage(file="background.png")
bgLabel=Label(screen,image=bgimage)
bgLabel.pack()
screen.iconbitmap('icon.ico')

#======================||   Menu Bar   ||===============================

menubar = Menu(screen)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=openn)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save As", command=saveas)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=close)
menubar.add_cascade(label="File", menu=filemenu)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Tuto..", command=tuto)
filemenu.add_command(label="Contact", command=contact)
menubar.add_cascade(label="help", menu=filemenu)

screen.config(menu=menubar)
    
#===========||  label  ||======================

label= Label(text= "Write here a task :",font=("Segoe UI", 10 ,"bold"),fg="white",bg="#FFB303")
label.place(x=30,y=50)

#=======||List Creation||=============================================================

listbox = Listbox(screen,width=27,height=10,bd=3, selectforeground='Black', activestyle='none',selectbackground='#FFB303' , font=("Segoe UI", 16),highlightcolor="#FFB303")
listbox.pack(side= LEFT, fill= BOTH)
listbox.place(x=30,y=150)

#scrollbar = Scrollbar(screen, orient= 'vertical')#this what i satrted with scroll bar
#scrollbar.pack(side= RIGHT, fill= BOTH)
#scrollbar.place(x=400,y=130)
#listbox.config(yscrollcommand= scrollbar.set)
#scrollbar.config(command= listbox.yview)

#=======||Task entry Creation||=============================================================

task = StringVar()
task_entry = Entry(textvariable=task,width=19,bd=3,font=("Segoe UI", 22))
task_entry.place(x=30,y=80)
task_entry.focus()

#============================||   BUTTONS   ||========================================================================

add_btn = Button(text="Add",fg="white",bg="#FFB303",height=1,pady=7,width=10,font=("Segoe UI", 12,"bold"),command=add)
add_btn.place(x=350,y=78)

edit_btn = Button(text="Edit",fg="white",bg="#FFB303",height=1,pady=7,width=10,font=("Segoe UI", 12,"bold"),command=edit)
edit_btn.place(x=350,y=200)

down_btn = Button(text="Down",fg="white",bg="#FFB303",height=1,pady=7,width=4,font=("Segoe UI", 10,"bold"),command=down)
down_btn.place(x=360,y=285)

up_btn = Button(text="Up",fg="white",bg="#FFB303",height=1,pady=7,width=4,font=("Segoe UI", 10,"bold"),command=up)
up_btn.place(x=410,y=285)

del_btn = Button(text="Del",fg="white",bg="#FFB303",height=1,pady=7,width=10,font=("Segoe UI", 12,"bold"),command=delete)
del_btn.place(x=350,y=360)


#=======||  opening last list auto  ||=========

try:
    f = open("last.txt","r")
    f2 = open(f.readline(),"r")
    for x in f2:
        listbox.insert(END,x)
    f2.close()
    f.close()
except FileNotFoundError:
    new()

#=======||  key binding  ||=========
    
screen.bind('<Return>',add)
screen.bind('<Escape>', close)
screen.bind('<Delete>', delete)
screen.bind('<Control_L>'+'s', save)
screen.bind('<Control_L>'+'o', openn)
screen.bind('<Control_L>'+'n', new)


screen.protocol("WM_DELETE_WINDOW", on_closing)
screen.mainloop()