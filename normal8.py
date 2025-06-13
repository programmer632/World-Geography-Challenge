from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu8 = None
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
        "q1": "8. What is the capital city of India?",
        "q2": "8. Which of the following cities has the largest population?",
        "q3": "8. What is the largest island in Canada?",
        "A1": "A) New Delhi", "B1": "B) Mumbai", "C1": "C) Bangalore", "D1": "D) Kolkata",
        "A2": "A) Seoul", "B2": "B) Shanghai", "C2": "C) Mumbai", "D2": "D) Tokyo",
        "A3": "A) Newfoundland", "B3": "B) Vancouver Island", "C3": "C) Baffin Island", "D3": "D) Victoria Island"
    },
    "Greek": {
        "q1": "8. Ποια είναι η πρωτεύουσα της Ινδίας;",
        "q2": "8. Ποια από τις παρακάτω πόλεις έχει τον μεγαλύτερο πληθυσμό;",
        "q3": "8. Ποιο είναι το μεγαλύτερο νησί του Καναδά;",
        "A1": "A) Νέο Δελχί", "B1": "B) Μουμπάι", "C1": "C) Μπανγκαλόρ", "D1": "D) Καλκούτα",
        "A2": "A) Σεούλ", "B2": "B) Σαγκάη", "C2": "C) Μουμπάι", "D2": "D) Τόκιο",
        "A3": "A) Νιουφάουντλαντ", "B3": "B) Νήσος Βανκούβερ", "C3": "C) Νήσος Μπάφιν", "D3": "D) Νήσος Βικτώρια"
    },
    "French": {
        "q1": "8. Quelle est la capitale de l'Inde ?",
        "q2": "8. Laquelle des villes suivantes a la plus grande population ?",
        "q3": "8. Quelle est la plus grande île du Canada ?",
        "A1": "A) New Delhi", "B1": "B) Mumbai", "C1": "C) Bangalore", "D1": "D) Calcutta",
        "A2": "A) Séoul", "B2": "B) Shanghai", "C2": "C) Mumbai", "D2": "D) Tokyo",
        "A3": "A) Terre-Neuve", "B3": "B) Île de Vancouver", "C3": "C) Île de Baffin", "D3": "D) Île Victoria"
    }
}
current_language = load_language()
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

def normal(window, ans7, qu7, qu6, qu5, qu4, qu3, qu2, qu1):
    global qu8, ans, current_language
    ans += ans7
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)
    current_language = load_language()

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
        import normal9
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu8)
        normal9.normal(window, ans, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1)

    # Answer button callbacks for each possible answer
    def answer_a():
        global qu8, ans
        if instance == 1:
            qu8 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu8 = False
            next_question()
        elif instance == 3:
            qu8 = False
            next_question()

    def answer_b():
        global qu8, ans
        if instance == 1:
            qu8 = False
            next_question()
        elif instance == 2:
            qu8 = False
            next_question()
        elif instance == 3:
            qu8 = False
            next_question()

    def answer_c():
        global qu8, ans
        if instance == 1:
            qu8 = False
            next_question()
        elif instance == 2:
            qu8 = False
            next_question()
        elif instance == 3:
            qu8 = True
            ans += 2
            next_question()

    def answer_d():
        global qu8, ans
        if instance == 1:
            qu8 = False
            next_question()
        elif instance == 2:
            qu8 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu8 = False
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