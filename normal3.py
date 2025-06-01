from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu3 = None
ans = 0

def normal(window, ans2, qu2, qu1):
    global qu3, ans
    ans += ans2
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)

    question = QLabel("", window)
    question.setFont(font)
    question.setWordWrap(True)
    question.setAlignment(Qt.AlignCenter)

    # Set the question text in English based on the random instance
    if instance == 1:
        question.setText("3. What is the largest island in South America?")
    elif instance == 2:
        question.setText("3. Which South American country has two official languages: Spanish and Guarani?")
    elif instance == 3:
        question.setText("3. Which country has the most languages in the world?")

    window_width = window.frameGeometry().width()
    question_width = 600
    question_height = 100
    question_x = (window_width - question_width) // 2
    question_y = 20
    question.setGeometry(question_x, question_y, question_width, question_height)
    question.setStyleSheet("font-size: 20px; font-weight: bold;")
    question.show()

    def next_question():
        import normal4
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu3)
        normal4.normal(window, ans, qu3, qu2, qu1)

    # Answer button callbacks for each possible answer
    # Each function checks which question is active and updates the score and correctness accordingly
    def answer_a():
        global qu3, ans
        if instance == 1:
            qu3 = False
            next_question()
        elif instance == 2:
            qu3 = False
            next_question()
        elif instance == 3:
            qu3 = False
            next_question()

    def answer_b():
        global qu3, ans
        if instance == 1:
            qu3 = False
            next_question()
        elif instance == 2:
            qu3 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu3 = False
            next_question()

    def answer_c():
        global qu3, ans
        if instance == 1:
            qu3 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu3 = False
            next_question()
        elif instance == 3:
            qu3 = False
            next_question()

    def answer_d():
        global qu3, ans
        if instance == 1:
            qu3 = False
            next_question()
        elif instance == 2:
            qu3 = False
            next_question()
        elif instance == 3:
            qu3 = True
            ans += 2
            next_question()

    # Set the button texts in English according to the question instance
    def set_button_texts():
        if instance == 1:
            button_a.setText("A) Margarita Island")
            button_b.setText("B) Chiloé Island")
            button_c.setText("C) Tierra del Fuego")  # correct
            button_d.setText("D) Saint Martin")
        elif instance == 2:
            button_a.setText("A) Chile")
            button_b.setText("B) Paraguay")  # correct
            button_c.setText("C) Suriname")
            button_d.setText("D) Venezuela")
        elif instance == 3:
            button_a.setText("A) India")
            button_b.setText("B) China")
            button_c.setText("C) Indonesia")
            button_d.setText("D) Papua New Guinea")  # correct

    # Create answer buttons and connect them to the correct callback
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

    set_button_texts()