import os
import psycopg2
from flask import Flask, request, render_template_string

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

LOGIN_PAGE = """
<h2>Login</h2>
<form method="post">
  Username: <input type="text" name="username"/><br>
  Password: <input type="password" name="password"/><br>
  <input type="submit"/>
</form>
<p>{{ message }}</p>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM users WHERE username=%s AND password=%s",
            (username, password)
        )
        user = cur.fetchone()
        cur.close()
        conn.close()

        message = "Login successful" if user else "Invalid credentials"
    return render_template_string(LOGIN_PAGE, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
