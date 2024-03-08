from tkinter import *
from PIL import Image, ImageTk
from random import randint, choice, shuffle

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.my_menu = Menu(root)
        root.config(menu=self.my_menu)
        self.quiz_frame = Frame(root)
        self.word_jumble_frame = Frame(root)
        self.quiz_img = None  # Initialize quiz_img as an instance variable
        self.setup_menu()

    def setup_menu(self):
        menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Menu", menu=menu)
        menu.add_command(label="Quiz", command=self.quiz)
        menu.add_command(label="Word Jumble", command=self.word_jumble)
        menu.add_separator()
        menu.add_command(label="Exit", command=self.root.quit)

    def quiz(self):
        self.hide_prev_frame()
        self.quiz_frame.pack(fill=BOTH, expand=1)
        my_label = Label(self.quiz_frame, text="Quiz")
        my_label.pack()

        self.our_quiz = ["bull", "bear", "crash", "dividend", "green", "ipo"]
        self.rando = randint(0, len(self.our_quiz)-1)
        state = "questions/"+ self.our_quiz[self.rando] + ".png"

        self.quiz_img = ImageTk.PhotoImage(Image.open(state))
        show_state = Label(self.quiz_frame, image=self.quiz_img)
        show_state.pack()

        self.answer_input = Entry(self.quiz_frame, font=("Helvetica", 12, "bold"))
        self.answer_input.pack(pady=7)

        rando_button = Button(self.quiz_frame, text="Next", command=self.next_question, width=10, pady=4)
        rando_button.pack(pady=7)

        answer_button = Button(self.quiz_frame, text="Check", command=self.quiz_answer, width=10, pady=4)
        answer_button.pack(pady=7)
        self.answer_label = Label(self.quiz_frame, text="", font=("Helvetica", 12, "bold"))
        self.answer_label.pack(pady=7)

    def quiz_answer(self):
        answer = self.answer_input.get()
        if answer.lower() == self.our_quiz[self.rando]:
            self.answer_label.config(text="Correct", foreground="green")
        else:
            self.answer_label.config(text="Incorrect", foreground="red")

    def word_jumble(self):
        self.hide_prev_frame()
        self.word_jumble_frame.pack(fill=BOTH, expand=1)
        my_label = Label(self.word_jumble_frame, text="Word Jumble")
        my_label.pack()

        self.jumble_label = Label(self.word_jumble_frame, text="", font=("Helvetica", 20, "bold"), background="#003872", foreground="white", pady="40", padx="40", width="30")
        self.jumble_label.pack(pady="20")

        self.shuffler() # Call shuffler to generate initial jumbled word

        self.entry_answer = Entry(self.word_jumble_frame, font=("Helvetica", 12))
        self.entry_answer.pack(pady="7")
        jumble_button = Button(self.word_jumble_frame, text="Next", command=self.next_word_jumble, width=10, pady=4)
        jumble_button.pack(pady="7")
        answer_button = Button(self.word_jumble_frame, text="Answer", command=self.answer_jumble, width=10, pady=4)
        answer_button.pack(pady="7")
        self.jumble_answer_label = Label(self.word_jumble_frame, text="", font=("Helvetica", 12, "bold"))
        self.jumble_answer_label.pack(pady=7)

    def shuffler(self):
        state2 = ["dividend", "stock", "broker", "ipo"]
        self.word = choice(state2)

        break_apart_word = list(self.word)
        shuffle(break_apart_word)

        shuffled_word = ""
        for letter in break_apart_word:
            shuffled_word += letter
        self.jumble_label.config(text=shuffled_word)

    def answer_jumble(self):
        if self.word == self.entry_answer.get():
            self.jumble_answer_label.config(text="Correct", foreground="green")
        else:
            self.jumble_answer_label.config(text="Incorrect", foreground="red")

    def hide_prev_frame(self):
        for widget in self.quiz_frame.winfo_children():
            widget.destroy()

        for widget in self.word_jumble_frame.winfo_children():
            widget.destroy()

        self.quiz_frame.pack_forget()
        self.word_jumble_frame.pack_forget()

    def next_question(self):
        self.quiz()  # Generate next question

    def next_word_jumble(self):
        self.shuffler() # Generate next word
        self.entry_answer.delete(0, END)  # Clear entry field
        self.jumble_answer_label.config(text="")  # Clear answer label

# Assuming Dashboard.py is correctly set up to create an instance of FlashcardApp
