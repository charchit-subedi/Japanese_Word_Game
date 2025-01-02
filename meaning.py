from gtts import gTTS
import os
import random
import subprocess
import time
from threading import Timer

def speak(text, language='en'):
    try:
        tts = gTTS(text=text, lang=language)
        tts.save("output.mp3")
        subprocess.run(["mplayer", "-quiet", "output.mp3"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("Error: 'mplayer' command not found. Make sure you have it installed.")
    except subprocess.CalledProcessError:
        print("Error: Audio playback failed.")

def save_high_score(score):
    try:
        with open("scoreboard.txt", "a", encoding="utf-8") as file:
            file.write(f"{score}\n")
    except IOError:
        print("Could not save the high score.")

def display_scoreboard():
    try:
        print("\n--- High Scores ---")
        with open("scoreboard.txt", "r", encoding="utf-8") as file:
            scores = file.readlines()
        scores = [int(score.strip()) for score in scores]
        scores.sort(reverse=True)
        for idx, score in enumerate(scores[:5], start=1):
            print(f"{idx}. {score} points")
        print("-------------------\n")
    except FileNotFoundError:
        print("No scores recorded yet. Be the first to set a high score!")

def play_game():
    try:
        # Choose difficulty
        while True:
            try:
                level = input("Select difficulty: [e]asy, [m]edium, [h]ard: ").strip().lower()
                if level in ['e', 'm', 'h']:
                    break
                print("Invalid input. Please enter 'e', 'm', or 'h'.")
            except KeyboardInterrupt:
                print("\nGame interrupted by user. Exiting...")
                return

        time_limits = {'e': 15, 'm': 10, 'h': 5}
        time_limit = time_limits[level]
        speak(f"You selected {level.upper()} mode. You have {time_limit} seconds per question.", language='en')

        # Select lesson
        while True:
            try:
                lesson_number = int(input("Which lesson do you want to practice? (Enter the number): "))
                break
            except ValueError:
                print("Please enter a valid number for the lesson.")
            except KeyboardInterrupt:
                print("\nGame interrupted by user. Exiting...")
                return

        filename = f"lesson{lesson_number}.txt"

        # Load vocabulary
        try:
            with open(filename, "r", encoding="utf-8") as file:
                vocabulary = file.readlines()
        except FileNotFoundError:
            print(f"Lesson {lesson_number} not found. Please check your files.")
            return

        random.shuffle(vocabulary)
        total_questions = len(vocabulary)
        solved = 0
        skipped = 0

        # Question loop
        for index, word_line in enumerate(vocabulary, start=1):
            parts = word_line.strip().split(",", 1)
            if len(parts) == 2:
                japanese_word, english_word = parts
                timed_out = False

                def timeout():
                    nonlocal timed_out
                    timed_out = True
                    print("\nTime's up!")
                    speak("Time's up!", language='en')

                timer = Timer(time_limit, timeout)

                speak(f"Question {index}/{total_questions}", language='en')
                speak("What is the English translation of", language='en')
                time.sleep(1.5)
                speak(japanese_word, language='ja')

                try:
                    timer.start()  
                    user_answer = input(f"Q{index}/{total_questions}: What is the English translation of '{japanese_word}'? ")
                    timer.cancel()  
                except KeyboardInterrupt:
                    print("\nGame interrupted.")
                    return

                if timed_out:
                    print(f"The correct answer was: {english_word}")
                    speak(f"The correct answer was {english_word}", language='en')
                elif user_answer.strip().lower() == english_word.strip().lower():
                    speak("Correct!", language='en')
                    solved += 1
                else:
                    speak("Wrong, try again", language='en')

            else:
                print(f"Skipping line: '{word_line.strip()}' - Invalid format.")
                skipped += 1

        # End of game summary
        speak(f"Game Over! You solved {solved} questions out of {total_questions}.", language='en')
        print(f"\nGame Over! You solved {solved}/{total_questions} questions.")
        if skipped > 0:
            print(f"You skipped {skipped} questions due to errors in the file.")
        if solved == total_questions:
            speak("Amazing! You solved all questions. You're a champion!", language='en')
        elif solved > total_questions // 2:
            speak("Great job! Keep practicing!", language='en')
        else:
            speak("Don't give up! Practice makes perfect.", language='en')

        # Save and display high score
        save_high_score(solved)
        display_scoreboard()

        print("\n--- This script is made by Charchit Subedi ---\n")
        speak("This script is made by Charchit Subedi.", language='en')

    except KeyboardInterrupt:
        print("\nGame interrupted by user. Exiting...")

print("\n--- Welcome to the Vocabulary Practice Game ---")
print("--- This script is made by Charchit Subedi ---")
print("------------------------------------------------")

display_scoreboard()

play_game()
