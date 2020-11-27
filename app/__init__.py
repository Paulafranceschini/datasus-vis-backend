from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS;
from sqlalchemy import create_engine

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
pw = os.environ['DB_PW']
url = os.environ['DB_URL']
db  = os.environ['DB_DB']
db_user  = os.environ['DB_USER']

uri = "postgresql://" + db_user + ":"  + pw + "@" + url + db; 
app.config["SQLALCHEMY_DATABASE_URI"] = uri

db = SQLAlchemy(app)

app.config.from_object(__name__)
CORS(app)

db_properties={}
db_properties['url_vis'] =uri

engine = create_engine(db_properties['url_vis'], echo=True)

from app import views

