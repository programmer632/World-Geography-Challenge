from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

# Variables for score and correctness of question 7
qu7 = None  # Whether question 7 was answered correctly
ans = 0     # User's score for the hard level

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
        "q1": "7. What is the capital of Ghana?",
        "q2": "7. What is the capital of Sudan?",
        "q3": "7. What is the capital of Libya?",
        "A1": "A) Ouagadougou", "B1": "B) Luanda", "C1": "C) Mombasa", "D1": "D) Accra",
        "A2": "A) Juba", "B2": "B) Khartoum", "C2": "C) Kigali", "D2": "D) Niamey",
        "A3": "A) Tripoli", "B3": "B) Algiers", "C3": "C) Lusaka", "D3": "D) Maputo"
    },
    "Greek": {
        "q1": "7. Ποια είναι η πρωτεύουσα της Γκάνας;",
        "q2": "7. Ποια είναι η πρωτεύουσα του Σουδάν;",
        "q3": "7. Ποια είναι η πρωτεύουσα της Λιβύης;",
        "A1": "A) Ουαγκαντούγκου", "B1": "B) Λουάντα", "C1": "C) Μομπάσα", "D1": "D) Άκκρα",
        "A2": "A) Τζούμπα", "B2": "B) Χαρτούμ", "C2": "C) Κιγκάλι", "D2": "D) Νιαμέι",
        "A3": "A) Τρίπολη", "B3": "B) Αλγέρι", "C3": "C) Λουσάκα", "D3": "D) Μαπούτο"
    },
    "French": {
        "q1": "7. Quelle est la capitale du Ghana ?",
        "q2": "7. Quelle est la capitale du Soudan ?",
        "q3": "7. Quelle est la capitale de la Libye ?",
        "A1": "A) Ouagadougou", "B1": "B) Luanda", "C1": "C) Mombasa", "D1": "D) Accra",
        "A2": "A) Djouba", "B2": "B) Khartoum", "C2": "C) Kigali", "D2": "D) Niamey",
        "A3": "A) Tripoli", "B3": "B) Alger", "C3": "C) Lusaka", "D3": "D) Maputo"
    }
}
current_language = load_language()
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

# Main function for the seventh 'Hard' quiz question
# Receives the window, previous score, and correctness of previous questions
# Sets up the question and answer buttons

def hard(window, prev_score, qu6, qu5, qu4, qu3, qu2, qu1):
    global qu7, ans, current_language
    ans += prev_score
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)
    current_language = load_language()

    # Create the question label, centered
    question_label = QLabel("", window)
    question_label.setFont(font)
    question_label.setWordWrap(True)  # Enable word wrap
    question_label.setAlignment(Qt.AlignCenter)

    # Set question text (multilingual)
    if instance == 1:
        question_label.setText(tr('q1'))
    elif instance == 2:
        question_label.setText(tr('q2'))
    elif instance == 3:
        question_label.setText(tr('q3'))

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
        if instance == 1:
            qu7 = False
            next_question()
        elif instance == 2:
            qu7 = False
            next_question()
        elif instance == 3:
            qu7 = True
            ans += 2
            next_question()

    def answer_b():
        global qu7, ans
        if instance == 1:
            qu7 = False
            next_question()
        elif instance == 2:
            qu7 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu7 = False
            next_question()

    def answer_c():
        global qu7, ans
        if instance == 1:
            qu7 = False
            next_question()
        elif instance == 2:
            qu7 = False
            next_question()
        elif instance == 3:
            qu7 = False
            next_question()

    def answer_d():
        global qu7, ans
        if instance == 1:
            qu7 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu7 = False
            next_question()
        elif instance == 3:
            qu7 = False
            next_question()

    # Set button texts according to the question (multilingual)
    def set_correct_text():
        if instance == 1:
            button_a.setText(tr('A1'))
            button_b.setText(tr('B1'))
            button_c.setText(tr('C1'))
            button_d.setText(tr('D1'))
        elif instance == 2:
            button_a.setText(tr('A2'))
            button_b.setText(tr('B2'))
            button_c.setText(tr('C2'))
            button_d.setText(tr('D2'))
        elif instance == 3:
            button_a.setText(tr('A3'))
            button_b.setText(tr('B3'))
            button_c.setText(tr('C3'))
            button_d.setText(tr('D3'))

    # Create answer buttons and connect them to the correct callback
    button_a = QPushButton("", window)
    button_a.resize(500, 120)
    button_a.move(250, 140)
    button_a.setFont(font)
    button_a.show()
    button_a.clicked.connect(answer_a)

    button_b = QPushButton("", window)
    button_b.setFont(font)
    button_b.resize(500, 120)
    button_b.move(250, 270)
    button_b.show()
    button_b.clicked.connect(answer_b)

    button_c = QPushButton("", window)
    button_c.resize(500, 120)
    button_c.move(250, 400)
    button_c.setFont(font)
    button_c.show()
    button_c.clicked.connect(answer_c)

    button_d = QPushButton("", window)
    button_d.resize(500, 120)
    button_d.move(250, 530)
    button_d.setFont(font)
    button_d.show()
    button_d.clicked.connect(answer_d)

    set_correct_text()