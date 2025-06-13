from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu2 = None
ans = 0
current_language = "English"  # Default language

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
        "q1": "2. What is the capital city of Canada?",
        "q2": "2. What is the longest river in India?",
        "q3": "2. Which country has Ankara as its capital city?",
        "A1": "A) Toronto", "B1": "B) Ottawa", "C1": "C) Montreal", "D1": "D) Vancouver",
        "A2": "A) Ganges", "B2": "B) Mekong", "C2": "C) Indus", "D2": "D) Brahmaputra",
        "A3": "A) Iran", "B3": "B) Pakistan", "C3": "C) Syria", "D3": "D) Turkey"
    },
    "Greek": {
        "q1": "2. Ποια είναι η πρωτεύουσα του Καναδά;",
        "q2": "2. Ποιος είναι ο μεγαλύτερος ποταμός στην Ινδία;",
        "q3": "2. Ποια χώρα έχει πρωτεύουσα την Άγκυρα;",
        "A1": "A) Τορόντο", "B1": "B) Οττάβα", "C1": "C) Μόντρεαλ", "D1": "D) Βανκούβερ",
        "A2": "A) Γάγγης", "B2": "B) Μεκόνγκ", "C2": "C) Ινδός", "D2": "D) Βραχμαπούτρα",
        "A3": "A) Ιράν", "B3": "B) Πακιστάν", "C3": "C) Συρία", "D3": "D) Τουρκία"
    },
    "French": {
        "q1": "2. Quelle est la capitale du Canada ?",
        "q2": "2. Quel est le plus long fleuve d'Inde ?",
        "q3": "2. Quel pays a Ankara pour capitale ?",
        "A1": "A) Toronto", "B1": "B) Ottawa", "C1": "C) Montréal", "D1": "D) Vancouver",
        "A2": "A) Gange", "B2": "B) Mékong", "C2": "C) Indus", "D2": "D) Brahmapoutre",
        "A3": "A) Iran", "B3": "B) Pakistan", "C3": "C) Syrie", "D3": "D) Turquie"
    }
}
current_language = load_language()
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

def normal(window, ans1, qu1):
    global qu2, ans, current_language
    ans += ans1
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)
    current_language = load_language()
    question = QLabel("", window)
    question.setFont(font)
    question.setWordWrap(True)
    question.setAlignment(Qt.AlignCenter)
    # Set the question text based on the random variant (multilingual)
    if instance == 1:
        question.setText(tr("q1"))
    elif instance == 2:
        question.setText(tr("q2"))
    elif instance == 3:
        question.setText(tr("q3"))

    window_width = window.frameGeometry().width()
    question_width = 600
    question_height = 100
    question_x = (window_width - question_width) // 2
    question_y = 20
    question.setGeometry(question_x, question_y, question_width, question_height)
    question.setStyleSheet("font-size: 20px; font-weight: bold;")
    question.show()

    def next_question():
        import normal3
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu2)
        normal3.normal(window, ans, qu2, qu1)

    # Answer button callbacks for each possible answer
    # Each function checks which question is active and updates the score and correctness accordingly
    def answer_a():
        global qu2, ans
        if instance == 1:
            qu2 = False
            next_question()
        elif instance == 2:
            qu2 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu2 = False
            next_question()

    def answer_b():
        global qu2, ans
        if instance == 1:
            qu2 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu2 = False
            next_question()
        elif instance == 3:
            qu2 = False
            next_question()

    def answer_c():
        global qu2, ans
        if instance == 1:
            qu2 = False
            next_question()
        elif instance == 2:
            qu2 = False
            next_question()
        elif instance == 3:
            qu2 = False
            next_question()

    def answer_d():
        global qu2, ans
        if instance == 1:
            qu2 = False
            next_question()
        elif instance == 2:
            qu2 = False
            next_question()
        elif instance == 3:
            qu2 = True
            ans += 2
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

    set_button_texts()