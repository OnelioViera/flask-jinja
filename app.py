from flask import (
    Flask,
    render_template,
    session,
    request,
    render_template,
    redirect,
    make_response,
    flash,
)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "home.html",
        title="Jinja Demo Site",
        description="Smarter page templates with Flask & Jinja",
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Perform login process
        username = request.form["username"]
        password = request.form["password"]

        # Validate user credentials
        if username == "your_username" and password == "your_password":
            # Set session variables or user tokens for authentication
            session["logged_in"] = True
            session["username"] = username
            flash("Login successful!")
            return redirect("/")
        else:
            flash("Invalid username or password!")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Perform registration process
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        # Validate registration details
        if password != confirm_password:
            flash("Passwords do not match!")
        else:
            # Perform registration logic (e.g., store user details in a database)
            flash("Registration successful! Please log in.")
            return redirect("/login")

    return render_template("register.html")


@app.route("/contact")
def contact_form():
    return render_template(
        "contact.html",
        title="Contact From",
        description="Contact Us",
    )
