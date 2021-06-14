from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:quachtinh95@localhost:3306/flask_restful_api'
db = SQLAlchemy(app)
ma = Marshmallow(app)

if __name__ == "__main__":
    app.run(debug=True)

print('test')
print(db)

class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    specialisation = db.Column(db.String(50))
    def __init__(self, name, specialisation):
        self.name = name
        self.specialisation = specialisation
    def __repr__(self):
      return '<Product %d>' % self.id
db.create_all()


class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Authors
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    specialisation = fields.String(required=True)


@app.route('/authors', methods = ['GET'])
def index():
    get_authors = Authors.query.all()
    author_schema = AuthorSchema(many=True)
    # authors, error = author_schema.dump(get_authors)
    return make_response(jsonify({"authors": []}))
