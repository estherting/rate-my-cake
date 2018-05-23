from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('index.html')

@app.route('/play/<x>')
def makeBoxes(x):
    return render_template('index.html', x=int(x))

@app.route('/play/<x>/<color>')
def makeBoxesChangeColor(x, color):
    return render_template('index.html', x=int(x), color=color)

if __name__=="__main__":
    app.run(debug=True)
