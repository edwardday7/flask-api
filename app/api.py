import datetime
import jwt
from flask import request, make_response, jsonify
from functools import wraps
from app import app

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Token needs to be passed in header as 'x-access-token'
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        # Make sure it was a valid token
        try:
            data = jwt.decode(token, 'secret')
            user = data['username']
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(user, *args, **kwargs)
    return decorated
        
@app.route('/recipes', methods=['GET'])
@token_required
def recipes(user):
    
    if user != 'admin':
        return jsonify({'message': 'Not Authorized!'}), 403

    return jsonify({'name' : 'Sausage Dip', 'description' : 'Instructions'}), 200


@app.route('/login', methods=['GET'])
def login():
    # 'auth' contains both username and password passed in header.
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if auth.username != 'username' and auth.password != 'password':
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Credentials invalid!"'})

    # Username and Password are supplied. Create jwt and return to client
    token = jwt.encode({'username' : 'admin', 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 'secret', algorithm='HS256')

    return jsonify({'token' : token.decode('UTF-8')}), 200