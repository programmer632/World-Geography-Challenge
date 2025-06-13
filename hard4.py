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
        "q1": "4. Which of the following cities is one of the capitals of South Africa?",
        "q2": "4. What is the largest island in Africa?",
        "q3": "4. Which of the following countries is located in the Sahel region?",
        "A1": "A) Pretoria", "B1": "B) Cape Town", "C1": "C) Bloemfontein", "D1": "D) All of the above",
        "A2": "A) Madagascar", "B2": "B) Seychelles", "C2": "C) Comoros", "D2": "D) Mauritius",
        "A3": "A) Ghana", "B3": "B) Botswana", "C3": "C) Mali", "D3": "D) Somalia"
    },
    "Greek": {
        "q1": "4. Ποια από τις παρακάτω πόλεις είναι μία από τις πρωτεύουσες της Νότιας Αφρικής;",
        "q2": "4. Ποιο είναι το μεγαλύτερο νησί της Αφρικής;",
        "q3": "4. Ποια από τις παρακάτω χώρες βρίσκεται στη ζώνη του Σαχέλ;",
        "A1": "A) Πρετόρια", "B1": "B) Κέιπ Τάουν", "C1": "C) Μπλουμφοντέιν", "D1": "D) Όλα τα παραπάνω",
        "A2": "A) Μαδαγασκάρη", "B2": "B) Σεϋχέλλες", "C2": "C) Κομόρες", "D2": "D) Μαυρίκιος",
        "A3": "A) Γκάνα", "B3": "B) Μποτσουάνα", "C3": "C) Μάλι", "D3": "D) Σομαλία"
    },
    "French": {
        "q1": "4. Laquelle des villes suivantes est l'une des capitales de l'Afrique du Sud ?",
        "q2": "4. Quelle est la plus grande île d'Afrique ?",
        "q3": "4. Lequel des pays suivants est situé dans la région du Sahel ?",
        "A1": "A) Pretoria", "B1": "B) Le Cap", "C1": "C) Bloemfontein", "D1": "D) Toutes les réponses ci-dessus",
        "A2": "A) Madagascar", "B2": "B) Seychelles", "C2": "C) Comores", "D2": "D) Maurice",
        "A3": "A) Ghana", "B3": "B) Botswana", "C3": "C) Mali", "D3": "D) Somalie"
    }
}
current_language = load_language()
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

def hard(window, prev_score, qu3, qu2, qu1):
    global qu4, ans, current_language
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
        import hard5
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu4)
        hard5.hard(window, ans, qu4, qu3, qu2, qu1)

    # Answer button callbacks for each possible answer
    def answer_a():
        global qu4, ans
        if instance == 1:
            qu4 = False
            next_question()
        elif instance == 2:
            qu4 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu4 = False
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
            qu4 = False
            next_question()
        elif instance == 2:
            qu4 = False
            next_question()
        elif instance == 3:
            qu4 = True
            ans += 2
            next_question()

    def answer_d():
        global qu4, ans
        if instance == 1:
            qu4 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu4 = False
            next_question()
        elif instance == 3:
            qu4 = False
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