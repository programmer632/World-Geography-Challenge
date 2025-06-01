from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu9 = None
ans = 0

# Main function for the ninth 'Easy' quiz question
# Receives the window, previous score, and correctness of previous questions
# Sets up the ninth question and answer buttons

def easy(window, ans8, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1):
    global qu9, ans
    ans += ans8  # Add previous score to current score
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)  # Randomly select which question to show

    # Create the question label, centered horizontally
    question = QLabel("", window)
    question.setFont(font)
    question.setAlignment(Qt.AlignCenter)

    # Set the question text based on the random variant (all in English)
    if instance == 1:
        question.setText('''9. What is the capital of Hungary?''')
    elif instance == 2:
        question.setText('''9. Which of the following country-capital pairs
is a correct match?''')
    elif instance == 3:
        question.setText('''9. What is the longest river in Europe?''')

    # Calculate position to center the label horizontally and place it near the top
    window_width = window.frameGeometry().width()
    question_width = 600
    question_height = 100
    question_x = (window_width - question_width) // 2
    question_y = 20
    question.setGeometry(question_x, question_y, question_width, question_height)
    question.setStyleSheet("font-size: 20px; font-weight: bold;")
    question.show()

    # Function to proceed to the next question (calls easy10.easy)
    def next_question():
        import easy10
        # Remove all widgets from the window before showing the next question
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu9)
        easy10.easy(window, ans, qu9, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1)

    # Answer button callbacks for each possible answer
    # Each function checks which question is active and updates the score and correctness accordingly
    def answer_dania():
        global qu9, ans
        if instance == 1:
            qu9 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu9 = False
            next_question()
        elif instance == 3:
            qu9 = False
            next_question()

    def answer_kroatia():
        global qu9, ans
        if instance == 1:
            qu9 = False
            next_question()
        elif instance == 2:
            qu9 = False
            next_question()
        elif instance == 3:
            qu9 = True
            ans += 2
            next_question()

    def answer_norway():
        global qu9, ans
        if instance == 1:
            qu9 = False
            next_question()
        elif instance == 2:
            qu9 = False
            next_question()
        elif instance == 3:
            qu9 = False
            next_question()

    def answer_lichtenstain():
        global qu9, ans
        if instance == 1:
            qu9 = False
            next_question()
        elif instance == 2:
            qu9 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu9 = False
            next_question()

    # Set the button texts according to the question instance (all in English)
    def set_correct_text():
        if instance == 1:
            dania.setText("A) Budapest")
            kroatia.setText("B) Belgrade")
            norway.setText("C) Vienna")
            poland.setText("D) Prague")
        if instance == 2:
            dania.setText("A) Georgia-Yerevan")
            kroatia.setText("B) Armenia-Tbilisi")
            norway.setText("C) Armenia-Baku")
            poland.setText("D) Georgia-Tbilisi")
        if instance == 3:
            dania.setText("A) Danube")
            kroatia.setText("B) Volga")
            norway.setText("C) Rhine")
            poland.setText("D) Seine")

    # Create answer buttons and connect them to the correct callback
    dania = QPushButton("A) Denmark", window)
    dania.resize(500, 120)
    dania.move(250, 140)
    dania.setFont(font)
    dania.show()
    dania.clicked.connect(answer_dania)

    kroatia = QPushButton("B) Croatia", window)
    kroatia.setFont(font)
    kroatia.resize(500, 120)
    kroatia.move(250, 270)
    kroatia.show()
    kroatia.clicked.connect(answer_kroatia)

    norway = QPushButton("C) Norway", window)
    norway.resize(500, 120)
    norway.move(250, 400)
    norway.setFont(font)
    norway.show()
    norway.clicked.connect(answer_norway)

    poland = QPushButton("D) Liechtenstein", window)
    poland.resize(500, 120)
    poland.move(250, 530)
    poland.setFont(font)
    poland.show()
    poland.clicked.connect(answer_lichtenstain)
    set_correct_text()