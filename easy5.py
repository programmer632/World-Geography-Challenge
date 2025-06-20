import os
import sys
import random
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

translations = {
    "English": {
        "q1": "5. Which country has German, Italian, French, and Romansh as official languages?",
        "q2": "5. Which country has Prague as its capital city?",
        "q3": "5. Which country has Sofia as its capital city?",
        "A1": "A) Switzerland", "B1": "B) Liechtenstein", "C1": "C) Belgium", "D1": "D) Austria",
        "A2": "A) Slovakia", "B2": "B) Czechia", "C2": "C) Latvia", "D2": "D) Albania",
        "A3": "A) Bosnia and Herzegovina", "B3": "B) Romania", "C3": "C) Moldova", "D3": "D) Bulgaria"
    },
    "Greek": {
        "q1": "5. Ποια χώρα έχει ως επίσημες γλώσσες τα γερμανικά, ιταλικά, γαλλικά και ρετορομανικά;",
        "q2": "5. Ποια χώρα έχει πρωτεύουσα την Πράγα;",
        "q3": "5. Ποια χώρα έχει πρωτεύουσα τη Σόφια;",
        "A1": "A) Ελβετία", "B1": "B) Λιχτενστάιν", "C1": "C) Βέλγιο", "D1": "D) Αυστρία",
        "A2": "A) Σλοβακία", "B2": "B) Τσεχία", "C2": "C) Λετονία", "D2": "D) Αλβανία",
        "A3": "A) Βοσνία-Ερζεγοβίνη", "B3": "B) Ρουμανία", "C3": "C) Μολδαβία", "D3": "D) Βουλγαρία"
    },
    "French": {
        "q1": "5. Quel pays a l'allemand, l'italien, le français et le romanche comme langues officielles ?",
        "q2": "5. Quel pays a Prague pour capitale ?",
        "q3": "5. Quel pays a Sofia pour capitale ?",
        "A1": "A) Suisse", "B1": "B) Liechtenstein", "C1": "C) Belgique", "D1": "D) Autriche",
        "A2": "A) Slovaquie", "B2": "B) Tchéquie", "C2": "C) Lettonie", "D2": "D) Albanie",
        "A3": "A) Bosnie-Herzégovine", "B3": "B) Roumanie", "C3": "C) Moldavie", "D3": "D) Bulgarie"
    }
}
current_language = "English"
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

qu5 = None
ans = 0

# Main function for the fifth 'Easy' quiz question
# Receives the window, previous score, and correctness of previous questions
# Sets up the fifth question and answer buttons

def easy(window, ans4, qu4, qu3, qu2, qu1, current_language):
    global qu5, ans
    ans += ans4
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

    # Function to proceed to the next question (calls easy6.easy)
    def next_question():
        import easy6
        # Remove all widgets from the window before showing the next question
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu5)
        easy6.easy(window, ans, qu5, qu4, qu3, qu2, qu1, current_language)

    # Answer button callbacks for each possible answer
    # Each function checks which question is active and updates the score and correctness accordingly
    def answer_a():
        global qu5, ans
        if instance == 1:
            qu5 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu5 = False
            next_question()
        elif instance == 3:
            qu5 = False
            next_question()

    def answer_b():
        global qu5, ans
        if instance == 1:
            qu5 = False
            next_question()
        elif instance == 2:
            qu5 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu5 = False
            next_question()

    def answer_c():
        global qu5, ans
        if instance == 1:
            qu5 = False
            next_question()
        elif instance == 2:
            qu5 = False
            next_question()
        elif instance == 3:
            qu5 = False
            next_question()

    def answer_d():
        global qu5, ans
        if instance == 1:
            qu5 = False
            next_question()
        elif instance == 2:
            qu5 = False
            next_question()
        elif instance == 3:
            qu5 = True
            ans += 2
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