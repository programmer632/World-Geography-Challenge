from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

# Variables for score and correctness of question 7
qu7 = None  # Whether question 7 was answered correctly
ans = 0     # User's score for the hard level

# Main function for the seventh 'Hard' quiz question
# Receives the window, previous score, and correctness of previous questions
# Sets up the question and answer buttons

def hard(window, prev_score, qu6, qu5, qu4, qu3, qu2, qu1):
    global qu7, ans
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
        question_label.setText('''7. What is the capital of Ghana?''')
    elif question_variant == 2:
        question_label.setText('''7. What is the capital of Sudan?''')
    elif question_variant == 3:
        question_label.setText('''7. What is the capital of Libya?''')

    # Calculate position for the question label
    window_width = window.frameGeometry().width()
    question_width = 600
    question_height = 100
    question_x = (window_width - question_width) // 2
    question_y = 20
    question_label.setGeometry(question_x, question_y, question_width, question_height)
    question_label.setStyleSheet("font-size: 20px; font-weight: bold;")
    question_label.show()

    # Function to proceed to the next question (calls hard8.hard)
    def next_question():
        import hard8
        # Remove all widgets before the next question
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu7)
        hard8.hard(window, ans, qu7, qu6, qu5, qu4, qu3, qu2, qu1)

    # Answer button callbacks for each possible answer
    def answer_a():
        global qu7, ans
        if question_variant == 1:
            qu7 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")
        elif question_variant == 2:
            qu7 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")
        elif question_variant == 3:
            qu7 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")

    def answer_b():
        global qu7, ans
        if question_variant == 1:
            qu7 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")
        elif question_variant == 2:
            qu7 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")
        elif question_variant == 3:
            qu7 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")

    def answer_c():
        global qu7, ans
        if question_variant == 1:
            qu7 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")
        elif question_variant == 2:
            qu7 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")
        elif question_variant == 3:
            qu7 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")

    def answer_d():
        global qu7, ans
        if question_variant == 1:
            qu7 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")
        elif question_variant == 2:
            qu7 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")
        elif question_variant == 3:
            qu7 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")

    # Set button texts in English according to the question
    def set_correct_text():
        if question_variant == 1:
            button_a.setText("A) Ouagadougou")
            button_b.setText("B) Luanda")
            button_c.setText("C) Mombasa")
            button_d.setText("D) Accra")
        if question_variant == 2:
            button_a.setText("A) Juba")
            button_b.setText("B) Khartoum")
            button_c.setText("C) Kigali")
            button_d.setText("D) Niamey")
        if question_variant == 3:
            button_a.setText("A) Tripoli")
            button_b.setText("B) Algiers")
            button_c.setText("C) Lusaka")
            button_d.setText("D) Maputo")

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