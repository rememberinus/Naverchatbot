from flask import Blueprint , render_template , request, url_for, g,flash,request
from werkzeug.utils import redirect
from Bookchat.forms import BookinfoForm
from Bookchat.Naverbookapi import Naverbook
import json

bp = Blueprint('main',__name__,url_prefix='/')

@bp.route('/')
def Main():
    return render_template('base.html')

@bp.route('/bookinfo' , methods=('POST','GET'))
def Bookinfo():
    form = BookinfoForm()

    if request.method == 'POST' and form.validate_on_submit():
        print(form.title.data)
        result =  Naverbook(form.title.data)
        result = json.loads(result)
        return render_template('book_info.html',book_info_list = result['items'], form=form)
        #네이버에서 위의 타이틀에 해당하는 책의 정보를 가져와서 html로 넘겨서 화면에 나오게한다.



    return render_template('book_info.html',form=form)


