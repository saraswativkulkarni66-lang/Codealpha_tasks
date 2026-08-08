import tkinter as tk
from datetime import datetime
import random

# ============================================================
# SMART CHATBOT
# ============================================================

root = tk.Tk()
root.title("SMART CHATBOT")
root.geometry("1100x720")
root.minsize(950, 650)
root.configure(bg="#070D16")


# ============================================================
# COLORS
# ============================================================

BG = "#070D16"
SIDEBAR = "#0B1421"
PANEL = "#101B2A"
CARD = "#162435"
CARD2 = "#1B2B3D"

BLUE = "#0797FF"
LIGHT_BLUE = "#4DB8FF"
CYAN = "#00D9FF"

WHITE = "#FFFFFF"
TEXT = "#DDE9F5"
MUTED = "#8EA3B8"


# ============================================================
# CURRENT SERVICE
# ============================================================

current_service = "General Chat"


# ============================================================
# DATE AND TIME
# ============================================================

def get_datetime():

    now = datetime.now()

    date = now.strftime("%d %B %Y")
    day = now.strftime("%A")
    time = now.strftime("%I:%M:%S %p")

    return date, day, time


def update_clock():

    date, day, time = get_datetime()

    clock_label.config(
        text=f"📅 {date}     •     {day}     •     🕐 {time}"
    )

    root.after(1000, update_clock)


# ============================================================
# ROBOT DESIGN
# ============================================================

def draw_robot(canvas):

    canvas.delete("all")

    # Outer glow
    canvas.create_oval(
        25, 20, 255, 250,
        outline="#075B9E",
        width=3
    )

    canvas.create_oval(
        45, 40, 235, 230,
        outline="#0A3B63",
        width=2
    )

    # Antenna
    canvas.create_line(
        140, 55,
        140, 25,
        fill=CYAN,
        width=4
    )

    canvas.create_oval(
        132, 17,
        148, 33,
        fill=CYAN,
        outline=""
    )

    # Robot head
    canvas.create_rectangle(
        72, 65,
        208, 165,
        fill="#D9E4EE",
        outline="#8DA5B8",
        width=3
    )

    # Side parts of head
    canvas.create_oval(
        62, 65,
        88, 165,
        fill="#D9E4EE",
        outline="#8DA5B8",
        width=3
    )

    canvas.create_oval(
        192, 65,
        218, 165,
        fill="#D9E4EE",
        outline="#8DA5B8",
        width=3
    )

    # Face screen
    canvas.create_rectangle(
        78, 75,
        202, 155,
        fill="#07111C",
        outline="#4C718C",
        width=2
    )

    # Eyes
    canvas.create_oval(
        96, 96,
        120, 120,
        fill=CYAN,
        outline=""
    )

    canvas.create_oval(
        160, 96,
        184, 120,
        fill=CYAN,
        outline=""
    )

    # Mouth
    canvas.create_line(
        125, 132,
        155, 132,
        fill=LIGHT_BLUE,
        width=4
    )

    # Body
    canvas.create_rectangle(
        90, 170,
        190, 235,
        fill="#C9D7E2",
        outline="#8DA5B8",
        width=3
    )

    # Chest light
    canvas.create_oval(
        130, 190,
        150, 210,
        fill=CYAN,
        outline=""
    )

    # Left arm
    canvas.create_line(
        90, 185,
        48, 215,
        fill="#C9D7E2",
        width=16
    )

    # Right arm
    canvas.create_line(
        190, 185,
        230, 145,
        fill="#C9D7E2",
        width=16
    )

    # Hand
    canvas.create_oval(
        220, 130,
        245, 155,
        fill="#E4EDF3",
        outline="#8DA5B8"
    )


# ============================================================
# ADD CHAT MESSAGE
# ============================================================

def add_message(sender, message):

    chat.config(state=tk.NORMAL)

    date, day, time = get_datetime()

    if sender == "You":

        chat.insert(
            tk.END,
            f"\n👤 You   •   {time}\n",
            "user_header"
        )

        chat.insert(
            tk.END,
            f"{message}\n",
            "user_message"
        )

    else:

        chat.insert(
            tk.END,
            f"\n🤖 SmartBot   •   {time}\n",
            "bot_header"
        )

        chat.insert(
            tk.END,
            f"{message}\n",
            "bot_message"
        )

    chat.config(state=tk.DISABLED)

    chat.see(tk.END)


