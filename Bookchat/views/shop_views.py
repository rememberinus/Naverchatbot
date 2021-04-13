from flask import Blueprint , render_template , request, url_for, g,flash,request
from werkzeug.utils import redirect
from Bookchat.forms import ShopinfoForm,ShopbuyForm
from Bookchat.Navershopapi import Navershop
import json
from ..models import rank,buy
from Bookchat import db
from datetime import datetime

bp = Blueprint('shop',__name__,url_prefix='/shop')


@bp.route('/info' , methods=('POST','GET'))
def shopinfo():
    form = ShopinfoForm()

    if request.method == 'POST' and form.validate_on_submit():
        result = Navershop(form.name.data)
        result = json.loads(result)
        return render_template('shop_info.html', shop_info_lst=result['items'], form=form)
        # 네이버에서 위의 타이틀에 해당하는 책의 정보를 가져와서 html로 넘겨서 화면에 나오게한다.

    return render_template('shop_info.html', form=form)

@bp.route('/buy' , methods=['POST'])
def shopbuy():
    form = ShopbuyForm()
    stitle = request.form['title']
    sbrand = request.form['brand']
    slprice = request.form['lprice']
    simage = request.form['image']

    return render_template('shop_buy.html',stitle=stitle,sbrand=sbrand,slprice=slprice,
                           simage=simage,form=form)

@bp.route('/buysave' , methods=['POST'])
def buysave():
    title = request.form['title']
    brand = request.form['brand']
    price = request.form['lprice']
    image = request.form['image']
    address = request.form['address']


    btemp =  buy(title=title, brand=brand, lprice=price, image=image,
                 address=address, buy_date=datetime.now())
    db.session.add(btemp)
    db.session.commit()
    return '상품구매를 완료하였습니다.'