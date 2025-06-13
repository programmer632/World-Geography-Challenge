import os
import sys
import random
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

# --- LANGUAGE SUPPORT ---
translations = {
    "English": {
        "q1": "8. Which country has a black five-pointed star on its flag, placed on a red background?",
        "q2": "8. Which country borders South Africa but is landlocked?",
        "q3": "8. What is the capital of Ivory Coast?",
        "A1": "A) Cameroon", "B1": "B) Morocco", "C1": "C) Mali", "D1": "D) Senegal",
        "A2": "A) Lesotho", "B2": "B) Namibia", "C2": "C) Mozambique", "D2": "D) Angola",
        "A3": "A) Monrovia", "B3": "B) Conakry", "C3": "C) Bamako", "D3": "D) Yamoussoukro"
    },
    "Greek": {
        "q1": "8. Ποια χώρα έχει μια μαύρη πεντάκτινη αστέρι στη σημαία της, τοποθετημένη σε κόκκινο φόντο;",
        "q2": "8. Ποια χώρα συνορεύει με τη Νότια Αφρική αλλά δεν έχει θάλασσα;",
        "q3": "8. Ποια είναι η πρωτεύουσα της Ακτής Ελεφαντοστού;",
        "A1": "A) Καμερούν", "B1": "B) Μαρόκο", "C1": "C) Μάλι", "D1": "D) Σενεγάλη",
        "A2": "A) Λεσότο", "B2": "B) Ναμίμπια", "C2": "C) Μοζαμβίκη", "D2": "D) Αγκόλα",
        "A3": "A) Μονρόβια", "B3": "B) Κονακρί", "C3": "C) Μπαμάκο", "D3": "D) Γιαμουσουκρό"
    },
    "French": {
        "q1": "8. Quel pays a une étoile noire à cinq branches sur son drapeau, placée sur un fond rouge ?",
        "q2": "8. Quel pays borde l'Afrique du Sud mais est enclavé ?",
        "q3": "8. Quelle est la capitale de la Côte d'Ivoire ?",
        "A1": "A) Cameroun", "B1": "B) Maroc", "C1": "C) Mali", "D1": "D) Sénégal",
        "A2": "A) Lesotho", "B2": "B) Namibie", "C2": "C) Mozambique", "D2": "D) Angola",
        "A3": "A) Monrovia", "B3": "B) Conakry", "C3": "C) Bamako", "D3": "D) Yamoussoukro"
    }
}
current_language = "English"
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

# Main function for the eighth 'Hard' quiz question
# Receives the window, previous score, and correctness of previous questions
# Sets up the question and answer buttons

def hard(window, prev_score, qu7, qu6, qu5, qu4, qu3, qu2, qu1, current_language):
    global qu8, ans
    ans += prev_score  # Add previous score to current score
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)

    # Create the question label, centered
    question_label = QLabel("", window)
    question_label.setFont(font)
    question_label.setWordWrap(True)  # Enable word wrap
    question_label.setAlignment(Qt.AlignCenter)  # Center the text in the label

    # Set question text (multilingual)
    if instance == 1:
        question_label.setText(tr('q1'))
    elif instance == 2:
        question_label.setText(tr('q2'))
    elif instance == 3:
        question_label.setText(tr('q3'))

    # Calculate position for the question label
    window_width = window.frameGeometry().width()
    question_width = 600
    question_height = 100
    question_x = (window_width - question_width) // 2
    question_y = 20
    question_label.setGeometry(question_x, question_y, question_width, question_height)
    question_label.setStyleSheet("font-size: 20px; font-weight: bold;")
    question_label.show()

    # Function to proceed to the next question (calls hard9.hard)
    def next_question():
        import hard9
        # Remove all widgets before the next question
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu8)
        hard9.hard(window, ans, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1, current_language)

    # Answer button callbacks for each possible answer
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
            qu8 = True
            ans += 2
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
            qu8 = False
            next_question()

    def answer_d():
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

    # Set button texts according to the question (multilingual)
    def set_correct_text():
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

    set_correct_text()