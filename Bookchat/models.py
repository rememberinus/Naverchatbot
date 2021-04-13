from Bookchat import db

class rank(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)

class buy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    brand = db.Column(db.String(200), nullable=False)
    lprice = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(200), nullable=True)
    address = db.Column(db.String(200), nullable=False)
    buy_date = db.Column(db.DateTime(), nullable=False)
