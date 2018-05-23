from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = "ThisIsSecret"


@app.route("/")
def showCount():
    if not('count' in session):
        session['count'] = 0
    session['count'] += 1
    print(session['count'])
    return render_template('index.html')

@app.route("/increaseBy2", methods=["GET", "POST"])
def increaseBy2():
    print("HELLO")
    if not('count' in session):
        session['count'] = 0
    session['count'] += 2
    print(session['count'])
    return render_template('index.html')

@app.route("/reset")
def reset():
    session.clear()
    return redirect('/')

@app.route("/destroy_session")
def destroy():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
