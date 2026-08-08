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


# ============================================================
# ANIMATED BACKGROUND
# ============================================================

canvas = tk.Canvas(
    root,
    width=850,
    height=750,
    bg="#ffd6e7",
    highlightthickness=0
)

canvas.pack(fill="both", expand=True)


# Store bubble information
bubbles = []

for i in range(25):

    x = (i * 83) % 850
    y = (i * 137) % 750

    size = 15 + (i % 5) * 8

    speed = 0.5 + (i % 4) * 0.25

    bubble = canvas.create_oval(
        x,
        y,
        x + size,
        y + size,
        fill="#ffb6d5",
        outline=""
    )

    bubbles.append({
        "id": bubble,
        "x": x,
        "y": y,
        "size": size,
        "speed": speed
    })


# ============================================================
# BACKGROUND ANIMATION
# ============================================================

def animate_background():

    for bubble in bubbles:

        bubble["y"] -= bubble["speed"]

        if bubble["y"] < -50:
            bubble["y"] = 750

        canvas.coords(
            bubble["id"],
            bubble["x"],
            bubble["y"],
            bubble["x"] + bubble["size"],
            bubble["y"] + bubble["size"]
        )

    root.after(30, animate_background)


animate_background()


# ============================================================
# WELCOME SCREEN
# ============================================================

welcome_frame = tk.Frame(
    root,
    bg="#fff5f9",
    width=700,
    height=690
)

welcome_frame.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)

welcome_frame.pack_propagate(False)


welcome_label = tk.Label(
    welcome_frame,
    text="",
    font=("Arial", 28, "bold"),
    bg="#fff5f9",
    fg="#d63384"
)

welcome_label.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)


# ============================================================
# WELCOME TYPING ANIMATION
# ============================================================

def welcome_animation(
    text="WELCOME TO THE PORTFOLIO",
    index=0
):

    if index <= len(text):

        welcome_label.config(
            text=text[:index]
        )

        root.after(
            80,
            lambda: welcome_animation(
                text,
                index + 1
            )
        )

    else:

        root.after(
            1500,
            show_main_screen
        )


# ============================================================
# SHOW MAIN SCREEN
# ============================================================

def show_main_screen():

    welcome_frame.destroy()

    create_main_screen()


# ============================================================
# MAIN PORTFOLIO SCREEN
# ============================================================

