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
    __tablename__ = 'shipwreck3'
    __table_args__={'extend_existing': True}

    recrd= db.Column(db.Integer, primary_key=True) 
    vessel_terms= db.Column(db.Unicode)
    feature_type= db.Column( db.Unicode)
    latdec= db.Column(db.Integer)
    londec= db.Column(db.Integer)
    gp_quality= db.Column(db.Unicode)
    water_depth= db.Column(db.Integer)
    sounding_type= db.Column(db.Unicode)
    yearsunk= db.Column(db.Unicode)
    history= db.Column(db.Unicode)
db.create_all()


if __name__ == '__main__':
    app.debug = True
    app.run()

