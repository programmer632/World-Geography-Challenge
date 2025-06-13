import os
import sys
import random
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

translations = {
    "English": {
        "q1": "8. Which mountain range separates Europe from Asia?",
        "q2": "8. What is the name of the peninsula that, along with the Scandinavian Peninsula,\nseparates the North Sea from the Baltic Sea?",
        "q3": "8. What is the capital of Belarus?",
        "A1": "A) Pyrenees", "B1": "B) Carpathians", "C1": "C) Alps", "D1": "D) Urals",
        "A2": "A) Jutland", "B2": "B) Kola", "C2": "C) Crimea", "D2": "D) Balkan Peninsula",
        "A3": "A) Vienna", "B3": "B) Chisinau", "C3": "C) Minsk", "D3": "D) Yerevan"
    },
    "Greek": {
        "q1": "8. Ποια οροσειρά χωρίζει την Ευρώπη από την Ασία;",
        "q2": "8. Ποια είναι η χερσόνησος που μαζί με τη Σκανδιναβική\nχωρίζει τη Βόρεια Θάλασσα από τη Βαλτική;",
        "q3": "8. Ποια είναι η πρωτεύουσα της Λευκορωσίας;",
        "A1": "A) Πυρηναία", "B1": "B) Καρπάθια", "C1": "C) Άλπεις", "D1": "D) Ουράλια",
        "A2": "A) Γιουτλάνδη", "B2": "B) Κόλα", "C2": "C) Κριμαία", "D2": "D) Βαλκανική Χερσόνησος",
        "A3": "A) Βιέννη", "B3": "B) Κισινάου", "C3": "C) Μινσκ", "D3": "D) Ερεβάν"
    },
    "French": {
        "q1": "8. Quelle chaîne de montagnes sépare l'Europe de l'Asie ?",
        "q2": "8. Quel est le nom de la péninsule qui, avec la péninsule scandinave,\nsépare la mer du Nord de la mer Baltique ?",
        "q3": "8. Quelle est la capitale de la Biélorussie ?",
        "A1": "A) Pyrénées", "B1": "B) Carpates", "C1": "C) Alpes", "D1": "D) Oural",
        "A2": "A) Jutland", "B2": "B) Kola", "C2": "C) Crimée", "D2": "D) Péninsule balkanique",
        "A3": "A) Vienne", "B3": "B) Chisinau", "C3": "C) Minsk", "D3": "D) Erevan"
    }
}
current_language = "English"
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

qu8 = None
ans = 0

# Main function for the eighth 'Easy' quiz question
# Receives the window, previous score, and correctness of previous questions
# Sets up the eighth question and answer buttons

def easy(window, ans7, qu7, qu6, qu5, qu4, qu3, qu2, qu1, current_language):
    global qu8, ans
    ans += ans7
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

    # Function to proceed to the next question (calls easy9.easy)
    def next_question():
        import easy9
        # Remove all widgets from the window before showing the next question
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu8)
        easy9.easy(window, ans, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1, current_language)

    # Answer button callbacks for each possible answer
    # Each function checks which question is active and updates the score and correctness accordingly
    def answer_a():
        global qu8, ans
        if instance == 1:
            qu8 = False
            next_question()
        elif instance == 2:
            qu8 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu8 = False
            next_question()

    def answer_b():
        global qu8, ans
        if instance == 1:
            qu8 = False
            next_question()
        elif instance == 2:
            qu8 = False
            next_question()
        elif instance == 3:
            qu8 = False
            next_question()

    def answer_c():
        global qu8, ans
        if instance == 1:
            qu8 = False
            next_question()
        elif instance == 2:
            qu8 = False
            next_question()
        elif instance == 3:
            qu8 = True
            ans += 2
            next_question()

    def answer_d():
        global qu8, ans
        if instance == 1:
            qu8 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu8 = False
            next_question()
        elif instance == 3:
            qu8 = False
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