def create_main_screen():

    main_frame = tk.Frame(
        root,
        bg="#fff5f9",
        width=700,
        height=690
    )

    main_frame.place(
        relx=0.5,
        rely=0.5,
        anchor="center"
    )

    main_frame.pack_propagate(False)


    # ========================================================
    # TITLE
    # ========================================================

    title = tk.Label(
        main_frame,
        text="STOCK PORTFOLIO TRACKER",
        font=("Arial", 24, "bold"),
        bg="#fff5f9",
        fg="#d63384"
    )

    title.pack(pady=(20, 3))


    subtitle = tk.Label(
        main_frame,
        text="Manage your stock investments easily",
        font=("Arial", 11),
        bg="#fff5f9",
        fg="#777777"
    )

    subtitle.pack(pady=(0, 12))


    # ========================================================
    # NAME
    # ========================================================

    name_label = tk.Label(
        main_frame,
        text="Enter Your Name",
        font=("Arial", 13, "bold"),
        bg="#fff5f9",
        fg="#333333"
    )

    name_label.pack(pady=(5, 4))


    name_entry = tk.Entry(
        main_frame,
        font=("Arial", 13),
        justify="center",
        width=35,
        bd=2,
        relief="solid"
    )

    name_entry.pack(ipady=7)


    # ========================================================
    # STOCK SYMBOL
    # ========================================================

    stock_label = tk.Label(
        main_frame,
        text="Enter Stock Symbol",
        font=("Arial", 13, "bold"),
        bg="#fff5f9",
        fg="#333333"
    )

    stock_label.pack(pady=(12, 4))


    stock_entry = tk.Entry(
        main_frame,
        font=("Arial", 13),
        justify="center",
        width=35,
        bd=2,
        relief="solid"
    )

    stock_entry.pack(ipady=7)


    stock_example = tk.Label(
        main_frame,
        text="Example: AAPL, TSLA, GOOGL, MSFT",
        font=("Arial", 9, "italic"),
        bg="#fff5f9",
        fg="#999999"
    )

    stock_example.pack(pady=(2, 0))


    # ========================================================
    # QUANTITY
    # ========================================================

    quantity_label = tk.Label(
        main_frame,
        text="Enter Quantity",
        font=("Arial", 13, "bold"),
        bg="#fff5f9",
        fg="#333333"
    )

    quantity_label.pack(pady=(10, 4))


    quantity_entry = tk.Entry(
        main_frame,
        font=("Arial", 13),
        justify="center",
        width=35,
        bd=2,
        relief="solid"
    )

    quantity_entry.pack(ipady=7)


    quantity_example = tk.Label(
        main_frame,
        text="Example: 5",
        font=("Arial", 9, "italic"),
        bg="#fff5f9",
        fg="#999999"
    )

    quantity_example.pack(pady=(2, 0))


    # ========================================================
    # RESULT BOX
    # ========================================================

    result_frame = tk.Frame(
        main_frame,
        bg="#ffe6f0",
        width=620,
        height=250
    )

    result_frame.pack(pady=12)

    result_frame.pack_propagate(False)


    result_label = tk.Label(
        result_frame,
        text="Enter your details and click Add Stock.",
        font=("Arial", 10),
        bg="#ffe6f0",
        fg="#333333",
        justify="left",
        anchor="nw"
    )

    result_label.pack(
        padx=18,
        pady=12,
        fill="both",
        expand=True
    )


    # ========================================================
    # RESULT TEXT ANIMATION
    # ========================================================

    def animate_text(text, index=0):

        if index <= len(text):

            result_label.config(
                text=text[:index]
            )

            root.after(
                15,
                lambda: animate_text(
                    text,
                    index + 1
                )
            )


    # ========================================================
    # ADD STOCK
    # ========================================================

    def add_stock():

        name = name_entry.get().strip()

        stock = stock_entry.get().upper().strip()

        quantity_text = quantity_entry.get().strip()


        # CHECK NAME

        if name == "":

            messagebox.showwarning(
                "Missing Name",
                "Please enter your name."
            )

            name_entry.focus()

            return


        # CHECK STOCK

        if stock == "":

            messagebox.showwarning(
                "Missing Stock",
                "Please enter a stock symbol."
            )

            stock_entry.focus()

            return


        # CHECK STOCK AVAILABILITY

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


        # CHECK QUANTITY

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


        # ====================================================
        # CALCULATE
        # ====================================================

        price = stock_prices[stock]

        value = price * quantity


        # ADD TO PORTFOLIO

        portfolio[stock] = (
            portfolio.get(stock, 0)
            + quantity
        )


        # ====================================================
        # TOTAL INVESTMENT
        # ====================================================

        total_investment = 0

        for s, q in portfolio.items():

            total_investment += (
                stock_prices[s] * q
            )


        # ====================================================
        # AVAILABLE STOCKS
        # ====================================================

        available_stocks = ""

        for s, p in stock_prices.items():

            available_stocks += (
                f"{s:<7}  ${p}\n"
            )


        # ====================================================
        # FULL RESULT
        # ====================================================

        message = (
            "STOCK ADDED SUCCESSFULLY!\n"
            "================================\n\n"
            f"Investor Name : {name}\n\n"
            f"Stock         : {stock}\n"
            f"Quantity      : {quantity}\n"
            f"Price         : ${price}\n"
            f"Investment    : ${value}\n\n"
            "================================\n"
            f"TOTAL INVESTMENT : ${total_investment}\n\n"
            "AVAILABLE STOCKS\n"
            "================================\n"
            f"{available_stocks}"
        )


        # ANIMATE RESULT

        animate_text(message)


        # CLEAR INPUTS

        stock_entry.delete(
            0,
            tk.END
        )

        quantity_entry.delete(
            0,
            tk.END
        )

        stock_entry.focus()


    # ========================================================
    # SAVE PORTFOLIO
    # ========================================================

    def save_portfolio():

        if not portfolio:

            messagebox.showwarning(
                "Nothing to Save",
                "Please add at least one stock first."
            )

            return


        name = name_entry.get().strip()

        total_investment = 0


        with open(
            "stock_portfolio.txt",
            "w"
        ) as file:

            file.write(
                "STOCK PORTFOLIO TRACKER\n"
            )

            file.write(
                "=" * 45
                + "\n\n"
            )

            file.write(
                f"Investor Name: {name}\n"
            )

            file.write(
                "Date: "
                + datetime.now().strftime(
                    "%d-%m-%Y %H:%M"
                )
                + "\n\n"
            )


            for stock, quantity in portfolio.items():

                price = stock_prices[stock]

                value = price * quantity

                total_investment += value


                file.write(
                    f"Stock       : {stock}\n"
                    f"Quantity    : {quantity}\n"
                    f"Price       : ${price}\n"
                    f"Investment  : ${value}\n"
                )

                file.write(
                    "-" * 35
                    + "\n"
                )


            file.write(
                "\n"
                + "=" * 45
                + "\n"
            )

            file.write(
                f"TOTAL INVESTMENT: ${total_investment}\n"
            )


        # ====================================================
        # SUCCESS MESSAGE
        # ====================================================

        success_message = (
            "PORTFOLIO SAVED SUCCESSFULLY!\n\n"
            "================================\n\n"
            f"Investor : {name}\n\n"
            f"Total Investment : ${total_investment}\n\n"
            "File saved as:\n"
            "stock_portfolio.txt"
        )


        animate_text(
            success_message
        )


        root.after(
            1500,
            lambda: messagebox.showinfo(
                "Success",
                "Portfolio saved successfully!\n\n"
                "File: stock_portfolio.txt"
            )
        )


    # ========================================================
    # BUTTON FRAME
    # ========================================================

    button_frame = tk.Frame(
        main_frame,
        bg="#fff5f9"
    )

    button_frame.pack(pady=3)


    # ========================================================
    # ADD STOCK BUTTON
    # ========================================================

    add_button = tk.Button(
        button_frame,
        text="Add Stock",
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
        padx=7
    )


    # ========================================================
    # SAVE BUTTON
    # ========================================================

    save_button = tk.Button(
        button_frame,
        text="Save Portfolio",
        font=("Arial", 11, "bold"),
        bg="#c2185b",
        fg="white",
        activebackground="#a3154d",
        activeforeground="white",
        width=15,
        bd=0,
        cursor="hand2",
        command=save_portfolio
    )

    save_button.grid(
        row=0,
        column=1,
        padx=7
    )


    # ========================================================
    # FOOTER
    # ========================================================

    footer = tk.Label(
        main_frame,
        text="Smart • Simple • Fast",
        font=("Arial", 9, "italic"),
        bg="#fff5f9",
        fg="#999999"
    )

    footer.pack(pady=4)


    # ========================================================
    # START WITH NAME
    # ========================================================

    name_entry.focus()


# ============================================================
# START WELCOME ANIMATION
# ============================================================

welcome_animation()


# ============================================================
# START PROGRAM
# ============================================================

root.mainloop()
