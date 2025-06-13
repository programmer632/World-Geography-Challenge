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
        "q1": "3. Which European country is completely\nsurrounded by Italy?",
        "q2": "3. Which country has Budapest as its capital city?",
        "q3": "3. Which country is crossed by the Danube river?",
        "A1": "A) San Marino", "B1": "B) Italy", "C1": "C) Vatican City", "D1": "D) Monaco",
        "A2": "A) Slovakia", "B2": "B) Hungary", "C2": "C) Romania", "D2": "D) Serbia",
        "A3": "A) Spain", "B3": "B) Germany", "C3": "C) France", "D3": "D) Portugal"
    },
    "Greek": {
        "q1": "3. Ποια ευρωπαϊκή χώρα περιβάλλεται εξ ολοκλήρου από την Ιταλία;",
        "q2": "3. Ποια χώρα έχει πρωτεύουσα τη Βουδαπέστη;",
        "q3": "3. Ποια χώρα διασχίζεται από τον ποταμό Δούναβη;",
        "A1": "A) Άγιος Μαρίνος", "B1": "B) Ιταλία", "C1": "C) Βατικανό", "D1": "D) Μονακό",
        "A2": "A) Σλοβακία", "B2": "B) Ουγγαρία", "C2": "C) Ρουμανία", "D2": "D) Σερβία",
        "A3": "A) Ισπανία", "B3": "B) Γερμανία", "C3": "C) Γαλλία", "D3": "D) Πορτογαλία"
    },
    "French": {
        "q1": "3. Quel pays européen est entièrement entouré par l'Italie ?",
        "q2": "3. Quel pays a Budapest pour capitale ?",
        "q3": "3. Quel pays est traversé par le Danube ?",
        "A1": "A) Saint-Marin", "B1": "B) Italie", "C1": "C) Vatican", "D1": "D) Monaco",
        "A2": "A) Slovaquie", "B2": "B) Hongrie", "C2": "C) Roumanie", "D2": "D) Serbie",
        "A3": "A) Espagne", "B3": "B) Allemagne", "C3": "C) France", "D3": "D) Portugal"
    }
}
current_language = load_language()
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

qu3 = None
ans = 0

# Main function for the third 'Easy' quiz question
# Receives the window, previous score, and correctness of previous questions
# Sets up the third question and answer buttons

def easy(window, ans2, qu2, qu1):
    global qu3, ans
    ans += ans2  # Add previous score to current score
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

    # Function to proceed to the next question (calls easy4.easy)
    def next_question():
        import easy4
        # Remove all widgets from the window before showing the next question
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu3)
        easy4.easy(window, ans, qu3, qu2, qu1)

    # Answer button callbacks for each possible answer
    # Each function checks which question is active and updates the score and correctness accordingly
    def answer_dania():
        global qu3, ans
        if instance == 1:
            qu3 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu3 = False
            next_question()
        elif instance == 3:
            qu3 = False
            next_question()

    def answer_kroatia():
        global qu3, ans
        if instance == 1:
            qu3 = False
            next_question()
        elif instance == 2:
            qu3 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu3 = True
            ans += 2
            next_question()

    def answer_norway():
        global qu3, ans
        if instance == 1:
            qu3 = False
            next_question()
        elif instance == 2:
            qu3 = False
            next_question()
        elif instance == 3:
            qu3 = False
            next_question()

    def answer_lichtenstain():
        global qu3, ans
        if instance == 1:
            qu3 = False
            next_question()
        elif instance == 2:
            qu3 = False
            next_question()
        elif instance == 3:
            qu3 = False
            next_question()

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

    lichtenstain = QPushButton(tr(f"D{instance}"), window)
    lichtenstain.resize(500, 120)
    lichtenstain.move(250, 530)
    lichtenstain.setFont(font)
    lichtenstain.show()
    lichtenstain.clicked.connect(answer_lichtenstain)