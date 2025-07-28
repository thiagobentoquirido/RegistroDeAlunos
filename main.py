from atexit import register
import sqlite3
from tkinter import messagebox

class RegisterSystem:
    def __init__ (self):
        self.conn = sqlite3.connect('students.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL UNIQUE,
                gender TEXT NOT NULL,
                birth_date TEXT NOT NULL,
                address TEXT NOT NULL,
                city TEXT NOT NULL,
                state TEXT NOT NULL,
                zip_code TEXT NOT NULL,
                country TEXT NOT NULL,
                picture TEXT NOT NULL,
                grade TEXT NOT NULL
            )
        ''')
   
    
    def register_student(self,students):
        self.c.execute("INSERT INTO students(name,email,phone,gender,birth_date,address,city,state,zip_code,country,picture,grade) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", students)
        self.conn.commit()

        messagebox.showinfo("Success", "Student registered successfully!")
    def view_all_studens(self):
        self.c.execute("SELECT * FROM students")
        dados = self.c.fetchall()
        return dados

    def delete_student(self, student_id):
        self.c.execute("DELETE FROM students WHERE id=?", (student_id,))
        self.conn.commit()
        messagebox.showinfo("Success", f"Student {student_id} deleted successfully!")
    
    def search_student(self, id):
        self.c.execute("SELECT * FROM students WHERE id=?", (id,))
        dados = self.c.fetchone()
        if dados:
            return dados 
        else:
            messagebox.showerror("Error", "Student not found.")
        return None


    def update_student(self, data):
        query = "UPDATE students set name = ?, email = ?,phone = ?,gender = ?,birth_date = ?,address = ?,city = ?,state = ?,zip_code = ?,country = ?,picture = ?,grade = ?WHERE id = ?"
        self.c.execute(query, data)   
        self.conn.commit()
        messagebox.showinfo("Success", f"Student id{id} updated successfully!")

register_system = RegisterSystem()


# set informations
#students1 = ("Mathew","mathewstudent@gmail.com","4534347","Male","2000-11-12","22 Main St","Springfield","IL","62704","USA",23,"A","./images/mthw.png")
#students2 = ("Peter","peterstudent@gmail.com","324265623","Male","2000-06-05","313 Main St","Springfield","IL","62704","USA",23,"./images/path.png","A")
#students3 = ("James","jamessstudent@gmail.com","6545774","Male","2000-03-25","412 Main St","Springfield","IL","62704","USA",23,"./images/path.png","A")
#register_system.register_student(students1) 
#register_system.register_student(students2) 
#register_system.register_student(students3) 




#searchstudents by id

#register_system.search_student(1)#search for student with id 1


#view all students
#allstudents = register_system.view_all_studens() ##shoow all students in console
#delete student by id



#register_system.delete_student(5) #delete student with id 1

#delete all students
#register_system.c.execute("DELETE FROM students")


#update student
#students1 = ("Mathew","mathewstudent@gmail.com","123","Male","2000-01-01","123 Main St","Springfield","IL","62704","USA",23,"/images/mthw.png","A")
#register_system.update_student = (students1,1) #update student with id 1

