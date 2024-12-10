from flask import Flask, render_template_string
app = Flask(__name__)

@app.route('/')
@app.route('/<usrname>')
def named_page(usrname="stranger"):
    page = '''
    <html>
<head>
<title>{{template_name}} ' s Page</title>
</head>
<body>
<h1>Hello there {{template_name}} </h1>
<p>
Nice to see you <i>again</i> {{ template_name }}
</p>
<p>
How have you <b> been </b> {{template_name}}
</p>
</body>
</html>
'''
    return render_template_string(page, template_name=usrname)

if __name__ == '__main__':
    app.run(debug=True)