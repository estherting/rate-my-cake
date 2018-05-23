from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def displayChecker():
    return render_template('index.html')

@app.route('/<x>/<y>')
def customChecker(x, y):
    x = int(x)/2
    y = int(y)/2
    return render_template('index.html', x=int(x), y=int(y))




if __name__=="__main__":
    app.run(debug=True)
