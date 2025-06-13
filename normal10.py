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
        "q1": "10. What is the largest active volcano in Asia?",
        "q2": "10. Which is the only South American country with coasts on both the Atlantic and Pacific Oceans?",
        "q3": "10. What is the highest mountain in North America?",
        "A1": "A) Mount Fuji", "B1": "B) Krakatoa", "C1": "C) Tambora", "D1": "D) Erebus",
        "A2": "A) Colombia", "B2": "B) Argentina", "C2": "C) Chile", "D2": "D) Uruguay",
        "A3": "A) Mount Rainier", "B3": "B) Mount St. Elias", "C3": "C) Mount McKinley (Denali)", "D3": "D) Orizaba"
    },
    "Greek": {
        "q1": "10. Ποιο είναι το μεγαλύτερο ενεργό ηφαίστειο στην Ασία;",
        "q2": "10. Ποια είναι η μόνη χώρα της Νότιας Αμερικής με ακτές τόσο στον Ατλαντικό όσο και στον Ειρηνικό Ωκεανό;",
        "q3": "10. Ποιο είναι το ψηλότερο βουνό στη Βόρεια Αμερική;",
        "A1": "A) Φούτζι", "B1": "B) Κρακατόα", "C1": "C) Ταμπόρα", "D1": "D) Έρεβος",
        "A2": "A) Κολομβία", "B2": "B) Αργεντινή", "C2": "C) Χιλή", "D2": "D) Ουρουγουάη",
        "A3": "A) Ρέινιερ", "B3": "B) Σεντ Έλιας", "C3": "C) ΜακΚίνλεϊ (Ντενάλι)", "D3": "D) Οριζάμπα"
    },
    "French": {
        "q1": "10. Quel est le plus grand volcan actif d'Asie ?",
        "q2": "10. Quel est le seul pays d'Amérique du Sud avec des côtes sur l'Atlantique et le Pacifique ?",
        "q3": "10. Quelle est la plus haute montagne d'Amérique du Nord ?",
        "A1": "A) Mont Fuji", "B1": "B) Krakatoa", "C1": "C) Tambora", "D1": "D) Erebus",
        "A2": "A) Colombie", "B2": "B) Argentine", "C2": "C) Chili", "D2": "D) Uruguay",
        "A3": "A) Mont Rainier", "B3": "B) Mont St. Elias", "C3": "C) Mont McKinley (Denali)", "D3": "D) Orizaba"
    }
}
current_language = load_language()
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

def normal(window, ans9, qu9, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1):
    global qu10, ans, current_language
    ans += ans9
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
        # Proceed to the marks/results screen (marks)
        import marks
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu10)
        marks.show_marks(window, ans, qu10, qu9, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1)

    # Answer button callbacks for each possible answer
    # Each function checks which question is active and updates the score and correctness accordingly
    # The correct answer for each question is marked in the set_button_texts function
    def answer_a():
        global qu10, ans
        if instance == 1:
            qu10 = True   # Mount Fuji is correct
            ans += 2
            next_question()
        elif instance == 2:
            qu10 = True   # Colombia is correct
            ans += 2
            next_question()
        elif instance == 3:
            qu10 = False  # Mount Rainier is not correct
            next_question()

    def answer_b():
        global qu10, ans
        if instance == 1:
            qu10 = False  # Krakatoa is not correct
            next_question()
        elif instance == 2:
            qu10 = False  # Argentina is not correct
            next_question()
        elif instance == 3:
            qu10 = False  # Mount St. Elias is not correct
            next_question()

    def answer_c():
        global qu10, ans
        if instance == 1:
            qu10 = False  # Tambora is not correct
            next_question()
        elif instance == 2:
            qu10 = False  # Chile is not correct
            next_question()
        elif instance == 3:
            qu10 = True   # Mount McKinley (Denali) is correct
            ans += 2
            next_question()

    def answer_d():
        global qu10, ans
        if instance == 1:
            qu10 = False  # Erebus is not correct
            next_question()
        elif instance == 2:
            qu10 = False  # Uruguay is not correct
            next_question()
        elif instance == 3:
            qu10 = False  # Orizaba is not correct
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
    # All buttons are styled and positioned consistently
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

    set_button_texts()  # Set the answer texts for the current question