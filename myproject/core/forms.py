from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, TextField
from wtforms.validators import DataRequired, Email
from flask_login import current_user

class SendEmailForm(FlaskForm):
    sender_email = StringField("Email: ", validators=[Email(), DataRequired()])
    receiver_email = StringField("Email: ", validators=[Email(), DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    subject = TextField("Subject", validators=[DataRequired()])
    body = TextAreaField("Body", validators=[DataRequired()])
    submit = SubmitField("Send")
