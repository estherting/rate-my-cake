from flask import Flask, render_template
app = Flask(__name__) # instanciating the Flask class

@app.route("/<name>")
def hello(name):
    return render_template('index.html', name=name)

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<name>")
def sayName(name):
    return "Hi " + name + "!"

@app.route("/repeat/<times>/<word>")
def repeat(times, word):
    return (word + " ")*int(times)



if __name__=="__main__":
    app.run(debug=True)
