import tkinter as tk
from tkinter import messagebox
import math

# =========================================================
# STOCK PORTFOLIO TRACKER
# =========================================================

# Hardcoded stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420,
    "AMZN": 190,
    "META": 500,
    "NFLX": 650,
    "NVDA": 120,
    "TGT": 105,
    "HD": 390,
    "SPY": 600,
    "QQQ": 500
}

# Portfolio entered by user
portfolio = {}


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()
root.title("Think Stocks Portfolio Tracker")
root.geometry("1280x720")
root.configure(bg="#242424")
root.resizable(False, False)


# =========================================================
# COLORS
# =========================================================

BG = "#242424"
PANEL = "#292929"
GREEN = "#00ff00"
WHITE = "#ffffff"
GRAY = "#aaaaaa"
DARK_GRAY = "#1c1c1c"


# =========================================================
# TITLE
# =========================================================

title = tk.Label(
    root,
    text="Think Stocks Portfolio Tracker",
    font=("Arial", 27, "bold"),
    bg=BG,
    fg=WHITE
)
title.place(x=30, y=25)


# =========================================================
# PROFIT DISPLAY
# =========================================================

profit_title = tk.Label(
    root,
    text="My Profit:",
    font=("Arial", 25, "bold"),
    bg=BG,
    fg=WHITE
)
profit_title.place(x=820, y=30)

profit_value = tk.Label(
    root,
    text="$0.00",
    font=("Arial", 25, "bold"),
    bg=BG,
    fg=GREEN
)
profit_value.place(x=1020, y=30)


# =========================================================
# LEFT INPUT PANEL
# =========================================================

input_frame = tk.Frame(
    root,
    bg=PANEL,
    highlightbackground=GREEN,
    highlightthickness=1
)
input_frame.place(x=25, y=90, width=300, height=300)

tk.Label(
    input_frame,
    text="Add Stock",
    font=("Arial", 19, "bold"),
    bg=PANEL,
    fg=WHITE
).pack(pady=15)

tk.Label(
    input_frame,
    text="Stock Symbol",
    font=("Arial", 11),
    bg=PANEL,
    fg=GRAY
).pack()

stock_entry = tk.Entry(
    input_frame,
    font=("Arial", 13),
    bg=DARK_GRAY,
    fg=WHITE,
    insertbackground=WHITE,
    justify="center"
)
stock_entry.pack(pady=5)

tk.Label(
    input_frame,
    text="Quantity",
    font=("Arial", 11),
    bg=PANEL,
    fg=GRAY
).pack()

quantity_entry = tk.Entry(
    input_frame,
    font=("Arial", 13),
    bg=DARK_GRAY,
    fg=WHITE,
    insertbackground=WHITE,
    justify="center"
)
quantity_entry.pack(pady=5)


# =========================================================
# ADD STOCK FUNCTION
# =========================================================

def add_stock():

    stock = stock_entry.get().upper().strip()
    quantity = quantity_entry.get().strip()

    if stock not in STOCK_PRICES:
        messagebox.showerror(
            "Invalid Stock",
            "Please enter a stock from the available list."
        )
        return

    try:
        quantity = int(quantity)

        if quantity <= 0:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Invalid Quantity",
            "Please enter a positive whole number."
        )
        return

    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

    stock_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

    update_dashboard()


add_button = tk.Button(
    input_frame,
    text="ADD STOCK",
    command=add_stock,
    font=("Arial", 11, "bold"),
    bg=GREEN,
    fg="black",
    activebackground=WHITE,
    relief="flat",
    width=20,
    cursor="hand2"
)
add_button.pack(pady=15)


# =========================================================
# AVAILABLE STOCKS
# =========================================================

available_text = tk.Label(
    input_frame,
    text="Available: AAPL  TSLA  GOOGL  MSFT\n"
         "AMZN  META  NFLX  NVDA  TGT  HD",
    font=("Arial", 8),
    bg=PANEL,
    fg=GRAY
)
available_text.pack()


# =========================================================
# CANVAS
# =========================================================

canvas = tk.Canvas(
    root,
    width=920,
    height=580,
    bg=BG,
    highlightthickness=0
)
canvas.place(x=340, y=90)


# =========================================================
# DRAW DONUT CHART
# =========================================================

def draw_donut():

    canvas.delete("donut")

    if not portfolio:
        canvas.create_oval(
            50, 100, 310, 360,
            outline="#444444",
            width=55,
            tags="donut"
        )

        canvas.create_text(
            180, 230,
            text="No Stocks",
            fill=GRAY,
            font=("Arial", 14, "bold"),
            tags="donut"
        )
        return

    total = sum(
        STOCK_PRICES[s] * q
        for s, q in portfolio.items()
    )

    start_angle = 0

    # Use several shades of green
    greens = [
        "#00ff00",
        "#00e600",
        "#00cc00",
        "#00b300",
        "#009900",
        "#008000"
    ]

    for i, (stock, quantity) in enumerate(portfolio.items()):

        value = STOCK_PRICES[stock] * quantity

        angle = value / total * 360

        canvas.create_arc(
            50,
            100,
            310,
            360,
            start=start_angle,
            extent=angle,
            outline=greens[i % len(greens)],
            width=55,
            style="arc",
            tags="donut"
        )

        start_angle += angle

    canvas.create_text(
        180,
        210,
        text="My Account Value",
        fill=WHITE,
        font=("Arial", 13, "bold"),
        tags="donut"
    )

    canvas.create_line(
        100,
        235,
        260,
        235,
        fill=WHITE,
        width=2,
        tags="donut"
    )

    canvas.create_text(
        180,
        260,
        text=f"${total:,.2f}",
        fill=WHITE,
        font=("Arial", 16, "bold"),
        tags="donut"
    )