# ============================================================
# GENERAL CHAT
# ============================================================

def general_response(user):

    user = user.lower().strip()

    # Name
    if (
        "my name is" in user
        or "i am" in user
        or "i'm" in user
    ):

        return (
            "😊 Nice to meet you!\n"
            "It's great to know your name."
        )

    # What are you doing
    if (
        "what are you doing" in user
        or "what do you do" in user
    ):

        return (
            "🤖 I'm SmartBot!\n\n"
            "I'm chatting with you, answering questions, "
            "helping you learn, and providing useful information."
        )

    # Studies
    if (
        "studies" in user
        or "study" in user
        or "college" in user
    ):

        return (
            "📚 That's great!\n\n"
            "Keep learning and practicing regularly. "
            "Would you like to learn something interesting about AI? 🤖"
        )

    # Yes to AI
    if user in ["yes", "yeah", "sure", "okay", "ok"]:

        return (
            "🤖 Great!\n\n"
            "AI stands for Artificial Intelligence. "
            "It helps computers perform tasks that normally "
            "require human intelligence.\n\n"
            "You can learn more about AI in the "
            "🧠 Smart Q&A section!"
        )

    return None


# ============================================================
# SMART Q&A
# ============================================================

def smart_qa(user):

    user = user.lower().strip()

    # What is AI
    if (
        "what is ai" in user
        or "tell me about ai" in user
        or user == "ai"
        or "artificial intelligence" in user
    ):

        return (
            "🤖 ABOUT ARTIFICIAL INTELLIGENCE\n\n"
            "Artificial Intelligence (AI) is a technology "
            "that enables computers to perform tasks that "
            "normally require human intelligence.\n\n"
            "Examples of AI include:\n"
            "• 🤖 Chatbots\n"
            "• 🎤 Voice assistants\n"
            "• 🖼️ Image recognition\n"
            "• 🌐 Language translation\n"
            "• 🎬 Recommendation systems\n"
            "• 📚 AI learning tools"
        )

    # AI assistant
    if (
        "ai assistant" in user
        or "assistant" in user
    ):

        return (
            "🤖 WHAT IS AN AI ASSISTANT?\n\n"
            "An AI assistant is software that can understand "
            "user questions and provide useful responses.\n\n"
            "It can help with:\n"
            "📚 Learning\n"
            "💻 Coding\n"
            "📝 Writing\n"
            "💡 Ideas\n"
            "🔎 Information\n"
            "⏰ Planning"
        )

    # How to use AI
    if (
        "how to use ai" in user
        or "use ai" in user
        or "how can i use ai" in user
    ):

        return (
            "💡 HOW TO USE AI\n\n"
            "1️⃣ Ask clear questions.\n"
            "2️⃣ Give enough information about your task.\n"
            "3️⃣ Ask AI to explain difficult topics.\n"
            "4️⃣ Use AI for learning and brainstorming.\n"
            "5️⃣ Check important information before relying on it.\n"
            "6️⃣ Use AI as a learning assistant."
        )

    # Benefits
    if "benefit" in user:

        return (
            "✨ BENEFITS OF AI\n\n"
            "• Saves time\n"
            "• Helps with learning\n"
            "• Supports problem solving\n"
            "• Automates repetitive tasks\n"
            "• Helps generate ideas\n"
            "• Provides personalized assistance"
        )

    return None


# ============================================================
# INFORMATION FINDER
# ============================================================

