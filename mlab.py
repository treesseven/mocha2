from mongoengine import *

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



