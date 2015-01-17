from flask import Flask
from flask import request, Response
from redis import Redis
import os
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

redis = Redis(host="redis_1", port=6379)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@db/postgres'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username




@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times. \n Databases: %s' % (redis.get('hits'), db)


@app.route('/user')
def get_user():
    users = User.query.all()
    user = users[0]
    return 'User name:%s email: %s' % (user.username, user.email)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

