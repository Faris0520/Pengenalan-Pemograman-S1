from flask import Flask, render_template_string, request
from wtforms import Form, validators, StringField
import string

app = Flask(__name__)

def compute(original_str):
    bad_chars = string.whitespace + string.punctuation
    modified_str = original_str.lower()
    for char in modified_str:
        if char in bad_chars:
            modified_str = modified_str.replace(char,'')
    if modified_str == modified_str[::-1]:
        return "It's a palindrome!"
    else:
        return "It is not a palindrome :-("
    
# html cuy
page = '''
<html>
    <head>
        <title>Kalkulator Palindrom</title>
    </head>
    
    <body>
        <h1>Check if a string is a palindrome</h1>
        
        <form method=post action="">
            Hello String Fans!
        <br>
        Enter a string 
            {{ template_form.text_field }}
        <br>
            {% if result != None %}
                {{ result }}
            {% endif %}
        <br>
            <input type=submit value=calculate>
        </form>

    </body>
</html>
'''

class InputForm(Form):
    text_field = StringField(validators=[validators.InputRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    palindrome_result = None
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        input_val = form.text_field.data
        palindrome_result = compute(input_val)
    return render_template_string(page, template_form=form, result = palindrome_result)

if __name__ == '__main__':
    app.run(debug=True)