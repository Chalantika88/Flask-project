from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/user/<name>")
def user(name):
    return f"User ID: {name}"

@app.route("/price/<float:amount>")
def price(amount):
    return f"Price: {amount}"

@app.route("/files/<file_path>")
def files(file_path):
    return file_path

if __name__ == "__main__":
    app.run(debug=True)