from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu4 = None
ans = 0

def normal(window, ans3, qu3, qu2, qu1):
    global qu4, ans
    ans += ans3
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)

    question = QLabel("", window)
    question.setFont(font)
    question.setWordWrap(True)
    question.setAlignment(Qt.AlignCenter)

    # Set the question text in English based on the random instance
    if instance == 1:
        question.setText("4. Which U.S. state is the largest by area?")
    elif instance == 2:
        question.setText("4. Which of the following Asian countries is an island nation?")
    elif instance == 3:
        question.setText("4. Which country has the highest population density in Asia?")

    window_width = window.frameGeometry().width()
    question_width = 600
    question_height = 100
    question_x = (window_width - question_width) // 2
    question_y = 20
    question.setGeometry(question_x, question_y, question_width, question_height)
    question.setStyleSheet("font-size: 20px; font-weight: bold;")
    question.show()

    def next_question():
        import normal5
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu4)
        normal5.normal(window, ans, qu4, qu3, qu2, qu1)

    # Answer button callbacks for each possible answer
    # Each function checks which question is active and updates the score and correctness accordingly
    def answer_a():
        global qu4, ans
        if instance == 1:
            qu4 = False
            next_question()
        elif instance == 2:
            qu4 = False
            next_question()
        elif instance == 3:
            qu4 = True
            ans += 2
            next_question()

    def answer_b():
        global qu4, ans
        if instance == 1:
            qu4 = False
            next_question()
        elif instance == 2:
            qu4 = False
            next_question()
        elif instance == 3:
            qu4 = False
            next_question()

    def answer_c():
        global qu4, ans
        if instance == 1:
            qu4 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu4 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu4 = False
            next_question()

    def answer_d():
        global qu4, ans
        if instance == 1:
            qu4 = False
            next_question()
        elif instance == 2:
            qu4 = False
            next_question()
        elif instance == 3:
            qu4 = False
            next_question()

    # Set the button texts in English according to the question instance
    def set_button_texts():
        if instance == 1:
            button_a.setText("A) Texas")
            button_b.setText("B) California")
            button_c.setText("C) Alaska")  # correct
            button_d.setText("D) Montana")
        elif instance == 2:
            button_a.setText("A) Malaysia")
            button_b.setText("B) Bangladesh")
            button_c.setText("C) Sri Lanka")  # correct
            button_d.setText("D) Myanmar")
        elif instance == 3:
            button_a.setText("A) Bangladesh")  # correct
            button_b.setText("B) India")
            button_c.setText("C) China")
            button_d.setText("D) Japan")

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