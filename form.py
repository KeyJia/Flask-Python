from flask.ext.wtf import Form
from  wtforms import StringField,PasswordField

from wtforms.validators import DataRequired

class LoginForm(Form):
    username =