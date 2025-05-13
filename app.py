from flask import Flask, request, render_template
import sqlite3
import os

app = Flask(__name__)

def init_db():
    if not os.path.exists("database.db"):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute('CREATE TABLE users (username TEXT, password TEXT)')
        c.execute("INSERT INTO users VALUES ('admin', 'supersecret')")
        conn.commit()
        conn.close()



@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print(f"[DEBUG] SQL query: {query}")
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute(query)
        result = c.fetchone()
        conn.close()

        if result:
            message = f"Bienvenue, {result[0]}!"
        else:
            message = "Nom d'utilisateur ou mot de passe incorrect."

    return render_template("login.html", message=message)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)