from flask import Flask,jsonify
from flask_restful import Api
from Resources.MainResource import LongShort, ShortLong

app = Flask(__name__)
api = Api(app)
app.secret_key = 'anykey'

app.config['PROPAGATE_EXCEPTIONS'] = True

api.add_resource(LongShort, '/')
api.add_resource(ShortLong, '/ShortLong')


app.run(debug=True)
