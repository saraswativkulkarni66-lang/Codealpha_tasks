import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# ============================================================
# STOCK PRICES
# ============================================================

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420,
    "AMZN": 190,
    "META": 500,
    "NFLX": 650
}

portfolio = {}


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()
root.title("Stock Portfolio Tracker")
root.geometry("850x750")
root.resizable(False, False)
root.configure(bg="#ffd6e7")


# ============================================================
# ANIMATED PINK BACKGROUND
# ============================================================

canvas = tk.Canvas(
    root,
    width=850,
    height=750,
    bg="#ffd6e7",
    highlightthickness=0
)

canvas.place(x=0, y=0)

circles = []

for i in range(20):

    x = 20 + (i * 53) % 820
    y = 50 + (i * 97) % 700
    size = 15 + (i % 4) * 8

    circle = canvas.create_oval(
        x,
        y,
        x + size,
        y + size,
        fill="#ffb6d5",
        outline=""
    )

    circles.append({
        "id": circle,
        "x": x,
        "y": y,
        "size": size,
        "speed": 0.5 + (i % 3) * 0.3
    })


def animate_background():

    for circle in circles:

        circle["y"] -= circle["speed"]

        if circle["y"] < -30:
            circle["y"] = 750

        canvas.coords(
            circle["id"],
            circle["x"],
            circle["y"],
            circle["x"] + circle["size"],
            circle["y"] + circle["size"]
        )

    root.after(30, animate_background)


animate_background()


# ============================================================
# MAIN FRAME
# ============================================================

main_frame = tk.Frame(
    root,
    bg="#fff5f9"
)

main_frame.place(
    relx=0.5,
    rely=0.5,
    anchor="center",
    width=700,
    height=690
)


# ============================================================
# TITLE
# ============================================================

title = tk.Label(
    main_frame,
    text="📈 STOCK PORTFOLIO TRACKER",
    font=("Arial", 24, "bold"),
    bg="#fff5f9",
    fg="#d63384"
)

title.pack(pady=(20, 3))


subtitle = tk.Label(
    main_frame,
    text="Track your investments easily",
    font=("Arial", 11),
    bg="#fff5f9",
    fg="#777777"
)

subtitle.pack()


# ============================================================
# NAME
# ============================================================

name_label = tk.Label(
    main_frame,
    text="👤 Enter Your First Name",
    font=("Arial", 13, "bold"),
    bg="#fff5f9",
    fg="#333333"
)

name_label.pack(pady=(18, 5))


name_entry = tk.Entry(
    main_frame,
    font=("Arial", 13),
    justify="center",
    width=35,
    bd=2,
    relief="solid"
)

name_entry.pack(ipady=7)


# ============================================================
# STOCK SYMBOL
# ============================================================

stock_label = tk.Label(
    main_frame,
    text="📊 Enter Stock Symbol",
    font=("Arial", 13, "bold"),
    bg="#fff5f9",
    fg="#333333"
)

stock_label.pack(pady=(15, 5))


stock_entry = tk.Entry(
    main_frame,
    font=("Arial", 13),
    justify="center",
    width=35,
    bd=2,
    relief="solid"
)

stock_entry.pack(ipady=7)


# ============================================================
# QUANTITY
# ============================================================

quantity_label = tk.Label(
    main_frame,
    text="🔢 Enter Quantity",
    font=("Arial", 13, "bold"),
    bg="#fff5f9",
    fg="#333333"
)

quantity_label.pack(pady=(15, 5))


quantity_entry = tk.Entry(
    main_frame,
    font=("Arial", 13),
    justify="center",
    width=35,
    bd=2,
    relief="solid"
)

quantity_entry.pack(ipady=7)


# ============================================================
# RESULT FRAME
# ============================================================

result_frame = tk.Frame(
    main_frame,
    bg="#ffe6f0",
    width=620,
    height=260
)

result_frame.pack(pady=12)

result_frame.pack_propagate(False)


result_label = tk.Label(
    result_frame,
    text="Enter your details and add a stock.",
    font=("Arial", 11),
    bg="#ffe6f0",
    fg="#333333",
    justify="left",
    anchor="nw"
)

result_label.pack(
    padx=18,
    pady=15,
    fill="both",
    expand=True
)


# ============================================================
# ANIMATED TEXT
# ============================================================

animation_id = None


def animate_text(text, index=0):

    global animation_id

    if index <= len(text):

        result_label.config(text=text[:index])

        animation_id = root.after(
            15,
            lambda: animate_text(text, index + 1)
        )


# ============================================================
# ADD STOCK
# ============================================================

