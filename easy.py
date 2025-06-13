from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

# --- LANGUAGE SUPPORT ---
language_file = os.path.join(os.path.dirname(__file__), "language.txt")
def load_language():
    try:
        with open(language_file, 'r', encoding='utf-8') as f:
            lang = f.read().strip().capitalize()
            if lang in translations:
                return lang
    except Exception:
        pass
    return "English"

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
current_language = load_language()
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

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

    # Create answer buttons with translated text and connect them to the correct callback
    dania = QPushButton(tr("A"), window)
    dania.resize(500, 120)
    dania.move(250, 130)
    dania.setFont(font)
    dania.show()
    dania.clicked.connect(answer_dania)

    andora = QPushButton(tr("B"), window)
    andora.setFont(font)
    andora.resize(500, 120)
    andora.move(250, 260)
    andora.show()
    andora.clicked.connect(answer_latvia)

    norway = QPushButton(tr("C"), window)
    norway.resize(500, 120)
    norway.move(250, 390)
    norway.setFont(font)
    norway.show()
    norway.clicked.connect(answer_norway)

    lichtenstain = QPushButton(tr("D"), window)
    lichtenstain.resize(500, 120)
    lichtenstain.move(250, 520)
    lichtenstain.setFont(font)
    lichtenstain.show()
    lichtenstain.clicked.connect(answer_lichtenstain)
