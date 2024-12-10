from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quote')
def quote():
    get_respon = requests.get('https://quotes-api-self.vercel.app/quote')
    respon = get_respon.json()
    return respon

if __name__ == '__main__':
    app.run(debug=True)