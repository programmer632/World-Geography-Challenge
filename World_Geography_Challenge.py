from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QCheckBox, QApplication, QFileDialog, QVBoxLayout,QComboBox
from PyQt5.QtGui import QFont, QIcon
import os
import sys
import threading
import random
import time
import subprocess
from PyQt5.QtCore import Qt

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

setting = resource_path("settings.txt")
path1 = resource_path("musik.wav")
path2 = resource_path("Vibramusic.wav")
path3 = resource_path("Memories-of-Spring(chosic.com).wav")
path4 = resource_path("Cinspirational.wav")
path5 = resource_path("Sarakinoi.wav")  # Translated from Greek to English
imaje = resource_path("186-europis-70x100-1.ico")

music_quest = []

if not os.path.exists(setting):
    print(f"{setting} not found. Creating with default values.")
    with open(setting, 'w', encoding='utf-8') as settings_file:
        settings_file.write("1\n0\n0\n0\n0\n")
try:
    with open(setting, 'r', encoding='utf-8') as settings_file:
        lines = settings_file.readlines()
        print(lines)
        if len(lines) < 5:
            raise ValueError("settings.txt has less than 5 lines.")
        Standard_Music = lines[0].strip()
        Memories_of_Spring = lines[1].strip()
        Vibramusic = lines[2].strip()
        Cinspirational = lines[3].strip()
        Sarakinoi = lines[4].strip()  # Translated from Greek to English
        # FIX: Use the same order as everywhere else: [Standard, Vibramusic, Memories, Cinspirational, Sarakinoi]
        quest_setting = [
            Standard_Music,    # path1
            Vibramusic,        # path2
            Memories_of_Spring,# path3
            Cinspirational,    # path4
            Sarakinoi          # path5
        ]
except Exception as e:
    print(f"Error reading {setting}: {e}. Using default values.")
    Standard_Music, Memories_of_Spring, Vibramusic, Cinspirational, Sarakinoi = "1", "0", "0", "0", "0"
    quest_setting = [Standard_Music, Vibramusic, Memories_of_Spring, Cinspirational, Sarakinoi]

# Build music_quest using the same order as everywhere else
for path, setting_val in zip([path1, path2, path3, path4, path5], quest_setting):
    if setting_val == "1" and os.path.exists(path):
        music_quest.append(path)
    elif setting_val == "1":
        print(f"Warning: {path} not found.")

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
if "1" in quest_setting and music_quest:
    thread = threading.Thread(target=sound, daemon=True)  # Create a daemon thread for music playback
    thread.start()

def go_to_easy():
    for widget in window.children():
        widget.deleteLater()
    window.repaint()
    easy.easy(window)

def go_to_normal():
    for widget in window.children():
        widget.deleteLater()
    window.repaint()
    normal.normal(window)

