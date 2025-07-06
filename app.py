from flask import Flask, render_template, redirect, url_for, flash, request
from forms import LoginForm, SignupForm
from flask_sqlalchemy import SQLAlchemy # type: ignore

app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://neondb_owner:npg_OFgDGMz0L8QE@ep-curly-glitter-a84a9h5j-pooler.eastus2.azure.neon.tech/neondb?sslmode=require&channel_binding=require'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "1q2w3e4r5t6y"


db = SQLAlchemy(app)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    message = db.Column(db.Text)


with app.app_context():
    db.create_all()

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/chief")
def chef():
    return render_template("chef.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        new_msg = Contact(name=name, email=email, message=message)
        db.session.add(new_msg)
        db.session.commit()

        flash("Message sent successfully!")
        return redirect(url_for("home"))

    return render_template("contact.html")

@app.route("/reserve", methods=['GET', 'POST'])
def reserve():
    if request.method == 'POST':
        name = request.form['name']
        date= request.form['date']
        time=request.form['time']
        table = request.form['table']
        flash(f'Dear {name} A Table Is Booked On {date} At {time} For {table} Persons')
        return redirect(url_for('home'))
    return render_template('reserve.html')

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/location")
def location():
    return render_template("location.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    email = form.email.data
    pw = form.password.data
    if form.validate_on_submit():
        flash("Login Successfully !")
        return redirect(url_for("home"))
    return render_template("login.html", title="LOGIN", form=form)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f"Successfully Registered {form.username.data}")
        return redirect(url_for("home"))
    return render_template("signup.html", title="SIGNUP", form=form)


if __name__ == "__main__":
    app.run(debug=True)
