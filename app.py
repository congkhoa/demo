from flask import Flask
from redis import Redis
import os
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

redis = Redis(host="redis_1", port=6379)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgressql://root:my_pass@db/my_db'
db = SQLAlchemy(app)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times. \n Databases: %s' % (redis.get('hits'), db)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


