from flask import Flask
from flask import request
from flask import jsonify
from flask import Flask
app = Flask(__name__)

#$env:FLASK_APP="sample_app.py" flask run --host=0.0.0.0

@app.route('/')
def hello():
    
    return 'whats uppzzz'