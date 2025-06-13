from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu5 = None
ans = 0

# --- LANGUAGE SUPPORT ---
language_file = os.path.join(os.path.dirname(__file__), "language.txt")

translations = {
    "English": {
        "q1": "5. In which country is the city of Dubai located?",
        "q2": "5. What is the largest island of Japan?",
        "q3": "5. Which is the largest country by area in Central America?",
        "A1": "A) Qatar", "B1": "B) Saudi Arabia", "C1": "C) United Arab Emirates", "D1": "D) Kuwait",
        "A2": "A) Hokkaido", "B2": "B) Kyushu", "C2": "C) Shikoku", "D2": "D) Honshu",
        "A3": "A) Nicaragua", "B3": "B) Guatemala", "C3": "C) El Salvador", "D3": "D) Panama"
    },
    "Greek": {
        "q1": "5. Σε ποια χώρα βρίσκεται η πόλη του Ντουμπάι;",
        "q2": "5. Ποιο είναι το μεγαλύτερο νησί της Ιαπωνίας;",
        "q3": "5. Ποια είναι η μεγαλύτερη χώρα σε έκταση στην Κεντρική Αμερική;",
        "A1": "A) Κατάρ", "B1": "B) Σαουδική Αραβία", "C1": "C) Ηνωμένα Αραβικά Εμιράτα", "D1": "D) Κουβέιτ",
        "A2": "A) Χοκάιντο", "B2": "B) Κιούσου", "C2": "C) Σικόκου", "D2": "D) Χονσού",
        "A3": "A) Νικαράγουα", "B3": "B) Γουατεμάλα", "C3": "C) Ελ Σαλβαδόρ", "D3": "D) Παναμάς"
    },
    "French": {
        "q1": "5. Dans quel pays se trouve la ville de Dubaï ?",
        "q2": "5. Quelle est la plus grande île du Japon ?",
        "q3": "5. Quel est le plus grand pays d'Amérique centrale par superficie ?",
        "A1": "A) Qatar", "B1": "B) Arabie Saoudite", "C1": "C) Émirats arabes unis", "D1": "D) Koweït",
        "A2": "A) Hokkaido", "B2": "B) Kyushu", "C2": "C) Shikoku", "D2": "D) Honshu",
        "A3": "A) Nicaragua", "B3": "B) Guatemala", "C3": "C) Salvador", "D3": "D) Panama"
    }
}
current_language = "English"
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

def normal(window, ans4, qu4, qu3, qu2, qu1, current_language):
    global qu5, ans
    ans += ans4
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)

    def tr(key):
        return translations.get(current_language, translations["English"]).get(key, key)

    question = QLabel("", window)
    question.setFont(font)
    question.setWordWrap(True)
    question.setAlignment(Qt.AlignCenter)

    # Set the question text (multilingual)
    if instance == 1:
        question.setText(tr('q1'))
    elif instance == 2:
        question.setText(tr('q2'))
    elif instance == 3:
        question.setText(tr('q3'))

    window_width = window.frameGeometry().width()
    question_width = 600
    question_height = 100
    question_x = (window_width - question_width) // 2
    question_y = 20
    question.setGeometry(question_x, question_y, question_width, question_height)
    question.setStyleSheet("font-size: 20px; font-weight: bold;")
    question.show()

    def next_question():
        import normal6
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu5)
        normal6.normal(window, ans, qu5, qu4, qu3, qu2, qu1, current_language)

    # Answer button callbacks for each possible answer
    def answer_a():
        global qu5, ans
        if instance == 1:
            qu5 = False
            next_question()
        elif instance == 2:
            qu5 = False
            next_question()
        elif instance == 3:
            qu5 = True
            ans += 2
            next_question()

    def answer_b():
        global qu5, ans
        if instance == 1:
            qu5 = False
            next_question()
        elif instance == 2:
            qu5 = False
            next_question()
        elif instance == 3:
            qu5 = False
            next_question()

    def answer_c():
        global qu5, ans
        if instance == 1:
            qu5 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu5 = False
            next_question()
        elif instance == 3:
            qu5 = False
            next_question()

    def answer_d():
        global qu5, ans
        if instance == 1:
            qu5 = False
            next_question()
        elif instance == 2:
            qu5 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu5 = False
            next_question()

    # Set the button texts according to the question instance (multilingual)
    def set_button_texts():
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

    set_button_texts()