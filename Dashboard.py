from tkinter import *

root = Tk()
root.geometry("1550x1000")
root.title("Dashboard")
root.configure(background="#003872")


def show_analyze():
    import AnalyzePage


def show_chart():
    import ChartPage


def show_compare():
    import ComparePage


def show_learn():
    import LearnPage

def show_news():
    import NewsPage


def show_games():
    import Flashcard


# Sidebar
f1 = Frame(root, background="#003872", relief=SUNKEN)
f1.place(anchor=CENTER, relx=0.5, rely=0.5)
f1.grid(row=1, column=0, padx=20, pady=20)
s1 = Button(f1, text="Analyze", command=show_analyze, background="#001F3F", foreground="white", font=("Helvetica", 15, "bold"), padx="50", pady="50")
s1.grid(row=1, column=0, padx=10, pady=10)
s2 = Button(f1, text="Charts", command=show_chart, background="#001F3F", foreground="white", font=("Helvetica", 15, "bold"), padx="50", pady="50")
s2.grid(row=1, column=1, padx=10, pady=10)
s3 = Button(f1, text="Compare", command=show_compare, background="#001F3F", foreground="white", font=("Helvetica", 15, "bold"), padx="50", pady="50")
s3.grid(row=1, column=2, padx=10, pady=10)
s4 = Button(f1, text="Learn", command=show_learn, background="#001F3F", foreground="white", font=("Helvetica", 15, "bold"), padx="50", pady="50")
s4.grid(row=2, column=0, padx=10, pady=10)
s5 = Button(f1, text="News", command=show_news, background="#001F3F", foreground="white", font=("Helvetica", 15, "bold"), padx="50", pady="50")
s5.grid(row=2, column=1, padx=10, pady=10)
s6 = Button(f1, text="Games", command=show_games, background="#001F3F", foreground="white", font=("Helvetica", 15, "bold"), padx="50", pady="50")
s6.grid(row=2, column=2, padx=10, pady=10)

# Header
f2 = Frame(root, background="#001F3F", relief=SUNKEN)
f2.grid(row=0, column=0, columnspan=5, sticky="ew")
l1 = Label(f2, text="Dashboard", background="#001F3F", foreground="white", font=("Helvetica", 15, "bold"))
l1.pack(side=LEFT)
icon1 = PhotoImage(file="account1.png")
resize_icon1 = icon1.subsample(10,10)
l2 = Label(f2, image=resize_icon1, background="#001F3F")
l2.pack(side=RIGHT)

# Configure column 0 of root to be expandable
root.columnconfigure(0, weight=1)

root.mainloop()
