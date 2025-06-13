import os
import sys
import random
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

translations = {
    "English": {
        "q1": "10. What is the currency of Sweden?",
        "q2": "10. In which country is Ben Nevis, \nthe highest peak of the Cambrian Mountains, located?",
        "q3": "10. Which country has the most islands in Europe?",
        "A1": "A) Euro", "B1": "B) Krona", "C1": "C) Franc", "D1": "D) Pound",
        "A2": "A) Ireland", "B2": "B) England", "C2": "C) Scotland", "D2": "D) Wales",
        "A3": "A) Italy", "B3": "B) Greece", "C3": "C) Norway", "D3": "D) Sweden"
    },
    "Greek": {
        "q1": "10. Ποιο είναι το νόμισμα της Σουηδίας;",
        "q2": "10. Σε ποια χώρα βρίσκεται το Ben Nevis, \nη ψηλότερη κορυφή των Καμβρίων Ορέων;",
        "q3": "10. Ποια χώρα έχει τα περισσότερα νησιά στην Ευρώπη;",
        "A1": "A) Ευρώ", "B1": "B) Κορόνα", "C1": "C) Φράγκο", "D1": "D) Λίρα",
        "A2": "A) Ιρλανδία", "B2": "B) Αγγλία", "C2": "C) Σκωτία", "D2": "D) Ουαλία",
        "A3": "A) Ιταλία", "B3": "B) Ελλάδα", "C3": "C) Νορβηγία", "D3": "D) Σουηδία"
    },
    "French": {
        "q1": "10. Quelle est la monnaie de la Suède ?",
        "q2": "10. Dans quel pays se trouve le Ben Nevis, \nle plus haut sommet des monts Cambriens ?",
        "q3": "10. Quel pays possède le plus d'îles en Europe ?",
        "A1": "A) Euro", "B1": "B) Couronne", "C1": "C) Franc", "D1": "D) Livre",
        "A2": "A) Irlande", "B2": "B) Angleterre", "C2": "C) Écosse", "D2": "D) Pays de Galles",
        "A3": "A) Italie", "B3": "B) Grèce", "C3": "C) Norvège", "D3": "D) Suède"
    }
}
current_language = "English"
def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

qu10 = None
ans = 0

# Main function for the tenth 'Easy' quiz question
# Receives the window, previous score, and correctness of previous questions
# Sets up the tenth question and answer buttons

def easy(window, ans9, qu9, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1, current_language):
    global qu10, ans
    ans += ans9
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

    # Function to proceed to the results screen (calls easy_marks.show_marks)
    def next_question():
        import marks
        # Remove all widgets from the window before showing the results
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu10)
        marks.show_marks(window, ans, qu10, qu9, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1, current_language)

    # Answer button callbacks for each possible answer
    # Each function checks which question is active and updates the score and correctness accordingly
    def answer_a():
        global qu10, ans
        if instance == 1:
            qu10 = False
            next_question()
        elif instance == 2:
            qu10 = False
            next_question()
        elif instance == 3:
            qu10 = False
            next_question()

    def answer_b():
        global qu10, ans
        if instance == 1:
            qu10 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu10 = False
            next_question()
        elif instance == 3:
            qu10 = False
            next_question()

    def answer_c():
        global qu10, ans
        if instance == 1:
            qu10 = False
            next_question()
        elif instance == 2:
            qu10 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu10 = False
            next_question()

    def answer_d():
        global qu10, ans
        if instance == 1:
            qu10 = False
            next_question()
        elif instance == 2:
            qu10 = False
            next_question()
        elif instance == 3:
            qu10 = True
            ans += 2
            next_question()

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

    set_correct_text()