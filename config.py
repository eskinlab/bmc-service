# config.py

import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
basedir = pathlib.Path(__file__).parent.resolve()
connex_app = connexion.App(__name__, specification_dir=basedir)
connex_app.add_api("swagger.yml")

DB_NAME = "titanic.db"
app = connex_app.app
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / DB_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)
use_sql = False