def information_response(user):

    user = user.lower().strip()

    # Nature
    if (
        "nature" in user
        or "forest" in user
        or "environment" in user
    ):

        return (
            "🌿 NATURE\n\n"
            "Nature includes forests, rivers, mountains, "
            "plants, animals, oceans, and many other natural systems.\n\n"
            "Protecting nature helps maintain biodiversity "
            "and a healthy environment."
        )

    # Education
    if (
        "education" in user
        or "learning" in user
        or "school" in user
        or "college" in user
    ):

        return (
            "🎓 EDUCATION\n\n"
            "Education helps us develop knowledge, skills, "
            "problem-solving abilities, and confidence.\n\n"
            "Learning can happen through school, college, "
            "books, courses, and practical projects."
        )

    # Books
    if (
        "book" in user
        or "books" in user
        or "read" in user
        or "reading" in user
    ):

        return (
            "📚 BOOKS & READING\n\n"
            "Reading can improve vocabulary, knowledge, "
            "creativity, and understanding.\n\n"
            "You can explore fiction, science, history, "
            "technology, biographies, and educational books."
        )

    # Temples
    if (
        "temple" in user
        or "temples" in user
    ):

        return (
            "🛕 TEMPLES\n\n"
            "Temples can be important places of worship "
            "and cultural heritage.\n\n"
            "They can also provide interesting information "
            "about architecture, history, art, and traditions."
        )

    # Places
    if (
        "place" in user
        or "places" in user
        or "travel" in user
    ):

        return (
            "🌍 PLACES & TRAVEL\n\n"
            "Places can be explored based on nature, "
            "history, culture, architecture, food, and adventure."
        )

    # General knowledge
    if (
        "general knowledge" in user
        or "knowledge" in user
    ):

        return (
            "💡 GENERAL KNOWLEDGE\n\n"
            "You can ask about science, technology, "
            "history, geography, nature, education, books, "
            "culture, and many other topics."
        )

    return None


# ============================================================
# STUDY HELPER
# ============================================================

def study_response(user):

    user = user.lower().strip()

    # Study tips
    if (
        "study tip" in user
        or "tips" in user
        or "how to study" in user
    ):

        return (
            "📚 SMART STUDY TIPS\n\n"
            "1️⃣ Set a small goal for every study session.\n"
            "2️⃣ Create a realistic timetable.\n"
            "3️⃣ Study difficult topics with full attention.\n"
            "4️⃣ Take short breaks.\n"
            "5️⃣ Revise regularly.\n"
            "6️⃣ Practice questions.\n"
            "7️⃣ Keep your study area organized."
        )

    # Concentration
    if (
        "concentration" in user
        or "focus" in user
    ):

        return (
            "🎯 CONCENTRATION TIPS\n\n"
            "• Study one topic at a time.\n"
            "• Keep unnecessary notifications away.\n"
            "• Set a clear goal before studying.\n"
            "• Use short focused study sessions.\n"
            "• Take regular breaks."
        )

    # Timetable
    if (
        "timetable" in user
        or "schedule" in user
    ):

        return (
            "🗓️ SIMPLE STUDY TIMETABLE\n\n"
            "🌅 Morning: Review difficult concepts\n"
            "📚 Afternoon: Classes / assignments\n"
            "💻 Evening: Practice or coding\n"
            "📝 Night: Quick revision\n\n"
            "Adjust the schedule according to your routine."
        )

    # Revision
    if "revision" in user:

        return (
            "📝 REVISION TIPS\n\n"
            "• Review regularly.\n"
            "• Make short notes.\n"
            "• Practice important questions.\n"
            "• Explain concepts in your own words.\n"
            "• Test yourself without looking at answers."
        )

    # Exams
    if "exam" in user:

        return (
            "🎓 EXAM PREPARATION TIPS\n\n"
            "• Start preparing early.\n"
            "• Divide the syllabus into smaller topics.\n"
            "• Practice previous questions.\n"
            "• Revise important concepts.\n"
            "• Take regular breaks.\n"
            "• Stay calm and focus on one topic at a time."
        )

    return None


# ============================================================
# MAIN BOT RESPONSE
# ============================================================

