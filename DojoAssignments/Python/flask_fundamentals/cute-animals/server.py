from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route("/")
def displayPics():
    x = 11
    return render_template('index.html', x=x)

@app.route("/<x>")
def displayXPics(x):
    x = int(x)+1
    return render_template('index.html', x=int(x))

@app.route("/danger")
def danger():
    print("danger! danger! danger!")
    return redirect('/')


if __name__== "__main__":
    app.run(debug=True)
