import os
import sys
import random
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

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
current_language = "English"
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

qu6 = None
ans = 0

# Main function for the sixth 'Easy' quiz question
# Receives the window, previous score, and correctness of previous questions
# Sets up the sixth question and answer buttons

def easy(window, ans5, qu5, qu4, qu3, qu2, qu1, current_language):
    global qu6, ans
    ans += ans5
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)

    def tr(key):
        return translations.get(current_language, translations["English"]).get(key, key)

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
        easy7.easy(window, ans, qu6, qu5, qu4, qu3, qu2, qu1, current_language)

    # Answer button callbacks for each possible answer
    # Each function checks which question is active and updates the score and correctness accordingly
    def answer_a():
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

    def answer_b():
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
            qu6 = False
            next_question()
        elif instance == 3:
            qu6 = False
            next_question()

    # Set the button texts according to the question instance (all in English)
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
    dania.clicked.connect(answer_a)

    kroatia = QPushButton(tr(f"B{instance}"), window)
    kroatia.setFont(font)
    kroatia.resize(500, 120)
    kroatia.move(250, 270)
    kroatia.show()
    kroatia.clicked.connect(answer_b)

    norway = QPushButton(tr(f"C{instance}"), window)
    norway.resize(500, 120)
    norway.move(250, 400)
    norway.setFont(font)
    norway.show()
    norway.clicked.connect(answer_c)

    poland = QPushButton(tr(f"D{instance}"), window)
    poland.resize(500, 120)
    poland.move(250, 530)
    poland.setFont(font)
    poland.show()
    poland.clicked.connect(answer_d)
    set_correct_text()