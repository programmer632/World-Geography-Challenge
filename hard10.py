from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu10 = None
ans = 0

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
        "q1": "10. What is the capital of Cameroon?",
        "q2": "10. Which country has a flag with only two colors: green and white?",
        "q3": "10. Which countries border Morocco?",
        "A1": "A) Yaoundé", "B1": "B) Douala", "C1": "C) Bangui", "D1": "D) Libreville",
        "A2": "A) Ghana", "B2": "B) Tunisia", "C2": "C) Nigeria", "D2": "D) Sudan",
        "A3": "A) Egypt and Sudan", "B3": "B) Algeria and Western Sahara", "C3": "C) South Africa", "D3": "D) Libya"
    },
    "Greek": {
        "q1": "10. Ποια είναι η πρωτεύουσα του Καμερούν;",
        "q2": "10. Ποια χώρα έχει σημαία μόνο με δύο χρώματα: πράσινο και λευκό;",
        "q3": "10. Ποιες χώρες συνορεύουν με το Μαρόκο;",
        "A1": "A) Γιαουντέ", "B1": "B) Ντουάλα", "C1": "C) Μπανγκί", "D1": "D) Λιμπρεβίλ",
        "A2": "A) Γκάνα", "B2": "B) Τυνησία", "C2": "C) Νιγηρία", "D2": "D) Σουδάν",
        "A3": "A) Αίγυπτος και Σουδάν", "B3": "B) Αλγερία και Δυτική Σαχάρα", "C3": "C) Νότια Αφρική", "D3": "D) Λιβύη"
    },
    "French": {
        "q1": "10. Quelle est la capitale du Cameroun ?",
        "q2": "10. Quel pays a un drapeau composé uniquement de deux couleurs : vert et blanc ?",
        "q3": "10. Quels pays bordent le Maroc ?",
        "A1": "A) Yaoundé", "B1": "B) Douala", "C1": "C) Bangui", "D1": "D) Libreville",
        "A2": "A) Ghana", "B2": "B) Tunisie", "C2": "C) Nigeria", "D2": "D) Soudan",
        "A3": "A) Égypte et Soudan", "B3": "B) Algérie et Sahara occidental", "C3": "C) Afrique du Sud", "D3": "D) Libye"
    }
}
current_language = load_language()
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

def hard(window, prev_score, qu9, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1):
    global qu10, ans, current_language
    ans += prev_score
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)
    current_language = load_language()

    question_label = QLabel("", window)
    question_label.setFont(font)
    question_label.setWordWrap(True)
    question_label.setAlignment(Qt.AlignCenter)

    # Set question text (multilingual)
    if instance == 1:
        question_label.setText(tr('q1'))
    elif instance == 2:
        question_label.setText(tr('q2'))
    elif instance == 3:
        question_label.setText(tr('q3'))

    window_width = window.frameGeometry().width()
    question_width = 600
    question_height = 100
    question_x = (window_width - question_width) // 2
    question_y = 20
    question_label.setGeometry(question_x, question_y, question_width, question_height)
    question_label.setStyleSheet("font-size: 20px; font-weight: bold;")
    question_label.show()

    def next_question():
        import marks
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu10)
        marks.show_marks(window, ans, qu10, qu9, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1)

    # Answer button callbacks for each possible answer
    def answer_a():
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

    def answer_b():
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

    def answer_c():
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

    def answer_d():
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