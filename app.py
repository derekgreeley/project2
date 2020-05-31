from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= "postgres://postgres:postgres@localhost:5432/shipwrecks"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db= SQLAlchemy(app)

@app.route('/')
def ships():
    return "this works!"

class shipwrecks (db.Model):
    __tablename__ = 'shipwrecks'
    __table_args__={'extend_existing': True}
    id= db.Column(db.Integer, primary_key=True) 
    name= db.Column(db.Unicode)
    type= db.Column( db.Unicode)
    lat= db.Column(db.Float)
    lon= db.Column(db.Float)
db.create_all()

@app.route('/api/v1.0/pacific')
def pacific():
    return "pacific works!"
class pacific (db.Model):
    __tablename__ = 'pacific'
    __table_args= {'extend_existing': True}
    id= db.Column(db.Unicode, primary_key= True)
    IDNumber= db.Column(db.Unicode)
    stormName= db.Column(db.Unicode)
    stormDate=db.Column(db.Unicode)
    stormTime= db.Column(db.Unicode)
    stormEvent= db.Column(db.Unicode)
    lat= db.Column(db.Float)
    lon=db.Column(db.Float) 
    maximumWind=db.Column(db.Float)
db.create_all()

@app.route('/api/v1.0/atlantic')
def atlantic():
    return "atlantic works!"
class atlantic (db.Model):
    __tablename__ = 'atlantic'
    __table_args= {'extend_existing': True}
    id= db.Column(db.Unicode, primary_key= True)
    IDNumber= db.Column(db.Unicode)
    stormName= db.Column(db.Unicode)
    stormDate=db.Column(db.Unicode)
    stormTime=db.Column(db.Unicode)
    stormEvent=db.Column(db.Unicode)
    lat= db.Column(db.Float)
    lon=db.Column(db.Float)
    maximumWind=db.Column(db.Float)
db.create_all()


if __name__ == '__main__':
    app.debug = True
    app.run()

