from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/', methods=['GET', 'POST'])
def mainPage():
    # random generation
    set('rounds')

    return render_template("index.html")

def set(name):
    if not(name in session):
        session[name] = []

@app.route('/play', methods=['POST'])
def play():
    moves = ['rock', 'paper', 'scissors']
    compMove = moves[random.randrange(0, 3)]
    playerMove = request.form['move']
    playerIdx = moves.index(playerMove)
    compIdx = moves.index(compMove)
    moveDist = abs(playerIdx - compIdx)
    win = False
    if moveDist == 1:   # if they are next to each other
        if playerIdx > compIdx:
            win = True
    if moveDist == 2:
        if playerIdx < compIdx:
            win = True

    session['rounds'] += [win]

    if len(session['rounds']) > 3:
        session.clear()



    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
