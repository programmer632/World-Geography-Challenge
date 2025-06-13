from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QCheckBox, QApplication, QFileDialog, QVBoxLayout,QComboBox,QGroupBox
from PyQt5.QtGui import QFont, QIcon
import os
import sys
import threading
import random
import time
import subprocess
from PyQt5.QtCore import Qt
import json

try:
    import vlc
except ImportError:
    print("Error: VLC not found. Install it with 'pip install python-vlc'.")
    sys.exit(1)
try:
    import easy
    import normal
    import hard
except ImportError as e:
    print(f"Error: Module {e.name} not found.")
    sys.exit(1)

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

setting = resource_path("extra_files/settings.json")
language_file = resource_path("extra_files/language.txt")
path1 = resource_path("extra_files/music.mp3")
path2 = resource_path("extra_files/Vibramusic.mp3")
path3 = resource_path("extra_files/Memories-of-Spring(chosic.com).mp3")
path4 = resource_path("extra_files/Cinspirational.mp3")
path5 = resource_path("extra_files/Sarakinoi.mp3")  # Translated from Greek to English
imaje = resource_path("extra_files/186-europis-70x100-1.ico")

# --- SETTINGS HANDLING WITH JSON ---
# Map string keys to actual file paths
path_map = {
    "path1": path1,
    "path2": path2,
    "path3": path3,
    "path4": path4,
    "path5": path5
}

# --- TRANSLATIONS ---
translations = {
    "English": {
        "main_title": "Geography Quiz",
        "select_level": "Select difficulty level",
        "settings": "Settings",
        "easy": "Easy",
        "normal": "Normal",
        "hard": "Hard",
        "back": "Back",
        "choose_language": "Choose your language",
        "choose_music": "Choose your music",
        "standard_music": "Standard Music",
        "memories": "Memories of Spring",
        "vibramusic": "Vibramusic",
        "cinspirational": "Cinspirational",
        "sarakinoi": "Sarakinoi",
        "try_music": "Try out the music you chose.",
        "play_custom": "Play from your own file.",
        "save_changes": "Save changes.",
        "note": "Note: If you don't save the changes next time nothing will have changed."
    },
    "Greek": {
        "main_title": "Κουίζ Γεωγραφίας",
        "select_level": "Επιλέξτε επίπεδο δυσκολίας",
        "settings": "Ρυθμίσεις",
        "easy": "Εύκολο",
        "normal": "Μεσαίο",
        "hard": "Δύσκολο",
        "back": "Πίσω",
        "choose_language": "Επιλέξτε γλώσσα",
        "choose_music": "Επιλέξτε μουσική",
        "standard_music": "Τυπική Μουσική",
        "memories": "Αναμνήσεις της Άνοιξης",
        "vibramusic": "Vibramusic",
        "cinspirational": "Cinspirational",
        "sarakinoi": "Σαρακηνοί",
        "try_music": "Δοκιμάστε τη μουσική που επιλέξατε.",
        "play_custom": "Αναπαραγωγή δικού σας αρχείου.",
        "save_changes": "Αποθήκευση αλλαγών.",
        "note": "Σημείωση: Αν δεν αποθηκεύσετε τις αλλαγές, την επόμενη φορά δεν θα έχουν εφαρμοστεί."
    },
    "French": {
        "main_title": "Quiz de Géographie",
        "select_level": "Sélectionnez le niveau de difficulté",
        "settings": "Paramètres",
        "easy": "Facile",
        "normal": "Moyen",
        "hard": "Difficile",
        "back": "Retour",
        "choose_language": "Choisissez votre langue",
        "choose_music": "Choisissez votre musique",
        "standard_music": "Musique Standard",
        "memories": "Souvenirs du Printemps",
        "vibramusic": "Vibramusic",
        "cinspirational": "Cinspirational",
        "sarakinoi": "Sarakinoi",
        "try_music": "Essayez la musique que vous avez choisie.",
        "play_custom": "Jouer votre propre fichier.",
        "save_changes": "Enregistrer les modifications.",
        "note": "Remarque : Si vous n'enregistrez pas les modifications, rien ne changera la prochaine fois."
    }
}

# --- LOAD LANGUAGE FROM TXT ---
def load_language():
    try:
        with open(language_file, 'r', encoding='utf-8') as f:
            lang = f.read().strip().capitalize()
            if lang in translations:
                return lang
    except Exception:
        pass
    return "English"

