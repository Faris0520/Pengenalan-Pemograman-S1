from flask import Flask, render_template_string, request
from wtforms import Form, validators, FloatField
import math

app = Flask(__name__)

def compute(val):
    result = math.sin(val)
    result_str = "Sine of {} is {:.4f}".format(val, result)
    return result_str

page = '''
<html>
<head>
<title>Sine Calculation</title>
</head>

<body>
<h1>Calculate the Sine </h1>

<form method=post action="">
Hello Calculation Fans !
<br>
Enter a floating−point value
{{ template_form.float_field }}
<br>
{% if result != None %}
{{ result }}
{% endif %}
<br>
<input type=submit value=calculate >
</form>

</body>
</html>
'''

class InputForm(Form):
    float_field = FloatField(validators=[validators.InputRequired()])
    
@app.route('/', methods=['GET', 'POST'])
def index():
    sine_val = None
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        input_val = form.float_field.data
        sine_val = compute(input_val)
    return render_template_string(page, template_form=form, result=sine_val)

if __name__ == '__main__':
    app.run(debug=True)