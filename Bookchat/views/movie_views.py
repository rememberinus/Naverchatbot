from flask import Blueprint , render_template , request, url_for, g,flash,request
from werkzeug.utils import redirect
from Bookchat.forms import MovieinfoForm
from Bookchat.Navermovieapi import Navermovie,Movierank
import json
from ..models import rank

bp = Blueprint('movie',__name__,url_prefix='/movie')


@bp.route('/info' , methods=('POST','GET'))
def Movieinfo():
    form = MovieinfoForm()

    if request.method == 'POST' and form.validate_on_submit():
        print(form.title.data)
        result =  Navermovie(form.title.data)
        result = json.loads(result)
        return render_template('movie_info.html',movie_info_lst = result['items'], form=form)
        #네이버에서 위의 타이틀에 해당하는 책의 정보를 가져와서 html로 넘겨서 화면에 나오게한다.


    return render_template('movie_info.html',form=form)


@bp.route('/rank')
def Getmovierank():

    data = rank.query.all()
    print('-----------',data)

    data_list = []
    for temp in data:
        data_list.append(temp.title)

    movierank = Movierank()


    return render_template('movie_rank.html',movie_rank_lst=data_list)