def bot_response(user):

    global current_service

    user_lower = user.lower().strip()

    # --------------------------------------------------------
    # BYE
    # --------------------------------------------------------

    if user_lower in [
        "bye",
        "goodbye",
        "see you",
        "bye bye"
    ]:

        return "👋 Bye! Nice to meet you. Have a good day!"

    # --------------------------------------------------------
    # TIME / DATE
    # --------------------------------------------------------

    if (
        "time" in user_lower
        or "date" in user_lower
        or "what day" in user_lower
        or "which day" in user_lower
    ):

        date, day, time = get_datetime()

        return (
            "🕐 CURRENT DATE & TIME\n\n"
            f"📅 Date : {date}\n"
            f"📆 Day  : {day}\n"
            f"⏰ Time : {time}"
        )

    # --------------------------------------------------------
    # SMART Q&A
    # --------------------------------------------------------

    if current_service == "Smart Q&A":

        answer = smart_qa(user_lower)

        if answer:
            return answer

    # --------------------------------------------------------
    # INFORMATION FINDER
    # --------------------------------------------------------

    if current_service == "Information Finder":

        answer = information_response(user_lower)

        if answer:
            return answer

    # --------------------------------------------------------
    # STUDY HELPER
    # --------------------------------------------------------

    if current_service == "Study Helper":

        answer = study_response(user_lower)

        if answer:
            return answer

    # --------------------------------------------------------
    # GENERAL CHAT
    # --------------------------------------------------------

    if current_service == "General Chat":

        answer = general_response(user_lower)

        if answer:
            return answer

    # --------------------------------------------------------
    # COMMON GREETING
    # --------------------------------------------------------

    if user_lower in [
        "hi",
        "hello",
        "hey",
        "hii",
        "hlo",
        "hai"
    ]:

        return random.choice([
            "Hello! 😊",
            "Hi there! 👋",
            "Hey! 🤖 Nice to chat with you!"
        ])

    # --------------------------------------------------------
    # HOW ARE YOU
    # --------------------------------------------------------

    if "how are you" in user_lower:

        return (
            "😊 I'm doing great!\n"
            "Thanks for asking!"
        )

    # --------------------------------------------------------
    # THANK YOU
    # --------------------------------------------------------

    if (
        "thank you" in user_lower
        or "thanks" in user_lower
    ):

        return random.choice([
            "😊 You're welcome!",
            "✨ Happy to help!",
            "🤖 Anytime!"
        ])

    # --------------------------------------------------------
    # PYTHON
    # --------------------------------------------------------

    if "python" in user_lower:

        return (
            "🐍 PYTHON\n\n"
            "Python is a popular programming language "
            "used for automation, web development, "
            "data analysis, AI, and many other applications."
        )

    # --------------------------------------------------------
    # AI
    # --------------------------------------------------------

    if (
        user_lower == "ai"
        or "artificial intelligence" in user_lower
    ):

        return (
            "🤖 AI stands for Artificial Intelligence.\n\n"
            "It enables computers to perform tasks that "
            "normally require human intelligence.\n\n"
            "Try asking me: 'Tell me about AI'."
        )

    # --------------------------------------------------------
    # JOKE
    # --------------------------------------------------------

    if (
        "joke" in user_lower
        or "funny" in user_lower
    ):

        return random.choice([
            "😂 Why do programmers prefer dark mode? "
            "Because light attracts bugs!",
            "😄 Why did the computer go to the doctor? "
            "Because it had a virus!",
            "🤣 Programmers love coffee because they need Java!"
        ])

    # --------------------------------------------------------
    # DEFAULT
    # --------------------------------------------------------

    if current_service == "Smart Q&A":

        return (
            "🧠 Ask me an AI question.\n\n"
            "Try:\n"
            "• Tell me about AI\n"
            "• What is an AI assistant?\n"
            "• How can I use AI?\n"
            "• What are the benefits of AI?"
        )

    if current_service == "Information Finder":

        return (
            "🔎 What would you like to explore?\n\n"
            "Try asking about:\n"
            "🌿 Nature\n"
            "🎓 Education\n"
            "📚 Books\n"
            "🛕 Temples\n"
            "🌍 Places"
        )

    if current_service == "Study Helper":

        return (
            "📚 I can help you with:\n\n"
            "💡 Study tips\n"
            "🎯 Concentration\n"
            "🗓️ Study timetable\n"
            "📝 Revision\n"
            "🎓 Exam preparation"
        )

    return (
        "🤔 That's interesting!\n\n"
        "Tell me more about it, or choose a service "
        "from the left side."
    )


