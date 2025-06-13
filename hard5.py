import os
import sys
import random
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

translations = {
    "English": {
        "q1": "5. What is the highest mountain in Africa?",
        "q2": "5. What is the capital of Kenya?",
        "q3": "5. Which of the following countries borders Egypt?",
        "A1": "A) Kilimanjaro", "B1": "B) Alma", "C1": "C) Makaron", "D1": "D) Everest",
        "A2": "A) Kimbo", "B2": "B) Nairobi", "C2": "C) Lusaka", "D2": "D) Dubai",
        "A3": "A) Sudan", "B3": "B) Morocco", "C3": "C) Nigeria", "D3": "D) Somalia"
    },
    "Greek": {
        "q1": "5. Ποιο είναι το ψηλότερο βουνό στην Αφρική;",
        "q2": "5. Ποια είναι η πρωτεύουσα της Κένυας;",
        "q3": "5. Ποια από τις παρακάτω χώρες συνορεύει με την Αίγυπτο;",
        "A1": "A) Κιλιμάντζαρο", "B1": "B) Άλμα", "C1": "C) Μακαρόν", "D1": "D) Έβερεστ",
        "A2": "A) Κίμπο", "B2": "B) Ναϊρόμπι", "C2": "C) Λουσάκα", "D2": "D) Ντουμπάι",
        "A3": "A) Σουδάν", "B3": "B) Μαρόκο", "C3": "C) Νιγηρία", "D3": "D) Σομαλία"
    },
    "French": {
        "q1": "5. Quelle est la plus haute montagne d'Afrique ?",
        "q2": "5. Quelle est la capitale du Kenya ?",
        "q3": "5. Lequel des pays suivants est limitrophe de l'Égypte ?",
        "A1": "A) Kilimandjaro", "B1": "B) Alma", "C1": "C) Makaron", "D1": "D) Everest",
        "A2": "A) Kimbo", "B2": "B) Nairobi", "C2": "C) Lusaka", "D2": "D) Dubaï",
        "A3": "A) Soudan", "B3": "B) Maroc", "C3": "C) Nigéria", "D3": "D) Somalie"
    }
}
current_language = "English"
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

def hard(window, prev_score, qu4, qu3, qu2, qu1):
    global qu5, ans, current_language
    ans += prev_score
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)
    current_language = "English"

    question_label = QLabel("", window)
    question_label.setFont(font)
    question_label.setWordWrap(True)  # Enable word wrap
    question_label.setAlignment(Qt.AlignCenter)  # Center the text in the label

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
        import hard6
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu5)
        hard6.hard(window, ans, qu5, qu4, qu3, qu2, qu1, current_language)

    # Answer button callbacks for each possible answer
    def answer_a():
        global qu5, ans
        if instance == 1:
            qu5 = True
            ans += 2
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
            qu5 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu5 = False
            next_question()

    def answer_c():
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

    def answer_d():
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