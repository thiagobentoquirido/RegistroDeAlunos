from importlib.resources import Anchor
from pydoc import text
from tkinter import CENTER, END, GROOVE, LEFT, NSEW, NW, RIDGE, Frame
from tkinter import Tk, Toplevel, Label, Button, Entry, messagebox, filedialog, RAISED,SOLID
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from turtle import bgcolor, st, width
from typing import Text
#===============[ IMPORTS ]==================#

from main import *



#pillow
from PIL import ImageTk, Image

#image
from tkinter import PhotoImage

#tkcalendar 
from tkcalendar import Calendar, DateEntry  
from datetime import date

# ================== COLORS ================== #

co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#146C94"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde
co10 = "#50C878"  # +++ verde


#======================== CRUD =======================#
#add func
def add_student():
    global image, image_string, l_image
    #getting values
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    gender = c_gender.get()
    birth_date = c_bday.get()
    address = entry_address.get()
    city = entry_city.get()
    state = entry_state.get()
    zip_code = entry_zip.get()
    country = entry_country.get()
    grade = c_grade.get()
    img = image  # Ensure 'image' is defined before this line


    list = [name,email,phone,gender,birth_date,address,city,state,zip_code,country,img,grade]
    #verifying if all fields are filled
    for i in list:
        if i == "":
            messagebox.showerror("Error", "Please fill all fields.")
            return
    
    #registering values in database
    register_system.register_student(list)


    #cleaning entry fields
    entry_name.delete(0,END)
    entry_email.delete(0,END)
    entry_phone.delete(0,END)
    c_gender.delete(0,END)
    c_bday.delete(0,END)
    entry_address.delete(0,END)
    entry_city.delete(0,END)
    entry_state.delete(0,END)
    entry_zip.delete(0,END)
    entry_country.delete(0,END)
    c_grade.delete(0,END)
    l_image.destroy()  # Remove the image label
    


    #showing the values in the table
    show_studens()

#====================== SEARCH STUDENT ==================#
def search_student():
    global image, image_string, l_image

    l_image = None  # Reset the image label
    if l_image is not None:
      l_image.destroy()


    student_id = e_search.get()
    
    if student_id == "":
        messagebox.showerror("Error", "Please enter a student ID.")
        return
    
    #searching for the student in the database
    dados = register_system.search_student(student_id)

    if not dados:
        return
    

    #cleaning entry fields
    entry_name.delete(0,END)
    entry_email.delete(0,END)
    entry_phone.delete(0,END)
    c_gender.delete(0,END)
    c_bday.delete(0,END)
    entry_address.delete(0,END)
    entry_city.delete(0,END)
    entry_state.delete(0,END)
    entry_zip.delete(0,END)
    entry_country.delete(0,END)
    c_grade.delete(0,END)
   

    #inserting values
    entry_name.insert(END,dados[1])
    entry_email.insert(END,dados[2])
    entry_phone.insert(END,dados[3])
    c_gender.insert(END,dados[4])
    c_bday.insert(END,dados[5])
    entry_address.insert(END,dados[6])
    entry_city.insert(END,dados[7])
    entry_state.insert(END,dados[8])
    entry_zip.insert(END,dados[9])
    entry_country.insert(END,dados[10])
    c_grade.insert(END,dados[12])
 
    img_path = dados[11]
    
    try:
        img = Image.open(img_path)
        img = img.resize((240, 240))
        image_string = ImageTk.PhotoImage(img)

        if l_image:
            l_image.destroy()

        l_image = Label(DetailFrame, image=image_string, bg=co0, width=200, height=200)
        l_image.image = image_string  
        l_image.place(x=670, y=20)

    except Exception as e:
        messagebox.showerror("Image Error", f"Could not load image:\n{e}")

    
    #showing the values in the table
    show_studens()

#===================== UPDATE STUDENT ==================#

