from tkinter import *
from PIL import Image, ImageTk
from random import randint, choice, shuffle

root = Tk()
root.title("Games")
root.geometry("800x600")

my_menu = Menu(root)
root.config(menu=my_menu)


def quiz():
    hide_prev_frame()
    quiz_frame.pack(fill=BOTH, expand=1)
    my_label = Label(quiz_frame, text="Quiz")
    my_label.pack()

    global our_quiz
    our_quiz = ["bull", "bear", "crash", "dividend", "green", "ipo"]
    global rando
    rando = randint(0, len(our_quiz)-1)
    state = "questions/"+ our_quiz[rando] + ".png"

    global quiz_img
    quiz_img = ImageTk.PhotoImage(Image.open(state))
    show_state = Label(quiz_frame, image=quiz_img)
    show_state.pack()

    # Answer input
    global answer_input
    answer_input = Entry(quiz_frame, font=("Helvetica", 12, "bold"))
    answer_input.pack(pady=7)

    # Button
    rando_button = Button(quiz_frame, text="Next", command=next_question, width=10, pady=4)
    rando_button.pack(pady=7)

    # Answer Button
    answer_button = Button(quiz_frame, text="Check", command=quiz_answer, width=10, pady=4)
    answer_button.pack(pady=7)
    # Answer Label
    global answer_label
    answer_label = Label(quiz_frame, text="", font=("Helvetica", 12, "bold"))
    answer_label.pack(pady=7)


def quiz_answer():
    answer = answer_input.get()
    if answer.lower() == our_quiz[rando]:
        answer_label.config(text="Correct", foreground="green")
    else:
        answer_label.config(text="Incorrect", foreground="red")

def word_jumble():
    hide_prev_frame()
    word_jumble_frame.pack(fill=BOTH, expand=1)
    my_label = Label(word_jumble_frame, text="Word Jumble")
    my_label.pack()

    global jumble_label
    jumble_label = Label(word_jumble_frame, text="", font=("Helvetica", 20, "bold"), background="#003872", foreground="white", pady="40", padx="40", width="30")
    jumble_label.pack(pady="20")

    shuffler()  # Call shuffler to generate initial jumbled word

    global entry_answer
    entry_answer = Entry(word_jumble_frame, font=("Helvetica", 12))
    entry_answer.pack(pady="7")
    jumble_button = Button(word_jumble_frame, text="Next", command=next_word_jumble, width=10, pady=4)
    jumble_button.pack(pady="7")
    answer_button = Button(word_jumble_frame, text="Answer", command=answer_jumble, width=10, pady=4)
    answer_button.pack(pady="7")
    global jumble_answer_label
    jumble_answer_label = Label(word_jumble_frame, text="", font=("Helvetica", 12, "bold"))
    jumble_answer_label.pack(pady="7")


def shuffler():
    state2 = ["dividend", "stock", "broker", "ipo"]
    global word
    word = choice(state2)

    # Break apart word
    break_apart_word = list(word)
    shuffle(break_apart_word)

    shuffled_word = ""
    for letter in break_apart_word:
        shuffled_word += letter
    jumble_label.config(text=shuffled_word)

def answer_jumble():
    if word == entry_answer.get():
        jumble_answer_label.config(text="Correct", foreground="green")
    else:
        jumble_answer_label.config(text="Incorrect", foreground="red")

def hide_prev_frame():
    for widget in quiz_frame.winfo_children():
        widget.destroy()

    for widget in word_jumble_frame.winfo_children():
        widget.destroy()

    quiz_frame.pack_forget()
    word_jumble_frame.pack_forget()


def next_question():
    quiz()  # Generate next question

def next_word_jumble():
    shuffler()  # Generate next word
    entry_answer.delete(0, END)  # Clear entry field
    jumble_answer_label.config(text="")  # Clear answer label


menu = Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=menu)
menu.add_command(label="Quiz", command=quiz)
menu.add_command(label="Word Jumble", command=word_jumble)
menu.add_separator()
menu.add_command(label="Exit", command=root.quit)

quiz_frame = Frame(root, height=500, width=500)
word_jumble_frame = Frame(root, height=500, width=500)

root.mainloop()