# =========================================================
# PORTFOLIO LABELS
# =========================================================

def draw_stock_labels():

    canvas.delete("labels")

    y = 110

    for stock, quantity in portfolio.items():

        value = STOCK_PRICES[stock] * quantity

        total = sum(
            STOCK_PRICES[s] * q
            for s, q in portfolio.items()
        )

        percentage = value / total * 100

        canvas.create_text(
            15,
            y,
            anchor="w",
            text=f"{stock}\n{percentage:.1f}%",
            fill=WHITE,
            font=("Arial", 10, "bold"),
            tags="labels"
        )

        y += 50

        if y > 400:
            break


# =========================================================
# PERFORMANCE BAR CHART
# =========================================================

def draw_bar_chart():

    canvas.delete("bars")

    canvas.create_text(
        650,
        30,
        text="Portfolio Performance",
        fill=WHITE,
        font=("Arial", 16, "bold"),
        tags="bars"
    )

    if not portfolio:
        canvas.create_text(
            650,
            180,
            text="Add stocks to view performance",
            fill=GRAY,
            font=("Arial", 12),
            tags="bars"
        )
        return

    max_value = max(
        STOCK_PRICES[s] * q
        for s, q in portfolio.items()
    )

    x = 410

    for stock, quantity in portfolio.items():

        value = STOCK_PRICES[stock] * quantity

        bar_height = (value / max_value) * 180

        canvas.create_rectangle(
            x,
            320 - bar_height,
            x + 35,
            320,
            fill=GREEN,
            outline="",
            tags="bars"
        )

        canvas.create_text(
            x + 17,
            340,
            text=stock,
            fill=WHITE,
            font=("Arial", 8, "bold"),
            tags="bars"
        )

        x += 55

        if x > 850:
            break


# =========================================================
# TODAY'S PERFORMANCE
# =========================================================

def draw_today():

    canvas.delete("today")

    canvas.create_text(
        650,
        405,
        text="Today's Performance",
        fill=WHITE,
        font=("Arial", 16, "bold"),
        tags="today"
    )

    if not portfolio:
        return

    x = 410

    for index, stock in enumerate(portfolio):

        # Demo performance values
        performance = ((index % 5) - 2) * 0.35

        y = 475 - performance * 40

        canvas.create_oval(
            x,
            y,
            x + 9,
            y + 9,
            fill=GREEN,
            outline="",
            tags="today"
        )

        canvas.create_text(
            x,
            520,
            text=stock,
            fill=WHITE,
            font=("Arial", 8),
            tags="today"
        )

        x += 55

        if x > 850:
            break


# =========================================================
# PORTFOLIO STATS
# =========================================================

stats_frame = tk.Frame(
    root,
    bg=PANEL
)
stats_frame.place(x=25, y=410, width=300, height=260)

tk.Label(
    stats_frame,
    text="Portfolio Stats",
    font=("Arial", 17, "bold"),
    bg=PANEL,
    fg=WHITE
).pack(pady=10)

stats_label = tk.Label(
    stats_frame,
    text="Account Value     $0.00\n"
         "Investment        $0.00\n"
         "Positions         0\n"
         "Profit/Loss       $0.00",
    font=("Arial", 10),
    bg=PANEL,
    fg=WHITE,
    justify="left"
)
stats_label.pack()


# =========================================================
# UPDATE DASHBOARD
# =========================================================

def update_dashboard():

    if not portfolio:
        return

    total_value = 0

    for stock, quantity in portfolio.items():
        total_value += STOCK_PRICES[stock] * quantity

    # Demo cost basis
    investment = total_value * 0.92

    profit = total_value - investment

    profit_value.config(
        text=f"${profit:,.2f}"
    )

    stats_label.config(
        text=
        f"Account Value     ${total_value:,.2f}\n"
        f"Investment        ${investment:,.2f}\n"
        f"Positions         {len(portfolio)}\n"
        f"Profit/Loss       ${profit:,.2f}"
    )

    draw_donut()
    draw_stock_labels()
    draw_bar_chart()
    draw_today()


# =========================================================
# SAVE PORTFOLIO
# =========================================================

def save_portfolio():

    if not portfolio:
        messagebox.showwarning(
            "No Portfolio",
            "Please add stocks first."
        )
        return

    total = sum(
        STOCK_PRICES[s] * q
        for s, q in portfolio.items()
    )

    with open("stock_portfolio.txt", "w") as file:

        file.write("THINK STOCKS PORTFOLIO TRACKER\n")
        file.write("=" * 40 + "\n\n")

        for stock, quantity in portfolio.items():

            price = STOCK_PRICES[stock]
            value = price * quantity

            file.write(
                f"{stock} | Quantity: {quantity} | "
                f"Price: ${price} | Value: ${value}\n"
            )

        file.write("\n")
        file.write(f"Total Account Value: ${total:,.2f}\n")

    messagebox.showinfo(
        "Saved",
        "Portfolio saved as stock_portfolio.txt"
    )


# =========================================================
# SAVE BUTTON
# =========================================================

save_button = tk.Button(
    root,
    text="SAVE PORTFOLIO",
    command=save_portfolio,
    font=("Arial", 10, "bold"),
    bg=GREEN,
    fg="black",
    relief="flat",
    cursor="hand2"
)
save_button.place(x=95, y=680, width=160, height=30)


# =========================================================
# INITIAL DISPLAY
# =========================================================

draw_donut()
draw_bar_chart()
draw_today()


# =========================================================
# RUN APPLICATION
# =========================================================

root.mainloop()