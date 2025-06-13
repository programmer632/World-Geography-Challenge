from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu7 = None
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
        "q1": "7. What is the longest river in Asia?",
        "q2": "7. In which American country is Machu Picchu located?",
        "q3": "7. What is the capital city of Argentina?",
        "A1": "A) Yangtze", "B1": "B) Ganges", "C1": "C) Mekong", "D1": "D) Ob",
        "A2": "A) Ecuador", "B2": "B) Bolivia", "C2": "C) Peru", "D2": "D) Chile",
        "A3": "A) Montevideo", "B3": "B) Santiago", "C3": "C) Buenos Aires", "D3": "D) Rio de Janeiro"
    },
    "Greek": {
        "q1": "7. Ποιος είναι ο μεγαλύτερος ποταμός στην Ασία;",
        "q2": "7. Σε ποια αμερικανική χώρα βρίσκεται το Μάτσου Πίτσου;",
        "q3": "7. Ποια είναι η πρωτεύουσα της Αργεντινής;",
        "A1": "A) Γιανγκτσέ", "B1": "B) Γάγγης", "C1": "C) Μεκόνγκ", "D1": "D) Ομπ",
        "A2": "A) Ισημερινός", "B2": "B) Βολιβία", "C2": "C) Περού", "D2": "D) Χιλή",
        "A3": "A) Μοντεβιδέο", "B3": "B) Σαντιάγο", "C3": "C) Μπουένος Άιρες", "D3": "D) Ρίο ντε Τζανέιρο"
    },
    "French": {
        "q1": "7. Quel est le plus long fleuve d'Asie ?",
        "q2": "7. Dans quel pays d'Amérique se trouve le Machu Picchu ?",
        "q3": "7. Quelle est la capitale de l'Argentine ?",
        "A1": "A) Yangtsé", "B1": "B) Gange", "C1": "C) Mékong", "D1": "D) Ob",
        "A2": "A) Équateur", "B2": "B) Bolivie", "C2": "C) Pérou", "D2": "D) Chili",
        "A3": "A) Montevideo", "B3": "B) Santiago", "C3": "C) Buenos Aires", "D3": "D) Rio de Janeiro"
    }
}
current_language = load_language()
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

def normal(window, ans6, qu6, qu5, qu4, qu3, qu2, qu1, current_language):
    global qu7, ans
    ans += ans6
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)

    def tr(key):
        return translations.get(current_language, translations["English"]).get(key, key)

    question = QLabel("", window)
    question.setFont(font)
    question.setWordWrap(True)
    question.setAlignment(Qt.AlignCenter)
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
        import normal8
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu7)
        normal8.normal(window, ans, qu7, qu6, qu5, qu4, qu3, qu2, qu1, current_language)

    def answer_a():
        global qu7, ans
        if instance == 1:
            qu7 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu7 = False
            next_question()
        elif instance == 3:
            qu7 = False
            next_question()

    def answer_b():
        global qu7, ans
        if instance == 1:
            qu7 = False
            next_question()
        elif instance == 2:
            qu7 = False
            next_question()
        elif instance == 3:
            qu7 = False
            next_question()

    def answer_c():
        global qu7, ans
        if instance == 1:
            qu7 = False
            next_question()
        elif instance == 2:
            qu7 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu7 = True
            ans += 2
            next_question()

    def answer_d():
        global qu7, ans
        if instance == 1:
            qu7 = False
            next_question()
        elif instance == 2:
            qu7 = False
            next_question()
        elif instance == 3:
            qu7 = False
            next_question()

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