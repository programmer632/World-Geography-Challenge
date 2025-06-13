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
        "q1": "2. What is the capital of Morocco?",
        "q2": "2. Which country has the largest population in Africa?",
        "q3": "2. Which is the second most populous country in Africa after Nigeria?",
        "A1": "A) Luxor", "B1": "B) Cairo", "C1": "C) Abu Dhabi", "D1": "D) Rabat",
        "A2": "A) Egypt", "B2": "B) Nigeria", "C2": "C) Ethiopia", "D2": "D) Congo",
        "A3": "A) Egypt", "B3": "B) Ethiopia", "C3": "C) Congo", "D3": "D) South Africa"
    },
    "Greek": {
        "q1": "2. Ποια είναι η πρωτεύουσα του Μαρόκου;",
        "q2": "2. Ποια χώρα έχει τον μεγαλύτερο πληθυσμό στην Αφρική;",
        "q3": "2. Ποια είναι η δεύτερη πιο πολυπληθής χώρα στην Αφρική μετά τη Νιγηρία;",
        "A1": "A) Λούξορ", "B1": "B) Κάιρο", "C1": "C) Άμπου Ντάμπι", "D1": "D) Ραμπάτ",
        "A2": "A) Αίγυπτος", "B2": "B) Νιγηρία", "C2": "C) Αιθιοπία", "D2": "D) Κονγκό",
        "A3": "A) Αίγυπτος", "B3": "B) Αιθιοπία", "C3": "C) Κονγκό", "D3": "D) Νότια Αφρική"
    },
    "French": {
        "q1": "2. Quelle est la capitale du Maroc ?",
        "q2": "2. Quel pays a la plus grande population d'Afrique ?",
        "q3": "2. Quel est le deuxième pays le plus peuplé d'Afrique après le Nigéria ?",
        "A1": "A) Louxor", "B1": "B) Le Caire", "C1": "C) Abou Dabi", "D1": "D) Rabat",
        "A2": "A) Égypte", "B2": "B) Nigéria", "C2": "C) Éthiopie", "D2": "D) Congo",
        "A3": "A) Égypte", "B3": "B) Éthiopie", "C3": "C) Congo", "D3": "D) Afrique du Sud"
    }
}
current_language = load_language()
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

# Variables for score and correctness of question 2
qu2 = None  # Whether question 2 was answered correctly
ans = 0     # User's score for the hard level

# Main function for the second 'Hard' quiz question
# Receives the window, previous score, and correctness of the first question
# Sets up the question and answer buttons

def hard(window, prev_score, qu1):
    global qu2, ans
    ans += prev_score  # Add previous score to current score
    font = QFont("Calibri", 13)
    question_variant = random.randint(1, 3)  # Randomly select question

    # Create the question label, centered
    question_label = QLabel("", window)
    question_label.setFont(font)
    question_label.setWordWrap(True)  # Enable word wrap
    question_label.setAlignment(Qt.AlignCenter)

    # Set question text (translated)
    if question_variant == 1:
        question_label.setText(tr("q1"))
    elif question_variant == 2:
        question_label.setText(tr("q2"))
    elif question_variant == 3:
        question_label.setText(tr("q3"))

    # Calculate position for the question label
    window_width = window.frameGeometry().width()
    question_width = 600
    question_height = 100
    question_x = (window_width - question_width) // 2
    question_y = 20
    question_label.setGeometry(question_x, question_y, question_width, question_height)
    question_label.setStyleSheet("font-size: 20px; font-weight: bold;")
    question_label.show()

    # Function to proceed to the next question (calls hard3.hard)
    def next_question():
        import hard3
        # Remove all widgets before the next question
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu2)
        hard3.hard(window, ans, qu2, qu1)

    # Answer button callbacks for each possible answer
    def answer_a():
        global qu2, ans
        if question_variant == 1:
            qu2 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")
        elif question_variant == 2:
            qu2 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")
        elif question_variant == 3:
            qu2 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")

    def answer_b():
        global qu2, ans
        if question_variant == 1:
            qu2 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")
        elif question_variant == 2:
            qu2 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")
        elif question_variant == 3:
            qu2 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")

    def answer_c():
        global qu2, ans
        if question_variant == 1:
            qu2 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")
        elif question_variant == 2:
            qu2 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")
        elif question_variant == 3:
            qu2 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")

    def answer_d():
        global qu2, ans
        if question_variant == 1:
            qu2 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")
        elif question_variant == 2:
            qu2 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")
        elif question_variant == 3:
            qu2 = False
            try:
                next_question()
            except Exception as e:
                print(f"Error: {e}")

    # Set button texts (translated)
    def set_correct_text():
        if question_variant == 1:
            button_a.setText(tr("A1"))
            button_b.setText(tr("B1"))
            button_c.setText(tr("C1"))
            button_d.setText(tr("D1"))
        if question_variant == 2:
            button_a.setText(tr("A2"))
            button_b.setText(tr("B2"))
            button_c.setText(tr("C2"))
            button_d.setText(tr("D2"))
        if question_variant == 3:
            button_a.setText(tr("A3"))
            button_b.setText(tr("B3"))
            button_c.setText(tr("C3"))
            button_d.setText(tr("D3"))

    # Create answer buttons and connect them to the correct callback
    button_a = QPushButton("A) France", window)
    button_a.resize(500, 120)
    button_a.move(250, 140)
    button_a.setFont(font)
    button_a.show()
    button_a.clicked.connect(answer_a)

    button_b = QPushButton("B) Spain", window)
    button_b.setFont(font)
    button_b.resize(500, 120)
    button_b.move(250, 270)
    button_b.show()
    button_b.clicked.connect(answer_b)

    button_c = QPushButton("C) Ukraine", window)
    button_c.resize(500, 120)
    button_c.move(250, 400)
    button_c.setFont(font)
    button_c.show()
    button_c.clicked.connect(answer_c)

    button_d = QPushButton("D) Poland", window)
    button_d.resize(500, 120)
    button_d.move(250, 530)
    button_d.setFont(font)
    button_d.show()
    button_d.clicked.connect(answer_d)
    set_correct_text()