def update_studentt():
    global image, image_string, l_image

    l_image = None  # Reset the image label
    if l_image is not None:
      l_image.destroy()


    student_id = e_search.get()
    
    if student_id == "":
        messagebox.showerror("Error", "Please enter a student ID.")
        return
    
    
    #searching for the student in the database
   

 
    

    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    gender = c_gender.get()
    birth_date = c_bday.get()
    address = entry_address.get()
    city = entry_city.get()
    state = entry_state.get()
    zip_code = entry_zip.get()
    country = entry_country.get()
    grade = c_grade.get()
   
    try:
        img = image
    except NameError:
        messagebox.showerror("Error", "No image selected. Please upload an image.")
        return
    
    datalist = [name,email,phone,gender,birth_date,address,city,state,zip_code,country,img,grade, student_id]
  
        
    register_system.update_student(datalist)


    #cleaning entry fields
    entry_name.delete(0,END)
    entry_email.delete(0,END)
    entry_phone.delete(0,END)
    c_gender.delete(0,END)
    c_bday.delete(0,END)
    entry_address.delete(0,END)
    entry_city.delete(0,END)
    entry_state.delete(0,END)
    entry_zip.delete(0,END)
    entry_country.delete(0,END)
    c_grade.delete(0,END)
   

   
    
    try:
        img_obj = Image.open(img)
        img_obj = img_obj.resize((240, 240))
        image_string = ImageTk.PhotoImage(img_obj)

        if l_image:
            l_image.destroy()

        l_image = Label(DetailFrame, image=image_string, bg=co0, width=200, height=200)
        l_image.image = image_string  
        l_image.place(x=670, y=20)

    except Exception as e:
        messagebox.showerror("Image Error", f"Could not load image:\n{e}")
    
    #showing the values in the table
    show_studens()


#===================== DELETE FUNCTION ==================#
def delete_student():
    student_id = e_search.get()
    
    if student_id == "":
        messagebox.showerror("Error", "Please enter a student ID.")
        return
    
    #searching for the student in the database
    dados = register_system.search_student(student_id)

    if not dados:
        return

    #confirming deletion
    confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete student {dados[1]}?")
    
    if confirm:
        register_system.delete_student(student_id)
        show_studens()  # Refresh the table after deletion
# ================== CREATING WINDOW ================== #

window = Tk()
window.title("Student Registration System")

# =========== Obter resolução da tela do usuário =============== #

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# ============ Definir tamanho da janela (60% da tela) =============== #

window_width = int(screen_width * 0.6)
window_height = int(screen_height * 0.6)

# ================== Calcular coordenadas para centralizar ===================== #

center_x = int((screen_width - window_width) / 2)
center_y = int((screen_height - window_height) / 2)

# ========================= Aplicar tamanho e posição ======================= #

window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
window.resizable(True, True)
window.configure(background=co0)
window.resizable(width=False, height=False)
icon = PhotoImage(file="./images/icon.png")
window.iconphoto(True, icon)

# ============ Window Style ================ #

style = ttk.Style(window)
style.theme_use("clam")

# =================== [ CREATING FRAMES ] ================== #

LogoFrame = Frame(window,width=window_width,height=66,bg=co10, relief='flat')
LogoFrame.grid(row=0, column=0, sticky='nsew',pady=0, padx=0,columnspan=5)

# =================== [ BUTTON FRAMES ] ================== #

ButtonFrame = Frame(window,width=150,height=250,bg=co0 , relief=RAISED)
ButtonFrame.grid(row=1, column=0, sticky='nsew',pady=1, padx=0)

# =================== [ DETAILS FRAMES ] ================== #

DetailFrame = Frame(window,width=window_width,height=100,bg=co0 , relief=SOLID)
DetailFrame.grid(row=1, column=1, sticky='nsew',pady=1, padx=10)

# =================== [ TABLE FRAMES ] ================== #