def add_stock():

    name = name_entry.get().strip()
    stock = stock_entry.get().upper().strip()
    quantity_text = quantity_entry.get().strip()

    # -------------------------
    # CHECK NAME
    # -------------------------

    if name == "":

        messagebox.showwarning(
            "Missing Name",
            "Please enter your first name."
        )

        name_entry.focus()
        return

    # -------------------------
    # CHECK STOCK
    # -------------------------

    if stock == "":

        messagebox.showwarning(
            "Missing Stock",
            "Please enter a stock symbol."
        )

        stock_entry.focus()
        return

    # -------------------------
    # CHECK STOCK AVAILABILITY
    # -------------------------

    if stock not in stock_prices:

        messagebox.showerror(
            "Invalid Stock",
            "Stock not available.\n\n"
            "Please choose from:\n\n"
            "AAPL, TSLA, GOOGL, MSFT,\n"
            "AMZN, META, NFLX"
        )

        stock_entry.focus()
        return

    # -------------------------
    # CHECK QUANTITY
    # -------------------------

    try:

        quantity = int(quantity_text)

        if quantity <= 0:
            raise ValueError

    except ValueError:

        messagebox.showerror(
            "Invalid Quantity",
            "Please enter a valid quantity greater than 0."
        )

        quantity_entry.focus()
        return

    # -------------------------
    # ADD TO PORTFOLIO
    # -------------------------

    portfolio[stock] = portfolio.get(stock, 0) + quantity

    price = stock_prices[stock]

    value = price * quantity

    # -------------------------
    # AVAILABLE STOCKS
    # -------------------------

    available_stocks = ""

    for s, p in stock_prices.items():

        available_stocks += f"{s:<7} → ${p}\n"

    # -------------------------
    # RESULT
    # -------------------------

    message = (
        f"Hello {name}! 👋\n\n"
        f"✨ STOCK ADDED SUCCESSFULLY ✨\n\n"
        f"Stock       : {stock}\n"
        f"Quantity    : {quantity}\n"
        f"Price       : ${price}\n"
        f"Investment  : ${value}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📈 AVAILABLE STOCKS\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"{available_stocks}"
    )

    animate_text(message)

    # Clear inputs

    stock_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

    stock_entry.focus()


# ============================================================
# SHOW PORTFOLIO
# ============================================================

def show_portfolio():

    if not portfolio:

        messagebox.showinfo(
            "Portfolio",
            "No stocks have been added yet."
        )

        return

    total_investment = 0

    output = (
        "📊 YOUR PORTFOLIO\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    )

    for stock, quantity in portfolio.items():

        price = stock_prices[stock]

        value = price * quantity

        total_investment += value

        output += (
            f"📌 {stock}\n"
            f"   Quantity : {quantity}\n"
            f"   Price    : ${price}\n"
            f"   Value    : ${value}\n\n"
        )

    output += (
        "━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"💰 TOTAL INVESTMENT: ${total_investment}"
    )

    animate_text(output)


# ============================================================
# SAVE PORTFOLIO
# ============================================================

def save_portfolio():

    if not portfolio:

        messagebox.showwarning(
            "Nothing to Save",
            "Please add at least one stock first."
        )

        return

    total_investment = 0

    name = name_entry.get().strip()

    with open("stock_portfolio.txt", "w") as file:

        file.write("STOCK PORTFOLIO TRACKER\n")
        file.write("=" * 45 + "\n")

        file.write(f"Investor: {name}\n")

        file.write(
            "Date: "
            + datetime.now().strftime("%d-%m-%Y %H:%M")
            + "\n\n"
        )

        for stock, quantity in portfolio.items():

            price = stock_prices[stock]

            value = price * quantity

            total_investment += value

            file.write(
                f"{stock} - "
                f"Quantity: {quantity}, "
                f"Price: ${price}, "
                f"Value: ${value}\n"
            )

        file.write("\n")
        file.write("=" * 45 + "\n")

        file.write(
            f"Total Investment: ${total_investment}\n"
        )

    messagebox.showinfo(
        "Saved Successfully",
        "✅ Portfolio saved successfully!\n\n"
        "File name:\n"
        "stock_portfolio.txt"
    )


# ============================================================
# BUTTON FRAME
# ============================================================

button_frame = tk.Frame(
    main_frame,
    bg="#fff5f9"
)

button_frame.pack(pady=5)


# ============================================================
# ADD STOCK BUTTON
# ============================================================

add_button = tk.Button(
    button_frame,
    text="➕ Add Stock",
    font=("Arial", 11, "bold"),
    bg="#d63384",
    fg="white",
    activebackground="#b82b70",
    activeforeground="white",
    width=15,
    bd=0,
    cursor="hand2",
    command=add_stock
)

add_button.grid(
    row=0,
    column=0,
    padx=5
)


# ============================================================
# SHOW PORTFOLIO BUTTON
# ============================================================

portfolio_button = tk.Button(
    button_frame,
    text="📊 Show Portfolio",
    font=("Arial", 11, "bold"),
    bg="#ff69a4",
    fg="white",
    activebackground="#e85b92",
    activeforeground="white",
    width=15,
    bd=0,
    cursor="hand2",
    command=show_portfolio
)

portfolio_button.grid(
    row=0,
    column=1,
    padx=5
)


# ============================================================
# SAVE BUTTON
# ============================================================

save_button = tk.Button(
    button_frame,
    text="💾 Save",
    font=("Arial", 11, "bold"),
    bg="#c2185b",
    fg="white",
    activebackground="#a3154d",
    activeforeground="white",
    width=12,
    bd=0,
    cursor="hand2",
    command=save_portfolio
)

save_button.grid(
    row=0,
    column=2,
    padx=5
)


# ============================================================
# FOOTER
# ============================================================

footer = tk.Label(
    main_frame,
    text="💗 Smart • Simple • Fast",
    font=("Arial", 9, "italic"),
    bg="#fff5f9",
    fg="#999999"
)

footer.pack(pady=3)


# ============================================================
# START
# ============================================================

name_entry.focus()

root.mainloop()