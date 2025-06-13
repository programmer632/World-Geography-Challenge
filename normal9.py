from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu9 = None
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
        "q1": "9. What is the most mountainous country in Asia?",
        "q2": "9. Which island hosts the capital city of Indonesia?",
        "q3": "9. Which Caribbean country has the largest area?",
        "A1": "A) Thailand", "B1": "B) Pakistan", "C1": "C) Nepal", "D1": "D) Kazakhstan",
        "A2": "A) Sumatra", "B2": "B) Java", "C2": "C) Borneo", "D2": "D) Bali",
        "A3": "A) Jamaica", "B3": "B) Dominican Republic", "C3": "C) Haiti", "D3": "D) Cuba"
    },
    "Greek": {
        "q1": "9. Ποια είναι η πιο ορεινή χώρα στην Ασία;",
        "q2": "9. Ποιο νησί φιλοξενεί την πρωτεύουσα της Ινδονησίας;",
        "q3": "9. Ποια χώρα της Καραϊβικής έχει τη μεγαλύτερη έκταση;",
        "A1": "A) Ταϊλάνδη", "B1": "B) Πακιστάν", "C1": "C) Νεπάλ", "D1": "D) Καζακστάν",
        "A2": "A) Σουμάτρα", "B2": "B) Ιάβα", "C2": "C) Βόρνεο", "D2": "D) Μπαλί",
        "A3": "A) Τζαμάικα", "B3": "B) Δομινικανή Δημοκρατία", "C3": "C) Αϊτή", "D3": "D) Κούβα"
    },
    "French": {
        "q1": "9. Quel est le pays le plus montagneux d'Asie ?",
        "q2": "9. Quelle île accueille la capitale de l'Indonésie ?",
        "q3": "9. Quel pays des Caraïbes a la plus grande superficie ?",
        "A1": "A) Thaïlande", "B1": "B) Pakistan", "C1": "C) Népal", "D1": "D) Kazakhstan",
        "A2": "A) Sumatra", "B2": "B) Java", "C2": "C) Bornéo", "D2": "D) Bali",
        "A3": "A) Jamaïque", "B3": "B) République dominicaine", "C3": "C) Haïti", "D3": "D) Cuba"
    }
}
current_language = load_language()
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

def normal(window, ans8, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1, current_language):
    global qu9, ans
    ans += ans8
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
        import normal10
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu9)
        normal10.normal(window, ans, qu9, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1, current_language)

    # Answer button callbacks for each possible answer
    def answer_a():
        global qu9, ans
        if instance == 1:
            qu9 = False
            next_question()
        elif instance == 2:
            qu9 = False
            next_question()
        elif instance == 3:
            qu9 = False
            next_question()

    def answer_b():
        global qu9, ans
        if instance == 1:
            qu9 = False
            next_question()
        elif instance == 2:
            qu9 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu9 = False
            next_question()

    def answer_c():
        global qu9, ans
        if instance == 1:
            qu9 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu9 = False
            next_question()
        elif instance == 3:
            qu9 = False
            next_question()

    def answer_d():
        global qu9, ans
        if instance == 1:
            qu9 = False
            next_question()
        elif instance == 2:
            qu9 = False
            next_question()
        elif instance == 3:
            qu9 = True
            ans += 2
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