TableFrame = Frame(window,width=window_width,height=100,bg=co0 , relief=SOLID)
TableFrame.grid(row=3, column=0, sticky='nsew',pady=5, padx=10,columnspan=5)


# =================== [ FRAME LOGO ] ================== #

global image,image_string,l_image

app_add_img = Image.open("./images/logo.png")
app_add_img= app_add_img.resize((70, 70))
app_add_img = ImageTk.PhotoImage(app_add_img)
app_logo = Label(LogoFrame, image=app_add_img, text="Student Registration System", padx=5,anchor=NW, bg=co10, fg=co1, font=('Ivy 20 bold'), relief='flat', compound=LEFT)
app_logo.place(x=-1, y=-5)


# ================== [FIELDS ENTRIES] ================== #
#-------------- Name ----------- #
label_name = Label(DetailFrame, text="Name *:",anchor=NW,bg=co0, fg=co1, font=('Ivy 10 '))
label_name.place(x=4, y=10) 
entry_name = Entry(DetailFrame, width=30, justify='left',relief='solid',font=('Ivy 10 '))
entry_name.place(x=7, y=30)

#-------------- EMAIL ----------- #
label_email = Label(DetailFrame, text="Email *:",anchor=NW,bg=co0, fg=co1, font=('Ivy 10 '))
label_email.place(x=4, y=70) 
entry_email = Entry(DetailFrame, width=30, justify='left',relief='solid',font=('Ivy 10 '))
entry_email.place(x=7, y=100)

#------------------ PHONE --------------- #
label_phone = Label(DetailFrame, text="Phone *:",anchor=NW,bg=co0, fg=co1, font=('Ivy 10 '))
label_phone.place(x=4, y=130) 
entry_phone = Entry(DetailFrame, width=15, justify='left',relief='solid',font=('Ivy 10 '))
entry_phone.place(x=7, y=160)

#-------------- GENDER --------------- #
label_gender = Label(DetailFrame, text="Gender *:",anchor=NW,bg=co0, fg=co1, font=('Ivy 10 '))
label_gender.place(x=127, y=130) 
c_gender = ttk.Combobox(DetailFrame, width=7, justify='center', font=('Ivy 10 bold'),state='readonly')
c_gender['values'] = ("Male","Female")
c_gender.place(x=130, y=160)

#------------------ B DAY --------------- #
label_bday = Label(DetailFrame, text="Birth Date *:",anchor=NW,bg=co0, fg=co1, font=('Ivy 10 '))
label_bday.place(x=220, y=10)
c_bday = DateEntry(DetailFrame, width=18, background='darkblue', foreground='white', borderwidth=2, font=('Ivy 10 bold'), date_pattern='yyyy-mm-dd', justify='center')
c_bday.place(x=224, y=30)

#------------------ ADDRESS --------------- #
label_address = Label(DetailFrame, text="Address *:",anchor=NW,bg=co0, fg=co1, font=('Ivy 10 '))
label_address.place(x=220, y=70)
entry_address = Entry(DetailFrame, width=25, justify='left',relief='solid',font=('Ivy 10 '))
entry_address.place(x=224, y=100)
#------------------ CITY --------------- #  
label_city = Label(DetailFrame, text="City *:",anchor=NW,bg=co0, fg=co1, font=('Ivy 10 '))
label_city.place(x=220, y=130)
entry_city = Entry(DetailFrame, width=15, justify='left',relief='solid',font=('Ivy 10 '))
entry_city.place(x=224, y=160)
#------------------ STATE --------------- #
label_state = Label(DetailFrame, text="State *:",anchor=NW,bg=co0, fg=co1, font=('Ivy 10 '))
label_state.place(x=350, y=130)
entry_state = Entry(DetailFrame, width=10, justify='left',relief='solid',font=('Ivy 10 '))
entry_state.place(x=350, y=160)
#------------------ ZIP CODE --------------- #
label_zip = Label(DetailFrame, text="Zip Code *:",anchor=NW,bg=co0, fg=co1, font=('Ivy 10 '))
label_zip.place(x=380, y=10)
entry_zip = Entry(DetailFrame, width=10, justify='left',relief='solid',font=('Ivy 10 '))
entry_zip.place(x=380, y=30)
#------------------ COUNTRY --------------- #
label_country = Label(DetailFrame, text="Country *:",anchor=NW,bg=co0, fg=co1, font=('Ivy 10 '))
label_country.place(x=415, y=70)
entry_country = Entry(DetailFrame, width=20, justify='left',relief='solid',font=('Ivy 10 '))
entry_country.place(x=415, y=100)
#------------------ GRADE------------- #
label_grade = Label(DetailFrame, text="Grade *:",anchor=NW,bg=co0, fg=co1, font=('Ivy 10 '))
label_grade.place(x=6, y=190)
c_grade = ttk.Combobox(DetailFrame, width=7, justify='center', font=('Ivy 10 bold'),state='readonly')
c_grade['values'] = ("A","B","C","D","E","F")
c_grade.place(x=60, y=190)


