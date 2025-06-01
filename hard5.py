from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

# Variables for score and correctness of question 5
qu5 = None  # Whether question 5 was answered correctly
ans = 0     # User's score for the hard level

# Main function for the fifth 'Hard' quiz question
# Receives the window, previous score, and correctness of previous questions
# Sets up the question and answer buttons

def hard(window, prev_score, qu4, qu3, qu2, qu1):
    global qu5, ans
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
        question_label.setText('''5. What is the highest mountain in Africa?''')
    elif question_variant == 2:
        question_label.setText('''5. What is the capital of Kenya?''')
    elif question_variant == 3:
        question_label.setText('''5. Which of the following countries borders Egypt?''')

    # Calculate position for the question label
    window_width = window.frameGeometry().width()
    question_width = 600
    question_height = 100
    question_x = (window_width - question_width) // 2
    question_y = 20
    question_label.setGeometry(question_x, question_y, question_width, question_height)
    question_label.setStyleSheet("font-size: 20px; font-weight: bold;")
    question_label.show()

    # Function to proceed to the next question (calls hard6.hard)
    def next_question():
        import hard6
        # Remove all widgets before the next question
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu5)
        hard6.hard(window, ans, qu5, qu4, qu3, qu2, qu1)

    # Answer button callbacks for each possible answer
    def answer_a():
        global qu5, ans
        if question_variant == 1:
            qu5 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")
        elif question_variant == 2:
            qu5 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")
        elif question_variant == 3:
            qu5 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")

    def answer_b():
        global qu5, ans
        if question_variant == 1:
            qu5 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")
        elif question_variant == 2:
            qu5 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")
        elif question_variant == 3:
            qu5 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")

    def answer_c():
        global qu5, ans
        if question_variant == 1:
            qu5 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")
        elif question_variant == 2:
            qu5 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")
        elif question_variant == 3:
            qu5 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")

    def answer_d():
        global qu5, ans
        if question_variant == 1:
            qu5 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")
        elif question_variant == 2:
            qu5 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")
        elif question_variant == 3:
            qu5 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")

    # Set button texts in English according to the question
    def set_correct_text():
        if question_variant == 1:
            button_a.setText("A) Kilimanjaro")
            button_b.setText("B) Alma")
            button_c.setText("C) Makaron")
            button_d.setText("D) Everest")
        if question_variant == 2:
            button_a.setText("A) Kimbo")
            button_b.setText("B) Nairobi")
            button_c.setText("C) Lusaka")
            button_d.setText("D) Dubai")
        if question_variant == 3:
            button_a.setText("A) Sudan")
            button_b.setText("B) Morocco")
            button_c.setText("C) Nigeria")
            button_d.setText("D) Somalia")

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