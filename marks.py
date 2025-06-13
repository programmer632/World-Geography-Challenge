from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QVBoxLayout, QLineEdit, QTableView
from PyQt5.QtGui import QIcon, QFont, QStandardItemModel, QStandardItem, QPixmap, QImage, QColor
from PyQt5.QtCore import QTimer, Qt
import sys
import threading
import matplotlib.pyplot as plt
import os
import io
import json

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
        "back": "Back",
        "return": "Return",
        "answers_progress": "Answers Progress",
        "completed": "🎉 Completed! Score: {score}/20",
        "checking": "⏳ Checking your answers...",
        "question": "Question {num}: ",
        "correct": "✅ Question {num}: Correct",
        "wrong": "❌ Question {num}: Wrong",
        "show_leaderboard": "Show Leaderboard",
        "save": "Save",
        "close": "Close",
        "clear": "Clear",
        "enter_name": "Enter your name",
        "leadboard": "Leaderboard"
    },
    "Greek": {
        "back": "Επιστροφή",
        "return": "Επιστροφή",
        "answers_progress": "Εξέλιξη Απαντήσεων",
        "completed": "🎉 Ολοκληρώθηκε! Βαθμολογία: {score}/20",
        "checking": "⏳ Έλεγχος απαντήσεων...",
        "question": "Ερώτηση {num}: ",
        "correct": "✅ Ερώτηση {num}: Σωστό",
        "wrong": "❌ Ερώτηση {num}: Λάθος",
        "show_leaderboard": "Προβολή Βαθμολογίας",
        "save": "Αποθήκευση",
        "close": "Κλείσιμο",
        "clear": "Εκκαθάριση",
        "enter_name": "Εισάγετε το όνομά σας",
        "leadboard": "Βαθμολογία"
    },
    "French": {
        "back": "Retour",
        "return": "Retour",
        "answers_progress": "Progression des réponses",
        "completed": "🎉 Terminé ! Score : {score}/20",
        "checking": "⏳ Vérification de vos réponses...",
        "question": "Question {num} : ",
        "correct": "✅ Question {num} : Correct",
        "wrong": "❌ Question {num} : Faux",
        "show_leaderboard": "Afficher le classement",
        "save": "Enregistrer",
        "close": "Fermer",
        "clear": "Effacer",
        "enter_name": "Entrez votre nom",
        "leadboard": "Classement"
    }
}
current_language = load_language()
def tr(key, **kwargs):
    text = translations.get(current_language, translations["English"]).get(key, key)
    if kwargs:
        return text.format(**kwargs)
    return text

# Path settings
if getattr(sys, 'frozen', False):
    # When running as .exe, base is the folder containing the executable
    base_path = os.path.dirname(sys.executable)
else:
    # When running as script, base is the current folder
    base_path = os.path.abspath(".")

def resource_path(relative_path):
    # Used for read-only resources (e.g. icons, sounds)
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# File paths
imaje = resource_path("186-europis-70x100-1.ico")
path = os.path.join(base_path, "data.json")         # Saved next to the .exe

font = QFont("Calibri", 18)
correct_color = QColor(0, 128, 0)    # Green
wrong_color = QColor(255, 0, 0)      # Red
info_color = QColor(0, 102, 204)     # Blue

# Global variables for answers and statistics
list_with_answers = None
true_list = [0]
correct_count = None
diagram_pixmap = None

def create_diagram():
    global list_with_answers, true_list
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in list_with_answers:
        length = len(true_list)
        if i:
            if length == 1:
                true_list.append(1)
            elif length >= 2:
                true_list.append(true_list[length-1] + 1)
        else:
            if length == 1:
                true_list.append(-1)
            elif length >= 2:
                true_list.append(true_list[length-1] - 1)
    # All labels and titles in English
    plt.plot(x, true_list, marker="o", linestyle="-", color="b", label=tr('answers_progress'))
    plt.xlabel(tr('question', num=''))
    plt.ylabel(tr('correct'))
    plt.title(tr('answers_progress'))
    plt.legend()
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format="png", dpi=150, bbox_inches="tight")
    img_buffer.seek(0)
    global diagram_pixmap
    image = QImage()
    image.loadFromData(img_buffer.getvalue())
    diagram_pixmap = QPixmap(image)
    img_buffer.close()
    plt.close()

def back(layout):
    widgets_to_remove = []
    for i in range(layout.count()):
        widget = layout.itemAt(i).widget()
        if widget and (isinstance(widget, QLabel) and widget.pixmap() or isinstance(widget, QPushButton) and widget.text() == tr("return")):
            widgets_to_remove.append(widget)
    for widget in widgets_to_remove:
        layout.removeWidget(widget)
        widget.deleteLater()
    for i in range(layout.count()):
        widget = layout.itemAt(i).widget()
        if widget:
            widget.show()