def go_to_hard():
    for widget in window.children():
        widget.deleteLater()
    window.repaint()
    hard.hard(window)

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

        def demo_music():
            demo_player = vlc.MediaPlayer()

            def back_to_settings():
                demo_player.stop()
                time.sleep(0.1)
                player.play()
                demo_window.deleteLater()
                settings()

            def demo_Standard_Music():
                if os.path.exists(path1):
                    y = vlc.Media(path1)
                    demo_player.set_media(y)
                    if demo_player.get_state() == vlc.State.Playing:
                        demo_player.stop()
                    demo_player.play()

            def demo_Vibramusic():
                if os.path.exists(path2):
                    y = vlc.Media(path2)
                    demo_player.set_media(y)
                    if demo_player.get_state() == vlc.State.Playing:
                        demo_player.stop()
                    demo_player.play()

            def demo_Memories_of_Spring():
                if os.path.exists(path3):
                    y = vlc.Media(path3)
                    demo_player.set_media(y)
                    if demo_player.get_state() == vlc.State.Playing:
                        demo_player.stop()
                    demo_player.play()

            def demo_Cinspirational():
                if os.path.exists(path4):
                    y = vlc.Media(path4)
                    demo_player.set_media(y)
                    if demo_player.get_state() == vlc.State.Playing:
                        demo_player.stop()
                    demo_player.play()

            def demo_Sarakinoi():
                if os.path.exists(path5):
                    y = vlc.Media(path5)
                    demo_player.set_media(y)
                    if demo_player.get_state() == vlc.State.Playing:
                        demo_player.stop()
                    demo_player.play()

            demo_window = QWidget()
            demo_window.setWindowTitle("Geography Quiz")
            demo_window.resize(500, 400)
            layout = QVBoxLayout()

            with open(setting, 'r', encoding='utf-8') as settings_file:
                lines = settings_file.readlines()
                Standard_Music = lines[0].strip()
                Memories_of_Spring = lines[1].strip()
                Vibramusic = lines[2].strip()
                Cinspirational = lines[3].strip()
                Sarakinoi = lines[4].strip()  # Translated from Greek to English

            if Standard_Music == "1" and os.path.exists(path1):
                but_Standard_Music = QPushButton("Standard Music", demo_window)
                but_Standard_Music.setFont(font)
                layout.addWidget(but_Standard_Music)
                but_Standard_Music.clicked.connect(demo_Standard_Music)
            if Memories_of_Spring == "1" and os.path.exists(path3):
                but_Memories_of_Spring = QPushButton("Memories of Spring", demo_window)
                but_Memories_of_Spring.setFont(font)
                layout.addWidget(but_Memories_of_Spring)
                but_Memories_of_Spring.clicked.connect(demo_Memories_of_Spring)
            if Vibramusic == "1" and os.path.exists(path2):
                but_Vibramusic = QPushButton("Vibramusic", demo_window)
                but_Vibramusic.setFont(font)
                layout.addWidget(but_Vibramusic)
                but_Vibramusic.clicked.connect(demo_Vibramusic)
            if Cinspirational == "1" and os.path.exists(path4):
                but_Cinspirational = QPushButton("Cinspirational", demo_window)
                but_Cinspirational.setFont(font)
                layout.addWidget(but_Cinspirational)
                but_Cinspirational.clicked.connect(demo_Cinspirational)
            if Sarakinoi == "1" and os.path.exists(path5):
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
            global music_quest, quest_setting
            # Save the current music settings to the settings file in the correct order
            with open(setting, 'w', encoding='utf-8') as settings_file:
                # Order: Standard, Vibramusic, Memories, Cinspirational, Sarakinoi
                settings_file.write("1\n" if music1.isChecked() else "0\n")  # Standard
                settings_file.write("1\n" if music3.isChecked() else "0\n")  # Vibramusic
                settings_file.write("1\n" if music2.isChecked() else "0\n")  # Memories
                settings_file.write("1\n" if music4.isChecked() else "0\n")  # Cinspirational
                settings_file.write("1\n" if music5.isChecked() else "0\n")  # Sarakinoi
            # Update quest_setting and music_quest in the same order
            music_quest.clear()
            quest_setting = [
                "1" if music1.isChecked() else "0",  # Standard
                "1" if music3.isChecked() else "0",  # Vibramusic
                "1" if music2.isChecked() else "0",  # Memories
                "1" if music4.isChecked() else "0",  # Cinspirational
                "1" if music5.isChecked() else "0"   # Sarakinoi
            ]
            for path, setting_val in zip([path1, path2, path3, path4, path5], quest_setting):
                if setting_val == "1" and os.path.exists(path):
                    music_quest.append(path)
            start()

        def reopen():
            # Save the current music settings to the settings file and update the music playlist immediately (no restart required)
            global music_quest, quest_setting
            with open(setting, 'w', encoding='utf-8') as settings_file:
                # Order: Standard, Vibramusic, Memories, Cinspirational, Sarakinoi
                settings_file.write("1\n" if music1.isChecked() else "0\n")  # Standard
                settings_file.write("1\n" if music3.isChecked() else "0\n")  # Vibramusic
                settings_file.write("1\n" if music2.isChecked() else "0\n")  # Memories
                settings_file.write("1\n" if music4.isChecked() else "0\n")  # Cinspirational
                settings_file.write("1\n" if music5.isChecked() else "0\n")  # Sarakinoi
            music_quest.clear()
            quest_setting = [
                "1" if music1.isChecked() else "0",  # Standard
                "1" if music3.isChecked() else "0",  # Vibramusic
                "1" if music2.isChecked() else "0",  # Memories
                "1" if music4.isChecked() else "0",  # Cinspirational
                "1" if music5.isChecked() else "0"   # Sarakinoi
            ]
            for path, setting_val in zip([path1, path2, path3, path4, path5], quest_setting):
                if setting_val == "1" and os.path.exists(path):
                    music_quest.append(path)
            # If music is playing, stop and restart with new playlist
            player.stop()
            if music_quest:
                x = random.choice(music_quest)
                media = vlc.Media(x)
                player.set_media(media)
                player.play()
                player.audio_set_volume(100)
            # No restart or exit needed

        def go_to_demo_music():
            player.pause()
            global music_quest, quest_setting
            with open(setting, 'w', encoding='utf-8') as settings_file:
                # Order: Standard, Vibramusic, Memories, Cinspirational, Sarakinoi
                settings_file.write("1\n" if music1.isChecked() else "0\n")  # Standard
                settings_file.write("1\n" if music3.isChecked() else "0\n")  # Vibramusic
                settings_file.write("1\n" if music2.isChecked() else "0\n")  # Memories
                settings_file.write("1\n" if music4.isChecked() else "0\n")  # Cinspirational
                settings_file.write("1\n" if music5.isChecked() else "0\n")  # Sarakinoi
            music_quest.clear()
            quest_setting = [
                "1" if music1.isChecked() else "0",  # Standard
                "1" if music3.isChecked() else "0",  # Vibramusic
                "1" if music2.isChecked() else "0",  # Memories
                "1" if music4.isChecked() else "0",  # Cinspirational
                "1" if music5.isChecked() else "0"   # Sarakinoi
            ]
            for path, setting_val in zip([path1, path2, path3, path4, path5], quest_setting):
                if setting_val == "1" and os.path.exists(path):
                    music_quest.append(path)
            demo_music()

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
        text = '''
              Select the music you want to play
              every time you open the game.
'''
        label_music = QLabel(text, window)
        label_music.setFont(font)
        label_music.resize(600, 150)
        label_music.setStyleSheet("""
            border: 2px solid black; border-radius: 10px; font-size: 20px;
        """)
        label_music.move(0, 0)

        music1 = QCheckBox("Standard Music", window)
        music1.resize(400, 70)
        music1.move(150, 160)
        music1.setFont(font)

        music2 = QCheckBox("Memories of Spring", window)
        music2.setFont(font)
        music2.resize(400, 70)
        music2.move(150, 200)

        music3 = QCheckBox("Vibramusic", window)
        music3.setFont(font)
        music3.resize(400, 70)
        music3.move(150, 240)

        music4 = QCheckBox("Cinspirational", window)
        music4.setFont(font)
        music4.resize(400, 70)
        music4.move(150, 280)

        music5 = QCheckBox("Sarakinoi", window)  # Translated from Greek to English
        music5.setFont(font)
        music5.resize(400, 70)
        music5.move(150, 320)

        btn_back = QPushButton("Back", window)
        btn_back.setFont(font)
        btn_back.resize(400, 100)
        btn_back.move(300, 390)

        btn_demo = QPushButton("Demo", window)
        btn_demo.setFont(font)
        btn_demo.resize(400, 100)
        btn_demo.move(568, 180)

        btn_open_custom = QPushButton("Play from your own file.", window)
        btn_open_custom.setFont(font)
        btn_open_custom.resize(400, 100)
        btn_open_custom.move(568, 285)

        note = QLabel('''Note: Changes take effect immediately\nafter restarting the game.''', window)
        note.setFont(font)
        note.resize(600, 150)
        note.setStyleSheet("""
            border: 2px solid black; border-radius: 10px; font-size: 20px;
        """)
        note.setAlignment(Qt.AlignCenter)
        note.move(200, 500)

        btn_restart = QPushButton("Save changes.", window)
        btn_restart.setFont(font)
        btn_restart.resize(400, 100)
        btn_restart.move(300, 670)

        # Εμφάνιση όλων των widgets
        btn_restart.show()
        btn_demo.show()
        btn_open_custom.show()
        music3.show()
        music5.show()
        music4.show()
        music2.show()
        music1.show()
        label_music.show()
        btn_back.show()
        note.show()

        # Συνδέσεις κουμπιών
        btn_open_custom.clicked.connect(open_the_file)
        btn_back.clicked.connect(go_to_back)
        btn_restart.clicked.connect(reopen)
        btn_demo.clicked.connect(go_to_demo_music)

        # Set the checkboxes according to the current settings file values
        with open(setting, 'r', encoding='utf-8') as settings_file:
            lines = settings_file.readlines()
            Standard_Music = lines[0].strip()
            Memories_of_Spring = lines[1].strip()
            Vibramusic = lines[2].strip()
            Cinspirational = lines[3].strip()
            Sarakinoi = lines[4].strip()
        music1.setChecked(Standard_Music == "1")
        music2.setChecked(Memories_of_Spring == "1")
        music3.setChecked(Vibramusic == "1")
        music4.setChecked(Cinspirational == "1")
        music5.setChecked(Sarakinoi == "1")

        # Update music_quest to match the order of checkboxes and settings (fix: correct mapping)
        global music_quest, quest_setting
        music_quest.clear()
        # The correct mapping is: [Standard, Vibramusic, Memories, Cinspirational, Sarakinoi]
        # So we must use the same order everywhere
        quest_setting = [
            Standard_Music,    # path1
            Vibramusic,        # path2
            Memories_of_Spring,# path3
            Cinspirational,    # path4
            Sarakinoi          # path5
        ]
        for path, setting_val in zip([path1, path2, path3, path4, path5], quest_setting):
            if setting_val == "1" and os.path.exists(path):
                music_quest.append(path)

    # --- LEVEL SELECTION SCREEN ---
    def leve():
        # This function displays the difficulty selection screen (Easy, Normal, Hard).

        but_level.deleteLater()
        but_settings.deleteLater()
        window.repaint()
        label = QLabel("Select difficulty level", window)
        label.setFont(font)
        label.setStyleSheet("""
            border: 2px solid black; border-radius: 10px; font-size: 22px; font-weight: bold; padding: 100px;
        """)
        label.resize(500, 125)
        label.move(250, 0)
        label.show()

        but_easy = QPushButton("Easy", window)
        but_easy.resize(500, 125)
        but_easy.setFont(font)
        but_easy.move(250, 140)

        but_normal = QPushButton("Normal", window)
        but_normal.setFont(font)
        but_normal.resize(500, 125)
        but_normal.move(250, 270)

        but_hard = QPushButton("Hard", window)
        but_hard.setFont(font)
        but_hard.resize(500, 125)
        but_hard.move(250, 400)

        but_ret = QPushButton("Back", window)
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
    but_level = QPushButton("Select difficulty level", window)
    but_level.setFont(font)
    but_level.resize(500, 150)
    but_level.move(250, 200)  # Center horizontally (1000-500)/2=250, vertically (800-2*150-50)/2 ≈ 200

    # Button for settings
    but_settings = QPushButton("Settings", window)
    but_settings.resize(500, 150)
    but_settings.setFont(font)
    but_settings.move(250, 400)  # Below the first button, with some space

    # Connect buttons to their respective functions
    but_level.clicked.connect(leve)
    but_settings.clicked.connect(settings)
    but_level.show()
    but_settings.show()
    # Ορισμός εικονιδίου παραθύρου αν υπάρχει
    if os.path.exists(imaje):
        window.setWindowIcon(QIcon(imaje))
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