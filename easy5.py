from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu5 = None
ans = 0

# Main function for the fifth 'Easy' quiz question
# Receives the window, previous score, and correctness of previous questions
# Sets up the fifth question and answer buttons

def easy(window, ans4, qu4, qu3, qu2, qu1):
    global qu5, ans
    ans += ans4  # Add previous score to current score
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)  # Randomly select which question to show

    # Create the question label, centered horizontally
    question = QLabel("", window)
    question.setFont(font)
    question.setAlignment(Qt.AlignCenter)

    # Set the question text based on the random variant (all in English)
    if instance == 1:
        question.setText('''5. Which country has German, Italian, French, and Romansh as official languages?''')
    elif instance == 2:
        question.setText('''5. Which country has Prague as its capital city?''')
    elif instance == 3:
        question.setText('''5. Which country has Sofia as its capital city?''')

    # Calculate position to center the label horizontally and place it near the top
    window_width = window.frameGeometry().width()
    question_width = 600
    question_height = 100
    question_x = (window_width - question_width) // 2
    question_y = 20
    question.setGeometry(question_x, question_y, question_width, question_height)
    question.setStyleSheet("font-size: 20px; font-weight: bold;")
    question.show()

    # Function to proceed to the next question (calls easy6.easy)
    def next_question():
        import easy6
        # Remove all widgets from the window before showing the next question
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu5)
        easy6.easy(window, ans, qu5, qu4, qu3, qu2, qu1)

    # Answer button callbacks for each possible answer
    # Each function checks which question is active and updates the score and correctness accordingly
    def answer_dania():
        global qu5, ans
        if instance == 1:
            qu5 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu5 = False
            next_question()
        elif instance == 3:
            qu5 = False
            next_question()

    def answer_kroatia():
        global qu5, ans
        if instance == 1:
            qu5 = False
            next_question()
        elif instance == 2:
            qu5 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu5 = False
            next_question()

    def answer_norway():
        global qu5, ans
        if instance == 1:
            qu5 = False
            next_question()
        elif instance == 2:
            qu5 = False
            next_question()
        elif instance == 3:
            qu5 = False
            next_question()

    def answer_lichtenstain():
        global qu5, ans
        if instance == 1:
            qu5 = False
            next_question()
        elif instance == 2:
            qu5 = False
            next_question()
        elif instance == 3:
            qu5 = True
            ans += 2
            next_question()

    # Set the button texts according to the question instance (all in English)
    def set_correct_text():
        if instance == 1:
            dania.setText("A) Switzerland")
            kroatia.setText("B) Liechtenstein")
            norway.setText("C) Belgium")
            poland.setText("D) Austria")
        if instance == 2:
            dania.setText("A) Slovakia")
            kroatia.setText("B) Czechia")
            norway.setText("C) Latvia")
            poland.setText("D) Albania")
        if instance == 3:
            dania.setText("A) Bosnia and Herzegovina")
            kroatia.setText("B) Romania")
            norway.setText("C) Moldova")
            poland.setText("D) Bulgaria")

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