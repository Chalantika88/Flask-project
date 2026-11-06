from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask!"

@app.route('/search')
def search():
    query = request.args.get('q')
    return f"Search Query: {query}"

@app.route('/user')
def user():
    name = request.args.get('name', 'Guest')
    age = request.args.get('age')

    return f"Name: {name}, Age: {age}"

if __name__ == "__main__":
    app.run(debug=True)