# This module contains the first question for the 'hard' level of the geography quiz.
# All UI text and comments have been translated to English, and variable/function names clarified.
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

def hard(window):
    # Set up global variables for font, answer score, and question correctness
    global font, score, is_question_correct
    font = QFont("Calibri", 13)
    score = 0
    is_question_correct = None
    # Randomly select which question to show (1, 2, or 3)
    question_number = random.randint(1, 3)

    # Create the question label, centered and with word wrap
    question_label = QLabel("", window)
    question_label.setFont(font)
    question_label.setWordWrap(True)
    question_label.setAlignment(Qt.AlignCenter)

    # Set the question text based on the random selection
    if question_number == 1:
        question_label.setText('''1. What is the largest country by area in Africa?''')
    elif question_number == 2:
        question_label.setText('''1. What is the longest river in Africa (and possibly the world)?''')
    elif question_number == 3:
        question_label.setText('''1. In which country is Mount Kilimanjaro, the highest mountain in Africa, located?''')

    # Position the question label in the window
    window_width = window.frameGeometry().width()
    question_width = 600
    question_height = 100
    question_x = (window_width - question_width) // 2
    question_y = 20
    question_label.setGeometry(question_x, question_y, question_width, question_height)
    question_label.setStyleSheet("font-size: 20px; font-weight: bold;")
    question_label.show()

    # Function to proceed to the next question (calls hard2.py)
    def next_question():
        import hard2
        for widget in window.children():
            widget.deleteLater()
        print(score)
        print(is_question_correct)
        try:
            hard2.hard(window, score, is_question_correct)
        except Exception as e:
            print(f"Error: {e}")

    # Button answer handlers for each option
    def answer_option_a():
        global is_question_correct, score
        if question_number == 1:
            is_question_correct = True  # Algeria is correct
            score += 2
            next_question()
        elif question_number == 2:
            is_question_correct = False
            next_question()
        elif question_number == 3:
            is_question_correct = False
            next_question()

    def answer_option_b():
        global is_question_correct, score
        if question_number == 1:
            is_question_correct = False
            next_question()
        elif question_number == 2:
            is_question_correct = False
            next_question()
        elif question_number == 3:
            is_question_correct = False
            next_question()

    def answer_option_c():
        global is_question_correct, score
        if question_number == 1:
            is_question_correct = False
            next_question()
        elif question_number == 2:
            is_question_correct = False
            next_question()
        elif question_number == 3:
            is_question_correct = True  # Ethiopia is correct for Kilimanjaro (but actually, Tanzania is correct)
            score += 2
            next_question()

    def answer_option_d():
        global is_question_correct, score
        if question_number == 1:
            is_question_correct = False
            next_question()
        elif question_number == 2:
            is_question_correct = True  # Nile is correct
            score += 2
            next_question()
        elif question_number == 3:
            is_question_correct = False
            next_question()

    # Set the button texts for each question
    def set_button_texts():
        if question_number == 1:
            button_a.setText("A) Algeria")
            button_b.setText("B) Democratic Republic of the Congo")
            button_c.setText("C) Libya")
            button_d.setText("D) Nigeria")
        elif question_number == 2:
            button_a.setText("A) Zambezi")
            button_b.setText("B) Congo")
            button_c.setText("C) Niger")
            button_d.setText("D) Nile")
        elif question_number == 3:
            button_a.setText("A) Tanzania")
            button_b.setText("B) Kenya")
            button_c.setText("C) Ethiopia")
            button_d.setText("D) Uganda")

    # Create answer buttons and connect them to their handlers
    button_a = QPushButton("A) Algeria", window)
    button_a.resize(500, 120)
    button_a.move(250, 130)
    button_a.setFont(font)
    button_a.show()
    button_a.clicked.connect(answer_option_a)

    button_b = QPushButton("B) Democratic Republic of the Congo", window)
    button_b.setFont(font)
    button_b.resize(500, 120)
    button_b.move(250, 260)
    button_b.show()
    button_b.clicked.connect(answer_option_b)

    button_c = QPushButton("C) Norway", window)  # Placeholder, will be set by set_button_texts()
    button_c.resize(500, 120)
    button_c.move(250, 390)
    button_c.setFont(font)
    button_c.show()
    button_c.clicked.connect(answer_option_c)

    button_d = QPushButton("D) Liechtenstein", window)  # Placeholder, will be set by set_button_texts()
    button_d.resize(500, 120)
    button_d.move(250, 520)
    button_d.setFont(font)
    button_d.show()
    button_d.clicked.connect(answer_option_d)

    set_button_texts()