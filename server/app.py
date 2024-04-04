#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries', methods=['GET'])
def bakeries():
    bakeries = Bakery.query.all()
    all_bakeries = []
    for bakery in bakeries:
        all_bakeries.append(bakery.to_dict())

    return all_bakeries, 200

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = Bakery.query.filter(Bakery.id == id).first()

    bakery_dict = bakery.to_dict()
    return bakery_dict, 200

    # if bakery == None:
    #     return {"error": "Bakery not found"}, 404
   
    # return bakery.to_dict(), 200
    
    
@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    price_order = BakedGood.query.order_by(BakedGood.price.desc()).all()
    goods_desc = []
    for good in price_order:
        goods_desc.append(good.to_dict())

    return goods_desc, 200

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    price_order = BakedGood.query.order_by(BakedGood.price.desc()).first()
    return price_order.to_dict()

if __name__ == '__main__':
    app.run(port=5555, debug=True)
