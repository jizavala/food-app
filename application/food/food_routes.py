from application import db
from . import food_bp
from flask import Blueprint, jsonify, request

""" Utilities """


def getInsertQuery():
    sqlQuery = """INSERT
                    INTO foodDB.foods(name, carbohydrate, protein, fat, calories)
                  VALUES ('{}', {}, {}, {}, {}){}"""

    return sqlQuery


def getUpdateQuery():
    sqlQuery = """UPDATE foodDB.foods
                     SET name = '{}',
                         carbohydrate = {},
                         protein = {},
                         fat = {},
                         calories = {}
                   WHERE id = {}"""

    return sqlQuery


def getSaveQuery(isUpdate=True):
    sqlQuery = getUpdateQuery() if isUpdate else getInsertQuery()

    print(sqlQuery)

    return sqlQuery


def getSearchQueryByOption(option, data):
    principalQuery = '''SELECT *
                          FROM foodDB.foods AS f
                     '''
    if option is None and data is None:
        return principalQuery

    principalQuery += ' WHERE {}'.format(
        getWhereSentence(option)).format(option, data)

    principalQuery.format(option, data)

    return principalQuery


def getWhereSentence(option):
    whereSentence = " 1 = 1 "

    if option == 'name':
        whereSentence = "f.{} LIKE '%{}%'"
    elif option == 'id':
        whereSentence = "f.{} = {}"
    else:
        whereSentence = "f.{} >= {}"

    return whereSentence


def executeQuery(sqlQuery, isSave=False):
    cur = db.connection.cursor()
    affectedRows = cur.execute(sqlQuery)

    if isSave:
        db.connection.commit()
        data = affectedRows > 0
    else:
        data = cur.fetchall()

    cur.close

    return data


""" Routes """


@food_bp.route('/food/save', methods=['POST'])
def save():
    requestContent = request.get_json()

    idFood = requestContent["id"] if "id" in requestContent else -1
    name = requestContent["name"]
    carbs = requestContent["carbohydrates"]
    protein = requestContent["protein"]
    fat = requestContent["fat"]
    # calories = cabs * 4 + protein * 4  + fat * 9
    calories = (4 * (carbs + protein)) + (fat * 9)

    sqlQuery = getSaveQuery(idFood > 0).format(name, carbs,
                                               protein, fat, calories,
                                               idFood if idFood > 0 else '')

    print(sqlQuery)
    response = executeQuery(sqlQuery, True)
    print(response)

    return jsonify({'response': response})


@food_bp.route('/food/getAll', methods=['GET'])
def getAll():

    response = executeQuery(getSearchQueryByOption(None, None))

    if len(response) == 0:
        response = "False"

    return jsonify({
        'request': request.get_json() if request.is_json else "No Request Data",
        'response': response
    })


@food_bp.route('/food/getFood/<optionToSearch>/<searchOptions>', methods=['GET'])
def getFoodBy(optionToSearch, searchOptions):

    data = optionToSearch
    options = searchOptions

    return jsonify({
        'response': executeQuery(getSearchQueryByOption(options, data))
    })


# @food_bp.route('/food/getFood/<id>', methods=['GET'])
# def getFoodById(idFood):
#     data = idFood

#     return
