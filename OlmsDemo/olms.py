from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///olms.db"
db = SQLAlchemy(app)


class Course(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    duration_in_month = db.Column(db.Integer(), nullable=False)
    payment = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Course {self.name}'

@app.route("/")
@app.route("/home")
def home():
    """ simply return hello world """
    return render_template("home.html")


@app.route("/enrollment")
def enroll():
    """ returns the enrollment details """
    courses = Course.query.all()
    return render_template("enroll.html", courses=courses)
