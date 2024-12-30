"""Blogly application."""

from flask import Flask
from models import db, connect_db
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET!"

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route("/")
def root():
    """Homepage redirects to list of users"""

    return redirect("/users")

# User Route --------------------------------------------------------------------------

#List all users
@app.route('/users')
def users_index():
    
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template(users/index.html, users=users)

# Show details
@app.route('/users', method=["GET"])
def users_details():
    return render_template("details.html")


# Add new user
@app.route('/users', methods=["GET"])
def new_user_form():
    return render_template('new.html')

#Process added user
@app.route('/users/new', methods=['POST'])
def add_user():
    new_id = max(users.keys()) + 1 if users else 1
    name = request.form['name']
    users[new_id] = {"name": name}
    return redirect('/users')
#show user
@app.route('/users/<int:user_id>')
def users_show(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('users/show.html', user=user)

#Edit user
@app.route('/users/<int:user_id>/edit')
def users_edit(user_id):
    
    user = User.query.get_or_404(user_id)
    return render_template('users/edit.html', user=user)

#process edited user
@app.route('/users/<int:user_id>/edit', methods=["POST"])
def users_update(user_id):

    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect("/users")

#Processing deleting user
@app.route('/users/<int:user_id>/delete', methods=["POST"])
def users_destroy(user_id):

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")