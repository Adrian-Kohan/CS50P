import os
import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd, current_date

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    cash = db.execute("SELECT cash FROM users WHERE id = ?", session.get("user_id"))
    stocks = db.execute("SELECT symbol, SUM(share) AS share FROM purchase WHERE user_id = ? GROUP BY symbol", session.get("user_id"))
    cash = cash[0]["cash"]
    total = round(float(cash), 2)

    # show the current price of each stock
    for stock in stocks:
        symbol = stock["symbol"]
        info = lookup(symbol)
        current_price = info["price"]
        stock.update({"price":current_price})
        total += round(float(stock["share"] * stock["price"]), 2)

    return render_template("index.html", stocks=stocks, cash=cash, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure symbol is not empty submitted
        if not request.form.get("symbol"):
            return apology("must provide symbol", 403)

        # Look for symbol status
        status = lookup(request.form.get("symbol"))

        # Ensure symbol existx
        if status is None:
            return apology("symbol does not exist", 400)

        try:
            # Ensure number of shares is a positive number
            if int(request.form.get("shares")) < 0 and float(request.form.get("shares")) < 0:
                return apology("number of shares must be positive", 400)
        except(ValueError):
                return apology("number of shares must be a simple number", 400)

        # Look up stock price
        price = status["price"]

        # Calculate the total price of the purchase
        total = float(price * int(request.form.get("shares")))

        # Amount of cash that user has
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session.get("user_id"))
        cash = float(cash[0]["cash"])

        # Check if the purchase is successful or not
        if total > cash:
            return apology("you cannot afford the number of shares at the current price", 403)

        else:
            # Calculate the remained user cash
            remained = round(float(cash - total), 2)

            # Add purchase table to the database
            #db.execute("""

            #                   CREATE TABLE purchase (
            #                       user_id INTEGER,
            #                       symbol TEXT,
            #                       price FLOAT,
            #                       share INTEGER,
            #                   )
            #                """)

            # db.execute("""
            #
            #                  CREATE TABLE history (
            #                      user_id INTEGER,
            #                      symbol TEXT,
            #                      price FLOAT,
            #                      share INTEGER,
            #                      date DATETIME,
            #                      transaction_type TEXT
            #                  )
            #               """)

            # Add purchase data to a new tabel
            db.execute(
            "INSERT INTO purchase (user_id, symbol, price, share) VALUES (?, ?, ?, ?)",
            session["user_id"],
            request.form.get("symbol"),
            status["price"],
            request.form.get("shares"),
            )

            # Add history data to a new tabel
            db.execute(
            "INSERT INTO history (user_id, symbol, price, share, date, transaction_type) VALUES (?, ?, ?, ?, ?,?)",
            session["user_id"],
            request.form.get("symbol"),
            status["price"],
            request.form.get("shares"),
            current_date(),
            "Buy"
            )

            # Update remained user cash
            db.execute(
            "UPDATE users SET cash = ? WHERE id = ?", remained, session.get("user_id")
            )

            flash("Bougth!")
            # Redirect user to home page
            return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    stocks = db.execute("SELECT * FROM history WHERE user_id = ?", session.get("user_id"))

    return render_template("history.html", stocks=stocks)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

         # Ensure symbol is not empty submitted
        if not request.form.get("symbol"):
            return apology("must provide symbol", 400)

         # Ensure symbol is valid
        if lookup(request.form.get("symbol")) is None:
            return apology("must provide a valid symbol", 400)


        # Look for symbol status
        status = lookup(request.form.get("symbol"))
        return render_template("quoted.html", status=status)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username is not empty submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username is not already exists
        if len(rows) != 0:
            return apology("username is already exists", 400)

        # Ensure password is not empty
        elif not request.form.get("password") or not request.form.get("confirmation"):
            return apology("must provide password", 400)


        # Ensure password and confirmation are the same
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("password do not match", 400)

        db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)",
            request.form.get("username"),
            generate_password_hash(request.form.get("password"), method='pbkdf2:sha256',salt_length=8),
        )

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    stocks = db.execute("SELECT symbol, SUM(share) AS share FROM purchase WHERE user_id = ? GROUP BY symbol", session.get("user_id"))

     # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        share = db.execute("SELECT symbol, SUM(share) AS share FROM purchase WHERE user_id = ? AND symbol = ? GROUP BY symbol", session.get("user_id"), request.form.get("symbol"))

        try:
            share = int(share[0]["share"])

            # Ensure symbol is not empty submitted
            if not request.form.get("symbol"):
                return apology("must provide symbol", 403)

            # Ensure user have share of the selected stock
            if share == 0:
                return apology("you don't have any share of this stock", 403)

            # Ensure number of shares is a positive number
            if int(request.form.get("shares")) < 0:
                return apology("number of shares must be positive", 400)
        except(ValueError, IndexError):
                return apology("amount of cash must be a simple number", 400)



        # ENSURE the user own that many shares of the stock
        if int(request.form.get("shares")) > share:
            return apology("you not own that many shares of the stocke", 403)

        # Look up stock price
        status = lookup(request.form.get("symbol"))
        price = status["price"]

        # Calculate the total price of the purchase
        total = price * int(request.form.get("shares"))

        # Amount of cash that user has
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session.get("user_id"))
        cash = cash[0]["cash"]

        # Calculate the final user cash
        final_cash = round(cash + total, 2)

        # Calculate the remained share
        remained_share = share - int(request.form.get("shares"))

         # Calculate the price of remained share
        price_r_share = float(remained_share * price)

        # Update purchase data
        db.execute(
                    "UPDATE purchase SET share = ?, price = ? WHERE symbol = ? AND user_id = ?", remained_share, price_r_share, request.form.get("symbol"), session.get("user_id")
                )

        # Update remained user cash
        db.execute(
            "UPDATE users SET cash = ? WHERE id = ?", final_cash, session.get("user_id")
            )

        # Add history data to the tabel
        db.execute(
            "INSERT INTO history (user_id, symbol, price, share, date, transaction_type) VALUES (?, ?, ?, ?, ?, ?)",
            session["user_id"],
            request.form.get("symbol"),
            status["price"],
            request.form.get("shares"),
            current_date(),
            "Sell"
            )

        flash("Sold!")
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("sell.html", stocks=stocks)




@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    """Add additional cash to their account."""

     # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        cash = db.execute("SELECT cash FROM users WHERE id = ?", session.get("user_id"))
        cash = cash[0]["cash"]

        try:
            additional_cash = int(request.form.get("cash"))

            # Ensure additional cash is not empty submitted
            if not additional_cash:
                return apology("must enter some cash", 403)

             # Ensure amount of cash is a positive number
            if additional_cash < 0:
                return apology("amount of cash must be positive", 403)
        except(ValueError):
                return apology("amount of cash must be a simple number", 403)


        # Calculate final cash
        final_cash = additional_cash + cash

        # Update user cash
        db.execute(
            "UPDATE users SET cash = ? WHERE id = ?", final_cash, session.get("user_id")
            )

        # Add history data to the tabel
        db.execute(
            "INSERT INTO history (user_id, symbol, price, share, date, transaction_type) VALUES (?, ?, ?, ?, ?, ?)",
            session["user_id"],
            "_",
            additional_cash,
            "_",
            current_date(),
            "Add Cash"
            )

        flash("added!")
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("add.html")