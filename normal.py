from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

ans = 0
qu1 = None

# Main function for the first 'Normal' quiz question
# Receives the window and sets up the first question and answer buttons
# All text, comments, and variable names are in English for consistency

def normal(window):
    global ans, qu1
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)  # Randomly select which question to show

    # Create the question label, centered horizontally
    question = QLabel("", window)
    question.setFont(font)
    question.setWordWrap(True)
    question.setAlignment(Qt.AlignCenter)

    # Set the question text based on the random variant (all in English)
    if instance == 1:
        question.setText("""1. What is the capital city of Colombia?""")
    elif instance == 2:
        question.setText("""1. What is the largest peninsula in Asia?""")
    elif instance == 3:
        question.setText("""1. Which of the following countries does NOT border Brazil?""")

    # Calculate position to center the label horizontally and place it near the top
    window_width = window.frameGeometry().width()
    question_width = 600
    question_height = 100
    question_x = (window_width - question_width) // 2
    question_y = 20
    question.setGeometry(question_x, question_y, question_width, question_height)
    question.setStyleSheet("font-size: 20px; font-weight: bold;")
    question.show()

    # Function to proceed to the next question (calls normal2.normal)
    def next_question():
        import normal2
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu1)
        try:
            normal2.normal(window, ans, qu1)
        except Exception as e:
            print(f"Error: {e}")

    # Answer button callbacks for each possible answer
    # Each function checks which question is active and updates the score and correctness accordingly
    def answer_a():
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

    def answer_b():
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

    def answer_c():
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

    def answer_d():
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

    # Set the button texts according to the question instance (all in English)
    def set_button_texts():
        if instance == 1:
            button_a.setText("A) Lima")
            button_b.setText("B) Caracas")
            button_c.setText("C) Bogotá")  # correct
            button_d.setText("D) Quito")
        elif instance == 2:
            button_a.setText("A) Indochina Peninsula")
            button_b.setText("B) Arabian Peninsula")  # correct
            button_c.setText("C) Kamchatka Peninsula")
            button_d.setText("D) Korean Peninsula")
        elif instance == 3:
            button_a.setText("A) Chile")  # correct
            button_b.setText("B) Bolivia")
            button_c.setText("C) Uruguay")
            button_d.setText("D) Peru")

    # Create answer buttons and connect them to the correct callback
    button_a = QPushButton("A)", window)
    button_a.resize(500, 120)
    button_a.move(250, 130)
    button_a.setFont(font)
    button_a.show()
    button_a.clicked.connect(answer_a)

    button_b = QPushButton("B)", window)
    button_b.setFont(font)
    button_b.resize(500, 120)
    button_b.move(250, 260)
    button_b.show()
    button_b.clicked.connect(answer_b)

    button_c = QPushButton("C)", window)
    button_c.resize(500, 120)
    button_c.move(250, 390)
    button_c.setFont(font)
    button_c.show()
    button_c.clicked.connect(answer_c)

    button_d = QPushButton("D)", window)
    button_d.resize(500, 120)
    button_d.move(250, 520)
    button_d.setFont(font)
    button_d.show()
    button_d.clicked.connect(answer_d)

    set_button_texts()