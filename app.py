from flask import Flask, render_template, g, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from flask_mysqldb import MySQL
import os
app = Flask(__name__)

# food
app.config['MYSQL_USER'] = os.environ.get('FOODAPP_USER')
# 'food123.'
app.config['MYSQL_PASSWORD'] = os.environ.get('FOODAPP_PASSWORD')
# 'localhost'
app.config['MYSQL_HOST'] = os.environ.get('FOODAPP_HOST')
# 'foodDB'
app.config['MYSQL_DB'] = os.environ.get('FOODAPP_DB')
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


mysql = MySQL(app)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "FoodAPI"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###


def executeSelect(sqlQuery):
    cur = mysql.connection.cursor()
    cur.execute(sqlQuery)
    rowsSelected = cur.fetchall()
    cur.close

    return rowsSelected


# def executeInsert(sqlQuery):
#     cur = mysql.connection.cursor()
#     cur.execute(sqlQuery)
#     cur.commit()
#     cur.close

#     return cur


@app.route('/')
def index():
    results = executeSelect('''SELECT * FROM foods''')
    if results:
        print(results)
    else:
        print('Nothing to see here')

    return 'DONE'


@app.route('/view', methods=['GET', 'POST'])
def view():
    return None


@app.route('/food', methods=['GET', 'POST'])
def food():
    return None


if __name__ == '__main__':
    app.run(debug=True)
