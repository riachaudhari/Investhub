from tkinter import *
import mysql.connector
from conn import db, cursor

root = Tk()
root.title("Register Page")
root.geometry("1550x1000")
root.minsize(200, 100)
root.configure(background="#001F3F")
# Variables
email_var = StringVar()
con_var = StringVar()
dob_var = StringVar()
name_var = StringVar()
pass_var = StringVar()


# Form Submit function
def submit():
    email = email_var.get()
    contact = con_var.get()
    age = e3.get()
    name = name_var.get()
    password = pass_var.get()

    # Verify email
    if not email.endswith("@gmail.com"):
        # Error Frame
        f2 = Frame(root, background="#001F3F")
        f2.place(anchor=CENTER, relx=0.5, rely=0.5)
        error_label = Label(f2, text="Please enter valid Email ID", padx="20", pady="20", background="#001F3F",
                            foreground="white", font=("Helvetica", 12, "bold"))
        error_label.pack()
        b1 = Button(f2, text="Close", command=f2.destroy, background="red")
        b1.pack(padx="20", pady="20")
        print("Invalid Email")
        return

    # Verify contact
    if not contact.isdigit() or len(contact) !=10:
        # Error Frame
        f2 = Frame(root, background="#001F3F")
        f2.place(anchor=CENTER, relx=0.5, rely=0.5)
        error_label = Label(f2, text="Please enter valid contact", padx="20", pady="20", background="#001F3F",
                            foreground="white", font=("Helvetica", 12, "bold"))
        error_label.pack()
        b1 = Button(f2, text="Close", command=f2.destroy, background="red")
        b1.pack(padx="20", pady="20")
        print("Invalid contact")
        return

    if not name or not password:
        # Error Frame
        f2 = Frame(root, background="#001F3F")
        f2.place(anchor=CENTER, relx=0.5, rely=0.5)
        error_label = Label(f2, text="Username and password cannot be blank", padx="20", pady="20", background="#001F3F",
                            foreground="white", font=("Helvetica", 12, "bold"))
        error_label.pack()
        b1 = Button(f2, text="Close", command=f2.destroy, background="red")
        b1.pack(padx="20", pady="20")
        return

    # Insert data into database
    query = "Insert into userinfo (useremail, usercontact, userage, username, userpassword) values(%s, %s, %s, %s, %s);"
    values = (email, contact, str(age), name, password)
    try:
        cursor.execute(query, values)
        db.commit()
        print("Registration successful")

        email_var.set("")
        con_var.set("")
        name_var.set("")
        pass_var.set("")
        #  Show login page function
        root.destroy()
        import LoginPage

    except mysql.connector.Error as err:
        print(f"Error {err}")
        db.rollback()

        # Error Frame
        f2 = Frame(root, background="#001F3F")
        f2.place(anchor=CENTER, relx=0.5, rely=0.5)
        error_label = Label(f2, text="Registration unsuccessful", padx="20", pady="20", background="#001F3F", foreground="white", font=("Helvetica", 12, "bold"))
        error_label.pack()
        b1 = Button(f2, text="Close", command=f2.destroy, background="red")
        b1.pack(padx="20", pady="20")


# Frame
f1 = Frame(root, background="#003872", relief=SUNKEN)
f1.place(anchor=CENTER, relx=0.5, rely=0.5)

# Login Photo
photo = PhotoImage(file="my-profile.png")
resize_login_photo = photo.subsample(5,5)
login_photo = Label(f1, image=resize_login_photo, background="#003872")
login_photo.grid(row=0, column=0, columnspan=2)

# Email
l2 = Label(f1, text="Email", background="#003872", padx="10", pady="5", foreground="white", font=("Helvetica", 12, "bold"))
l2.grid(row=1, column=0)
e2 = Entry(f1, textvariable=email_var, font=("Helvetica", 12))
e2.grid(row=1, column=1, padx="20", pady="5")

# Contact
l3 = Label(f1, text="Contact", background="#003872", padx="10", pady="5", foreground="white", font=("Helvetica", 12, "bold"))
l3.grid(row=2, column=0)
e3 = Entry(f1, textvariable=con_var, font=("Helvetica", 12))
e3.grid(row=2, column=1, padx="20", pady="5")

# Age
l3 = Label(f1, text="Age", background="#003872", padx="10", pady="5", foreground="white", font=("Helvetica", 12, "bold"))
l3.grid(row=3, column=0)
e3 = Scale(f1, from_=18, to=100, orient=HORIZONTAL, length="175")
e3.grid(row=3, column=1, padx="20", pady="5")

# Username
l4 = Label(f1, text="Username", background="#003872", padx="10", pady="5", foreground="white", font=("Helvetica", 12, "bold"))
l4.grid(row=4, column=0)
e4 = Entry(f1, textvariable=name_var, font=("Helvetica", 12))
e4.grid(row=4, column=1, padx="20", pady="5")

# Password
l5 = Label(f1, text="Password", background="#003872", padx="10", pady="5", foreground="white", font=("Helvetica", 12, "bold"))
l5.grid(row=5, column=0)
e5 = Entry(f1, textvariable=pass_var, font=("Helvetica", 12), show="*")
e5.grid(row=5, column=1, padx="20", pady="5")

# register button
button1 = Button(f1, text="Register", command=submit, background="#E9AB17", foreground="black", padx=20, pady=10, font=("Helvetica", 10, "bold"))
button1.grid(row=6, column=0, columnspan=2, pady="10")

root.mainloop()