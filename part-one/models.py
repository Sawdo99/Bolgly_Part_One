"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database"""

    db.app = app
    db.init_app(app)

DEFAULT_IMAGE_URL = "https://img.icons8.com/?size=100&id=7819&format=png&color=000000"


# MODELS --------------------------------------------------------------------------
class User(db.Model):
   
    __tablename__ = "Users"

    id = db.Column(db.Integar, primary_key=True, autoincrement=True)
    first_name = db.Column(db.text, nullable=False)
    last_name = db.Column(db.text, nullable=False)
    image_url = db.Column(db.text, nullable=False, default=DEFAULT_IMAGE_URL)

    @property
    def full_name(self):
        """returns user name"""
        return f"{self.first_name} {self.last_name}"

    def connect_db(app):
        """Connects to db"""

        db.app = app
        db.init_app(app)



