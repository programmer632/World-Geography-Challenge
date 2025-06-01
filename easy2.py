from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu2 = None
ans = 0

# Main function for the second 'Easy' quiz question
# Receives the window, previous score, and correctness of the first question
# Sets up the second question and answer buttons

def easy(window, ans1, qu1):
    global qu2, ans
    ans += ans1  # Add previous score to current score
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)  # Randomly select which question to show

    # Create the question label, centered horizontally
    question = QLabel("", window)
    question.setFont(font)
    question.setAlignment(Qt.AlignCenter)

    # Set the question text based on the random variant (all in English)
    if instance == 1:
        question.setText('''2. To which country does Corsica belong?''')
    elif instance == 2:
        question.setText('''2. Which is the largest country by area
located entirely in Europe?''')
    elif instance == 3:
        question.setText('''2. To which country do the Faroe Islands belong?''')

    # Calculate position to center the label horizontally and place it near the top
    window_width = window.frameGeometry().width()
    question_width = 600
    question_height = 100
    question_x = (window_width - question_width) // 2
    question_y = 20

    question.setGeometry(question_x, question_y, question_width, question_height)
    question.setStyleSheet("font-size: 20px; font-weight: bold;")
    question.show()

    # Function to proceed to the next question (calls easy3.easy)
    def next_question():
        import easy3
        # Remove all widgets from the window before showing the next question
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu2)
        easy3.easy(window, ans, qu2, qu1)

    # Answer button callbacks for each possible answer
    # Each function checks which question is active and updates the score and correctness accordingly
    def answer_france():
        global qu2, ans
        if instance == 1:
            qu2 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu2 = False
            next_question()
        elif instance == 3:
            qu2 = False
            next_question()

    def answer_spain():
        global qu2, ans
        if instance == 1:
            qu2 = False
            next_question()
        elif instance == 2:
            qu2 = False
            next_question()
        elif instance == 3:
            qu2 = False
            next_question()

    def answer_ukraine():
        global qu2, ans
        if instance == 1:
            qu2 = False
            next_question()
        elif instance == 2:
            qu2 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu2 = False
            next_question()

    def answer_poland():
        global qu2, ans
        if instance == 1:
            qu2 = False
            next_question()
        elif instance == 2:
            qu2 = False
            next_question()
        elif instance == 3:
            qu2 = True
            ans += 2
            next_question()

    # Set the button texts according to the question instance (all in English)
    def set_correct_text():
        if instance == 1:
            button_a.setText("A) France")
            button_b.setText("B) Spain")
            button_c.setText("C) Ukraine")
            button_d.setText("D) Poland")
        elif instance == 2:
            button_a.setText("A) France")
            button_b.setText("B) Spain")
            button_c.setText("C) Ukraine")
            button_d.setText("D) Poland")
        elif instance == 3:
            button_a.setText("A) France")
            button_b.setText("B) Spain")
            button_c.setText("C) Ukraine")
            button_d.setText("D) Poland")

    # Create answer buttons and connect them to the correct callback
    button_a = QPushButton("A) France", window)
    button_a.resize(500, 120)
    button_a.move(250, 140)
    button_a.setFont(font)
    button_a.show()
    button_a.clicked.connect(answer_france)

    button_b = QPushButton("B) Spain", window)
    button_b.setFont(font)
    button_b.resize(500, 120)
    button_b.move(250, 270)
    button_b.show()
    button_b.clicked.connect(answer_spain)

    button_c = QPushButton("C) Ukraine", window)
    button_c.resize(500, 120)
    button_c.move(250, 400)
    button_c.setFont(font)
    button_c.show()
    button_c.clicked.connect(answer_ukraine)

    button_d = QPushButton("D) Poland", window)
    button_d.resize(500, 120)
    button_d.move(250, 530)
    button_d.setFont(font)
    button_d.show()
    button_d.clicked.connect(answer_poland)

    set_correct_text()