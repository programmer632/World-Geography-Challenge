from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

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
        "q1": "6. Which of the following rivers\nflows through the city of London?",
        "q2": "6. Which of the following mountains is\nthe highest in Europe?",
        "q3": "6. Which of the following cities is\nthe capital of Austria?",
        "A1": "A) Seine", "B1": "B) Rhine", "C1": "C) Thames", "D1": "D) Danube",
        "A2": "A) Elbrus", "B2": "B) Matterhorn", "C2": "C) Mont Blanc", "D2": "D) Kilimanjaro",
        "A3": "A) Vienna", "B3": "B) Budapest", "C3": "C) Bern", "D3": "D) Nicosia"
    },
    "Greek": {
        "q1": "6. Ποιος από τους παρακάτω ποταμούς\nδιασχίζει το Λονδίνο;",
        "q2": "6. Ποιο από τα παρακάτω βουνά είναι\nτο ψηλότερο στην Ευρώπη;",
        "q3": "6. Ποια από τις παρακάτω πόλεις είναι\nπρωτεύουσα της Αυστρίας;",
        "A1": "A) Σηκουάνας", "B1": "B) Ρήνος", "C1": "C) Τάμεσης", "D1": "D) Δούναβης",
        "A2": "A) Ελμπρούς", "B2": "B) Μάττερχορν", "C2": "C) Μον Μπλαν", "D2": "D) Κιλιμάντζαρο",
        "A3": "A) Βιέννη", "B3": "B) Βουδαπέστη", "C3": "C) Βέρνη", "D3": "D) Λευκωσία"
    },
    "French": {
        "q1": "6. Lequel des fleuves suivants\ntraverse la ville de Londres ?",
        "q2": "6. Lequel des montagnes suivantes est\nle plus haut d'Europe ?",
        "q3": "6. Laquelle des villes suivantes est\nla capitale de l'Autriche ?",
        "A1": "A) Seine", "B1": "B) Rhin", "C1": "C) Tamise", "D1": "D) Danube",
        "A2": "A) Elbrouz", "B2": "B) Cervin", "C2": "C) Mont Blanc", "D2": "D) Kilimandjaro",
        "A3": "A) Vienne", "B3": "B) Budapest", "C3": "C) Berne", "D3": "D) Nicosie"
    }
}
current_language = load_language()
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

qu6 = None
ans = 0

# Main function for the sixth 'Easy' quiz question
# Receives the window, previous score, and correctness of previous questions
# Sets up the sixth question and answer buttons

def easy(window, ans5, qu5, qu4, qu3, qu2, qu1):
    global qu6, ans
    ans += ans5  # Add previous score to current score
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)  # Randomly select which question to show

    # Create the question label, centered horizontally
    question = QLabel("", window)
    question.setFont(font)
    question.setAlignment(Qt.AlignCenter)

    # Set the question text based on the random variant (translated)
    if instance == 1:
        question.setText(tr("q1"))
    elif instance == 2:
        question.setText(tr("q2"))
    elif instance == 3:
        question.setText(tr("q3"))

    # Calculate position to center the label horizontally and place it near the top
    window_width = window.frameGeometry().width()
    question_width = 600
    question_height = 100
    question_x = (window_width - question_width) // 2
    question_y = 20
    question.setGeometry(question_x, question_y, question_width, question_height)
    question.setStyleSheet("font-size: 20px; font-weight: bold;")
    question.show()

    # Function to proceed to the next question (calls easy7.easy)
    def next_question():
        import easy7
        # Remove all widgets from the window before showing the next question
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu6)
        easy7.easy(window, ans, qu6, qu5, qu4, qu3, qu2, qu1)

    # Answer button callbacks for each possible answer
    # Each function checks which question is active and updates the score and correctness accordingly
    def answer_dania():
        global qu6, ans
        if instance == 1:
            qu6 = False
            next_question()
        elif instance == 2:
            qu6 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu6 = True
            ans += 2
            next_question()

    def answer_kroatia():
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

    def answer_norway():
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

    def answer_lichtenstain():
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

    # Set the button texts according to the question instance (all in English)
    def set_correct_text():
        if instance == 1:
            dania.setText("A) Seine")
            kroatia.setText("B) Rhine")
            norway.setText("C) Thames")
            poland.setText("D) Danube")
        if instance == 2:
            dania.setText("A) Elbrus")
            kroatia.setText("B) Matterhorn")
            norway.setText("C) Mont Blanc")
            poland.setText("D) Kilimanjaro")
        if instance == 3:
            dania.setText("A) Vienna")
            kroatia.setText("B) Budapest")
            norway.setText("C) Bern")
            poland.setText("D) Nicosia")

    # Create answer buttons with translated text and connect them to the correct callback
    dania = QPushButton(tr(f"A{instance}"), window)
    dania.resize(500, 120)
    dania.move(250, 140)
    dania.setFont(font)
    dania.show()
    dania.clicked.connect(answer_dania)

    kroatia = QPushButton(tr(f"B{instance}"), window)
    kroatia.setFont(font)
    kroatia.resize(500, 120)
    kroatia.move(250, 270)
    kroatia.show()
    kroatia.clicked.connect(answer_kroatia)

    norway = QPushButton(tr(f"C{instance}"), window)
    norway.resize(500, 120)
    norway.move(250, 400)
    norway.setFont(font)
    norway.show()
    norway.clicked.connect(answer_norway)

    poland = QPushButton(tr(f"D{instance}"), window)
    poland.resize(500, 120)
    poland.move(250, 530)
    poland.setFont(font)
    poland.show()
    poland.clicked.connect(answer_lichtenstain)
    set_correct_text()