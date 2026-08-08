import tkinter as tk
from datetime import datetime
import random
import re

# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()
root.title("🤖 Smart Chatbot")
root.geometry("650x650")
root.resizable(False, False)

# ============================================================
# COLORS
# ============================================================

BG = "#EAF2F8"
HEADER = "#1565C0"
USER_COLOR = "#1976D2"
BOT_COLOR = "#43A047"
WHITE = "#FFFFFF"
DARK = "#263238"

root.configure(bg=BG)

# ============================================================
# USER DATA
# ============================================================

user_name = None


# ============================================================
# TIME
# ============================================================

def get_time():
    return datetime.now().strftime("%I:%M %p")


# ============================================================
# ADD MESSAGE
# ============================================================

def add_message(sender, message):

    chat.config(state=tk.NORMAL)

    time = get_time()

    if sender == "You":

        chat.insert(
            tk.END,
            f"\n  You  •  {time}\n",
            "user_name"
        )

        chat.insert(
            tk.END,
            f"  {message}\n",
            "user_msg"
        )

    else:

        chat.insert(
            tk.END,
            f"\n  🤖 Bot  •  {time}\n",
            "bot_name"
        )

        chat.insert(
            tk.END,
            f"  {message}\n",
            "bot_msg"
        )

    chat.config(state=tk.DISABLED)
    chat.see(tk.END)


# ============================================================
# DETECT NAME
# ============================================================

def detect_name(text):

    text = text.strip()

    # My name is Saraswati
    match = re.match(
        r"^my name is\s+([A-Za-z]+)$",
        text,
        re.IGNORECASE
    )

    if match:
        return match.group(1).capitalize()

    # My name's Saraswati
    match = re.match(
        r"^my name's\s+([A-Za-z]+)$",
        text,
        re.IGNORECASE
    )

    if match:
        return match.group(1).capitalize()

    # I am Saraswati
    match = re.match(
        r"^i am\s+([A-Za-z]+)$",
        text,
        re.IGNORECASE
    )

    if match:
        return match.group(1).capitalize()

    # I'm Saraswati
    match = re.match(
        r"^i'm\s+([A-Za-z]+)$",
        text,
        re.IGNORECASE
    )

    if match:
        return match.group(1).capitalize()

    # I am called Saraswati
    match = re.match(
        r"^i am called\s+([A-Za-z]+)$",
        text,
        re.IGNORECASE
    )

    if match:
        return match.group(1).capitalize()

    # I'm called Saraswati
    match = re.match(
        r"^i'm called\s+([A-Za-z]+)$",
        text,
        re.IGNORECASE
    )

    if match:
        return match.group(1).capitalize()

    # ONLY NAME
    if re.match(r"^[A-Za-z]+$", text):

        common_words = [
            "hello",
            "hi",
            "hey",
            "bye",
            "help",
            "thanks",
            "thank",
            "python",
            "college",
            "project",
            "internship",
            "ai"
        ]

        if text.lower() not in common_words:
            return text.capitalize()

    return None


# ============================================================
# FULL SCREEN PERSONAL WELCOME ANIMATION
# ============================================================

