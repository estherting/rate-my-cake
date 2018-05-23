from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def displayStore():
    return render_template('index.html')

@app.route("/checkout", methods=["POST"])
def checkout():
    strawberry = request.form['strawberry']
    raspberry = request.form['raspberry']
    apple = request.form['apple']
    fruits = ['Strawberry', 'Raspberry', 'Apple']
    items = int(strawberry) + int(raspberry) + int(apple)
    name = request.form['name']
    id = request.form['id']
    print(strawberry, raspberry, apple, name, id)
    return render_template('checkout.html', fruits=fruits, fruitCount=[strawberry, raspberry, apple], items=items, name=name, id=id)

if __name__ == "__main__":
    app.run(debug=True)
