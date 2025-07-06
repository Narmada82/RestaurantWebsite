from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,DateField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,optional,EqualTo 






class SignupForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(),Length(4,15)]
    )
    email = StringField(
        "Email",
        validators=[DataRequired(),Email()]
    )
    gender = SelectField(

        "Gender",
        choices=["male","female","other"],
        validators=[optional()]
    )

    dob = DateField(
        "Date Of Birth",
        validators=[DataRequired()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired(),Length(5,18)]
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired(),Length(5,18),EqualTo("password")]
    )

    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):

        
    email = StringField(
        "Email",
        validators=[DataRequired(),Email()]
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(),Length(5,18)]
    )

    remember = BooleanField(
        "Remember Me",
        
    )

    submit = SubmitField("Login")