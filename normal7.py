from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu7 = None
ans = 0

def normal(window, ans6, qu6, qu5, qu4, qu3, qu2, qu1):
    global qu7, ans
    ans += ans6
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)

    question = QLabel("", window)
    question.setFont(font)
    question.setWordWrap(True)
    question.setAlignment(Qt.AlignCenter)

    # Set the question text in English based on the random instance
    # Each question is unique and tests knowledge of world geography
    if instance == 1:
        question.setText("7. What is the longest river in Asia?")
    elif instance == 2:
        question.setText("7. In which American country is Machu Picchu located?")
    elif instance == 3:
        question.setText("7. What is the capital city of Argentina?")

    window_width = window.frameGeometry().width()
    question_width = 600
    question_height = 100
    question_x = (window_width - question_width) // 2
    question_y = 20
    question.setGeometry(question_x, question_y, question_width, question_height)
    question.setStyleSheet("font-size: 20px; font-weight: bold;")
    question.show()

    def next_question():
        # Proceed to the next question (normal8)
        import normal8
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu7)
        normal8.normal(window, ans, qu7, qu6, qu5, qu4, qu3, qu2, qu1)

    # Answer button callbacks for each possible answer
    # Each function checks which question is active and updates the score and correctness accordingly
    # The correct answer for each question is marked in the set_button_texts function
    def answer_a():
        global qu7, ans
        if instance == 1:
            qu7 = True   # Yangtze is correct
            ans += 2
            next_question()
        elif instance == 2:
            qu7 = False  # Ecuador is not correct
            next_question()
        elif instance == 3:
            qu7 = False  # Montevideo is not correct
            next_question()

    def answer_b():
        global qu7, ans
        if instance == 1:
            qu7 = False  # Ganges is not correct
            next_question()
        elif instance == 2:
            qu7 = False  # Bolivia is not correct
            next_question()
        elif instance == 3:
            qu7 = False  # Santiago is not correct
            next_question()

    def answer_c():
        global qu7, ans
        if instance == 1:
            qu7 = False  # Mekong is not correct
            next_question()
        elif instance == 2:
            qu7 = True   # Peru is correct
            ans += 2
            next_question()
        elif instance == 3:
            qu7 = True   # Buenos Aires is correct
            ans += 2
            next_question()

    def answer_d():
        global qu7, ans
        if instance == 1:
            qu7 = False  # Ob is not correct
            next_question()
        elif instance == 2:
            qu7 = False  # Chile is not correct
            next_question()
        elif instance == 3:
            qu7 = False  # Rio de Janeiro is not correct
            next_question()

    # Set the button texts in English according to the question instance
    # The correct answer is marked with a comment for clarity
    def set_button_texts():
        if instance == 1:
            button_a.setText("A) Yangtze")  # correct
            button_b.setText("B) Ganges")
            button_c.setText("C) Mekong")
            button_d.setText("D) Ob")
        elif instance == 2:
            button_a.setText("A) Ecuador")
            button_b.setText("B) Bolivia")
            button_c.setText("C) Peru")  # correct
            button_d.setText("D) Chile")
        elif instance == 3:
            button_a.setText("A) Montevideo")
            button_b.setText("B) Santiago")
            button_c.setText("C) Buenos Aires")  # correct
            button_d.setText("D) Rio de Janeiro")

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