def show_personal_animation(name):

    animation = tk.Toplevel(root)

    # Full screen
    animation.attributes(
        "-fullscreen",
        True
    )

    # Background
    animation.configure(
        bg="#0D47A1"
    )

    # Prevent using main chatbot during animation
    animation.grab_set()

    # ========================================================
    # MAIN LABEL
    # ========================================================

    main_label = tk.Label(
        animation,
        text="",
        font=("Arial", 48, "bold"),
        bg="#0D47A1",
        fg="white",
        wraplength=1200,
        justify="center"
    )

    main_label.place(
        relx=0.5,
        rely=0.42,
        anchor="center"
    )

    # ========================================================
    # SECOND LABEL
    # ========================================================

    second_label = tk.Label(
        animation,
        text="",
        font=("Arial", 25, "bold"),
        bg="#0D47A1",
        fg="#BBDEFB",
        wraplength=1100,
        justify="center"
    )

    second_label.place(
        relx=0.5,
        rely=0.58,
        anchor="center"
    )

    # ========================================================
    # THIRD LABEL
    # ========================================================

    third_label = tk.Label(
        animation,
        text="",
        font=("Arial", 22),
        bg="#0D47A1",
        fg="#E3F2FD",
        wraplength=1000,
        justify="center"
    )

    third_label.place(
        relx=0.5,
        rely=0.70,
        anchor="center"
    )

    # ========================================================
    # ANIMATION SEQUENCE
    # ========================================================

    sequence = [

        # Welcome
        {
            "main": f"✨ WELCOME, {name.upper()}! ✨",
            "second": "💙 Nice to meet you!",
            "third": "",
            "time": 3000
        },

        # Study
        {
            "main": "📚 HOW ARE YOUR STUDIES GOING?",
            "second": "Keep learning and improving every day!",
            "third": "🎓 Your education is an important step toward your goal.",
            "time": 3500
        },

        # Food
        {
            "main": "🍕 WHAT DO YOU LIKE TO EAT?",
            "second": "Enjoy your favorite food!",
            "third": "😋 A balanced day also includes taking care of yourself.",
            "time": 3500
        },

        # Goal
        {
            "main": "🎯 WHAT IS YOUR MAIN GOAL?",
            "second": "Think about what you want to achieve.",
            "third": "🚀 Your goal gives you a direction to work toward.",
            "time": 3500
        },

        # Motivation
        {
            "main": "🌟 DON'T SIT IDLE! 🌟",
            "second": "💡 Learn something new",
            "third": "",
            "time": 2200
        },

        {
            "main": "💻 DO SOMETHING USEFUL",
            "second": "Build a small project",
            "third": "Practice your coding skills!",
            "time": 2200
        },

        {
            "main": "📚 KEEP LEARNING",
            "second": "Study something useful today",
            "third": "Even a little progress counts.",
            "time": 2200
        },

        {
            "main": "🚀 IMPROVE YOUR SKILLS",
            "second": "Practice • Build • Learn",
            "third": "Your skills grow when you use them.",
            "time": 2200
        },

        {
            "main": "🎯 STAY FOCUSED",
            "second": "Remember your goal",
            "third": "Don't give up when things become difficult.",
            "time": 2200
        },

        {
            "main": "✨ KEEP MOVING FORWARD! ✨",
            "second": f"Believe in yourself, {name}!",
            "third": "💪 Small steps every day can lead to big progress.",
            "time": 3500
        }
    ]

    # ========================================================
    # LETTER ANIMATION
    # ========================================================

    def type_text(
        text,
        label,
        callback,
        index=0
    ):

        if index <= len(text):

            label.config(
                text=text[:index]
            )

            animation.after(
                45,
                lambda: type_text(
                    text,
                    label,
                    callback,
                    index + 1
                )
            )

        else:

            animation.after(
                400,
                callback
            )

    # ========================================================
    # SHOW ONE SEQUENCE
    # ========================================================

    def show_sequence(index):

        if index >= len(sequence):

            finish_animation()

            return

        item = sequence[index]

        # Clear old text
        main_label.config(
            text=""
        )

        second_label.config(
            text=""
        )

        third_label.config(
            text=""
        )

        # ----------------------------------------------------
        # Type main message
        # ----------------------------------------------------

        def show_second():

            second_label.config(
                text=item["second"]
            )

            third_label.config(
                text=item["third"]
            )

            animation.after(
                item["time"],
                lambda: show_sequence(
                    index + 1
                )
            )

        type_text(
            item["main"],
            main_label,
            show_second
        )

    # ========================================================
    # FINISH
    # ========================================================

    def finish_animation():

        animation.grab_release()

        animation.destroy()

        # Return to chatbot only after everything is finished
        add_message(
            "Bot",
            f"💬 Welcome again, {name}! What would you like to talk about?"
        )

        entry.focus()

    # Start sequence
    show_sequence(0)


# ============================================================
# TYPING INDICATOR
# ============================================================

def show_typing():

    chat.config(
        state=tk.NORMAL
    )

    chat.insert(
        tk.END,
        "\n  🤖 Bot is typing...\n",
        "typing"
    )

    chat.config(
        state=tk.DISABLED
    )

    chat.see(
        tk.END
    )


# ============================================================
# REMOVE TYPING
# ============================================================

def remove_typing():

    chat.config(
        state=tk.NORMAL
    )

    content = chat.get(
        "1.0",
        tk.END
    )

    if "🤖 Bot is typing..." in content:

        position = content.rfind(
            "\n  🤖 Bot is typing..."
        )

        try:

            start_index = f"1.0 + {position} chars"

            chat.delete(
                start_index,
                tk.END
            )

        except:
            pass

    chat.config(
        state=tk.DISABLED
    )


# ============================================================
# BOT RESPONSES
# ============================================================

