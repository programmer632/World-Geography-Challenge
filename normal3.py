from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu3 = None
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
        "q1": "3. What is the largest island in South America?",
        "q2": "3. Which South American country has two official languages: Spanish and Guarani?",
        "q3": "3. Which country has the most languages in the world?",
        "A1": "A) Margarita Island", "B1": "B) Chiloé Island", "C1": "C) Tierra del Fuego", "D1": "D) Saint Martin",
        "A2": "A) Chile", "B2": "B) Paraguay", "C2": "C) Suriname", "D2": "D) Venezuela",
        "A3": "A) India", "B3": "B) China", "C3": "C) Indonesia", "D3": "D) Papua New Guinea"
    },
    "Greek": {
        "q1": "3. Ποιο είναι το μεγαλύτερο νησί στη Νότια Αμερική;",
        "q2": "3. Ποια χώρα της Νότιας Αμερικής έχει δύο επίσημες γλώσσες: Ισπανικά και Γκουαρανί;",
        "q3": "3. Ποια χώρα έχει τις περισσότερες γλώσσες στον κόσμο;",
        "A1": "A) Νήσος Μαργαρίτα", "B1": "B) Νήσος Τσιλόε", "C1": "C) Γη του Πυρός", "D1": "D) Άγιος Μαρτίνος",
        "A2": "A) Χιλή", "B2": "B) Παραγουάη", "C2": "C) Σουρινάμ", "D2": "D) Βενεζουέλα",
        "A3": "A) Ινδία", "B3": "B) Κίνα", "C3": "C) Ινδονησία", "D3": "D) Παπούα Νέα Γουινέα"
    },
    "French": {
        "q1": "3. Quelle est la plus grande île d'Amérique du Sud ?",
        "q2": "3. Quel pays d'Amérique du Sud a deux langues officielles : l'espagnol et le guarani ?",
        "q3": "3. Quel pays a le plus de langues au monde ?",
        "A1": "A) Île Margarita", "B1": "B) Île Chiloé", "C1": "C) Terre de Feu", "D1": "D) Saint-Martin",
        "A2": "A) Chili", "B2": "B) Paraguay", "C2": "C) Suriname", "D2": "D) Venezuela",
        "A3": "A) Inde", "B3": "B) Chine", "C3": "C) Indonésie", "D3": "D) Papouasie-Nouvelle-Guinée"
    }
}
current_language = load_language()
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

def normal(window, ans2, qu2, qu1):
    global qu3, ans, current_language
    ans += ans2
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)
    current_language = load_language()
    question = QLabel("", window)
    question.setFont(font)
    question.setWordWrap(True)
    question.setAlignment(Qt.AlignCenter)
    # Set the question text based on the random variant (multilingual)
    if instance == 1:
        question.setText(tr("q1"))
    elif instance == 2:
        question.setText(tr("q2"))
    elif instance == 3:
        question.setText(tr("q3"))

    window_width = window.frameGeometry().width()
    question_width = 600
    question_height = 100
    question_x = (window_width - question_width) // 2
    question_y = 20
    question.setGeometry(question_x, question_y, question_width, question_height)
    question.setStyleSheet("font-size: 20px; font-weight: bold;")
    question.show()

    def next_question():
        import normal4
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu3)
        normal4.normal(window, ans, qu3, qu2, qu1)

    # Answer button callbacks for each possible answer
    # Each function checks which question is active and updates the score and correctness accordingly
    def answer_a():
        global qu3, ans
        if instance == 1:
            qu3 = False
            next_question()
        elif instance == 2:
            qu3 = False
            next_question()
        elif instance == 3:
            qu3 = False
            next_question()

    def answer_b():
        global qu3, ans
        if instance == 1:
            qu3 = False
            next_question()
        elif instance == 2:
            qu3 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu3 = False
            next_question()

    def answer_c():
        global qu3, ans
        if instance == 1:
            qu3 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu3 = False
            next_question()
        elif instance == 3:
            qu3 = False
            next_question()

    def answer_d():
        global qu3, ans
        if instance == 1:
            qu3 = False
            next_question()
        elif instance == 2:
            qu3 = False
            next_question()
        elif instance == 3:
            qu3 = True
            ans += 2
            next_question()

    # Set the button texts according to the question instance (multilingual)
    def set_button_texts():
        if instance == 1:
            button_a.setText(tr("A1"))
            button_b.setText(tr("B1"))
            button_c.setText(tr("C1"))
            button_d.setText(tr("D1"))
        elif instance == 2:
            button_a.setText(tr("A2"))
            button_b.setText(tr("B2"))
            button_c.setText(tr("C2"))
            button_d.setText(tr("D2"))
        elif instance == 3:
            button_a.setText(tr("A3"))
            button_b.setText(tr("B3"))
            button_c.setText(tr("C3"))
            button_d.setText(tr("D3"))

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