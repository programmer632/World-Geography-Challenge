from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

# Main function for the 'Easy' quiz level
# Sets up the first question and answer buttons

def easy(window):  
    global font, ans, qu1
    font = QFont("Calibri", 13)  # Set the font for all widgets
    ans = 0  # User's score for this level
    qu1 = None  # Whether the first question was answered correctly
    instance = random.randint(1, 3)  # Randomly select which question to show

    # Create the question label, centered horizontally
    question = QLabel("", window)
    question.setFont(font)
    question.setAlignment(Qt.AlignCenter)  # Center the text in the label

    # Set the question text based on the random variant (all in English)
    if instance == 1:
        question.setText('''1. Which of the following countries
is located on the Scandinavian Peninsula?''')
    elif instance == 2:
        question.setText('''1. Which of the following countries
is landlocked (has no access to the sea)?''')
    elif instance == 3:
        question.setText('''1. Which of the following countries has
Copenhagen as its capital city?''')

    # Calculate position to center the label horizontally and place it near the top
    window_width = window.frameGeometry().width()
    question_width = 600
    question_height = 100  # Smaller height so the label isn't too big
    question_x = (window_width - question_width) // 2  # Center horizontally
    question_y = 20  # Near the top, with a small margin

    question.setGeometry(question_x, question_y, question_width, question_height)
    question.setStyleSheet("font-size: 20px; font-weight: bold;")
    question.show()

    # Function to proceed to the next question (calls easy2.easy)
    def next_question():
        import easy2
        # Remove all widgets from the window before showing the next question
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu1)
        try:
            easy2.easy(window, ans, qu1)
        except Exception as e:
            print(f"Error: {e}")  # Print any error that occurs

    # Answer button callbacks for each possible answer
    # Each function checks which question is active and updates the score and correctness accordingly
    def answer_dania():
        global qu1, ans
        if instance == 1:
            qu1 = False
            next_question()
        elif instance == 2:
            qu1 = False
            next_question()
        elif instance == 3:
            qu1 = True
            ans += 2
            next_question()

    def answer_latvia():
        global qu1, ans
        if instance == 1:
            qu1 = False
            next_question()
        elif instance == 2:
            qu1 = False
            next_question()
        elif instance == 3:
            qu1 = False
            next_question()

    def answer_norway():
        global qu1, ans
        if instance == 1:
            qu1 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu1 = False
            next_question()
        elif instance == 3:
            qu1 = False
            next_question()

    def answer_lichtenstain():
        global qu1, ans
        if instance == 1:
            qu1 = False
            next_question()
        elif instance == 2:
            qu1 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu1 = False
            next_question()

    # Create answer buttons with English text and connect them to the correct callback
    dania = QPushButton("A) Denmark", window)
    dania.resize(500, 120)
    dania.move(250, 130)
    dania.setFont(font)
    dania.show()
    dania.clicked.connect(answer_dania)

    andora = QPushButton("B) Latvia", window)
    andora.setFont(font)
    andora.resize(500, 120)
    andora.move(250, 260)
    andora.show()
    andora.clicked.connect(answer_latvia)

    norway = QPushButton("C) Norway", window)
    norway.resize(500, 120)
    norway.move(250, 390)
    norway.setFont(font)
    norway.show()
    norway.clicked.connect(answer_norway)

    lichtenstain = QPushButton("D) Liechtenstein", window)
    lichtenstain.resize(500, 120)
    lichtenstain.move(250, 520)
    lichtenstain.setFont(font)
    lichtenstain.show()
    lichtenstain.clicked.connect(answer_lichtenstain)
