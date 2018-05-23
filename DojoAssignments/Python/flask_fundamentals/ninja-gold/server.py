from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key = "SecretKey"

@app.route('/', methods=['GET'])
def mainPage():
    if not('gold' in session) and not('activity' in session):
        session['gold'] = 0
        session['activity'] = ""
    return render_template("index.html")


@app.route('/process_gold', methods=["POST"])
def processGold():
    if request.form['building'] == "farm":
        gold = random.randrange(10, 21)
        session['gold'] += gold
        session['activity'] += "Earned " + str(gold) + " golds from the farm!<br>"
    if request.form['building'] == "cave":
        gold = random.randrange(5, 11)
        session['gold'] += gold
        session['activity'] += "Earned " + str(gold) + " golds from the cave!<br>"
    if request.form['building'] == "house":
        gold = random.randrange(2, 6)
        session['gold'] += gold
        session['activity'] += "Earned " + str(gold) + " golds from the house!<br>"
    if request.form['building'] == "casino":
        gold = random.randrange(-50, 51)
        if gold < 0:
            session['text-color'] = "red"
        else:
            session['text-color'] = "black"
        # text-color = session['text-color']
        session['gold'] += gold
        session['activity'] += "<p class='"+ session['text-color'] +"'>Earned " + str(gold) + " golds from the casino!</p><br>"
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
