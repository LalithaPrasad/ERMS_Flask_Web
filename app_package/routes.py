from flask import render_template, flash, redirect, url_for, session
from app_package import app, db
from app_package.forms import LoginForm, RegistrationForm
from app_package.forms import AddEmployeeForm, DeleteEmployeeForm
from app_package.forms import ModifyEmployeeForm
from app_package.models import Admin, Employee
from app_package import auth

@app.route("/", methods=["GET", "POST"])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        admin=Admin.query.filter_by(username=form.username.data).first()
        if admin is None or not admin.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        else:
            session["token"]=admin.get_token()
            return redirect(url_for("menu"))
    else:
        return render_template("login.html", title="Login", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    admin=Admin.query.get(1)
    if admin:
        flash("Admin already registered. Only one admin can exist");
        return redirect(url_for("login"))
    else:
        form=RegistrationForm()
        if form.validate_on_submit():
            admin=Admin(username=form.username.data)
            admin.set_password(form.password.data)
            db.session.add(admin)
            db.session.commit()
            flash("Admin registered. You may login now")
            return redirect(url_for("login"))
        else:
            return render_template("register.html", title="Register", form=form)

@app.route("/logout")
def logout():
    if "token" in session:
        session.pop("token")
    return redirect(url_for("login"))

@app.route("/menu")
@auth.valid_token
def menu():
    return render_template("menu.html")

@app.route('/display_all_employees')
@auth.valid_token
def display_all_employees():
    employees=Employee.query.all()
    if employees:
        return render_template("display_employees.html", title="Display employees", employees=employees)
    else:
        return render_template("no_employees.html", title="No employees")

@app.route('/add_employee', methods=['GET', 'POST'])
@auth.valid_token
def add_employee():
    form=AddEmployeeForm()
    if form.validate_on_submit():
        employee=Employee(name=form.name.data, age=form.age.data, ed=form.ed.data,
                role=form.role.data)
        db.session.add(employee)
        db.session.commit()
        flash("Employee added")
        return redirect(url_for('menu'))
    else:
        return render_template("add_employee.html", title="Add employee", form=form)

@app.route('/delete_employee', methods=['GET', 'POST'])
@auth.valid_token
def delete_employee():
    form=DeleteEmployeeForm()
    if form.validate_on_submit():
        employee=Employee.query.filter_by(id=form.id.data).first()
        db.session.delete(employee)
        db.session.commit()
        flash("Employee deleted")
        return redirect(url_for("menu"))
    else:
        return render_template("delete_employee.html", title="Delete employee", form=form)

@app.route('/modify_employee', methods=['GET', 'POST'])
@auth.valid_token
def modify_employee():
    form=ModifyEmployeeForm()
    if form.validate_on_submit():
        employee=Employee.query.filter_by(id=form.id.data).first()
        if form.ed.data!="": employee.ed=form.ed.data
        if form.role.data!="": employee.role=form.role.data
        db.session.commit()
        flash("Employee modified")
        return redirect(url_for("menu"))
    else:
        return render_template("modify_employee.html", title="Modify employee", form=form)
