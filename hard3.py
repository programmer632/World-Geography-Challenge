import os
import sys
import random
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

translations = {
    "English": {
        "q1": "3. What is the largest lake in Africa?",
        "q2": "3. In which country are the Victoria Falls located?",
        "q3": "3. Which of the following islands belongs to Africa?",
        "A1": "A) Lake Victoria", "B1": "B) Lake Tanganyika", "C1": "C) Lake Nyasa", "D1": "D) Lake Malawi",
        "A2": "A) Zimbabwe", "B2": "B) Zambia", "C2": "C) Mozambique", "D2": "D) A and B",
        "A3": "A) Christmas Island", "B3": "B) Maldives", "C3": "C) Cyprus", "D3": "D) Madagascar"
    },
    "Greek": {
        "q1": "3. Ποια είναι η μεγαλύτερη λίμνη στην Αφρική;",
        "q2": "3. Σε ποια χώρα βρίσκονται οι Καταρράκτες Βικτώρια;",
        "q3": "3. Ποιο από τα παρακάτω νησιά ανήκει στην Αφρική;",
        "A1": "A) Λίμνη Βικτώρια", "B1": "B) Λίμνη Τανγκανίκα", "C1": "C) Λίμνη Νιάσα", "D1": "D) Λίμνη Μαλάουι",
        "A2": "A) Ζιμπάμπουε", "B2": "B) Ζάμπια", "C2": "C) Μοζαμβίκη", "D2": "D) Α και Β",
        "A3": "A) Νησί των Χριστουγέννων", "B3": "B) Μαλδίβες", "C3": "C) Κύπρος", "D3": "D) Μαδαγασκάρη"
    },
    "French": {
        "q1": "3. Quel est le plus grand lac d'Afrique ?",
        "q2": "3. Dans quel pays se trouvent les chutes Victoria ?",
        "q3": "3. Laquelle des îles suivantes appartient à l'Afrique ?",
        "A1": "A) Lac Victoria", "B1": "B) Lac Tanganyika", "C1": "C) Lac Nyasa", "D1": "D) Lac Malawi",
        "A2": "A) Zimbabwe", "B2": "B) Zambie", "C2": "C) Mozambique", "D2": "D) A et B",
        "A3": "A) Île Christmas", "B3": "B) Maldives", "C3": "C) Chypre", "D3": "D) Madagascar"
    }
}
current_language = "English"
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

def hard(window, prev_score, qu2, qu1):
    global qu3, ans, current_language
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
        import hard4
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu3)
        hard4.hard(window, ans, qu3, qu2, qu1, current_language)

    # Answer button callbacks for each possible answer
    def answer_a():
        global qu3, ans
        if instance == 1:
            qu3 = True
            ans += 2
        elif instance == 2:
            qu3 = False
        elif instance == 3:
            qu3 = False
        next_question()

    def answer_b():
        global qu3, ans
        if instance == 1:
            qu3 = False
        elif instance == 2:
            qu3 = True
            ans += 2
        elif instance == 3:
            qu3 = False
        next_question()

    def answer_c():
        global qu3, ans
        if instance == 1:
            qu3 = False
        elif instance == 2:
            qu3 = False
        elif instance == 3:
            qu3 = False
        next_question()

    def answer_d():
        global qu3, ans
        if instance == 1:
            qu3 = False
        elif instance == 2:
            qu3 = False
        elif instance == 3:
            qu3 = True
            ans += 2
        next_question()

    # Set the button texts according to the question (multilingual)
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