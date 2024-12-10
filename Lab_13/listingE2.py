from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login')
def login_page():
    return 'Welcome to the login page'

@app.route('/login/message')
def message_page():
    return 'The message is: xyxyx'

if __name__ == '__main__':
    app.run(debug=True)
    