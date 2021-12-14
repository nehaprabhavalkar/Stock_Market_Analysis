from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy  
from wtforms import SelectField
from flask_wtf import FlaskForm
import pandas as pd
import json
import plotly
import plotly.express as px
import os 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

app.config['SECRET_KEY'] = '123'
 
db = SQLAlchemy(app) 

class Sector(db.Model):
    __tablename__ = 'sectors'
  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
  
class Stock(db.Model):
    __tablename__ = 'stocks'
  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    sector_id = db.Column(db.Integer)
 
class Form(FlaskForm):
    sector = SelectField('sector', choices=[])
    stock = SelectField('stock', choices=[])
         
@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()
    form.sector.choices = [(sector.id, sector.name) for sector in Sector.query.all()]

    if request.method == 'POST':
       sector = Sector.query.filter_by(id=form.sector.data).first()
       stock = Stock.query.filter_by(id=form.stock.data).first()
       path = 'C:/Users/DELL/Stock_Market_Analysis/data/' + stock.name + '.csv'
       df = pd.read_csv(path)
       fig = px.line(df, x='date', y='open')
       graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
       return render_template('results.html', graphJSON=graphJSON, stock=stock.name)
       #return '<h1>Sector : {}, Stock: {}</h1>'.format(sector.name, stock.name)
    return render_template('index.html', form=form)
 
@app.route('/stock/<get_stock>')
def stockbysector(get_stock):
    stock = Stock.query.filter_by(sector_id=get_stock).all()
    stock_array = []
    for s in stock:
        stock_obj = {}
        stock_obj['id'] = s.id
        stock_obj['name'] = s.name
        stock_array.append(stock_obj)
    return jsonify({'stocksector' : stock_array})
  
if __name__ == '__main__':
    app.run(debug=True)
