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
app.config["SECRET_KEY"] = "your-secret-key"

users = {}  # Placeholder to store registered


@app.route("/")
def index():
    return render_template(
        "home.html",
        title="Jinja Demo Site",
        Description="Smarter page templates with Flask & Jinja",
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if username in users:
            flash("Username already exists!")
        elif password != confirm_password:
            flash("Passwords do not match!")
        else:
            # Store the user details in a dictionary or database
            users[username] = password
            flash("Registration successful! Please log in.")
            return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Perform login process
        username = request.form["username"]
        password = request.form["password"]

        # Validate user credentials
        if username in users and users[username] == password:
            # Set session variables or user tokens for authentication
            session["logged_in"] = True
            session["username"] = username
            flash("Login successful!")
            return redirect("/")
        else:
            flash("Invalid username or password!")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully!")
    return redirect("/")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # Display a success message or redirect to a thank you page
        return """
        <h2 style="color: green; text-align: center; padding-top: 100px;">Thank you for contacting us!</h2>
        <p style="text-align: center;">We will get back to you soon.</p>
        """

    return render_template(
        "contact.html",
        title="Contact Form",
        description="Contact Us",
    )


if __name__ == "__main__":
    app.run(debug=True)
