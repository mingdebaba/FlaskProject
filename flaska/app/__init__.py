from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#创建app应用,__name__是python预定义变量，被设置为使用本模块.
app = Flask(__name__)
#如果你使用的IDE，在routes这里会报错，因为我们还没有创建呀，为了一会不要再回来写一遍，因此我先写上了
app.config.from_object(Config)

#建立数据库关系
db = SQLAlchemy(app)
#绑定app和数据库，以便进行操作
migrate = Migrate(app,db)

from app import routes,models

