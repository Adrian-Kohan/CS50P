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
    stocks = db.execute("SELECT symbol, SUM(share) FROM purchase WHERE user_id = ? GROUP BY symbol", session.get("user_id"))
    cash = cash[0]["cash"]

    # show the current price of each stock
    for stock in stocks:
        symbol = stock["symbol"]
        info = lookup(symbol)
        current_price = info["price"]
        stock.update({"price":current_price})

    return render_template("index.html", stocks=stocks, cash=cash)


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
            return apology("symbol does not exist", 403)

        # Ensure number of shares is a positive number
        if int(request.form.get("shares")) < 0:
            return apology("number of shares must be positive", 403)


        # Look up stock price
        price = status["price"]

        # Calculate the total price of the purchase
        total = price * int(request.form.get("shares"))

        # Amount of cash that user has
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = cash[0]["cash"]
        # Check if the purchase is successful or not
        if total > cash:
            return apology("you cannot afford the number of shares at the current price", 403)

        else:
            # Calculate the remained user cash
            remained = cash - total

            # Add purchase table to the database
            #db.execute("""

            #                   CREATE TABLE purchase (
            #                       user_id INTEGER,
            #                       symbol TEXT,
            #                       price FLOAT,
            #                       share INTEGER,
            #                       date DATETIME
            #                   )
            #                """)
            # Add purchase data to a new tabel
            db.execute(
            "INSERT INTO purchase (user_id, symbol, price, share, date) VALUES (?, ?, ?, ?, ?)",
            session["user_id"],
            request.form.get("symbol"),
            status["price"],
            request.form.get("shares"),
            current_date()
            )

            # Update remained user cash
            db.execute(
            "UPDATE users SET cash = ? WHERE id = ?", remained, session["user_id"]
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
    return apology("TODO")


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
            return apology("must provide symbol", 403)

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
            return apology("must provide username", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username is not already exists
        if len(rows) != 0:
            return apology("username is already exists", 403)

        # Ensure password is not empty
        elif not request.form.get("password") or not request.form.get("confirmation"):
            return apology("must provide password", 403)

        # Ensure password and confirmation are the same
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("password do not match", 403)

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

    stocks = db.execute("SELECT symbol, SUM(share) FROM purchase WHERE user_id = ? GROUP BY symbol", session.get("user_id"))

     # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        share = db.execute("SELECT share FROM purchase WHERE user_id = ? AND symbol = ?", session.get("user_id"), request.form.get("symbol"))
        share = int(share[0]["share"])
        # Ensure symbol is not empty submitted
        if not request.form.get("symbol"):
            return apology("must provide symbol", 403)

        # Ensure user have share of the selected stock
        if share == 0:
            return apology("you don't have any share of this stock", 403)

        # Ensure number of shares is a positive number
        if int(request.form.get("shares")) < 0:
            return apology("number of shares must be positive", 403)

        # ENSURE the user own that many shares of the stock
        if int(request.form.get("shares")) > share:
            return apology("you not own that many shares of the stocke", 403)

        # Look up stock price
        status = lookup(request.form.get("symbol"))
        price = status["price"]

        # Calculate the total price of the purchase
        total = price * int(request.form.get("shares"))

        # Amount of cash that user has
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = cash[0]["cash"]

        # Calculate the remained user cash
        remained = cash + total

        # Calculate the remained share
        remained_share = share - int(request.form.get("shares"))

        # Update purchase data
        db.execute(
            "UPDATE purchase SET share = ? AND price = ? WHERE user_id = ?", remained_share, total, session["user_id"]
            )

        # Update remained user cash
        db.execute(
            "UPDATE users SET cash = ? WHERE id = ?", remained, session["user_id"]
            )

        flash("Sold!")
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("sell.html", stocks=stocks)