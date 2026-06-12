from flask import Flask,render_template
from database import conn,cursor

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)