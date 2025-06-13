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
        "q1": "7. In which country is the region of Tuscany located?",
        "q2": "7. What is the largest lake in Europe?",
        "q3": "7. Which country borders Latvia?",
        "A1": "A) France", "B1": "B) Italy", "C1": "C) Greece", "D1": "D) Spain",
        "A2": "A) Balaton", "B2": "B) Vänern", "C2": "C) Ladoga", "D2": "D) Como",
        "A3": "A) Lithuania", "B3": "B) Poland", "C3": "C) Finland", "D3": "D) Moldova"
    },
    "Greek": {
        "q1": "7. Σε ποια χώρα βρίσκεται η περιοχή της Τοσκάνης;",
        "q2": "7. Ποια είναι η μεγαλύτερη λίμνη στην Ευρώπη;",
        "q3": "7. Ποια χώρα συνορεύει με τη Λετονία;",
        "A1": "A) Γαλλία", "B1": "B) Ιταλία", "C1": "C) Ελλάδα", "D1": "D) Ισπανία",
        "A2": "A) Μπάλατον", "B2": "B) Βένερν", "C2": "C) Λάντογκα", "D2": "D) Κόμο",
        "A3": "A) Λιθουανία", "B3": "B) Πολωνία", "C3": "C) Φινλανδία", "D3": "D) Μολδαβία"
    },
    "French": {
        "q1": "7. Dans quel pays se trouve la région de Toscane ?",
        "q2": "7. Quel est le plus grand lac d'Europe ?",
        "q3": "7. Quel pays borde la Lettonie ?",
        "A1": "A) France", "B1": "B) Italie", "C1": "C) Grèce", "D1": "D) Espagne",
        "A2": "A) Balaton", "B2": "B) Vänern", "C2": "C) Ladoga", "D2": "D) Côme",
        "A3": "A) Lituanie", "B3": "B) Pologne", "C3": "C) Finlande", "D3": "D) Moldavie"
    }
}
current_language = load_language()
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

qu7 = None
ans = 0

# Main function for the seventh 'Easy' quiz question
# Receives the window, previous score, and correctness of previous questions
# Sets up the seventh question and answer buttons

def easy(window, ans6, qu6, qu5, qu4, qu3, qu2, qu1):
    global qu7, ans
    ans += ans6  # Add previous score to current score
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

    # Function to proceed to the next question (calls easy8.easy)
    def next_question():
        import easy8
        # Remove all widgets from the window before showing the next question
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu7)
        easy8.easy(window, ans, qu7, qu6, qu5, qu4, qu3, qu2, qu1)

    # Answer button callbacks for each possible answer
    # Each function checks which question is active and updates the score and correctness accordingly
    def answer_dania():
        global qu7, ans
        if instance == 1:
            qu7 = False
            next_question()
        elif instance == 2:
            qu7 = False
            next_question()
        elif instance == 3:
            qu7 = True
            ans += 2
            next_question()

    def answer_kroatia():
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

    def answer_norway():
        global qu7, ans
        if instance == 1:
            qu7 = False
            next_question()
        elif instance == 2:
            qu7 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu7 = False
            next_question()

    def answer_lichtenstain():
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

    # Set the button texts according to the question instance (all in English)
    def set_correct_text():
        if instance == 1:
            dania.setText("A) France")
            kroatia.setText("B) Italy")
            norway.setText("C) Greece")
            poland.setText("D) Spain")
        if instance == 2:
            dania.setText("A) Balaton")
            kroatia.setText("B) Vänern")
            norway.setText("C) Ladoga")
            poland.setText("D) Como")
        if instance == 3:
            dania.setText("A) Lithuania")
            kroatia.setText("B) Poland")
            norway.setText("C) Finland")
            poland.setText("D) Moldova")

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