current_language = load_language()

def tr(key):
    return translations.get(current_language, translations["English"]).get(key, key)

# If settings.json does not exist, create it with default values
if not os.path.exists(setting):
    print(f"{setting} not found. Creating with default values.")
    dict_setting = {k: ("1" if k == "path1" else "0") for k in path_map}
    with open(setting, 'w', encoding='utf-8') as settings_file:
        json.dump(dict_setting, settings_file, indent=4)
else:
    with open(setting, "r", encoding="utf-8") as settings_file:
        dict_setting = json.load(settings_file)
        print(dict_setting)

# Build music_quest from dict_setting
music_quest = [path_map[k] for k in path_map if str(dict_setting.get(k, "0")) == "1" and os.path.exists(path_map[k])]

# Create the default font for all widgets
font = QFont("Calibri", 15)
# Create the main QApplication instance (required for all PyQt5 apps)
app = QApplication([])
# Create the main window for the application
window = QWidget()
# Set the window title
window.setWindowTitle("Geography Quiz")
# Create the VLC MediaPlayer instance for background music
player = vlc.MediaPlayer()

# Function to handle background music playback in a loop
# This function runs in a separate thread and keeps playing random music from the enabled list
# It uses the global music_quest list, which contains the paths to enabled music files
# The player object is used to play the music
# If no music is available, it prints a message and exits
# The function checks the state of the player and, if a track ends, starts a new random one
# A small sleep is used to avoid high CPU usage

def sound():
    def random_choice():
        global music_quest
        if not music_quest:
            print("No music available.")
            return
        x = random.choice(music_quest)  # Select a random music file from the enabled list
        media = vlc.Media(x)            # Create a VLC media object for the selected file
        player.set_media(media)         # Set the media to the player
        player.play()                   # Start playback
        player.audio_set_volume(100)    # Set volume to 100%
    random_choice()
    while True:
        state = player.get_state()      # Get the current state of the player
        time.sleep(0.2)
        if state == vlc.State.Ended:    # If the track ended, play another random one
            random_choice()
        time.sleep(1)  # Small delay to avoid CPU overload

# If at least one music track is enabled and available, start the background music thread
if music_quest:
    thread = threading.Thread(target=sound, daemon=True)  # Create a daemon thread for music playback
    thread.start()

def go_to_easy():
    for widget in window.children():
        widget.deleteLater()
    window.repaint()
    easy.easy(window, current_language)

def go_to_normal():
    for widget in window.children():
        widget.deleteLater()
    window.repaint()
    normal.normal(window, current_language)

def go_to_hard():
    for widget in window.children():
        widget.deleteLater()
    window.repaint()
    hard.hard(window, current_language)

