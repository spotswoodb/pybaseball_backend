from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
import os

from sqlalchemy import ForeignKey


app = Flask(__name__)
api = Api(app)


POSTGRES_URI = os.environ.get('POSTGRES_URI')

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRES_URI
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Player(db.Model):
    __table__name = 'mlb_player'
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(10))
    birth_country = db.Column(db.String(200))
    weight = db.Column(db.Integer)
    birth_state = db.Column(db.String(200))
    name_display_first_last = db.Column(db.String(200))
    college = db.Column(db.String(200))
    height_inches = db.Column(db.Integer)
    name_display_roster = db.Column(db.String(200))
    sport_code = db.Column(db.String(200))
    bats = db.Column(db.String(10))
    name_first = db.Column(db.String(200))
    team_code = db.Column(db.String(200))
    team_code = db.Column(db.String(10))
    birth_city = db.Column(db.String(200))
    height_feet = db.Column(db.Integer)
    birth_city = db.Column(db.String(200))
    pro_debut_date = db.Column(db.String(200))
    team_full = db.Column(db.String(200))
    team_abbrev = db.Column(db.String(200))
    birth_date = db.Column(db.String(200))
    throws = db.Column(db.String(5))
    league = db.Column(db.String(5))
    name_display_last_first = db.Column(db.String(200))
    position_id = db.Column(db.Integer)
    high_school = db.Column(db.String(200))
    name_use = db.Column(db.String(200))
    player_id = db.Column(db.Integer, foreign_key=True)
    name_last = db.Column(db.String(200))
    team_id = db.Column(db.Integer)
    service_years = db.Column(db.Intger)
    active_sw = db.Column(db.String(5))

    # def __init__(self, position, birth_country, weight, birth_state, name_display_first_last, ):


if __name__ == '__main__':
    app.run()