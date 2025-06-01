from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu10 = None
ans = 0

def normal(window, ans9, qu9, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1):
    global qu10, ans
    ans += ans9
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)

    question = QLabel("", window)
    question.setFont(font)
    question.setWordWrap(True)
    question.setAlignment(Qt.AlignCenter)

    # Set the question text in English based on the random instance
    # Each question is unique and tests knowledge of world geography
    if instance == 1:
        question.setText("10. What is the largest active volcano in Asia?")
    elif instance == 2:
        question.setText("10. Which is the only South American country with coasts on both the Atlantic and Pacific Oceans?")
    elif instance == 3:
        question.setText("10. What is the highest mountain in North America?")

    window_width = window.frameGeometry().width()
    question_width = 600
    question_height = 100
    question_x = (window_width - question_width) // 2
    question_y = 20
    question.setGeometry(question_x, question_y, question_width, question_height)
    question.setStyleSheet("font-size: 20px; font-weight: bold;")
    question.show()

    def next_question():
        # Proceed to the marks/results screen (marks)
        import marks
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu10)
        marks.show_marks(window, ans, qu10, qu9, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1)

    # Answer button callbacks for each possible answer
    # Each function checks which question is active and updates the score and correctness accordingly
    # The correct answer for each question is marked in the set_button_texts function
    def answer_a():
        global qu10, ans
        if instance == 1:
            qu10 = True   # Mount Fuji is correct
            ans += 2
            next_question()
        elif instance == 2:
            qu10 = True   # Colombia is correct
            ans += 2
            next_question()
        elif instance == 3:
            qu10 = False  # Mount Rainier is not correct
            next_question()

    def answer_b():
        global qu10, ans
        if instance == 1:
            qu10 = False  # Krakatoa is not correct
            next_question()
        elif instance == 2:
            qu10 = False  # Argentina is not correct
            next_question()
        elif instance == 3:
            qu10 = False  # Mount St. Elias is not correct
            next_question()

    def answer_c():
        global qu10, ans
        if instance == 1:
            qu10 = False  # Tambora is not correct
            next_question()
        elif instance == 2:
            qu10 = False  # Chile is not correct
            next_question()
        elif instance == 3:
            qu10 = True   # Mount McKinley (Denali) is correct
            ans += 2
            next_question()

    def answer_d():
        global qu10, ans
        if instance == 1:
            qu10 = False  # Erebus is not correct
            next_question()
        elif instance == 2:
            qu10 = False  # Uruguay is not correct
            next_question()
        elif instance == 3:
            qu10 = False  # Orizaba is not correct
            next_question()

    # Set the button texts in English according to the question instance
    # The correct answer is marked with a comment for clarity
    def set_button_texts():
        if instance == 1:
            button_a.setText("A) Mount Fuji")  # correct
            button_b.setText("B) Krakatoa")
            button_c.setText("C) Tambora")
            button_d.setText("D) Erebus")
        elif instance == 2:
            button_a.setText("A) Colombia")  # correct
            button_b.setText("B) Argentina")
            button_c.setText("C) Chile")
            button_d.setText("D) Uruguay")
        elif instance == 3:
            button_a.setText("A) Mount Rainier")
            button_b.setText("B) Mount St. Elias")
            button_c.setText("C) Mount McKinley (Denali)")  # correct
            button_d.setText("D) Orizaba")

    # Create answer buttons and connect them to the correct callback
    # All buttons are styled and positioned consistently
    button_a = QPushButton("A)", window)
    button_a.resize(500, 120)
    button_a.move(250, 140)
    button_a.setFont(font)
    button_a.show()
    button_a.clicked.connect(answer_a)

    button_b = QPushButton("B)", window)
    button_b.setFont(font)
    button_b.resize(500, 120)
    button_b.move(250, 270)
    button_b.show()
    button_b.clicked.connect(answer_b)

    button_c = QPushButton("C)", window)
    button_c.resize(500, 120)
    button_c.move(250, 400)
    button_c.setFont(font)
    button_c.show()
    button_c.clicked.connect(answer_c)

    button_d = QPushButton("D)", window)
    button_d.resize(500, 120)
    button_d.move(250, 530)
    button_d.setFont(font)
    button_d.show()
    button_d.clicked.connect(answer_d)

    set_button_texts()  # Set the answer texts for the current question