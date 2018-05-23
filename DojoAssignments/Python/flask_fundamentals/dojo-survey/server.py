from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route("/")
def surveyForm():
    return render_template('index.html')

@app.route("/result", methods=["POST"])
def result():
    print("results received!")
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template('result.html', name=name, location=location, language=language, comment=comment)

@app.route("/danger")
def danger():
    print "User tried to visit /danger"
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