def show_diagrams(layout):
    for i in range(layout.count()):
        widget = layout.itemAt(i).widget()
        if widget:
            widget.hide()
    label_statistic = QLabel()
    label_statistic.setPixmap(diagram_pixmap)
    layout.addWidget(label_statistic)
    but_return = QPushButton(tr("return"))
    but_return.setFont(font)
    but_return.setStyleSheet("""
        QPushButton { background-color: #006633; color: white; padding: 10px; border-radius: 5px; min-width: 200px; }
        QPushButton:hover { background-color: #008040; }
    """)
    but_return.clicked.connect(lambda: back(layout))
    layout.addWidget(but_return)

def false(question_number, layout):
    # Show a label for a wrong answer for each question
    if (question_number-1) <= 9:
        wrong_label = QLabel(tr("wrong", num=question_number))
        wrong_label.setFont(font)
        wrong_label.setStyleSheet(f"color: {wrong_color.name()}; padding: 5px; background-color: #ffe6e6;")
        layout.addWidget(wrong_label)
    # On the last question, show the statistics button
    if question_number == 10:
        statistics_button = QPushButton(tr("answers_progress"))
        statistics_button.setFont(font)
        statistics_button.setStyleSheet("""
            QPushButton { background-color: #006633; color: white; padding: 10px; border-radius: 5px; min-width: 200px; }
            QPushButton:hover { background-color: #008040; }
        """)
        # Create the diagram in a background thread
        thread = threading.Thread(target=create_diagram, daemon=True)
        thread.start()
        statistics_button.clicked.connect(lambda: show_diagrams(layout))
        layout.addWidget(statistics_button)

def true(question_number, layout):
    # Show a label for a correct answer for each question
    correct_label = QLabel(tr("correct", num=question_number))
    correct_label.setFont(font)
    correct_label.setStyleSheet(f"color: {correct_color.name()}; padding: 5px; background-color: #e6ffe6;")
    layout.addWidget(correct_label)
    # On the last question, show the statistics button
    if question_number == 10:
        statistics_button = QPushButton(tr("answers_progress"))
        statistics_button.setFont(font)
        statistics_button.setStyleSheet("""
            QPushButton { background-color: #006633; color: white; padding: 10px; border-radius: 5px; min-width: 200px; }
            QPushButton:hover { background-color: #008040; }
        """)
        thread = threading.Thread(target=create_diagram, daemon=True)
        thread.start()
        statistics_button.clicked.connect(lambda: show_diagrams(layout))
        layout.addWidget(statistics_button)

# Function to show the leaderboard window
def show_leaderboard_window():
    leaderboard_window = QWidget()
    leaderboard_window.setWindowTitle(tr("leadboard"))
    leaderboard_window.setStyleSheet("background-color: #f0f0f0;")
    if os.path.exists(imaje):
        leaderboard_window.setWindowIcon(QIcon(imaje))
    leaderboard_window.resize(450, 500)

    leaderboard_layout = QVBoxLayout()
    leaderboard_layout.setAlignment(Qt.AlignCenter)
    leaderboard_layout.setSpacing(10)
    leaderboard_window.setLayout(leaderboard_layout)

    text_field = QLineEdit()
    text_field.setFont(font)
    text_field.setPlaceholderText(tr("enter_name"))

    button_save = QPushButton(tr("save"))
    button_save.setFont(font)
    button_save.setStyleSheet("""
        QPushButton { background-color: #006633; color: white; padding: 10px; border-radius: 5px; min-width: 200px; }
        QPushButton:hover { background-color: #008040; }
    """)
    button_save.clicked.connect(lambda: save_name(text_field, leaderboard_window))

    button_close = QPushButton(tr("close"))
    button_close.setFont(font)
    button_close.setStyleSheet("""
        QPushButton { background-color: #006633; color: white; padding: 10px; border-radius: 5px; min-width: 200px; }
        QPushButton:hover { background-color: #008040; }
    """)
    button_close.clicked.connect(leaderboard_window.close)

    button_clear = QPushButton(tr("clear"))
    button_clear.setFont(font)
    button_clear.setStyleSheet("""
        QPushButton { background-color: #006633; color: white; padding: 10px; border-radius: 5px; min-width: 200px; }
        QPushButton:hover { background-color: #008040; }
    """)
    button_clear.clicked.connect(lambda: clear_leaderboard(leaderboard_window))

    leaderboard_layout.addWidget(text_field)
    leaderboard_layout.addWidget(button_save)
    leaderboard_layout.addWidget(button_close)
    leaderboard_layout.addWidget(button_clear)

    create_leaderboard_table(leaderboard_window, leaderboard_layout)
    leaderboard_window.show()

def save_name(text_field, leaderboard_window):
    name = text_field.text()
    if name.strip():
        save_all(name, leaderboard_window)
    else:
        print("Please enter a valid name.")

