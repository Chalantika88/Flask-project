from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask!"

@app.route('/user/<username>')
def show_user(username):
    return f"Hello, {username}!"

@app.route('/user/<int:user_id>')
def show_user_id(user_id):
    return f"User ID: {user_id}"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Post ID: {post_id}"

if __name__ == '__main__':
    app.run(debug=True)