#------------------ CHOOSE IMAGE FUNC ------------- #
def choose_image():
    global image, image_string, l_image
    image_string = Image
    
    file_path = fd.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        image = Image.open(file_path)
        image = image.resize((240, 240))
        image_string = ImageTk.PhotoImage(image)
        l_image = Label(DetailFrame, image=image_string, bg=co0, width=200, height=200 )
        l_image.place(x=670, y=20)
        l_image.configure(image=image_string)
        l_image.image = image_string
        load_button['text'] = 'Change Image'.upper()
        load_button['command'] = choose_image  # Update the command to allow changing the image again

        image = file_path 
    

load_button = Button(DetailFrame, text="Upload Image".upper(), compound=CENTER,anchor=CENTER,overrelief=RIDGE, command=choose_image, bg=co10, fg=co1, font=('Ivy 14 bold'), relief='raised', width=15)
load_button.place(x=440, y=150)


# ================== [ STUDENS' TABLE ] ================== #
def show_studens():
    #====================== [ CREATING TREE VIEW ] ================== #
    list_header = ['id','name','email','phone','gender','birth date','adress','city','state','zip code','country','Picture','grade']
    # ======== [ VIEW ALL STUDENTS ] ========== #
    df_list = register_system.view_all_studens() #return list of tuples from database
    if not df_list:#if is empty 
        messagebox.showinfo("Info", "No students registered.")
        return
    # ================== [ TABLE FRAME ] ================== #
    tree_aluno = ttk.Treeview(TableFrame, columns=list_header, show='headings')
    tree_aluno.grid(row=0, column=0, sticky='nsew')  # Expande dentro do frame
    
    # === Vertical Scrollbar === #
    vsb = ttk.Scrollbar(TableFrame, orient="vertical", command=tree_aluno.yview)
    vsb.grid(row=0, column=1, sticky='ns')

    # === Horizontal Scrollbar === #
    hsb = ttk.Scrollbar(TableFrame, orient="horizontal", command=tree_aluno.xview)
    hsb.grid(row=1, column=0, sticky='ew')

    # ===  Scrolls === #
    TableFrame.grid_rowconfigure(0, weight=1)   # Treeview
    TableFrame.grid_rowconfigure(1, weight=0)   # Scroll horizontal
    TableFrame.grid_columnconfigure(0, weight=1) # Treeview + scroll horizontal
    TableFrame.grid_columnconfigure(1, weight=0) # Scroll vertical

    # === Permitir expansão === #

    TableFrame.grid_rowconfigure(0, weight=1)
    TableFrame.grid_columnconfigure(0, weight=1)

    hd = ['center',  # id
        'w',       # name   
        'w',       # email
        'center',  # phone
        'center',  # gender
        'center',  # birth date
        'w',       # address
        'w',       # city
        'center',  # state
        'center',  # zip code
        'w',       # country
        'center',  # img
        'center']  # grade
        #====================== [ TREEVIEW CONFIGURATION ] ================== #
    h = [40,    # id
        90,   # name
        120,   # email
        90,   # phone
        70,    # gender
        100,    # birth date
        120,   # address
        120,   # city
        90,    # state
        80,    # zip code
        90,   # country
        60,    # img
        70]    # grade
    n = 0 

    for idx, (col, width, anchor) in enumerate(zip(list_header, h, hd)):
        tree_aluno.heading(col, text=col.title(), anchor='w')
        tree_aluno.column(col, width=width, anchor=anchor, stretch=False)

