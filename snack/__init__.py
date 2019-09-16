from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from snack.config import DevConfig

app=Flask(__name__)
app.config.from_object(DevConfig)

db=SQLAlchemy(app)

from snack import routes