# ============================================================
# TYPING INDICATOR
# ============================================================

def show_typing():

    chat.config(state=tk.NORMAL)

    chat.insert(
        tk.END,
        "\n🤖 SmartBot is typing...\n",
        "typing"
    )

    chat.config(state=tk.DISABLED)

    chat.see(tk.END)


def remove_typing():

    chat.config(state=tk.NORMAL)

    content = chat.get(
        "1.0",
        tk.END
    )

    position = content.rfind(
        "\n🤖 SmartBot is typing..."
    )

    if position != -1:

        start = f"1.0 + {position} chars"

        chat.delete(
            start,
            tk.END
        )

    chat.config(state=tk.DISABLED)


# ============================================================
# SEND MESSAGE
# ============================================================

def reply(event=None):

    user = entry.get().strip()

    if user == "":
        return

    add_message(
        "You",
        user
    )

    entry.delete(
        0,
        tk.END
    )

    response = bot_response(user)

    show_typing()

    root.after(
        700,
        lambda: finish_reply(response)
    )


# ============================================================
# FINISH RESPONSE
# ============================================================

def finish_reply(response):

    remove_typing()

    add_message(
        "Bot",
        response
    )

    # ========================================================
    # CLOSE CHATBOT AFTER BYE
    # ========================================================

    if response == "👋 Bye! Nice to meet you. Have a good day!":

        root.after(
            2500,
            root.destroy
        )


# ============================================================
# CLEAR CHAT
# ============================================================

def clear_chat():

    chat.config(state=tk.NORMAL)

    chat.delete(
        "1.0",
        tk.END
    )

    chat.config(state=tk.DISABLED)

    add_message(
        "Bot",
        "Hi! 👋 I'm SmartBot."
    )

    add_message(
        "Bot",
        "How can I help you today?"
    )


# ============================================================
# START SERVICE
# ============================================================

