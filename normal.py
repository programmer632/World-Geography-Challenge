from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

ans = 0
qu1 = None

# --- LANGUAGE SUPPORT ---
language_file = os.path.join(os.path.dirname(__file__), "language.txt")

translations = {
    "English": {
        "q1": "1. What is the capital city of Colombia?",
        "q2": "1. What is the largest peninsula in Asia?",
        "q3": "1. Which of the following countries does NOT border Brazil?",
        "A1": "A) Lima", "B1": "B) Caracas", "C1": "C) Bogotá", "D1": "D) Quito",
        "A2": "A) Indochina Peninsula", "B2": "B) Arabian Peninsula", "C2": "C) Kamchatka Peninsula", "D2": "D) Korean Peninsula",
        "A3": "A) Chile", "B3": "B) Bolivia", "C3": "C) Uruguay", "D3": "D) Peru"
    },
    "Greek": {
        "q1": "1. Ποια είναι η πρωτεύουσα της Κολομβίας;",
        "q2": "1. Ποια είναι η μεγαλύτερη χερσόνησος στην Ασία;",
        "q3": "1. Ποια από τις παρακάτω χώρες ΔΕΝ συνορεύει με τη Βραζιλία;",
        "A1": "A) Λίμα", "B1": "B) Καράκας", "C1": "C) Μπογκοτά", "D1": "D) Κίτο",
        "A2": "A) Χερσόνησος Ινδοκίνας", "B2": "B) Αραβική Χερσόνησος", "C2": "C) Χερσόνησος Καμτσάτκα", "D2": "D) Κορεατική Χερσόνησος",
        "A3": "A) Χιλή", "B3": "B) Βολιβία", "C3": "C) Ουρουγουάη", "D3": "D) Περού"
    },
    "French": {
        "q1": "1. Quelle est la capitale de la Colombie ?",
        "q2": "1. Quelle est la plus grande péninsule d'Asie ?",
        "q3": "1. Lequel des pays suivants ne borde PAS le Brésil ?",
        "A1": "A) Lima", "B1": "B) Caracas", "C1": "C) Bogotá", "D1": "D) Quito",
        "A2": "A) Péninsule d'Indochine", "B2": "B) Péninsule Arabique", "C2": "C) Péninsule du Kamtchatka", "D2": "D) Péninsule Coréenne",
        "A3": "A) Chili", "B3": "B) Bolivie", "C3": "C) Uruguay", "D3": "D) Pérou"
    }
}
current_language = "English"
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

# Main function for the first 'Normal' quiz question
# Receives the window and sets up the first question and answer buttons
# All text, comments, and variable names are in English for consistency

def normal(window, current_language):
    global ans, qu1
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)

    def tr(key):
        return translations.get(current_language, translations["English"]).get(key, key)

    # Create the question label, centered horizontally
    question = QLabel("", window)
    question.setFont(font)
    question.setWordWrap(True)
    question.setAlignment(Qt.AlignCenter)

    # Reload language in case it was changed in settings before this question
    # Set the question text based on the random variant (multilingual)
    if instance == 1:
        question.setText(tr("q1"))
    elif instance == 2:
        question.setText(tr("q2"))
    elif instance == 3:
        question.setText(tr("q3"))

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
            normal2.normal(window, ans, qu1, current_language)
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

    # Set the button texts according to the question instance (multilingual)
    def set_button_texts():
        if instance == 1:
            button_a.setText(tr("A1"))
            button_b.setText(tr("B1"))
            button_c.setText(tr("C1"))
            button_d.setText(tr("D1"))
        elif instance == 2:
            button_a.setText(tr("A2"))
            button_b.setText(tr("B2"))
            button_c.setText(tr("C2"))
            button_d.setText(tr("D2"))
        elif instance == 3:
            button_a.setText(tr("A3"))
            button_b.setText(tr("B3"))
            button_c.setText(tr("C3"))
            button_d.setText(tr("D3"))

    # Create answer buttons and connect them to the correct callback
    button_a = QPushButton("", window)
    button_a.resize(500, 120)
    button_a.move(250, 130)
    button_a.setFont(font)
    button_a.show()
    button_a.clicked.connect(answer_a)

    button_b = QPushButton("", window)
    button_b.setFont(font)
    button_b.resize(500, 120)
    button_b.move(250, 260)
    button_b.show()
    button_b.clicked.connect(answer_b)

    button_c = QPushButton("", window)
    button_c.resize(500, 120)
    button_c.move(250, 390)
    button_c.setFont(font)
    button_c.show()
    button_c.clicked.connect(answer_c)

    button_d = QPushButton("", window)
    button_d.resize(500, 120)
    button_d.move(250, 520)
    button_d.setFont(font)
    button_d.show()
    button_d.clicked.connect(answer_d)

    set_button_texts()