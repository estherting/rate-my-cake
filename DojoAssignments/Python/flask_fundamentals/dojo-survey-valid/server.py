from flask import Flask, render_template, url_for, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "Secret!!!!!!"

@app.route("/")
def surveyForm():
    return render_template('index.html')

@app.route("/result")
def result():
    return render_template('result.html')


@app.route('/process', methods=['POST'])
def process():
    msg = ""
    if len(request.form['name']) < 1 or len(request.form['comment']) > 120:
        print("did not pass validation")
        if len(request.form['name']) < 1:
            msg += "Please enter your name."
        if len(request.form['comment']) > 120:
            msg += "Comment cannot have more than 120 characters."
        flash(msg)
        return redirect('/')
    else:
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route("/danger")
def danger():
    print("User tried to visit /danger")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