def start_service(service):

    global current_service

    current_service = service

    clear_chat()

    # --------------------------------------------------------
    # GENERAL CHAT
    # --------------------------------------------------------

    if service == "General Chat":

        add_message(
            "Bot",
            "💬 Welcome to General Chat!"
        )

        add_message(
            "Bot",
            "Hi! 👋 What's your name?"
        )

        add_message(
            "Bot",
            "What are you doing today?"
        )

        add_message(
            "Bot",
            "How are your studies going? 📚"
        )

        add_message(
            "Bot",
            "Would you like to learn about AI? 🤖"
        )

    # --------------------------------------------------------
    # SMART Q&A
    # --------------------------------------------------------

    elif service == "Smart Q&A":

        add_message(
            "Bot",
            "🧠 Welcome to Smart Q&A!"
        )

        add_message(
            "Bot",
            "Did you know about AI assistants? 🤖"
        )

        add_message(
            "Bot",
            "Ask me questions like:\n\n"
            "• Tell me about AI\n"
            "• What is an AI assistant?\n"
            "• How can I use AI?\n"
            "• What are the benefits of AI?"
        )

    # --------------------------------------------------------
    # INFORMATION FINDER
    # --------------------------------------------------------

    elif service == "Information Finder":

        add_message(
            "Bot",
            "🔎 Welcome to Information Finder!"
        )

        add_message(
            "Bot",
            "What would you like to explore?"
        )

        add_message(
            "Bot",
            "🌿 Nature\n"
            "🎓 Education\n"
            "📚 Books\n"
            "🛕 Temples\n"
            "🌍 Places\n"
            "💡 General Knowledge"
        )

    # --------------------------------------------------------
    # TIME AND DATE
    # --------------------------------------------------------

    elif service == "Time & Date":

        date, day, time = get_datetime()

        add_message(
            "Bot",
            "🕐 CURRENT INFORMATION\n\n"
            f"📅 Date : {date}\n"
            f"📆 Day  : {day}\n"
            f"⏰ Time : {time}"
        )

    # --------------------------------------------------------
    # STUDY HELPER
    # --------------------------------------------------------

    elif service == "Study Helper":

        add_message(
            "Bot",
            "📚 Welcome to Study Helper!"
        )

        add_message(
            "Bot",
            "Here are some smart study tips:"
        )

        add_message(
            "Bot",
            "1️⃣ Make a daily timetable.\n"
            "2️⃣ Set small study goals.\n"
            "3️⃣ Take short breaks.\n"
            "4️⃣ Revise regularly.\n"
            "5️⃣ Practice questions.\n"
            "6️⃣ Keep distractions away."
        )

        add_message(
            "Bot",
            "You can ask me about concentration, "
            "revision, exams, or study timetables."
        )

    # --------------------------------------------------------
    # CODE ASSISTANT
    # --------------------------------------------------------

    elif service == "Code Assistant":

        add_message(
            "Bot",
            "💻 Welcome to Code Assistant!"
        )

        add_message(
            "Bot",
            "Ask me about Python, programming concepts, "
            "loops, functions, lists, dictionaries, "
            "errors, or coding projects."
        )

    # --------------------------------------------------------
    # TRANSLATION
    # --------------------------------------------------------

    elif service == "Translation":

        add_message(
            "Bot",
            "🌐 Welcome to Translation!"
        )

        add_message(
            "Bot",
            "Send me text that you want help understanding "
            "or translating."
        )

    # --------------------------------------------------------
    # REMINDER
    # --------------------------------------------------------

    elif service == "Reminder":

        add_message(
            "Bot",
            "⏰ Welcome to Reminder!"
        )

        add_message(
            "Bot",
            "I can help you organize:\n\n"
            "📚 Study time\n"
            "💻 Project work\n"
            "📝 Assignment work\n"
            "🎯 Daily goals"
        )

    # --------------------------------------------------------
    # FUN ZONE
    # --------------------------------------------------------

    elif service == "Fun Zone":

        add_message(
            "Bot",
            "🎮 Welcome to Fun Zone!"
        )

        add_message(
            "Bot",
            "Ask me for a joke, riddle, quiz, "
            "or interesting fact! 😄"
        )

    # --------------------------------------------------------
    # FEEDBACK
    # --------------------------------------------------------

    elif service == "Feedback":

        add_message(
            "Bot",
            "⭐ FEEDBACK\n\n"
            "Tell me what you like about Smart Chatbot "
            "or what you would like to improve."
        )

    entry.focus()


# ============================================================
# SERVICE BUTTON
# ============================================================

def create_service(
    parent,
    icon,
    name,
    description
):

    button = tk.Frame(
        parent,
        bg=CARD,
        height=55,
        cursor="hand2"
    )

    button.pack(
        fill="x",
        padx=12,
        pady=3
    )

    button.pack_propagate(False)

    icon_label = tk.Label(
        button,
        text=icon,
        font=("Arial", 16),
        bg=CARD,
        fg=LIGHT_BLUE,
        width=3
    )

    icon_label.pack(
        side=tk.LEFT,
        padx=(7, 3)
    )

    text_frame = tk.Frame(
        button,
        bg=CARD
    )

    text_frame.pack(
        side=tk.LEFT,
        fill="both",
        expand=True,
        pady=5
    )

    name_label = tk.Label(
        text_frame,
        text=name,
        font=("Arial", 9, "bold"),
        bg=CARD,
        fg=WHITE,
        anchor="w"
    )

    name_label.pack(
        fill="x"
    )

    desc_label = tk.Label(
        text_frame,
        text=description,
        font=("Arial", 7),
        bg=CARD,
        fg=MUTED,
        anchor="w"
    )

    desc_label.pack(
        fill="x"
    )

    def clicked(event=None):

        start_service(name)

    for widget in [
        button,
        icon_label,
        text_frame,
        name_label,
        desc_label
    ]:

        widget.bind(
            "<Button-1>",
            clicked
        )


# ============================================================
# MAIN LAYOUT
# ============================================================

main = tk.Frame(
    root,
    bg=BG
)

main.pack(
    fill="both",
    expand=True
)


