from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField , PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import  DataRequired,Length,EqualTo,Email

class BookinfoForm(FlaskForm):
    title=StringField('책제목',validators=[DataRequired()])

class MovieinfoForm(FlaskForm):
    title=StringField('영화제목',validators=[DataRequired()])

class ShopinfoForm(FlaskForm):
    name=StringField('상품이름',validators=[DataRequired()])

class ShopbuyForm(FlaskForm):
    address=StringField('주소',validators=[DataRequired()])
