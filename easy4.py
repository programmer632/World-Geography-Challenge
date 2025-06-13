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
        "q1": "4. What is the most densely populated\ncountry in Europe?",
        "q2": "4. What is the smallest country in Europe?",
        "q3": "4. Which country borders the most\nother countries in Europe?",
        "A1": "A) Netherlands", "B1": "B) Germany", "C1": "C) Belgium", "D1": "D) Monaco",
        "A2": "A) Liechtenstein", "B2": "B) San Marino", "C2": "C) Vatican City", "D2": "D) Andorra",
        "A3": "A) France", "B3": "B) Germany", "C3": "C) Italy", "D3": "D) Switzerland"
    },
    "Greek": {
        "q1": "4. Ποια είναι η πιο πυκνοκατοικημένη χώρα\nστην Ευρώπη;",
        "q2": "4. Ποια είναι η μικρότερη χώρα στην Ευρώπη;",
        "q3": "4. Ποια χώρα συνορεύει με τις περισσότερες\nάλλες χώρες στην Ευρώπη;",
        "A1": "A) Ολλανδία", "B1": "B) Γερμανία", "C1": "C) Βέλγιο", "D1": "D) Μονακό",
        "A2": "A) Λιχτενστάιν", "B2": "B) Άγιος Μαρίνος", "C2": "C) Βατικανό", "D2": "D) Ανδόρα",
        "A3": "A) Γαλλία", "B3": "B) Γερμανία", "C3": "C) Ιταλία", "D3": "D) Ελβετία"
    },
    "French": {
        "q1": "4. Quel est le pays le plus densément peuplé\nd'Europe ?",
        "q2": "4. Quel est le plus petit pays d'Europe ?",
        "q3": "4. Quel pays a le plus de frontières\navec d'autres pays en Europe ?",
        "A1": "A) Pays-Bas", "B1": "B) Allemagne", "C1": "C) Belgique", "D1": "D) Monaco",
        "A2": "A) Liechtenstein", "B2": "B) Saint-Marin", "C2": "C) Vatican", "D2": "D) Andorre",
        "A3": "A) France", "B3": "B) Allemagne", "C3": "C) Italie", "D3": "D) Suisse"
    }
}
current_language = load_language()
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

# Main function for the fourth 'Easy' quiz question
# Receives the window, previous score, and correctness of previous questions
# Sets up the fourth question and answer buttons

def easy(window, ans3, qu3, qu2, qu1):
    global qu4, ans
    ans += ans3  # Add previous score to current score
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)  # Randomly select which question to show

    # Create the question label, centered horizontally
    question = QLabel("", window)
    question.setFont(font)
    question.setAlignment(Qt.AlignCenter)

    # Set the question text based on the random variant (multilingual)
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

    # Function to proceed to the next question (calls easy5.easy)
    def next_question():
        import easy5
        # Remove all widgets from the window before showing the next question
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu4)
        easy5.easy(window, ans, qu4, qu3, qu2, qu1)

    # Answer button callbacks for each possible answer
    # Each function checks which question is active and updates the score and correctness accordingly
    def answer_dania():
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

    def answer_kroatia():
        global qu4, ans
        if instance == 1:
            qu4 = False
            ans += 2
            next_question()
        elif instance == 2:
            qu4 = False
            next_question()
        elif instance == 3:
            qu4 = True
            ans += 2
            next_question()

    def answer_norway():
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

    def answer_lichtenstain():
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

    # Set the button texts according to the question instance (multilingual)
    def set_correct_text():
        if instance == 1:
            dania.setText(tr("A1"))
            kroatia.setText(tr("B1"))
            norway.setText(tr("C1"))
            poland.setText(tr("D1"))
        elif instance == 2:
            dania.setText(tr("A2"))
            kroatia.setText(tr("B2"))
            norway.setText(tr("C2"))
            poland.setText(tr("D2"))
        elif instance == 3:
            dania.setText(tr("A3"))
            kroatia.setText(tr("B3"))
            norway.setText(tr("C3"))
            poland.setText(tr("D3"))

    # Create answer buttons and connect them to the correct callback
    dania = QPushButton("", window)
    dania.resize(500, 120)
    dania.move(250, 140)
    dania.setFont(font)
    dania.show()
    dania.clicked.connect(answer_dania)

    kroatia = QPushButton("", window)
    kroatia.setFont(font)
    kroatia.resize(500, 120)
    kroatia.move(250, 270)
    kroatia.show()
    kroatia.clicked.connect(answer_kroatia)

    norway = QPushButton("", window)
    norway.resize(500, 120)
    norway.move(250, 400)
    norway.setFont(font)
    norway.show()
    norway.clicked.connect(answer_norway)

    poland = QPushButton("", window)
    poland.resize(500, 120)
    poland.move(250, 530)
    poland.setFont(font)
    poland.show()
    poland.clicked.connect(answer_lichtenstain)
    set_correct_text()