from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu10 = None
ans = 0

# Main function for the tenth 'Easy' quiz question
# Receives the window, previous score, and correctness of previous questions
# Sets up the tenth question and answer buttons

def easy(window, ans9, qu9, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1):
    global qu10, ans
    ans += ans9  # Add previous score to current score
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)  # Randomly select which question to show

    # Create the question label, centered horizontally
    question = QLabel("", window)
    question.setFont(font)
    question.setAlignment(Qt.AlignCenter)

    # Set the question text based on the random variant (all in English)
    if instance == 1:
        question.setText('''10. What is the currency of Sweden?''')
    elif instance == 2:
        question.setText('''10. In which country is Ben Nevis, 
the highest peak of the Cambrian Mountains, located?''')
    elif instance == 3:
        question.setText('''10. Which country has the most islands in Europe?''')

    # Calculate position to center the label horizontally and place it near the top
    window_width = window.frameGeometry().width()
    question_width = 600
    question_height = 100
    question_x = (window_width - question_width) // 2
    question_y = 20
    question.setGeometry(question_x, question_y, question_width, question_height)
    question.setStyleSheet("font-size: 20px; font-weight: bold;")
    question.show()

    # Function to proceed to the results screen (calls easy_marks.show_marks)
    def next_question():
        import marks
        # Remove all widgets from the window before showing the results
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu10)
        marks.show_marks(window, ans, qu10, qu9, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1)

    # Answer button callbacks for each possible answer
    # Each function checks which question is active and updates the score and correctness accordingly
    def answer_dania():
        global qu10, ans
        if instance == 1:
            qu10 = False
            next_question()
        elif instance == 2:
            qu10 = False
            next_question()
        elif instance == 3:
            qu10 = False
            next_question()

    def answer_kroatia():
        global qu10, ans
        if instance == 1:
            qu10 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu10 = False
            next_question()
        elif instance == 3:
            qu10 = False
            next_question()

    def answer_norway():
        global qu10, ans
        if instance == 1:
            qu10 = False
            next_question()
        elif instance == 2:
            qu10 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu10 = False
            next_question()

    def answer_lichtenstain():
        global qu10, ans
        if instance == 1:
            qu10 = False
            next_question()
        elif instance == 2:
            qu10 = False
            next_question()
        elif instance == 3:
            qu10 = True
            ans += 2
            next_question()

    # Set the button texts according to the question instance (all in English)
    def set_correct_text():
        if instance == 1:
            dania.setText("A) Euro")
            kroatia.setText("B) Krona")
            norway.setText("C) Franc")
            poland.setText("D) Pound")
        if instance == 2:
            dania.setText("A) Ireland")
            kroatia.setText("B) England")
            norway.setText("C) Scotland")
            poland.setText("D) Wales")
        if instance == 3:
            dania.setText("A) Italy")
            kroatia.setText("B) Greece")
            norway.setText("C) Norway")
            poland.setText("D) Sweden")

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