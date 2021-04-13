from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

app=Flask(__name__)
app.debug = True
app.config.from_object(config)

db = SQLAlchemy()
migrate = Migrate()
# ORM
db.init_app(app)
migrate.init_app(app, db)

from .views import main_views,movie_views,shop_views
app.register_blueprint(main_views.bp)
app.register_blueprint(movie_views.bp)
app.register_blueprint(shop_views.bp)

#필터등록
from .filter import Shortword,Replacebar
app.jinja_env.filters['shortword'] = Shortword
app.jinja_env.filters['barhide'] = Replacebar