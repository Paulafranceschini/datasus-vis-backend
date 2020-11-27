from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS;
from sqlalchemy import create_engine

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:0yEIpgye8jvEd9rq@34.95.217.119:5432/bd-vis"

#app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres+pg8000://postgres:0yEIpgye8jvEd9rq@/tcc-datasus?unix_sock=/cloudsql/tcc-datasus-289918:us-central1:tcc-datasus-postgres/.s.PGSQL.5432'

db = SQLAlchemy(app)

app.config.from_object(__name__)
CORS(app)

db_properties={}
db_properties['url_vis']= "postgresql://postgres:0yEIpgye8jvEd9rq@34.95.217.119:5432/bd-vis"

engine = create_engine(db_properties['url_vis'], echo=True)

from app import views