def save_all(name, leaderboard_window):
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as json_file:
                dictionary = json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError):
            dictionary = {}
    else:
        dictionary = {}
    dictionary[name] = correct_count * 2
    try:
        with open(path, "w", encoding="utf-8") as json_file:
            json.dump(dictionary, json_file, indent=4)
    except PermissionError:
        print("Error: No write permissions in the folder.")
    create_leaderboard_table(leaderboard_window, leaderboard_window.layout())

def clear_leaderboard(leaderboard_window):
    dictionary = {}
    try:
        with open(path, "w", encoding="utf-8") as json_file:
            json.dump(dictionary, json_file, indent=4)
    except PermissionError:
        print("Error: No write permissions in the folder.")
    create_leaderboard_table(leaderboard_window, leaderboard_window.layout())

def create_leaderboard_table(leaderboard_window, layout):
    for i in reversed(range(layout.count())):
        widget = layout.itemAt(i).widget()
        if isinstance(widget, QTableView):
            layout.removeWidget(widget)
            widget.deleteLater()
    try:
        with open(path, "r", encoding="utf-8") as json_file:
            dictionary = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        dictionary = {}

    if not dictionary:
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Rank", tr("enter_name"), "Score"])
        table_view = QTableView()
        table_view.setModel(model)
        table_view.setStyleSheet("""
            QTableView { background-color: #ffffff; padding: 5px; font: 18pt Calibri; }
            QHeaderView::section { background-color: #e6f3ff; padding: 5px; }
        """)
        layout.insertWidget(0, table_view)
        return

    sorted_data = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(["Rank", tr("enter_name"), "Score"])

    for i, (name, score) in enumerate(sorted_data, start=1):
        rank_item = QStandardItem(str(i))
        name_item = QStandardItem(name)
        score_item = QStandardItem(str(score))
        rank_item.setEditable(False)
        name_item.setEditable(False)
        score_item.setEditable(False)
        model.setItem(i - 1, 0, rank_item)
        model.setItem(i - 1, 1, name_item)
        model.setItem(i - 1, 2, score_item)

    table_view = QTableView()
    table_view.setModel(model)
    table_view.setStyleSheet("""
        QTableView { background-color: #ffffff; padding: 5px; font: 18pt Calibri; }
        QHeaderView::section { background-color: #e6f3ff; padding: 5px; }
    """)
    layout.insertWidget(0, table_view)

def show_leaderboard():
    global correct_count
    show_leaderboard_window()

def show_marks(window, ans10, qu10, qu9, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1, current_language=None):
    # --- LANGUAGE HANDLING ---
    # Αν δοθεί όρισμα, χρησιμοποίησέ το, αλλιώς φόρτωσε από αρχείο
    if current_language is not None:
        lang = current_language
    else:
        try:
            with open(language_file, 'r', encoding='utf-8') as f:
                lang = f.read().strip().capitalize()
                if lang not in translations:
                    lang = "English"
        except Exception:
            lang = "English"
    def tr(key, **kwargs):
        text = translations.get(lang, translations["English"]).get(key, key)
        if kwargs:
            return text.format(**kwargs)
        return text

    layout = QVBoxLayout()
    layout.setAlignment(Qt.AlignCenter)
    layout.setSpacing(10)
    window.setStyleSheet("background-color: #f0f0f0;")
    window.setLayout(layout)

    start_label = QLabel(tr("checking"))
    start_label.setFont(font)
    start_label.setStyleSheet(f"color: {info_color.name()}; padding: 10px;")
    start_label.setAlignment(Qt.AlignCenter)
    layout.addWidget(start_label)

    def scan_answers():
        global list_with_answers
        list_with_answers = [qu1, qu2, qu3, qu4, qu5, qu6, qu7, qu8, qu9, qu10]
        for y, answer in enumerate(list_with_answers, start=1):
            if answer:
                timer.singleShot(y * 800, lambda y=y: true(y, layout))
            else:
                timer.singleShot(y * 800, lambda y=y: false(y, layout))
        timer.singleShot(len(list_with_answers) * 800 + 1000, lambda: start_label.hide())
        timer.singleShot(len(list_with_answers) * 800 + 1500, show_summary)

    def show_summary():
        global correct_count
        correct_count = sum(1 for ans in [qu1, qu2, qu3, qu4, qu5, qu6, qu7, qu8, qu9, qu10] if ans)
        summary_label = QLabel(tr("completed", score=correct_count*2))
        summary_label.setFont(QFont("Calibri", 20, QFont.Bold))
        summary_label.setStyleSheet("color: #006633; padding: 15px; background-color: #e6f3ff;")
        summary_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(summary_label)

        button_leaderboard = QPushButton(tr("show_leaderboard"))
        button_leaderboard.setFont(font)
        button_leaderboard.setStyleSheet("""
            QPushButton { background-color: #004080; color: white; padding: 10px; border-radius: 5px; min-width: 200px; }
            QPushButton:hover { background-color: #0059b3; }
        """)
        button_leaderboard.clicked.connect(show_leaderboard)
        layout.addWidget(button_leaderboard)

    timer = QTimer()
    scan_answers()