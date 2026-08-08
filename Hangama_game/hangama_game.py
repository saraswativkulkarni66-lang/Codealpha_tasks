import tkinter as tk
import random

# --------------------------------
# 5 PREDEFINED WORDS
# --------------------------------
words = ["python", "computer", "program", "hangman", "student"]

# --------------------------------
# GAME VARIABLES
# --------------------------------
current_word_index = 0
word = ""
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6
game_finished = False


# --------------------------------
# CREATE WINDOW
# --------------------------------
root = tk.Tk()
root.title("Hangman Game")
root.geometry("700x700")
root.configure(bg="#101820")
root.resizable(False, False)


# --------------------------------
# TITLE
# --------------------------------
title_label = tk.Label(
    root,
    text="HANGMAN GAME",
    font=("Arial", 30, "bold"),
    bg="#101820",
    fg="white"
)
title_label.pack(pady=20)


# --------------------------------
# CANVAS
# --------------------------------
canvas = tk.Canvas(
    root,
    width=500,
    height=300,
    bg="#182A3A",
    highlightthickness=0
)
canvas.pack()


# --------------------------------
# WORD DISPLAY
# --------------------------------
word_label = tk.Label(
    root,
    text="",
    font=("Arial", 30, "bold"),
    bg="#101820",
    fg="#00FFFF"
)
word_label.pack(pady=20)


# --------------------------------
# STATUS
# --------------------------------
status_label = tk.Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    bg="#101820",
    fg="white"
)
status_label.pack()


# --------------------------------
# ATTEMPTS
# --------------------------------
attempts_label = tk.Label(
    root,
    text="Wrong guesses: 0 / 6",
    font=("Arial", 15),
    bg="#101820",
    fg="orange"
)
attempts_label.pack(pady=10)


# --------------------------------
# INPUT
# --------------------------------
entry = tk.Entry(
    root,
    font=("Arial", 22),
    width=5,
    justify="center"
)
entry.pack(pady=5)


# --------------------------------
# HANGMAN ANIMATION
# --------------------------------
def draw_hangman():

    canvas.delete("all")

    if wrong_guesses >= 1:
        canvas.create_line(
            100, 270, 400, 270,
            width=5
        )

    if wrong_guesses >= 2:
        canvas.create_line(
            150, 270, 150, 50,
            width=5
        )

    if wrong_guesses >= 3:
        canvas.create_line(
            150, 50, 300, 50,
            width=5
        )

    if wrong_guesses >= 4:
        canvas.create_line(
            300, 50, 300, 90,
            width=5
        )

    if wrong_guesses >= 5:
        canvas.create_oval(
            270, 90, 330, 150,
            width=5
        )

    if wrong_guesses >= 6:
        canvas.create_line(
            300, 150, 300, 230,
            width=5
        )


# --------------------------------
# UPDATE WORD
# --------------------------------
def update_word():

    display = ""
    i = 0

    # WHILE LOOP
    # Used to display the word one letter at a time
    while i < len(word):

        if word[i] in guessed_letters:
            display += word[i].upper() + " "
        else:
            display += "_ "

        i += 1

    word_label.config(text=display)

    return display


# --------------------------------
# START NEXT WORD
# --------------------------------
def start_next_word():

    global word
    global guessed_letters
    global wrong_guesses
    global game_finished

    # All 5 words completed
    if current_word_index >= len(words):

        game_finished = True

        title_label.config(
            text="HANGMAN COMPLETED!"
        )

        status_label.config(
            text="🎉 You completed all 5 words! 🎉",
            fg="lightgreen"
        )

        word_label.config(
            text="GREAT JOB!"
        )

        entry.config(state="disabled")
        guess_button.config(state="disabled")

        return

    # Select the next predefined word
    word = words[current_word_index]

    guessed_letters = []
    wrong_guesses = 0
    game_finished = False

    # Clear Hangman
    canvas.delete("all")

    # Reset screen
    title_label.config(
        text="HANGMAN GAME"
    )

    attempts_label.config(
        text="Wrong guesses: 0 / 6"
    )

    status_label.config(
        text="Guess the letter!",
        fg="white"
    )

    entry.config(state="normal")
    guess_button.config(state="normal")

    update_word()

    entry.focus()


# --------------------------------
# CHECK GUESS
# --------------------------------
def check_guess():

    global wrong_guesses
    global game_finished
    global current_word_index

    if game_finished:
        return

    guess = entry.get().lower().strip()

    entry.delete(0, tk.END)

    # --------------------------------
    # VALIDATION
    # --------------------------------

    if len(guess) != 1 or not guess.isalpha():

        status_label.config(
            text="⚠️ Enter only ONE letter!",
            fg="orange"
        )

        return

    # Duplicate guess
    if guess in guessed_letters:

        status_label.config(
            text="⚠️ You already guessed this letter!",
            fg="orange"
        )

        return

    guessed_letters.append(guess)

    # --------------------------------
    # CORRECT GUESS
    # --------------------------------

    if guess in word:

        status_label.config(
            text="✅ Correct guess!",
            fg="lightgreen"
        )

    # --------------------------------
    # WRONG GUESS
    # --------------------------------

    else:

        wrong_guesses += 1

        status_label.config(
            text="❌ Wrong guess!",
            fg="red"
        )

        attempts_label.config(
            text="Wrong guesses: "
            + str(wrong_guesses)
            + " / 6"
        )

        # Draw next Hangman part
        draw_hangman()

    # Update hidden word
    display = update_word()

    # --------------------------------
    # WIN
    # --------------------------------

    if "_" not in display:

        game_finished = True

        status_label.config(
            text="🎉 YOU WON! NEXT WORD... 🎉",
            fg="lightgreen"
        )

        word_label.config(
            text="WORD COMPLETED!"
        )

        entry.config(state="disabled")
        guess_button.config(state="disabled")

        current_word_index += 1

        # Next word after 2 seconds
        root.after(2000, start_next_word)

    # --------------------------------
    # LOSE
    # --------------------------------

    elif wrong_guesses >= max_wrong_guesses:

        game_finished = True

        status_label.config(
            text="💀 GAME OVER! NEXT WORD...",
            fg="red"
        )

        word_label.config(
            text="The word was: " + word.upper()
        )

        entry.config(state="disabled")
        guess_button.config(state="disabled")

        current_word_index += 1

        # Next word after 2 seconds
        root.after(2000, start_next_word)


# --------------------------------
# GUESS BUTTON
# --------------------------------
guess_button = tk.Button(
    root,
    text="GUESS",
    font=("Arial", 16, "bold"),
    command=check_guess,
    bg="#00A8E8",
    fg="white",
    width=10
)
guess_button.pack(pady=15)


# --------------------------------
# ENTER KEY
# --------------------------------
entry.bind(
    "<Return>",
    lambda event: check_guess()
)


# --------------------------------
# START FIRST WORD
# --------------------------------
start_next_word()


# --------------------------------
# START PROGRAM
# --------------------------------
root.mainloop()