def bot_response(user):

    user = user.lower().strip()

    responses = {

        "hello": [
            "👋 Hi! Welcome to Smart Chatbot!",
            "😊 Hello! How can I help you?",
            "🤖 Hey there! Nice to meet you!"
        ],

        "hi": [
            "👋 Hi!",
            "😊 Hello!",
            "🤖 Hey! How are you?"
        ],

        "hey": [
            "👋 Hey! What's up?",
            "😊 Hello there!"
        ],

        "how are you": [
            "😊 I'm doing great! Thanks for asking.",
            "🤖 I'm fine and ready to chat!",
            "✨ I'm doing awesome!"
        ],

        "what is your name": [
            "🤖 My name is SmartBot!",
            "😊 You can call me SmartBot."
        ],

        "who are you": [
            "🤖 I'm a Python Tkinter chatbot.",
            "✨ I'm your friendly SmartBot!"
        ],

        "help": [
            "💡 You can ask me about Python, AI, college, projects, or internships."
        ],

        "thank you": [
            "😊 You're welcome!",
            "✨ Anytime!",
            "🤖 Happy to help!"
        ],

        "thanks": [
            "😊 You're welcome!",
            "✨ No problem!"
        ],

        "good morning": [
            "🌞 Good morning! Have a wonderful day!"
        ],

        "good night": [
            "🌙 Good night! Sleep well!"
        ],

        "bye": [
            "👋 Goodbye! Have a wonderful day!",
            "😊 Bye! See you again!",
            "✨ Take care!"
        ]
    }

    if user in responses:

        return random.choice(
            responses[user]
        )

    # Python
    if "python" in user:

        return (
            "🐍 Python is a popular programming language "
            "known for its simplicity and readability."
        )

    # AI
    if (
        "ai" in user
        or
        "artificial intelligence" in user
    ):

        return (
            "🤖 Artificial Intelligence allows computers "
            "to perform tasks that normally require human intelligence."
        )

    # College
    if "college" in user:

        return (
            "🎓 College is a great place to learn, "
            "build projects, and develop your skills!"
        )

    # Project
    if "project" in user:

        return (
            "💻 Building projects is one of the best ways "
            "to improve your programming skills."
        )

    # Internship
    if "internship" in user:

        return (
            "🚀 Internships are a great way to gain "
            "practical experience."
        )

    return (
        "🤔 I'm still learning!\n"
        "💡 Try asking me about Python, AI, "
        "projects, college, or internships."
    )


# ============================================================
# REPLY
# ============================================================

def reply(event=None):

    global user_name

    user = entry.get().strip()

    if user == "":
        return

    # Display user message
    add_message(
        "You",
        user
    )

    # Clear input
    entry.delete(
        0,
        tk.END
    )

    # ========================================================
    # NAME DETECTION
    # ========================================================

    detected_name = detect_name(
        user
    )

    if detected_name:

        user_name = detected_name

        # Open complete full-screen animation
        show_personal_animation(
            user_name
        )

        return

    # ========================================================
    # NORMAL CHAT
    # ========================================================

    response = bot_response(
        user
    )

    show_typing()

    root.after(
        800,
        lambda: finish_reply(
            response,
            user.lower()
        )
    )


# ============================================================
# FINISH REPLY
# ============================================================

def finish_reply(
    response,
    user
):

    remove_typing()

    add_message(
        "Bot",
        response
    )

    if user == "bye":

        root.after(
            1800,
            root.destroy
        )


# ============================================================
# CLEAR CHAT
# ============================================================

def clear_chat():

    global user_name

    user_name = None

    chat.config(
        state=tk.NORMAL
    )

    chat.delete(
        "1.0",
        tk.END
    )

    chat.insert(
        tk.END,
        "\n  🤖 Bot  •  " +
        get_time() +
        "\n  Hello! 👋 I'm SmartBot.\n\n"
        "  💬 Tell me your name to get started!\n\n"
        "  Example:\n"
        "  My name is Saraswati\n",
        "bot_msg"
    )

    chat.config(
        state=tk.DISABLED
    )


# ============================================================
# DARK MODE
# ============================================================

def toggle_theme():

    if root.cget("bg") == "#EAF2F8":

        root.configure(
            bg="#121212"
        )

        frame.configure(
            bg="#121212"
        )

        bottom_frame.configure(
            bg="#121212"
        )

        chat.configure(
            bg="#1E1E1E",
            fg="white"
        )

        entry.configure(
            bg="#2C2C2C",
            fg="white",
            insertbackground="white"
        )

        theme_button.configure(
            text="☀ Light"
        )

    else:

        root.configure(
            bg="#EAF2F8"
        )

        frame.configure(
            bg="#EAF2F8"
        )

        bottom_frame.configure(
            bg="#EAF2F8"
        )

        chat.configure(
            bg="white",
            fg="black"
        )

        entry.configure(
            bg="white",
            fg="black",
            insertbackground="black"
        )

        theme_button.configure(
            text="🌙 Dark"
        )


