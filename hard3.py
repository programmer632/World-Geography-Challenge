from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

# Variables for score and correctness of question 3
qu3 = None  # Whether question 3 was answered correctly
ans = 0     # User's score for the hard level

# Main function for the third 'Hard' quiz question
# Receives the window, previous score, and correctness of previous questions
# Sets up the question and answer buttons

def hard(window, prev_score, qu2, qu1):
    global qu3, ans
    ans += prev_score  # Add previous score to current score
    font = QFont("Calibri", 13)
    question_variant = random.randint(1, 3)  # Randomly select question

    # Create the question label, centered
    question_label = QLabel("", window)
    question_label.setFont(font)
    question_label.setWordWrap(True)  # Enable word wrap
    question_label.setAlignment(Qt.AlignCenter)

    # Set question text in English
    if question_variant == 1:
        question_label.setText("3. What is the largest lake in Africa?")
    elif question_variant == 2:
        question_label.setText("3. In which country are the Victoria Falls located?")
    elif question_variant == 3:
        question_label.setText("3. Which of the following islands belongs to Africa?")

    # Calculate position to center the label horizontally and place it near the top
    window_width = window.frameGeometry().width()
    question_width = 600
    question_height = 100
    question_x = (window_width - question_width) // 2
    question_y = 20
    question_label.setGeometry(question_x, question_y, question_width, question_height)
    question_label.setStyleSheet("font-size: 20px; font-weight: bold;")
    question_label.show()

    # Function to proceed to the next question (calls hard4.hard)
    def next_question():
        import hard4
        # Remove all widgets from the window before showing the next question
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu3)
        hard4.hard(window, ans, qu3, qu2, qu1)

    # Answer button callbacks for each possible answer
    # Each function checks which question is active and updates the score and correctness accordingly
    def answer_a():
        global qu3, ans
        if question_variant == 1:
            qu3 = True
            ans += 2
        elif question_variant == 2:
            qu3 = False
        elif question_variant == 3:
            qu3 = False
        next_question()

    def answer_b():
        global qu3, ans
        if question_variant == 1:
            qu3 = False
        elif question_variant == 2:
            qu3 = True
            ans += 2
        elif question_variant == 3:
            qu3 = False
        next_question()

    def answer_c():
        global qu3, ans
        if question_variant == 1:
            qu3 = False
        elif question_variant == 2:
            qu3 = False
        elif question_variant == 3:
            qu3 = False
        next_question()

    def answer_d():
        global qu3, ans
        if question_variant == 1:
            qu3 = False
        elif question_variant == 2:
            qu3 = False
        elif question_variant == 3:
            qu3 = True
            ans += 2
        next_question()

    # Set the button texts in English according to the question
    def set_correct_text():
        if question_variant == 1:
            button_a.setText("A) Lake Victoria")
            button_b.setText("B) Lake Tanganyika")
            button_c.setText("C) Lake Nyasa")
            button_d.setText("D) Lake Malawi")
        elif question_variant == 2:
            button_a.setText("A) Zimbabwe")
            button_b.setText("B) Zambia")
            button_c.setText("C) Mozambique")
            button_d.setText("D) A and B")
        elif question_variant == 3:
            button_a.setText("A) Christmas Island")
            button_b.setText("B) Maldives")
            button_c.setText("C) Cyprus")
            button_d.setText("D) Madagascar")

    # Create answer buttons and connect them to the correct callback
    button_a = QPushButton("A) Denmark", window)
    button_a.resize(500, 120)
    button_a.move(250, 140)
    button_a.setFont(font)
    button_a.show()
    button_a.clicked.connect(answer_a)

    button_b = QPushButton("B) Croatia", window)
    button_b.setFont(font)
    button_b.resize(500, 120)
    button_b.move(250, 270)
    button_b.show()
    button_b.clicked.connect(answer_b)

    button_c = QPushButton("C) Norway", window)
    button_c.resize(500, 120)
    button_c.move(250, 400)
    button_c.setFont(font)
    button_c.show()
    button_c.clicked.connect(answer_c)

    button_d = QPushButton("D) Liechtenstein", window)
    button_d.resize(500, 120)
    button_d.move(250, 530)
    button_d.setFont(font)
    button_d.show()
    button_d.clicked.connect(answer_d)

    set_correct_text()