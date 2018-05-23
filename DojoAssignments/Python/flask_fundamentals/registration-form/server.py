from flask import Flask, render_template, url_for, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "Secret!!!!!!"

@app.route("/")
def surveyForm():
    return render_template('index.html')


@app.route("/process", methods=["GET", "POST"])
def process():
    validity = 0
    for field in request.form:
        if len(request.form[field]) < 1:
            flash("All fields are required and must not be blank.")
            validity += 1
            break

    for c in request.form['first_name']:
        numArr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if c in numArr:
            flash("First and Last Name cannot contain any numbers.")
            validity += 1
            break

    if len(request.form['pw']) <= 8:
        flash("Password should be more than 8 characters")
        validity += 1

    count = 0
    for c in request.form['email']:
        if c == "@":
            count += 1
            break
    if count == 0:
        flash("Email should be a valid email")
        validity += 1

    if request.form['pw'] != request.form['confirm-pw']:
        flash("Password and Password Confirmation should match")
        validity += 1

    if validity == 0:
        flash("Thanks for submitting your information")

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
