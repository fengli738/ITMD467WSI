from flask import Flask
from werkzeug.security import check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

app = Flask(__name__)
#mysql+pymysql://(username):password@127.0.0.1:3306/(databasename)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:qwasqwas2271@127.0.0.1:3306/artcms"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


class User(db.Model):
    try:
     __tablename__ = "user"
     id = db.Column(db.Integer, primary_key=True)
     username = db.Column(db.String(20), nullable=False)
     password = db.Column(db.String(150), nullable=False)
     addtime = db.Column(db.DateTime, nullable=False)
    except Exception as e:
        print(e)

    def __repr__(self):
        return "<User %r>" % self.name

    def check_password(self, password):
        try:
         return check_password_hash(self.password, password)
        except Exception as e:
         print(e);




class Article(db.Model):
    try:
     __tablename__ = "article"
     id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String(50), nullable=False)
     category = db.Column(db.Integer, nullable=False)
     user_id = db.Column(db.Integer, nullable=False)
     logo = db.Column(db.String(100), nullable=False)
     content = db.Column(db.Text, nullable=False)
     addTime = db.Column(db.DateTime, nullable=False)
    except Exception as e:
        print(e)

    def __repr__(self):
        return "<Art %r>" % self.title


if __name__ == "__main__":
    db.create_all()
