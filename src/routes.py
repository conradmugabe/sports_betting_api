from src.response import jsonResponse
from src.middleware import tokenRequired
from flask import Blueprint, json, request
from src.validation import Validation
from src.db import DataBase

api_url = "/api/sportsbetting"
sports = Blueprint('sports', __name__, url_prefix=api_url)

# use this db for now
# DB = 'test.db'

db = DataBase.getInstance(re_init=False)


@sports.route('/create', methods=['POST'])
# @tokenRequired
def createOdds():
    """
    creates an entry in the db
    """
    data = request.get_json()
    validation = Validation(data)
    [validation.check("league"), validation.check("home_team"), validation.check("away_team"), validation.check(
        "home_team_win_odds"), validation.check("away_team_win_odds"), validation.check("draw_odds"), validation.check("game_date")]
    if validation.errors():
        return jsonResponse(status_code=400, error=validation.errors())

    data_created = db.create(data)
    if data_created is None:
        return jsonResponse(status_code=500, error="something went wrong")

    return jsonResponse(status_code=201, data=data_created)


@sports.route('/read', methods=['GET'])
# @tokenRequired
def readOdds():
    """
    Returns all entries in the database
    """
    data = db.read()
    print(data)
    if data is None:
        return jsonResponse(status_code=500, error="something went wrong")

    return jsonResponse(data=data)


@sports.route('/update', methods=['PUT'])
# @tokenRequired
def updateOdds():
    return "update odds"


@sports.route('/delete', methods=['DELETE'])
# @tokenRequired
def deleteOdds():
    data = request.get_json()
    validation = Validation(data)
    [validation.check("league"), validation.check("home_team"), validation.check(
        "away_team"), validation.check("game_date")]
    if validation.errors():
        return jsonResponse(status_code=400, error=validation.errors())

    data = db.delete()
    if data is None:
        return jsonResponse(status_code=500, error="something went wrong")

    return jsonResponse(data=data)
