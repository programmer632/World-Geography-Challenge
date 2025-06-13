import os
import sys
import random
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

translations = {
    "English": {
        "q1": "1. Which of the following countries\nis located on the Scandinavian Peninsula?",
        "q2": "1. Which of the following countries\nis landlocked (has no access to the sea)?",
        "q3": "1. Which of the following countries has\nCopenhagen as its capital city?",
        "A": "A) Denmark",
        "B": "B) Latvia",
        "C": "C) Norway",
        "D": "D) Liechtenstein"
    },
    "Greek": {
        "q1": "1. Ποια από τις παρακάτω χώρες\nβρίσκεται στη Σκανδιναβική Χερσόνησο;",
        "q2": "1. Ποια από τις παρακάτω χώρες\nδεν έχει πρόσβαση στη θάλασσα;",
        "q3": "1. Ποια από τις παρακάτω χώρες έχει\nπρωτεύουσα την Κοπεγχάγη;",
        "A": "A) Δανία",
        "B": "B) Λετονία",
        "C": "C) Νορβηγία",
        "D": "D) Λιχτενστάιν"
    },
    "French": {
        "q1": "1. Lequel des pays suivants\nest situé sur la péninsule scandinave ?",
        "q2": "1. Lequel des pays suivants\nn'a pas d'accès à la mer ?",
        "q3": "1. Lequel des pays suivants a\nCopenhague pour capitale ?",
        "A": "A) Danemark",
        "B": "B) Lettonie",
        "C": "C) Norvège",
        "D": "D) Liechtenstein"
    }
}
current_language = "English"
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

# Main function for the 'Easy' quiz level
# Sets up the first question and answer buttons

def easy(window, current_language):  
    global font, ans, qu1
    font = QFont("Calibri", 13)
    ans = 0
    qu1 = None
    instance = random.randint(1, 3)

    def tr(key):
        return translations.get(current_language, translations["English"]).get(key, key)

    # Create the question label, centered horizontally
    question = QLabel("", window)
    question.setFont(font)
    question.setWordWrap(True)  # Enable word wrap
    question.setAlignment(Qt.AlignCenter)  # Center the text in the label

    # Set the question text based on the random variant (translated)
    if instance == 1:
        question.setText(tr("q1"))
    elif instance == 2:
        question.setText(tr("q2"))
    elif instance == 3:
        question.setText(tr("q3"))

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
            easy2.easy(window, ans, qu1, current_language)
        except Exception as e:
            print(f"Error: {e}")  # Print any error that occurs

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
            qu1 = False
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
            qu1 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu1 = False
            next_question()

    # Create answer buttons with generic names and connect them to the correct callback
    button_a = QPushButton(tr("A"), window)
    button_a.resize(500, 120)
    button_a.move(250, 130)
    button_a.setFont(font)
    button_a.show()
    button_a.clicked.connect(answer_a)

    button_b = QPushButton(tr("B"), window)
    button_b.setFont(font)
    button_b.resize(500, 120)
    button_b.move(250, 260)
    button_b.show()
    button_b.clicked.connect(answer_b)

    button_c = QPushButton(tr("C"), window)
    button_c.resize(500, 120)
    button_c.move(250, 390)
    button_c.setFont(font)
    button_c.show()
    button_c.clicked.connect(answer_c)

    button_d = QPushButton(tr("D"), window)
    button_d.resize(500, 120)
    button_d.move(250, 520)
    button_d.setFont(font)
    button_d.show()
    button_d.clicked.connect(answer_d)