# ============================================================
# LEFT SIDEBAR
# ============================================================

sidebar = tk.Frame(
    main,
    bg=SIDEBAR,
    width=300
)

sidebar.pack(
    side=tk.LEFT,
    fill="y"
)

sidebar.pack_propagate(False)


# ============================================================
# ROBOT
# ============================================================

robot_canvas = tk.Canvas(
    sidebar,
    width=280,
    height=250,
    bg=SIDEBAR,
    highlightthickness=0
)

robot_canvas.pack(
    pady=(10, 0)
)

draw_robot(robot_canvas)


# ============================================================
# CHATBOT NAME
# ============================================================

chatbot_name = tk.Label(
    sidebar,
    text="SMART CHATBOT",
    font=("Arial", 20, "bold"),
    bg=SIDEBAR,
    fg=WHITE
)

chatbot_name.pack()


tagline = tk.Label(
    sidebar,
    text="Your Intelligent AI Assistant",
    font=("Arial", 10),
    bg=SIDEBAR,
    fg=CYAN
)

tagline.pack(
    pady=(2, 10)
)


# ============================================================
# HOME BUTTON
# ============================================================

home_button = tk.Button(
    sidebar,
    text="⌂   Home",
    font=("Arial", 11, "bold"),
    bg=BLUE,
    fg=WHITE,
    activebackground="#0076D7",
    activeforeground=WHITE,
    relief=tk.FLAT,
    cursor="hand2",
    anchor="w",
    padx=20,
    pady=8
)

home_button.pack(
    fill="x",
    padx=15,
    pady=(0, 8)
)


def home():

    global current_service

    current_service = "General Chat"

    clear_chat()

    add_message(
        "Bot",
        "Hi! 👋 What's your name?"
    )

    add_message(
        "Bot",
        "What are you doing today?"
    )

    add_message(
        "Bot",
        "How are your studies going? 📚"
    )

    add_message(
        "Bot",
        "Would you like to learn about AI? 🤖"
    )


home_button.config(
    command=home
)


# ============================================================
# SERVICES TITLE
# ============================================================

services_title = tk.Label(
    sidebar,
    text="━━  OUR SERVICES  ━━",
    font=("Arial", 10, "bold"),
    bg=SIDEBAR,
    fg=CYAN
)

services_title.pack(
    pady=(0, 5)
)


# ============================================================
# SERVICES
# ============================================================

create_service(
    sidebar,
    "💬",
    "General Chat",
    "Friendly everyday conversation"
)

create_service(
    sidebar,
    "🧠",
    "Smart Q&A",
    "AI questions and answers"
)

create_service(
    sidebar,
    "🔎",
    "Information Finder",
    "Nature, education, books & more"
)

create_service(
    sidebar,
    "🕐",
    "Time & Date",
    "Current time, date & day"
)

create_service(
    sidebar,
    "📚",
    "Study Helper",
    "Study tips & exam preparation"
)

create_service(
    sidebar,
    "💻",
    "Code Assistant",
    "Programming & coding help"
)

create_service(
    sidebar,
    "🌐",
    "Translation",
    "Language assistance"
)

create_service(
    sidebar,
    "⏰",
    "Reminder",
    "Tasks & study planning"
)

create_service(
    sidebar,
    "🎮",
    "Fun Zone",
    "Jokes, riddles & quizzes"
)

create_service(
    sidebar,
    "⭐",
    "Feedback",
    "Share your feedback"
)


# ============================================================
# RIGHT CONTENT
# ============================================================

content = tk.Frame(
    main,
    bg=BG
)

content.pack(
    side=tk.LEFT,
    fill="both",
    expand=True,
    padx=(10, 15),
    pady=15
)


# ============================================================
# HEADER
# ============================================================

top_header = tk.Frame(
    content,
    bg=PANEL,
    height=95
)

top_header.pack(
    fill="x"
)

top_header.pack_propagate(False)


welcome_label = tk.Label(
    top_header,
    text="🤖  Welcome to Smart Chatbot",
    font=("Arial", 22, "bold"),
    bg=PANEL,
    fg=CYAN,
    anchor="w"
)

