from flask import Flask, render_template, request, session
import random
app = Flask(__name__)
app.secret_key = "SecretKey"

@app.route('/', methods=['GET'])
def mainPage():
    session.clear()
    if not('num' in session):
        session['num'] = random.randrange(0, 101)
    return render_template("index.html")


@app.route('/compare', methods=['GET', 'POST'])
def compare():
    display = "none"
    user_guess = int(request.form['guess'])
    if user_guess < session['num']:
        response = "Too low!"
        color = "red"
    elif user_guess > session['num']:
        response = "Too high!"
        color = "red"
    else:
        response = str(user_guess) + " was the number!"
        color = "green"
        display = "display"
        session.clear()
    return render_template("index.html", response=response, color=color, display=display)



if __name__ == "__main__":
    app.run(debug=True)
