from tkinter import *

root = Tk()
root.title("Stock Market Analysis")
root.geometry("1550x1000")
root.minsize(200, 100)
root.configure(background="#001F3F")


#  Show login page function
def show_login_page():
    root.destroy()
    import LoginPage


#  Show register page function
def show_register_page():
    root.destroy()
    import RegisterPage


# Frame
f1 = Frame(root, background="#003872", relief=SUNKEN)
f1.place(anchor=CENTER, relx=0.5, rely=0.5)

# LOGO NAME
n1 = Label(text="InvestHub", background="#001F3F", foreground="white", font=("Tahoma", 40, "bold"))
n1.pack(pady=50)

# Login Photo
photo = PhotoImage(file="my-profile.png")
resize_login_photo = photo.subsample(5,5)
login_photo = Label(f1, image=resize_login_photo, background="#003872")
login_photo.pack()

# Login label
login_label = Label(f1, text="Welcome! Please Login or Register", background="#003872", foreground="white", font=("Helvetica", 10, "italic"))
login_label.pack()

# Button Frame
button_frame = Frame(f1, background="#003872")
button_frame.pack()

# login button
button1 = Button(button_frame, width=14, command=show_login_page, text="Login", background="#E9AB17", foreground="black", pady=10, font=("Helvetica", 12, "bold"))
button1.pack(side=LEFT)
# register button
button1 = Button(button_frame, width=15, command=show_register_page, text="Register", background="#E9AB17", foreground="black", pady=10, font=("Helvetica", 12, "bold"))
button1.pack(side=LEFT)
# close button
button = Button(f1, width=30, text="Exit", command=root.destroy, background="red", foreground="white", pady=10, font=("Helvetica", 12, "bold"))
button.pack()
root.mainloop()