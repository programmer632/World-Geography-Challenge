# 🌍 World Geography Challenge Application

Welcome to the **World Geography Challenge** — an interactive and educational desktop app built with **Python** and **PyQt5**. Designed for users of all ages, this game makes learning world geography fun and accessible!

---

## 🎯 Purpose & Goals

- 📚 **Educational**: Make geography accessible and engaging for all.
- 🤝 **Open Source**: Encourage contribution, learning, and community development.
- 🔧 **Extensible**: Easily add your own questions or difficulty levels.
- 🌐 **Accessible**: All code, comments, and UI text are in English for global reach.
- 🌍 **Multilingual**: Supports English, Greek, and French for both UI and quiz content.
- 🎵 **Customizable Music**: Choose from built-in tracks or play your own music file.

---

## 🚀 Features

- 🧩 **Three Difficulty Levels**: Easy, Normal, and Hard – 10 randomized questions per level.
- ✅ **Instant Feedback**: Know right away whether your answer was correct.
- 📈 **Score Tracking**: Real-time updates to your score.
- 🏆 **Leaderboard**: Compete with yourself or friends for high scores!
- 🎵 **Background Music**: Choose from built-in tracks or add your own.
- ⚙️ **Settings Menu**: Customize your experience, including language and music selection.
- 🧱 **Modular Code**: Clean file structure for easy maintenance and contributions.
- 🌐 **Multilingual Support**: All quiz questions and UI elements are available in English, Greek, and French.
- 🗂️ **Settings & Data in JSON**: User preferences and leaderboard data are stored in JSON for easy editing and portability.

---

## 🗂️ Project Structure

```
📁 World Geography Challenge/
├── World_Geography_Challenge.py       # Main launcher and UI logic
├── easy.py, easy2.py ... easy10.py    # Easy questions (multilingual)
├── normal.py, ... normal10.py         # Normal questions (multilingual)
├── hard.py, ... hard10.py             # Hard questions (multilingual)
├── marks.py                           # Results screen & leaderboard
├── extra_files/
│   ├── settings.json                  # Settings (music, language)
│   ├── language.txt                   # Current language selection
│   ├── *.mp3                          # Built-in music tracks
│   └── *.ico                          # App icon
├── data.json                          # Leaderboard data
├── Project Overview.pdf               # Full project documentation
```

---

## 📥 Download & Quick Start

### 🟢 **Download the Ready-to-Use App**

You can always download the latest version of the application without needing to install Python or any libraries!

👉 **Go to [Releases](https://github.com/programmer632/World-Geography-Challenge/releases) and download the latest ZIP from the assets.**

1. Download the `.zip` file from the latest release.
2. Unzip it to a folder of your choice.
3. Run `World Geography Challenge.exe` — and start playing, no installation required!

> All necessary files for the application to work are included in the ZIP.

---

### 🛠️ **Run from Source (Developers/Contributors)**

#### Requirements

- [Python 3.x](https://www.python.org/)
- [PyQt5](https://pypi.org/project/PyQt5/) → `pip install PyQt5`
- [python-vlc](https://pypi.org/project/python-vlc/) for background music → `pip install python-vlc`

#### Run the Application

1. Clone or download this repository.
2. Run the launcher:

```bash
python World_Geography_Challenge.py
```

3. Choose your difficulty and enjoy the quiz!

---

## 🧪 Example Flow

- Choose your difficulty (Easy / Normal / Hard)
- Answer the 10 multiple-choice questions (in your selected language)
- See your score, correct/wrong answers
- Check your position on the leaderboard
- Play again or switch levels 🎮

---

## 💡 Contribution Guide

Contributions are welcome — and beginners are encouraged!

### 🛠️ What You Can Do

- Add new quiz questions or difficulty levels (in all supported languages)
- Improve UI/UX (themes, animations, layout)
- Translate to other languages (add to the translation dictionaries)
- Implement new game modes (e.g., timed mode, multiplayer)
- Add accessibility features (keyboard support, colorblind mode)
- Write unit tests for core logic

### ✅ How to Contribute

1. Fork the repository
2. Make your changes
3. Open a Pull Request with a clear description

> 📄 **Tip:** Read `Project Overview.pdf` before diving into the code for a full breakdown of how it all works.

---

## 🧰 Files That Store Data

- `extra_files/settings.json`: Stores user preferences like music and language settings.
- `extra_files/language.txt`: Stores the currently selected language.
- `data.json`: Tracks and stores leaderboard information.

---

## 📎 Additional Resources

- 📘 **Documentation**: See `Project Overview.pdf` for a full technical guide.
- 🛠️ Need help? Open an [issue](https://github.com/programmer632/World-Geography-Challenge/issues) or start a discussion.

---

## 📝 License

This project is **open source** and released under a permissive license. Feel free to use, modify, and share it!

---

## 🙌 Final Notes

- No coding experience? No problem — jump in!
- Want to add a fun twist? Suggest or implement it!
- Help us make geography fun and accessible for everyone.

> Let’s build something amazing — one question at a time! 🌍✨
