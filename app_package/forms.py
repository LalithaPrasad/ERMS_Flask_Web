from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    username=StringField("Username: ", validators=[DataRequired()])
    password=PasswordField("Password: ", validators=[DataRequired()])
    submit=SubmitField("Sign in")

class RegistrationForm(FlaskForm):
    username=StringField("Usernname: ", validators=[DataRequired()])
    password=PasswordField("Password: ", validators=[DataRequired()])
    password2=PasswordField("Repeat password: ", validators=[DataRequired(),
        EqualTo('password')])
    submit=SubmitField("Register")

class AddEmployeeForm(FlaskForm):
    name=StringField("Name: ", validators=[DataRequired()])
    age=IntegerField("Age: ", validators=[DataRequired()])
    ed=StringField("Education: ", validators=[DataRequired()])
    role=StringField("Role: ", validators=[DataRequired()])
    submit=SubmitField("Add Employee")

class DeleteEmployeeForm(FlaskForm):
    id=IntegerField("Id of employee to be deleted: ",
            validators=[DataRequired()])
    submit=SubmitField("Delete Employee")

class ModifyEmployeeForm(FlaskForm):
    id=IntegerField("Id of employee to be modified: ",
            validators=[DataRequired()])
    ed=StringField("Education: ")
    role=StringField("Role: ")
    submit=SubmitField("Modify Employee")
