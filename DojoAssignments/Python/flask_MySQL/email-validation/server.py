from flask import Flask, render_template, redirect, request, session, flash
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key="SECRET!"
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('emailsdb')
# now, we may invoke the query_db method
print("all the emails", mysql.query_db("SELECT * FROM emails;"))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=["POST"])
def processEmail():
    # if not('email' in session):
    #     session['email'] = []
    #     print("new session created")
    user_email = request.form['email']
    valid = False
    for c in user_email:
        if c == "@":
            valid = True
            print("*"*50 + "email is valid")
            break

    query = "select * from emails where email = %(userEmail)s;"
    data = {"userEmail": user_email}
    exist = mysql.query_db(query, data)

    if valid and not(exist):
        session['email'] = user_email
        query = "insert into emails (email, created_at) values (%(userEmail)s, now());"
        data = {
                'userEmail': user_email
        }
        mysql.query_db(query, data)
        return redirect('/success')
    flash("Email is not valid!")
    return redirect('/')


@app.route('/success')
def success():
    query = "select * from emails"
    emails = mysql.query_db(query)
    email = session['email']
    flash("The email address you entered "+email+" is a VALID email address! Thank you!")
    return render_template('success.html', emails=emails)



if __name__ == "__main__":
    app.run(debug=True)
