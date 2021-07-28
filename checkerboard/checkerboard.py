from flask import Flask, render_template
app = Flask(__name__)

print(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/4')
def index_4():
    return render_template("index4.html")

@app.route('/<number1>/<number2>')
def index_x():
    return render_template("indexx.html")
if __name__=="__main__":
    app.run(debug=True)