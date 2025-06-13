from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu4 = None
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
        "q1": "4. Which U.S. state is the largest by area?",
        "q2": "4. Which of the following Asian countries is an island nation?",
        "q3": "4. Which country has the highest population density in Asia?",
        "A1": "A) Texas", "B1": "B) California", "C1": "C) Alaska", "D1": "D) Montana",
        "A2": "A) Malaysia", "B2": "B) Bangladesh", "C2": "C) Sri Lanka", "D2": "D) Myanmar",
        "A3": "A) Bangladesh", "B3": "B) India", "C3": "C) China", "D3": "D) Japan"
    },
    "Greek": {
        "q1": "4. Ποια πολιτεία των ΗΠΑ είναι η μεγαλύτερη σε έκταση;",
        "q2": "4. Ποια από τις παρακάτω ασιατικές χώρες είναι νησιωτικό κράτος;",
        "q3": "4. Ποια χώρα έχει τη μεγαλύτερη πληθυσμιακή πυκνότητα στην Ασία;",
        "A1": "A) Τέξας", "B1": "B) Καλιφόρνια", "C1": "C) Αλάσκα", "D1": "D) Μοντάνα",
        "A2": "A) Μαλαισία", "B2": "B) Μπανγκλαντές", "C2": "C) Σρι Λάνκα", "D2": "D) Μιανμάρ",
        "A3": "A) Μπανγκλαντές", "B3": "B) Ινδία", "C3": "C) Κίνα", "D3": "D) Ιαπωνία"
    },
    "French": {
        "q1": "4. Quel État des États-Unis est le plus grand en superficie ?",
        "q2": "4. Lequel des pays asiatiques suivants est une nation insulaire ?",
        "q3": "4. Quel pays a la plus grande densité de population en Asie ?",
        "A1": "A) Texas", "B1": "B) Californie", "C1": "C) Alaska", "D1": "D) Montana",
        "A2": "A) Malaisie", "B2": "B) Bangladesh", "C2": "C) Sri Lanka", "D2": "D) Myanmar",
        "A3": "A) Bangladesh", "B3": "B) Inde", "C3": "C) Chine", "D3": "D) Japon"
    }
}
current_language = load_language()
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

def normal(window, ans3, qu3, qu2, qu1):
    global qu4, ans, current_language
    ans += ans3
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
        import normal5
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu4)
        normal5.normal(window, ans, qu4, qu3, qu2, qu1)

    # Answer button callbacks for each possible answer
    def answer_a():
        global qu4, ans
        if instance == 1:
            qu4 = False
            next_question()
        elif instance == 2:
            qu4 = False
            next_question()
        elif instance == 3:
            qu4 = True
            ans += 2
            next_question()

    def answer_b():
        global qu4, ans
        if instance == 1:
            qu4 = False
            next_question()
        elif instance == 2:
            qu4 = False
            next_question()
        elif instance == 3:
            qu4 = False
            next_question()

    def answer_c():
        global qu4, ans
        if instance == 1:
            qu4 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu4 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu4 = False
            next_question()

    def answer_d():
        global qu4, ans
        if instance == 1:
            qu4 = False
            next_question()
        elif instance == 2:
            qu4 = False
            next_question()
        elif instance == 3:
            qu4 = False
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