# Evita redimensionamento das colunas
    tree_aluno.bind('<Button-1>', disable_column_resize)

    #====================== [ INSERTING DATA ] ================== #
    for i in df_list:
        tree_aluno.insert('', 'end', values=i)
    


def disable_column_resize(event):
    return "break"

# ================== [CALLING TABLE FUNCTION] ================== #	
show_studens()

# =============== [ SEARCH STUDENT ] ================ #

Search_frame = Frame(ButtonFrame, width=150, height=250, bg=co0, relief=RAISED)
Search_frame.grid(row=0, column=0, sticky=NSEW, pady=10, padx=10)


l_name = Label(Search_frame,text="Search Student [Type ID]",anchor=NW,bg=co0, fg=co1, font=('Ivy 10 '))
l_name.grid(row=0, column=0, sticky=NSEW, pady=10, padx=0)

e_search = Entry(Search_frame, width=5, justify='center',relief='solid',font=('Ivy 10'))
e_search.grid(row=1, column=0   , sticky=NSEW, pady=10, padx=0)

s_button = Button(Search_frame, command=search_student, text="Search", width=9,anchor=CENTER,overrelief=RIDGE, bg=co10, fg=co0, font=('Ivy 9 bold'), relief='raised')
s_button.grid(row=1, column=1, sticky=NSEW, pady=10, padx=0)



# ================== [ BUTTONS ] ================== #

app_add_img = Image.open("./images/plus.png")
app_add_img= app_add_img.resize((40, 40))
app_add_img = ImageTk.PhotoImage(app_add_img)
add_img = Button(ButtonFrame,image=app_add_img, text="  Add",relief=GROOVE, command=add_student,width=100,overrelief=RIDGE,compound=LEFT, bg=co10, fg=co0, font=('Ivy 10 bold'))
add_img.grid(row=1, column=0, sticky=NSEW, pady=5, padx=10)

app_update_img = Image.open("./images/update.png")
app_update_img= app_update_img.resize((40, 40))
app_update_img= ImageTk.PhotoImage(app_update_img)
update_img = Button(ButtonFrame,command=update_studentt,image=app_update_img, text="   Update",relief=GROOVE, width=100,overrelief=RIDGE,compound=LEFT, bg=co10, fg=co0, font=('Ivy 10 bold'))
update_img.grid(row=2, column=0, sticky=NSEW, pady=5, padx=10)

app_delete_img = Image.open("./images/delete.png")
app_delete_img= app_delete_img.resize((40, 40))
app_delete_img= ImageTk.PhotoImage(app_delete_img)
delete_img = Button(ButtonFrame,command=delete_student,image=app_delete_img, text="   Delete",relief=GROOVE, width=100,overrelief=RIDGE,compound=LEFT, bg=co10, fg=co0, font=('Ivy 10 bold'))
delete_img.grid(row=3, column=0, sticky=NSEW, pady=5, padx=10)

 

# ================== [ separating line ] ================== #

sl = Label(ButtonFrame, text="h", width=1,anchor=NW,bg=co1, fg=co0, font=('Ivy 1  '),relief=GROOVE, height=150)
sl.place(x=240,y=15)





















































# ================== RUNNING ================== #
window.mainloop()