# The main function that initializes the main menu and handles navigation between screens.
def start():
    # Remove all widgets from the window to prepare for the new screen.
    for widget in window.children():
        widget.deleteLater()
    window.repaint()

    # --- SETTINGS SCREEN ---
    def settings():
        # This function displays the settings screen, allowing the user to select which music tracks are enabled.
        # It also provides options to demo music, open a custom file, and restart the game to apply changes.

        def set_language(selected_language):
            global current_language
            current_language = selected_language
            # Save to language.txt immediately when language changes
            with open(language_file, 'w', encoding='utf-8') as f:
                f.write(selected_language.lower())
            # Update all widget texts dynamically
            languages_frame.setTitle(tr("choose_language"))
            group_music.setTitle(tr("choose_music"))
            music1.setText(tr("standard_music"))
            music2.setText(tr("memories"))
            music3.setText(tr("vibramusic"))
            music4.setText(tr("cinspirational"))
            music5.setText(tr("sarakinoi"))
            btn_back.setText(tr("back"))
            btn_demo.setText(tr("try_music"))
            btn_open_custom.setText(tr("play_custom"))
            btn_save_changes.setText(tr("save_changes"))
            note.setText(tr("note"))
            window.setWindowTitle(tr("main_title"))

        def demo_music():
            demo_player = vlc.MediaPlayer()
            player.stop()  # Stop the main player to avoid conflicts

            def back_to_settings():
                demo_player.stop()
                time.sleep(0.1)
                player.play()
                demo_window.deleteLater()
                settings()

            def demo_Standard_Music():
                if dict_setting["path1"] == "1" and os.path.exists(path1):
                    y = vlc.Media(path1)
                    demo_player.set_media(y)
                    if demo_player.get_state() == vlc.State.Playing:
                        demo_player.stop()
                    demo_player.play()

            def demo_Vibramusic():
                if dict_setting["path2"] == "1" and os.path.exists(path2):
                    y = vlc.Media(path2)
                    demo_player.set_media(y)
                    if demo_player.get_state() == vlc.State.Playing:
                        demo_player.stop()
                    demo_player.play()

            def demo_Memories_of_Spring():
                if dict_setting["path3"] == "1" and os.path.exists(path3):
                    y = vlc.Media(path3)
                    demo_player.set_media(y)
                    if demo_player.get_state() == vlc.State.Playing:
                        demo_player.stop()
                    demo_player.play()

            def demo_Cinspirational():
                if dict_setting["path4"] == "1" and os.path.exists(path4):
                    y = vlc.Media(path4)
                    demo_player.set_media(y)
                    if demo_player.get_state() == vlc.State.Playing:
                        demo_player.stop()
                    demo_player.play()

            def demo_Sarakinoi():
                if dict_setting["path5"] == "1" and os.path.exists(path5):
                    y = vlc.Media(path5)
                    demo_player.set_media(y)
                    if demo_player.get_state() == vlc.State.Playing:
                        demo_player.stop()
                    demo_player.play()

            demo_window = QWidget()
            demo_window.setWindowTitle("Geography Quiz")
            demo_window.resize(500, 400)
            layout = QVBoxLayout()

            if dict_setting["path1"] == "1" and os.path.exists(path1):
                but_Standard_Music = QPushButton("Standard Music", demo_window)
                but_Standard_Music.setFont(font)
                layout.addWidget(but_Standard_Music)
                but_Standard_Music.clicked.connect(demo_Standard_Music)
            if dict_setting["path3"] == "1" and os.path.exists(path3):
                but_Memories_of_Spring = QPushButton("Memories of Spring", demo_window)
                but_Memories_of_Spring.setFont(font)
                layout.addWidget(but_Memories_of_Spring)
                but_Memories_of_Spring.clicked.connect(demo_Memories_of_Spring)
            if dict_setting["path2"] == "1" and os.path.exists(path2):
                but_Vibramusic = QPushButton("Vibramusic", demo_window)
                but_Vibramusic.setFont(font)
                layout.addWidget(but_Vibramusic)
                but_Vibramusic.clicked.connect(demo_Vibramusic)
            if dict_setting["path4"] == "1" and os.path.exists(path4):
                but_Cinspirational = QPushButton("Cinspirational", demo_window)
                but_Cinspirational.setFont(font)
                layout.addWidget(but_Cinspirational)
                but_Cinspirational.clicked.connect(demo_Cinspirational)
            if dict_setting["path5"] == "1" and os.path.exists(path5):
                but_Sarakinoi = QPushButton("Sarakinoi", demo_window)
                but_Sarakinoi.setFont(font)
                layout.addWidget(but_Sarakinoi)
                but_Sarakinoi.clicked.connect(demo_Sarakinoi)

            back = QPushButton("Back", demo_window)
            back.setFont(font)
            layout.addWidget(back)
            back.clicked.connect(back_to_settings)

            demo_window.setLayout(layout)
            demo_window.show()

        def go_to_back():
            global music_quest, quest_setting, dict_setting
            # Ενημέρωσε το dict_setting με βάση τα checkbox
            dict_setting["path1"] = "1" if music1.isChecked() else "0"
            dict_setting["path2"] = "1" if music3.isChecked() else "0"
            dict_setting["path3"] = "1" if music2.isChecked() else "0"
            dict_setting["path4"] = "1" if music4.isChecked() else "0"
            dict_setting["path5"] = "1" if music5.isChecked() else "0"
            # Αποθήκευσε ως JSON
            with open(setting, 'w', encoding='utf-8') as settings_file:
                json.dump(dict_setting, settings_file, indent=4)
            # Ενημέρωσε το music_quest
            music_quest.clear()
            for k in path_map:
                if dict_setting[k] == "1" and os.path.exists(path_map[k]):
                    music_quest.append(path_map[k])
            start()

        def save_changes():
            global music_quest, dict_setting
            dict_setting["path1"] = "1" if music1.isChecked() else "0"
            dict_setting["path2"] = "1" if music3.isChecked() else "0"
            dict_setting["path3"] = "1" if music2.isChecked() else "0"
            dict_setting["path4"] = "1" if music4.isChecked() else "0"
            dict_setting["path5"] = "1" if music5.isChecked() else "0"
            with open(setting, 'w', encoding='utf-8') as settings_file:
                json.dump(dict_setting, settings_file, indent=4)
            # Save language
            with open(language_file, 'w', encoding='utf-8') as f:
                f.write(current_language.lower())
            # Update music_quest
            music_quest.clear()
            for k in path_map:
                if dict_setting[k] == "1" and os.path.exists(path_map[k]):
                    music_quest.append(path_map[k])
            # Restart music if needed
            player.stop()
            if music_quest:
                x = random.choice(music_quest)
                media = vlc.Media(x)
                player.set_media(media)
                player.play()
                player.audio_set_volume(100)

        def open_the_file():
            music_file, _ = QFileDialog.getOpenFileName(window, "Open Video", "", "Music Files (*.mp3 *.wav *.m4a *.opus)")
            if music_file:
                player.stop()
                media = vlc.Media(music_file)
                player.set_media(media)
                time.sleep(0.1)
                player.play()

        for widget in window.children():
            widget.hide()

        #Create QGroupBox with a QComboBox widget for language selection
        languages_frame=QGroupBox(tr("choose_language"), window)
        languages_frame.setFont(font)
        languages_frame.move(565,10)
        layout=QVBoxLayout()#This layout is just for languages_frame
        languages_frame.resize(400,100)
        languages_frame.setLayout(layout)
        languages=QComboBox(window)
        languages.addItems(["English","Greek","French"])
        languages.setFont(font)
        languages.currentTextChanged.connect(set_language)
        layout.addWidget(languages)

        # Create QCheckBox widgets for music selection
        music1 = QCheckBox(tr("standard_music"))
        music1.setFont(font)

        music2 = QCheckBox(tr("memories"))
        music2.setFont(font)

        music3 = QCheckBox(tr("vibramusic"))
        music3.setFont(font)

        music4 = QCheckBox(tr("cinspirational"))
        music4.setFont(font)

        music5 = QCheckBox(tr("sarakinoi"))
        music5.setFont(font)

        btn_back = QPushButton(tr("back"), window)
        btn_back.setFont(font)
        btn_back.resize(400, 100)
        btn_back.move(300, 390)

        btn_demo = QPushButton(tr("try_music"), window)
        btn_demo.setFont(font)
        btn_demo.resize(400, 100)
        btn_demo.move(568, 180)

        btn_open_custom = QPushButton(tr("play_custom"), window)
        btn_open_custom.setFont(font)
        btn_open_custom.resize(400, 100)
        btn_open_custom.move(568, 285)

        note = QLabel(tr("note"), window)
        note.setFont(font)
        note.resize(600, 150)
        note.setStyleSheet("""
            border: 2px solid black; border-radius: 10px; font-size: 20px;
        """)
        
        note.setAlignment(Qt.AlignCenter)
        note.setWordWrap(True)
        note.move(200, 500)

        btn_save_changes = QPushButton(tr("save_changes"), window)
        btn_save_changes.setFont(font)
        btn_save_changes.resize(400, 100)
        btn_save_changes.move(300, 670)

        group_music=QGroupBox(tr("choose_music"),window)
        layout_for_music = QVBoxLayout()
        group_music.setLayout(layout_for_music)
        group_music.setFont(font)
        group_music.resize(520,350)
        group_music.move(10,10)

        # Add the music checkboxes to the GroupBox
        layout_for_music.addWidget(music1)
        layout_for_music.addWidget(music2)
        layout_for_music.addWidget(music3)
        layout_for_music.addWidget(music4)
        layout_for_music.addWidget(music5)
        
        # Show all widgets
        btn_save_changes.show()
        btn_demo.show()
        btn_open_custom.show()
        btn_back.show()
        group_music.show()
        note.show()
        languages.show()
        languages_frame.show()

        # Button connections
        btn_open_custom.clicked.connect(open_the_file)
        btn_back.clicked.connect(go_to_back)
        btn_save_changes.clicked.connect(save_changes)
        btn_demo.clicked.connect(demo_music)

        # Set the checkboxes according to the current settings file values
        music1.setChecked(dict_setting["path1"] == "1")
        music2.setChecked(dict_setting["path3"] == "1")
        music3.setChecked(dict_setting["path2"] == "1")
        music4.setChecked(dict_setting["path4"] == "1")
        music5.setChecked(dict_setting["path5"] == "1")

        # Update music_quest to match the order of checkboxes and settings
        global music_quest
        music_quest.clear()
        for k in ["path1", "path2", "path3", "path4", "path5"]:
            if dict_setting[k] == "1" and os.path.exists(path_map[k]):
                music_quest.append(path_map[k])

    # --- LEVEL SELECTION SCREEN ---
    def level():
        # This function displays the difficulty selection screen (Easy, Normal, Hard).

        but_level.deleteLater()
        but_settings.deleteLater()
        window.repaint()
        label = QLabel(tr("select_level"), window)
        label.setFont(font)
        label.setStyleSheet("""
            border: 2px solid black; border-radius: 10px; font-size: 22px; font-weight: bold; padding: 100px;
        """)
        label.resize(500, 125)
        label.move(250, 0)
        label.show()

        but_easy = QPushButton(tr("easy"), window)
        but_easy.resize(500, 125)
        but_easy.setFont(font)
        but_easy.move(250, 140)

        but_normal = QPushButton(tr("normal"), window)
        but_normal.setFont(font)
        but_normal.resize(500, 125)
        but_normal.move(250, 270)

        but_hard = QPushButton(tr("hard"), window)
        but_hard.setFont(font)
        but_hard.resize(500, 125)
        but_hard.move(250, 400)

        but_ret = QPushButton(tr("back"), window)
        but_ret.setFont(font)
        but_ret.resize(400, 100)
        but_ret.move(300, 530)

        but_ret.clicked.connect(start)
        but_easy.clicked.connect(go_to_easy)
        but_normal.clicked.connect(go_to_normal)
        but_hard.clicked.connect(go_to_hard)

        but_ret.show()
        label.show()
        but_easy.show()
        but_normal.show()
        but_hard.show()

    # --- MAIN MENU BUTTONS ---
    # Button for selecting difficulty level
    but_level = QPushButton(tr("select_level"), window)
    but_level.setFont(font)
    but_level.resize(500, 150)
    but_level.move(250, 200)  # Center horizontally (1000-500)/2=250, vertically (800-2*150-50)/2 ≈ 200

    # Button for settings
    but_settings = QPushButton(tr("settings"), window)
    but_settings.resize(500, 150)
    but_settings.setFont(font)
    but_settings.move(250, 400)  # Below the first button, with some space

    # Connect buttons to their respective functions
    but_level.clicked.connect(level)
    but_settings.clicked.connect(settings)
    but_level.show()
    but_settings.show()
    # Set window icon if the file exists
    if os.path.exists(imaje):
        window.setWindowIcon(QIcon(imaje))
    window.setWindowTitle(tr("main_title"))
    window.resize(1000, 800)
    window.show()

# --- PROGRAM ENTRY POINT ---
# Start the main menu when the program launches.
start()
# Enter the Qt event loop to keep the application running.
sys.exit(app.exec_())

# --- VARIABLE EXPLANATIONS ---
# font: The default font used for all widgets.
# app: The QApplication instance required for all PyQt5 applications.
# window: The main QWidget window for the application.
# player: The VLC MediaPlayer instance for background music.
# music_quest: List of enabled music file paths, based on user settings.
# setting: Path to the settings file (settings.txt).
# path1, path2, path3, path4, path5: Paths to the available music files.
# imaje: Path to the window icon file.
# quest_setting: List of music enable/disable settings read from settings.txt.
#
# --- PROGRAM FLOW ---
# 1. The program starts by reading settings and preparing the music playlist.
# 2. The main menu is displayed (start()).
# 3. The user can select difficulty or open settings
# 4. In settings, the user can enable/disable music, demo tracks, or restart the app.
# 5. When a difficulty is selected, the corresponding module (easy, normal, hard) is loaded.
# 6. Music plays in the background, looping through enabled tracks.
# 7. The program runs until the user closes the window.