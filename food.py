from mlab import *

class Food(Document):
    img = StringField()
    name = StringField()
    desc = StringField()

