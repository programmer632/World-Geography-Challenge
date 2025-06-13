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
        "q1": "9. What is the capital of Hungary?",
        "q2": "9. Which of the following country-capital pairs\nis a correct match?",
        "q3": "9. What is the longest river in Europe?",
        "A1": "A) Budapest", "B1": "B) Belgrade", "C1": "C) Vienna", "D1": "D) Prague",
        "A2": "A) Georgia-Yerevan", "B2": "B) Armenia-Tbilisi", "C2": "C) Armenia-Baku", "D2": "D) Georgia-Tbilisi",
        "A3": "A) Danube", "B3": "B) Volga", "C3": "C) Rhine", "D3": "D) Seine"
    },
    "Greek": {
        "q1": "9. Ποια είναι η πρωτεύουσα της Ουγγαρίας;",
        "q2": "9. Ποιο από τα παρακάτω ζεύγη χώρας-πρωτεύουσας είναι σωστό;",
        "q3": "9. Ποιος είναι ο μεγαλύτερος ποταμός της Ευρώπης;",
        "A1": "A) Βουδαπέστη", "B1": "B) Βελιγράδι", "C1": "C) Βιέννη", "D1": "D) Πράγα",
        "A2": "A) Γεωργία-Γερεβάν", "B2": "B) Αρμενία-Τιφλίδα", "C2": "C) Αρμενία-Μπακού", "D2": "D) Γεωργία-Τιφλίδα",
        "A3": "A) Δούναβης", "B3": "B) Βόλγας", "C3": "C) Ρήνος", "D3": "D) Σηκουάνας"
    },
    "French": {
        "q1": "9. Quelle est la capitale de la Hongrie ?",
        "q2": "9. Laquelle des paires pays-capitale suivantes\nest correcte ?",
        "q3": "9. Quel est le plus long fleuve d'Europe ?",
        "A1": "A) Budapest", "B1": "B) Belgrade", "C1": "C) Vienne", "D1": "D) Prague",
        "A2": "A) Géorgie-Erevan", "B2": "B) Arménie-Tbilissi", "C2": "C) Arménie-Bakou", "D2": "D) Géorgie-Tbilissi",
        "A3": "A) Danube", "B3": "B) Volga", "C3": "C) Rhin", "D3": "D) Seine"
    }
}
current_language = load_language()
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

qu9 = None
ans = 0

# Main function for the ninth 'Easy' quiz question
# Receives the window, previous score, and correctness of previous questions
# Sets up the ninth question and answer buttons

def easy(window, ans8, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1):
    global qu9, ans
    ans += ans8  # Add previous score to current score
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

    # Function to proceed to the next question (calls easy10.easy)
    def next_question():
        import easy10
        # Remove all widgets from the window before showing the next question
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu9)
        easy10.easy(window, ans, qu9, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1)

    # Answer button callbacks for each possible answer
    # Each function checks which question is active and updates the score and correctness accordingly
    def answer_dania():
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

    def answer_kroatia():
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

    def answer_norway():
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

    def answer_lichtenstain():
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

    # Set the button texts according to the question instance (translated)
    def set_correct_text():
        if instance == 1:
            dania.setText(tr("A1"))
            kroatia.setText(tr("B1"))
            norway.setText(tr("C1"))
            poland.setText(tr("D1"))
        if instance == 2:
            dania.setText(tr("A2"))
            kroatia.setText(tr("B2"))
            norway.setText(tr("C2"))
            poland.setText(tr("D2"))
        if instance == 3:
            dania.setText(tr("A3"))
            kroatia.setText(tr("B3"))
            norway.setText(tr("C3"))
            poland.setText(tr("D3"))

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