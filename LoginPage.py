from tkinter import *
import mysql.connector
from conn import db, cursor

root = Tk()
root.title("Login Page")
root.geometry("1550x1000")
root.minsize(200, 100)
root.configure(background="#001F3F")
# Variables
name_var = StringVar()
pass_var = StringVar()


# Form Submit function
def submit():
    name = name_var.get()
    password = pass_var.get()
    if check_cred(name, password):
        print("Login successful")
        name_var.set("")
        pass_var.set("")
        #  Show register page function
        root.destroy()
        import Dashboard
    else:
        print("Invalid credentials")
        # Error Frame
        f2 = Frame(root, background="#001F3F")
        f2.place(anchor=CENTER, relx=0.5, rely=0.5)
        error_label = Label(f2, text="Invalid credentials", padx="20", pady="20", background="#001F3F", foreground="white", font=("Helvetica", 12, "bold"))
        error_label.pack()
        b1 = Button(f2, text="Close", command=f2.destroy, background="red")
        b1.pack(padx="20", pady="20")


def check_cred(username, password):
    try:
        query = "select * from userinfo where username = %s and userpassword = %s"
        values = (username, password)
        cursor.execute(query, values)
        result = cursor.fetchone()
        return result is not None
    except mysql.connector.Error as err:
        print(f"Error {err}")
        return False


# Frame
f1 = Frame(root, background="#003872", relief=SUNKEN)
f1.place(anchor=CENTER, relx=0.5, rely=0.5)


# Login Photo
photo = PhotoImage(file="my-profile.png")
resize_login_photo = photo.subsample(5,5)
login_photo = Label(f1, image=resize_login_photo, background="#003872")
login_photo.grid(row=0, column=0, columnspan=2)

# Username
l1 = Label(f1, text="Username", background="#003872", padx="10", pady="10", foreground="white", font=("Helvetica", 12, "bold"))
l1.grid(row=1, column=0)
e1 = Entry(f1, textvariable=name_var, font=("Helvetica", 12))
e1.grid(row=1, column=1, padx="20", pady="10")

# Password
l1 = Label(f1, text="Password", background="#003872", padx="10", pady="10", foreground="white", font=("Helvetica", 12, "bold"))
l1.grid(row=2, column=0)
e1 = Entry(f1, textvariable=pass_var, font=("Helvetica", 12), show="*")
e1.grid(row=2, column=1, padx="20", pady="10")

# login button
button1 = Button(f1, text="Login", command=submit, background="#E9AB17", foreground="black", padx=20, pady=10, font=("Helvetica", 10, "bold"))
button1.grid(row=3, column=0, columnspan=2, pady="10")

root.mainloop()