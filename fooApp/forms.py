from wtforms import Form, TextAreaField, TextField, FloatField, PasswordField
from wtforms.validators import Length, NumberRange, required


class ProductForm(Form):
    name = TextField('Name', [Length(max=255)])
    description = TextAreaField('Description')
    price = FloatField('price', [NumberRange(0.00), required()])


class LoginForm(Form):
    """Render HTML input for user login form.

    Authentication (i.e. password verification) happens in the view function.
    """
    username = TextField('Username', [required()])
    password = PasswordField('Password', [required()])
