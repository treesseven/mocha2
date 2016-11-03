from flask import *
from mongoengine import *

app = Flask(__name__)

db_name = "treesseven"
host = "ds021915.mlab.com"
port = 21915
user_name = "admin"
password = "admin"

connect(db_name,
        host=host,
        port=port,
        username=user_name,
        password=password)

class Food(Document):
    name = StringField()
    img = StringField()
    desc = StringField()

class User(Document):
    name = StringField()
    email = StringField()
    food = EmbeddedDocumentField("Food")

@app.route('/')
def film():
    return render_template('mocha.html')

@app.route('/mocha2', methods = ["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("mocha2.html")
    elif request.method == "POST":
        #print(request.form["name"], request.form["email"])
        user = User(name = request.form["name"], email = request.form["email"])
        user.food = Food(name = request.form["food_name"], img = request.form["image"], desc = request.form["desc"])
        user.save()
        return "Thanks for sharing your experience with me, your food might be archived in my foodlist portfolio :D"

if __name__ == '__main__':
    app.run()
