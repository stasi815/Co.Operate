from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/resources")
def resources():
    return render_template('resources.html')

if __name__ == "__main__":
    app.run(debug=True)