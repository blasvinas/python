import os
from flask import Flask, g  #g is the global object
import sqlite3

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))  #Get the current path

#Simple route funtion
@app.route('/')
def index():
    return '<h1>Hello World</h1>'

def connect_db():
    sql = sqlite3.connect(os.path.join(basedir, 'data.db'))
    sql.row_factory = sqlite3.Row  #Return rows as a dictionary
    return sql

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext  #Call after each route finish
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/viewresults')
def viewresutls():
    db = get_db()
    cur = db.execute('select id, name, location from users')
    results = cur.fetchall()
    return f"<h1>The ID is {results[0]['id']}.  Tha name is {results[0]['name']}. The location is {results[0]['location']}.</h1>"