welcome_label.pack(
    padx=22,
    pady=(12, 2),
    anchor="w"
)


welcome_subtitle = tk.Label(
    top_header,
    text="Your friendly AI-style assistant • Ask • Learn • Explore",
    font=("Arial", 10),
    bg=PANEL,
    fg=MUTED,
    anchor="w"
)

welcome_subtitle.pack(
    padx=25,
    anchor="w"
)


clock_label = tk.Label(
    top_header,
    text="",
    font=("Arial", 9, "bold"),
    bg=PANEL,
    fg=LIGHT_BLUE
)

clock_label.pack(
    padx=25,
    pady=7,
    anchor="w"
)


# ============================================================
# CHAT PANEL
# ============================================================

chat_panel = tk.Frame(
    content,
    bg=PANEL
)

chat_panel.pack(
    fill="both",
    expand=True,
    pady=(10, 10)
)


chat = tk.Text(
    chat_panel,
    font=("Calibri", 12),
    bg=PANEL,
    fg=TEXT,
    wrap=tk.WORD,
    relief=tk.FLAT,
    padx=20,
    pady=15,
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
    chat_panel,
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
# CHAT TEXT STYLES
# ============================================================

chat.tag_config(
    "user_header",
    foreground=LIGHT_BLUE,
    font=("Calibri", 10, "bold")
)

chat.tag_config(
    "user_message",
    foreground=WHITE,
    font=("Calibri", 12)
)

chat.tag_config(
    "bot_header",
    foreground=CYAN,
    font=("Calibri", 10, "bold")
)

chat.tag_config(
    "bot_message",
    foreground=TEXT,
    font=("Calibri", 12)
)

chat.tag_config(
    "typing",
    foreground=MUTED,
    font=("Calibri", 10, "italic")
)


# ============================================================
# INPUT AREA
# ============================================================

input_frame = tk.Frame(
    content,
    bg=PANEL,
    height=65
)

input_frame.pack(
    fill="x"
)

input_frame.pack_propagate(False)


entry = tk.Entry(
    input_frame,
    font=("Arial", 12),
    bg=CARD,
    fg=WHITE,
    insertbackground=WHITE,
    relief=tk.FLAT,
    bd=0
)

entry.pack(
    side=tk.LEFT,
    fill="both",
    expand=True,
    padx=(15, 8),
    pady=10,
    ipady=8
)


# ============================================================
# SEND BUTTON
# ============================================================

send_button = tk.Button(
    input_frame,
    text="➤  Send",
    font=("Arial", 11, "bold"),
    bg=BLUE,
    fg=WHITE,
    activebackground="#0076D7",
    activeforeground=WHITE,
    relief=tk.FLAT,
    cursor="hand2",
    padx=20,
    command=reply
)

send_button.pack(
    side=tk.LEFT,
    padx=(0, 8),
    pady=10
)


# ============================================================
# CLEAR BUTTON
# ============================================================

clear_button = tk.Button(
    input_frame,
    text="Clear",
    font=("Arial", 10, "bold"),
    bg=CARD2,
    fg=TEXT,
    activebackground=CARD,
    activeforeground=WHITE,
    relief=tk.FLAT,
    cursor="hand2",
    padx=12,
    command=clear_chat
)

clear_button.pack(
    side=tk.LEFT,
    padx=(0, 15),
    pady=10
)


# ============================================================
# ENTER KEY
# ============================================================

entry.bind(
    "<Return>",
    reply
)


# ============================================================
# INITIAL CHAT
# ============================================================

add_message(
    "Bot",
    "👋 Welcome to Smart Chatbot!"
)

add_message(
    "Bot",
    "Hi! What's your name?"
)

add_message(
    "Bot",
    "What are you doing today?"

)

add_message(
    "Bot",
    "How are your studies going? 📚"
)

add_message(
    "Bot",
    "Would you like to learn about AI? 🤖"
)


# ============================================================
# START CLOCK
# ============================================================

update_clock()

entry.focus()


# ============================================================
# RUN CHATBOT
# ============================================================

root.mainloop()