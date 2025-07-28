from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        score = random.randint(1, 100)
        if score > 70:
            result = f"😴 Ваш компьютер СКУЧНЫЙ на {score}%!"
        else:
            result = f"🔥 Ваш компьютер НЕСКУЧНЫЙ! Только {score}% скуки."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
