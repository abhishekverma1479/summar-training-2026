import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

root = tk.Tk()
root.title("Student Management System - GLA University")
root.geometry("650x480")

DATA_FILE = "students.json"

def load_students():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_students(students):
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=2)

students = load_students()

# ---------- Menu Bar ----------
menubar = tk.Menu(root)
root.config(menu=menubar)

def show_about():
    messagebox.showinfo("About", "Student Management System v1.0\nGLA University")

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menubar.add_cascade(label="Help", menu=help_menu)

# ---------- Notebook (Tabs) ----------
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

records_tab = ttk.Frame(notebook)
add_tab = ttk.Frame(notebook)
notebook.add(records_tab, text="Student Records")
notebook.add(add_tab, text="Add / Update Student")

# ---------- Records Tab: Treeview + Search ----------
search_frame = tk.Frame(records_tab)
search_frame.pack(fill="x", pady=5)

tk.Label(search_frame, text="Search by name:").pack(side="left", padx=5)
search_var = tk.StringVar()
search_entry = tk.Entry(search_frame, textvariable=search_var)
search_entry.pack(side="left", padx=5)

columns = ("roll_no", "name", "course", "cgpa")
tree = ttk.Treeview(records_tab, columns=columns, show="headings", height=12)
for col, label in zip(columns, ["Roll No", "Name", "Course", "CGPA"]):
    tree.heading(col, text=label)
    tree.column(col, width=130)
tree.pack(fill="both", expand=True, padx=5, pady=5)

def refresh_tree(filtered=None):
    tree.delete(*tree.get_children())
    data = filtered if filtered is not None else students
    for s in data:
        tree.insert("", "end", values=(s["roll_no"], s["name"], s["course"], s["cgpa"]))

def search_students(*args):
    query = search_var.get().lower()
    filtered = [s for s in students if query in s["name"].lower()]
    refresh_tree(filtered)

search_var.trace_add("write", search_students)   # runs search_students on every keystroke

def delete_selected():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("No Selection", "Select a student to delete.")
        return
    values = tree.item(selected[0])["values"]
    roll_no = values[0]
    students[:] = [s for s in students if s["roll_no"] != roll_no]
    save_students(students)
    refresh_tree()

tk.Button(records_tab, text="Delete Selected", command=delete_selected, bg="#B9791F", fg="white").pack(pady=5)

# ---------- Add/Update Tab ----------
form = tk.LabelFrame(add_tab, text="Student Details", padx=15, pady=15)
form.pack(padx=10, pady=10, fill="x")

labels = ["Roll No", "Name", "Course", "CGPA"]
entries = {}
for i, lbl in enumerate(labels):
    tk.Label(form, text=lbl + ":").grid(row=i, column=0, sticky="e", pady=5, padx=5)
    e = tk.Entry(form, width=30)
    e.grid(row=i, column=1, pady=5, padx=5)
    entries[lbl] = e

def add_student():
    roll_no = entries["Roll No"].get().strip()
    name = entries["Name"].get().strip()
    course = entries["Course"].get().strip()
    cgpa = entries["CGPA"].get().strip()

    if not (roll_no and name and course and cgpa):
        messagebox.showwarning("Missing Fields", "Please fill in all fields.")
        return
    try:
        cgpa = float(cgpa)
    except ValueError:
        messagebox.showerror("Invalid CGPA", "CGPA must be a number.")
        return

    # Update if roll_no already exists, else add new
    for s in students:
        if s["roll_no"] == roll_no:
            s.update({"name": name, "course": course, "cgpa": cgpa})
            break
    else:
        students.append({"roll_no": roll_no, "name": name, "course": course, "cgpa": cgpa})

    save_students(students)
    refresh_tree()
    for e in entries.values():
        e.delete(0, "end")
    messagebox.showinfo("Saved", f"Student {roll_no} saved successfully.")

tk.Button(add_tab, text="Save Student", command=add_student, bg="#1B2A4A", fg="white").pack(pady=10)

