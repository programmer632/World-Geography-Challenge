from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu6 = None
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
        "q1": "6. What is the longest river in North America?",
        "q2": "6. Which South American country is the only one with Portuguese as its official language?",
        "q3": "6. Which of the following countries does NOT border China?",
        "A1": "A) Rio Grande", "B1": "B) Colorado", "C1": "C) Mississippi", "D1": "D) Ohio",
        "A2": "A) Guyana", "B2": "B) Paraguay", "C2": "C) Venezuela", "D2": "D) Brazil",
        "A3": "A) Mongolia", "B3": "B) Thailand", "C3": "C) Vietnam", "D3": "D) Afghanistan"
    },
    "Greek": {
        "q1": "6. Ποιος είναι ο μεγαλύτερος ποταμός στη Βόρεια Αμερική;",
        "q2": "6. Ποια χώρα της Νότιας Αμερικής είναι η μόνη με επίσημη γλώσσα τα πορτογαλικά;",
        "q3": "6. Ποια από τις παρακάτω χώρες ΔΕΝ συνορεύει με την Κίνα;",
        "A1": "A) Ρίο Γκράντε", "B1": "B) Κολοράντο", "C1": "C) Μισισιπής", "D1": "D) Οχάιο",
        "A2": "A) Γουιάνα", "B2": "B) Παραγουάη", "C2": "C) Βενεζουέλα", "D2": "D) Βραζιλία",
        "A3": "A) Μογγολία", "B3": "B) Ταϊλάνδη", "C3": "C) Βιετνάμ", "D3": "D) Αφγανιστάν"
    },
    "French": {
        "q1": "6. Quel est le plus long fleuve d'Amérique du Nord ?",
        "q2": "6. Quel pays d'Amérique du Sud est le seul dont la langue officielle est le portugais ?",
        "q3": "6. Lequel des pays suivants ne borde PAS la Chine ?",
        "A1": "A) Rio Grande", "B1": "B) Colorado", "C1": "C) Mississippi", "D1": "D) Ohio",
        "A2": "A) Guyana", "B2": "B) Paraguay", "C2": "C) Venezuela", "D2": "D) Brésil",
        "A3": "A) Mongolie", "B3": "B) Thaïlande", "C3": "C) Vietnam", "D3": "D) Afghanistan"
    }
}
current_language = load_language()
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

def normal(window, ans5, qu5, qu4, qu3, qu2, qu1):
    global qu6, ans, current_language
    ans += ans5
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
        import normal7
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu6)
        normal7.normal(window, ans, qu6, qu5, qu4, qu3, qu2, qu1)

    # Answer button callbacks for each possible answer
    def answer_a():
        global qu6, ans
        if instance == 1:
            qu6 = False
            next_question()
        elif instance == 2:
            qu6 = False
            next_question()
        elif instance == 3:
            qu6 = False
            next_question()

    def answer_b():
        global qu6, ans
        if instance == 1:
            qu6 = False
            next_question()
        elif instance == 2:
            qu6 = False
            next_question()
        elif instance == 3:
            qu6 = True
            ans += 2
            next_question()

    def answer_c():
        global qu6, ans
        if instance == 1:
            qu6 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu6 = False
            next_question()
        elif instance == 3:
            qu6 = False
            next_question()

    def answer_d():
        global qu6, ans
        if instance == 1:
            qu6 = False
            next_question()
        elif instance == 2:
            qu6 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu6 = False
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