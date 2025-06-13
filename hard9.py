import os
import sys
import random
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

# --- LANGUAGE SUPPORT ---
translations = {
    "English": {
        "q1": "9. Which of the following countries does NOT border the Democratic Republic of the Congo?",
        "q2": "9. Which African country has the only flag that is not rectangular, but has two triangles?",
        "q3": "9. What is the capital of Botswana?",
        "A1": "A) Angola", "B1": "B) Central African Republic", "C1": "C) Zambia", "D1": "D) Nigeria",
        "A2": "A) Nepal", "B2": "B) Botswana", "C2": "C) South Africa", "D2": "D) There is no such African country",
        "A3": "A) Francistown", "B3": "B) Livingstone", "C3": "C) Gaborone", "D3": "D) Windhoek"
    },
    "Greek": {
        "q1": "9. Ποια από τις παρακάτω χώρες ΔΕΝ συνορεύει με τη Λαϊκή Δημοκρατία του Κονγκό;",
        "q2": "9. Ποια αφρικανική χώρα έχει τη μοναδική σημαία που δεν είναι ορθογώνια αλλά έχει δύο τρίγωνα;",
        "q3": "9. Ποια είναι η πρωτεύουσα της Μποτσουάνα;",
        "A1": "A) Αγκόλα", "B1": "B) Κεντροαφρικανική Δημοκρατία", "C1": "C) Ζάμπια", "D1": "D) Νιγηρία",
        "A2": "A) Νεπάλ", "B2": "B) Μποτσουάνα", "C2": "C) Νότια Αφρική", "D2": "D) Δεν υπάρχει τέτοια αφρικανική χώρα",
        "A3": "A) Φράνσισταουν", "B3": "B) Λίβινγκστον", "C3": "C) Γκαμπορόνε", "D3": "D) Βίντχουκ"
    },
    "French": {
        "q1": "9. Lequel des pays suivants ne borde PAS la République démocratique du Congo ?",
        "q2": "9. Quel pays africain a le seul drapeau qui n'est pas rectangulaire, mais a deux triangles ?",
        "q3": "9. Quelle est la capitale du Botswana ?",
        "A1": "A) Angola", "B1": "B) République centrafricaine", "C1": "C) Zambie", "D1": "D) Nigeria",
        "A2": "A) Népal", "B2": "B) Botswana", "C2": "C) Afrique du Sud", "D2": "D) Il n'y a pas un tel pays africain",
        "A3": "A) Francistown", "B3": "B) Livingstone", "C3": "C) Gaborone", "D3": "D) Windhoek"
    }
}
current_language = "English"
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

# Main function for the ninth 'Hard' quiz question
# Receives the window, previous score, and correctness of previous questions
# Sets up the question and answer buttons

def hard(window, prev_score, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1, current_language):
    global qu9, ans
    ans += prev_score
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)
    def tr(key):
        return translations.get(current_language, translations["English"]).get(key, key)

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

    # Function to proceed to the next question (calls hard10.hard)
    def next_question():
        import hard10
        # Remove all widgets before the next question
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu9)
        hard10.hard(window, ans, qu9, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1, current_language)

    # Answer button callbacks for each possible answer
    def answer_a():
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

    def answer_b():
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

    def answer_c():
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

    def answer_d():
        global qu9, ans
        if instance == 1:
            qu9 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu9 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu9 = False
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