refresh_tree()
root.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

root = tk.Tk()
root.title("Student Management System - GLA University")
root.geometry("650x480")

DATA_FILE = "students.json"

def load_students():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_students(students):
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=2)

students = load_students()

# ---------- Menu Bar ----------
menubar = tk.Menu(root)
root.config(menu=menubar)

def show_about():
    messagebox.showinfo("About", "Student Management System v1.0\nGLA University")

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menubar.add_cascade(label="Help", menu=help_menu)

# ---------- Notebook (Tabs) ----------
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

records_tab = ttk.Frame(notebook)
add_tab = ttk.Frame(notebook)
notebook.add(records_tab, text="Student Records")
notebook.add(add_tab, text="Add / Update Student")

# ---------- Records Tab: Treeview + Search ----------
search_frame = tk.Frame(records_tab)
search_frame.pack(fill="x", pady=5)

tk.Label(search_frame, text="Search by name:").pack(side="left", padx=5)
search_var = tk.StringVar()
search_entry = tk.Entry(search_frame, textvariable=search_var)
search_entry.pack(side="left", padx=5)

columns = ("roll_no", "name", "course", "cgpa")
tree = ttk.Treeview(records_tab, columns=columns, show="headings", height=12)
for col, label in zip(columns, ["Roll No", "Name", "Course", "CGPA"]):
    tree.heading(col, text=label)
    tree.column(col, width=130)
tree.pack(fill="both", expand=True, padx=5, pady=5)

def refresh_tree(filtered=None):
    tree.delete(*tree.get_children())
    data = filtered if filtered is not None else students
    for s in data:
        tree.insert("", "end", values=(s["roll_no"], s["name"], s["course"], s["cgpa"]))

def search_students(*args):
    query = search_var.get().lower()
    filtered = [s for s in students if query in s["name"].lower()]
    refresh_tree(filtered)

search_var.trace_add("write", search_students)   # runs search_students on every keystroke

def delete_selected():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("No Selection", "Select a student to delete.")
        return
    values = tree.item(selected[0])["values"]
    roll_no = values[0]
    students[:] = [s for s in students if s["roll_no"] != roll_no]
    save_students(students)
    refresh_tree()

tk.Button(records_tab, text="Delete Selected", command=delete_selected, bg="#B9791F", fg="white").pack(pady=5)

# ---------- Add/Update Tab ----------
form = tk.LabelFrame(add_tab, text="Student Details", padx=15, pady=15)
form.pack(padx=10, pady=10, fill="x")

labels = ["Roll No", "Name", "Course", "CGPA"]
entries = {}
for i, lbl in enumerate(labels):
    tk.Label(form, text=lbl + ":").grid(row=i, column=0, sticky="e", pady=5, padx=5)
    e = tk.Entry(form, width=30)
    e.grid(row=i, column=1, pady=5, padx=5)
    entries[lbl] = e

def add_student():
    roll_no = entries["Roll No"].get().strip()
    name = entries["Name"].get().strip()
    course = entries["Course"].get().strip()
    cgpa = entries["CGPA"].get().strip()

    if not (roll_no and name and course and cgpa):
        messagebox.showwarning("Missing Fields", "Please fill in all fields.")
        return
    try:
        cgpa = float(cgpa)
    except ValueError:
        messagebox.showerror("Invalid CGPA", "CGPA must be a number.")
        return

    # Update if roll_no already exists, else add new
    for s in students:
        if s["roll_no"] == roll_no:
            s.update({"name": name, "course": course, "cgpa": cgpa})
            break
    else:
        students.append({"roll_no": roll_no, "name": name, "course": course, "cgpa": cgpa})

    save_students(students)
    refresh_tree()
    for e in entries.values():
        e.delete(0, "end")
    messagebox.showinfo("Saved", f"Student {roll_no} saved successfully.")

tk.Button(add_tab, text="Save Student", command=add_student, bg="#1B2A4A", fg="white").pack(pady=10)

refresh_tree()
root.mainloop()