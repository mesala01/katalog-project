from flask import Flask, render_template, redirect, session, g
from forms import SignupForm, LoginForm
from models import db, connect, Users


app = Flask(__name__)
connect(app)
app.config['SECRET_KEY'] = '\xa6\x9f\xd7\x85X\xe9\x01\x12\x17\xa8\x1c\xdafL[\xadlL\x93Gc\xed\xd2w'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres:///salesman"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db.create_all()

CURR_USER_KEY = "current_user"
@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = Users.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.userID


def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]
        del g.user





@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    """
        get the sign up form and add new user to DB.
    """
    form = SignupForm()
    if form.validate_on_submit():
        user = Users.signup(form.name.data, form.email.data, form.password.data)
        do_login(user)
        add_user_to_g()
        print(g.user.fullname)
        return redirect('/')
    return render_template("register.html", form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user= Users.login(form.email.data, form.password.data)
        do_login(user)
        add_user_to_g()
        return redirect('/')
    return render_template("login.html", form = form)

@app.route('/cart')
def cart():
    return render_template("cart.html")

@app.route('/logout')
def logout():
    if session["current_user"]:
        del session["current_user"]
        g.user = None
    return redirect('/')


    
