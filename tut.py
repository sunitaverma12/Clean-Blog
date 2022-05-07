import  flack
from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello() -> str:
    return render_template('index.html')

@app.route("/sunita")
def sunita() -> str:
    return render_template('orders/orders.html')
@app.route("/bootstrap")
def bootstrap() -> str:
    return render_template('bootstrap.html')


app.run(debug=True)
