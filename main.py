from flask import Flask, render_template

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Length,  Email
from flask_bootstrap import Bootstrap5  # pip install bootstrap-flask



'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(message='Email is required.'), Email(message='That\'s not a valid email address.'), Length(min=6, max=35, message='Email must be between 6 and 35 characters long.')])
    password = PasswordField(label='Password', validators=[DataRequired(message='Password is required.'), Length(min=8, message='Password must be at least 8 characters long.')])
    submit = SubmitField(label='Log In')

app = Flask(__name__)

app.secret_key = "sdfaKKd0asdfjafds34"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()

    
    if form.validate_on_submit():
        # Process the form data
        print(form.email.data)
        if form.email.data=="admin@email.com" and form.password.data=="12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)
    
    


if __name__ == '__main__':
    app.run(debug=True)