# ============================================================
# HEADER
# ============================================================

header = tk.Frame(
    root,
    bg=HEADER,
    height=75
)

header.pack(
    fill="x"
)

title = tk.Label(
    header,
    text="🤖 Smart Chatbot",
    font=("Arial", 22, "bold"),
    bg=HEADER,
    fg="white"
)

title.pack(
    pady=(10, 0)
)

subtitle = tk.Label(
    header,
    text="Python • Tkinter • AI Style Chat",
    font=("Arial", 10),
    bg=HEADER,
    fg="#D6EAF8"
)

subtitle.pack()


# ============================================================
# CHAT FRAME
# ============================================================

frame = tk.Frame(
    root,
    bg=BG
)

frame.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=15
)


# ============================================================
# CHAT BOX
# ============================================================

chat = tk.Text(
    frame,
    width=65,
    height=22,
    font=("Calibri", 12),
    bg=WHITE,
    fg=DARK,
    wrap=tk.WORD,
    relief=tk.FLAT,
    padx=15,
    pady=10,
    state=tk.DISABLED
)

chat.pack(
    side=tk.LEFT,
    fill="both",
    expand=True
)


# ============================================================
# SCROLLBAR
# ============================================================

scrollbar = tk.Scrollbar(
    frame,
    command=chat.yview
)

scrollbar.pack(
    side=tk.RIGHT,
    fill=tk.Y
)

chat.configure(
    yscrollcommand=scrollbar.set
)


# ============================================================
# TEXT STYLES
# ============================================================

chat.tag_config(
    "user_name",
    foreground=USER_COLOR,
    font=("Calibri", 11, "bold")
)

chat.tag_config(
    "user_msg",
    foreground=DARK,
    font=("Calibri", 12)
)

chat.tag_config(
    "bot_name",
    foreground=BOT_COLOR,
    font=("Calibri", 11, "bold")
)

chat.tag_config(
    "bot_msg",
    foreground=DARK,
    font=("Calibri", 12)
)

chat.tag_config(
    "typing",
    foreground="#888888",
    font=("Calibri", 11, "italic")
)


# ============================================================
# FIRST MESSAGE
# ============================================================

chat.config(
    state=tk.NORMAL
)

chat.insert(
    tk.END,
    "\n  🤖 Bot  •  " +
    get_time() +
    "\n  Hello! 👋 I'm SmartBot.\n\n"
    "  💬 Tell me your name to get started!\n\n"
    "  Example:\n"
    "  My name is Saraswati\n",
    "bot_msg"
)

chat.config(
    state=tk.DISABLED
)


# ============================================================
# BOTTOM FRAME
# ============================================================

bottom_frame = tk.Frame(
    root,
    bg=BG
)

bottom_frame.pack(
    fill="x",
    padx=15,
    pady=(0, 15)
)


# ============================================================
# INPUT
# ============================================================

entry = tk.Entry(
    bottom_frame,
    width=38,
    font=("Arial", 13),
    relief=tk.FLAT,
    bd=5
)

entry.pack(
    side=tk.LEFT,
    padx=(0, 8),
    ipady=8
)


# ============================================================
# SEND BUTTON
# ============================================================

send = tk.Button(
    bottom_frame,
    text="Send 🚀",
    command=reply,
    bg="#43A047",
    fg="white",
    activebackground="#2E7D32",
    activeforeground="white",
    font=("Arial", 11, "bold"),
    relief=tk.FLAT,
    cursor="hand2",
    padx=15,
    pady=8
)

send.pack(
    side=tk.LEFT
)


# ============================================================
# CLEAR BUTTON
# ============================================================

clear = tk.Button(
    bottom_frame,
    text="Clear 🧹",
    command=clear_chat,
    bg="#E53935",
    fg="white",
    activebackground="#C62828",
    activeforeground="white",
    font=("Arial", 10, "bold"),
    relief=tk.FLAT,
    cursor="hand2",
    padx=10,
    pady=8
)

clear.pack(
    side=tk.LEFT,
    padx=5
)


# ============================================================
# DARK MODE
# ============================================================

theme_button = tk.Button(
    bottom_frame,
    text="🌙 Dark",
    command=toggle_theme,
    bg="#546E7A",
    fg="white",
    activebackground="#37474F",
    font=("Arial", 10, "bold"),
    relief=tk.FLAT,
    cursor="hand2",
    padx=10,
    pady=8
)

theme_button.pack(
    side=tk.LEFT
)


# ============================================================
# ENTER KEY
# ============================================================

entry.bind(
    "<Return>",
    reply
)

entry.focus()


# ============================================================
# START
# ============================================================

root.mainloop()