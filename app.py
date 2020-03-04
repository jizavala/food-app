from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return None

@app.route('/view')
def view()
    return render_template('day.html')

@app.route('/food')
    return render_template('add_food.html')

if __name__ == '__main__':
    app.run(debug=True)