# Tkinter GUI version of your OOP-based Student Management System with centered window
import tkinter as tk
from tkinter import messagebox

# Base class with encapsulation
class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

# Student class with inheritance
class Student(Person):
    def __init__(self, name, roll_no, branch):
        super().__init__(name)
        self.__roll_no = roll_no
        self.__branch = branch

    def get_roll_no(self):
        return self.__roll_no

    def get_branch(self):
        return self.__branch

    def set_branch(self, branch):
        self.__branch = branch

    def __str__(self):
        return f"Student: {self.get_name()}, Roll No: {self.__roll_no}, Branch: {self.__branch}"

# PG Student with Polymorphism
class PGStudent(Student):
    def __init__(self, name, roll_no, branch, thesis_topic):
        super().__init__(name, roll_no, branch)
        self.thesis_topic = thesis_topic

    def __str__(self):
        return f"PG Student: {self.get_name()}, Roll No: {self.get_roll_no()}, Branch: {self.get_branch()}, Thesis: {self.thesis_topic}"

# Manager with abstraction of student list
class StudentManager:
    def __init__(self):
        self.__students = []

    def add_student(self, student):
        self.__students.append(student)

    def get_all_students(self):
        return self.__students

    def find_by_roll(self, roll_no):
        for s in self.__students:
            if s.get_roll_no() == roll_no:
                return s
        return None

# GUI Application
class StudentApp:
    def __init__(self, root):
        self.manager = StudentManager()
        self.root = root
        self.root.title("Student Management System")
        self.center_window(500, 400)

        self.name_var = tk.StringVar()
        self.roll_var = tk.StringVar()
        self.branch_var = tk.StringVar()
        self.thesis_var = tk.StringVar()

        self.build_gui()

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def build_gui(self):
        tk.Label(self.root, text="Name").grid(row=0, column=0)
        tk.Entry(self.root, textvariable=self.name_var).grid(row=0, column=1)

        tk.Label(self.root, text="Roll No").grid(row=1, column=0)
        tk.Entry(self.root, textvariable=self.roll_var).grid(row=1, column=1)

        tk.Label(self.root, text="Branch").grid(row=2, column=0)
        tk.Entry(self.root, textvariable=self.branch_var).grid(row=2, column=1)

        tk.Label(self.root, text="Thesis Topic (for PG only)").grid(row=3, column=0)
        tk.Entry(self.root, textvariable=self.thesis_var).grid(row=3, column=1)

        tk.Button(self.root, text="Add UG Student", command=self.add_ug).grid(row=4, column=0)
        tk.Button(self.root, text="Add PG Student", command=self.add_pg).grid(row=4, column=1)
        tk.Button(self.root, text="View All Students", command=self.view_students).grid(row=5, column=0, columnspan=2)
        tk.Button(self.root, text="Search by Roll", command=self.search_student).grid(row=6, column=0, columnspan=2)

        self.result_box = tk.Text(self.root, height=10, width=60)
        self.result_box.grid(row=7, column=0, columnspan=2)

    def add_ug(self):
        student = Student(self.name_var.get(), self.roll_var.get(), self.branch_var.get())
        self.manager.add_student(student)
        messagebox.showinfo("Success", "UG Student Added")
        self.clear_entries()

    def add_pg(self):
        student = PGStudent(self.name_var.get(), self.roll_var.get(), self.branch_var.get(), self.thesis_var.get())
        self.manager.add_student(student)
        messagebox.showinfo("Success", "PG Student Added")
        self.clear_entries()

    def view_students(self):
        self.result_box.delete("1.0", tk.END)
        students = self.manager.get_all_students()
        if not students:
            self.result_box.insert(tk.END, "No students found.\n")
        for student in students:
            self.result_box.insert(tk.END, str(student) + "\n")

    def search_student(self):
        roll_no = self.roll_var.get()
        student = self.manager.find_by_roll(roll_no)
        self.result_box.delete("1.0", tk.END)
        if student:
            self.result_box.insert(tk.END, f"Found: {student}\n")
        else:
            self.result_box.insert(tk.END, "Student not found.\n")

    def clear_entries(self):
        self.name_var.set("")
        self.roll_var.set("")
        self.branch_var.set("")
        self.thesis_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()
