# Vocabulary Practice Game

This is a Python-based interactive command-line game designed to help users practice Japanese vocabulary. The game provides a fun and engaging way to test your knowledge of vocabulary words from different lessons, with built-in support for audio feedback and high-score tracking.

## Features:
- **Multilingual Support**: The game uses the Google Text-to-Speech (gTTS) API to speak out questions in both English and Japanese, making it easier for learners to hear and pronounce words.
- **Difficulty Levels**: Choose from three difficulty levels – easy, medium, or hard – each with different time limits for answering the questions.
- **Audio Feedback**: Questions are spoken aloud, and audio feedback is provided for correct and incorrect answers, using the gTTS library and mplayer for playback.
- **High Score Tracking**: The game saves and displays the top 5 high scores in a scoreboard, encouraging players to improve their performance.
- **Timed Questions**: Each question is time-bound depending on the selected difficulty, with time limits ranging from 5 to 15 seconds.
- **Lesson-based Vocabulary**: The vocabulary words are loaded from text files corresponding to different lessons (e.g., lesson1.txt, lesson2.txt), allowing users to focus on specific lessons they want to practice.
- **User-Friendly**: Provides a simple and clear interface with prompts and error handling to guide the player through the game.

## How It Works:
1. **Lesson Selection**: The user selects a lesson by entering the corresponding lesson number. The vocabulary words from the chosen lesson are loaded from a text file in the format `japanese_word,english_translation`.
2. **Vocabulary Quiz**: The user is quizzed on the English meaning of Japanese words. The system uses a timer based on the difficulty level, and the user must input the correct English translation before time runs out.
3. **Score and Feedback**: The game keeps track of the user's score and provides feedback through audio (correct, incorrect, or timed-out responses). The high score is saved and displayed at the end of each game.

## File Structure:
- `meaning.py`: The main game script.
- `lesson<number>.txt`: Vocabulary files containing comma-separated Japanese words and their English translations (e.g., 日本語,English).
- `scoreboard.txt`: A file that stores the high scores for the game.

## Prerequisites:
- Python 3.x
- gTTS (Google Text-to-Speech)
- mplayer (for audio playback)
- pygame (for handling game events)

## How to Play:
1. Download the Termux App on Android: [Termux APK v0.118.1](https://github.com/termux/termux-app/releases/download/v0.118.1/termux-app_v0.118.1+github-debug_arm64-v8a.apk)
2. Give storage permission to the installed Termux app.
3. Enter the app and type the following commands:
    ```bash
    pkg update
    pkg upgrade
    pkg install python3
    pkg install pip
    pkg install git
    git clone https://github.com/charchit-subedi/Japanese_Word_Game.git
    pip install -r requirements.txt
    python meaning.py
    ```
4. Select your difficulty level, choose a lesson, and start practicing!
