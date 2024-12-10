from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    page = '''
<html>
<head>
<title>Default Page</title>
</head>
<body>
<h1>Hello there friend</h1>
<p>
Nice to see you <i>again</i>
</p>
<p>
How have you <b>been</b>?
</p>
</body>
</html>
'''
    return page

if __name__ == '__main__':
    app.run(debug=True)