from flask import render_template
from app import app
from models.list_orders import orders

@app.route('/')
def index():
    return render_template('index.html', title="Order List", orders=orders)