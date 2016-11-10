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

food = Food.objects
print(food[0].name)

@app.route('/', methods = ["GET", "POST"])
def film():
    if request.method == "GET":
        return render_template("mocha.html", food = Food.objects)
    if request.method == "POST":
        # print(request.form["name"], request.form["email"])
        # user = User(name = request.form["name"], email = request.form["email"])
        food = Food(name=request.form["food_name"], img=request.form["image"], desc=request.form["desc"])
        food.save()
        return render_template('mocha.html', food = Food.objects)

# @app.route('/mocha2', methods = ["GET", "POST"])
# def add():
#     if request.method == "GET":
#
#         return render_template("mocha2.html")
#     elif request.method == "POST":
#         #print(request.form["name"], request.form["email"])
#         #user = User(name = request.form["name"], email = request.form["email"])
#         food = Food(name = request.form["food_name"], img = request.form["image"], desc = request.form["desc"])
#         food.save()
#         return "Thanks for sharing your experience with me, your food might be archived in my foodlist portfolio :D"

if __name__ == '__main__':
    app.run()
