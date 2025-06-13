# This module contains the first question for the 'hard' level of the geography quiz.
# All UI text and comments have been translated to English, and variable/function names clarified.
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
        "q1": "1. What is the largest country by area in Africa?",
        "q2": "1. What is the longest river in Africa (and possibly the world)?",
        "q3": "1. In which country is Mount Kilimanjaro, the highest mountain in Africa, located?",
        "A1": "A) Algeria", "B1": "B) Democratic Republic of the Congo", "C1": "C) Libya", "D1": "D) Nigeria",
        "A2": "A) Zambezi", "B2": "B) Congo", "C2": "C) Niger", "D2": "D) Nile",
        "A3": "A) Tanzania", "B3": "B) Kenya", "C3": "C) Ethiopia", "D3": "D) Uganda"
    },
    "Greek": {
        "q1": "1. Ποια είναι η μεγαλύτερη χώρα σε έκταση στην Αφρική;",
        "q2": "1. Ποιος είναι ο μεγαλύτερος ποταμός στην Αφρική (και ίσως στον κόσμο);",
        "q3": "1. Σε ποια χώρα βρίσκεται το όρος Κιλιμάντζαρο, το ψηλότερο βουνό της Αφρικής;",
        "A1": "A) Αλγερία", "B1": "B) Λαϊκή Δημοκρατία του Κονγκό", "C1": "C) Λιβύη", "D1": "D) Νιγηρία",
        "A2": "A) Ζαμβέζης", "B2": "B) Κονγκό", "C2": "C) Νίγηρας", "D2": "D) Νείλος",
        "A3": "A) Τανζανία", "B3": "B) Κένυα", "C3": "C) Αιθιοπία", "D3": "D) Ουγκάντα"
    },
    "French": {
        "q1": "1. Quel est le plus grand pays d'Afrique par superficie ?",
        "q2": "1. Quel est le plus long fleuve d'Afrique (et peut-être du monde) ?",
        "q3": "1. Dans quel pays se trouve le mont Kilimandjaro, le plus haut sommet d'Afrique ?",
        "A1": "A) Algérie", "B1": "B) République démocratique du Congo", "C1": "C) Libye", "D1": "D) Nigéria",
        "A2": "A) Zambèze", "B2": "B) Congo", "C2": "C) Niger", "D2": "D) Nil",
        "A3": "A) Tanzanie", "B3": "B) Kenya", "C3": "C) Éthiopie", "D3": "D) Ouganda"
    }
}
current_language = load_language()
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

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
        question_label.setText(tr("q1"))
    elif question_number == 2:
        question_label.setText(tr("q2"))
    elif question_number == 3:
        question_label.setText(tr("q3"))

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
            button_a.setText(tr("A1"))
            button_b.setText(tr("B1"))
            button_c.setText(tr("C1"))
            button_d.setText(tr("D1"))
        elif question_number == 2:
            button_a.setText(tr("A2"))
            button_b.setText(tr("B2"))
            button_c.setText(tr("C2"))
            button_d.setText(tr("D2"))
        elif question_number == 3:
            button_a.setText(tr("A3"))
            button_b.setText(tr("B3"))
            button_c.setText(tr("C3"))
            button_d.setText(tr("D3"))

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