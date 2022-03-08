from flask import Flask
# from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRES_URI
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)