import datetime
import jwt
import sqlalchemy
import bcrypt
from flask import request, make_response, jsonify
from functools import wraps
from app import app, db

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
            data = jwt.decode(token, app.config['SECRET_KEY'])
            stmt = sqlalchemy.text(
                "SELECT UserID FROM Users WHERE UserID=:user_id"
            )
            with db.connect() as conn:
                user = conn.execute(stmt, user_id=data['user_id'])
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(user, *args, **kwargs)
    return decorated

@app.route('/ingredients', methods=['GET'])
@token_required
def ingredients(user):

    ingredients = []
    with db.connect() as conn:
        # Execute the query and fetch all results
        result = conn.execute(
            "SELECT * FROM Ingredients"
        ).fetchall()
    for item in result:
        ingredients.append({'Ingredient': item['IngredientName'],
                            'Quantity' : item['Quantity'],
                            'Unit' : item['Unit']})

    return jsonify(ingredients), 200
        
@app.route('/recipetest', methods=['GET'])
@token_required
def recipe_test(user):

    return jsonify({'name' : 'Sausage Dip', 'description' : 'Instructions'}), 200


@app.route('/login', methods=['GET'])
def login():
    # 'auth' contains both username and password passed in header.
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    stmt = sqlalchemy.text(
        "SELECT UserID, Password FROM Users WHERE Username=:username"
    )

    with db.connect() as conn:
        user = conn.execute(stmt, username=auth.username)
    
    # If no user match in the DB
    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Credentials invalid!"'})
    
    row = user.fetchone()
    user_id = row[0]
    password = row[1]

    if bcrypt.checkpw(auth.password.encode('utf-8'), password.encode('utf-8')):
        # Username and Password are valid. Create jwt and return to client
        token = jwt.encode({'user_id' : user_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token' : token.decode('UTF-8')}), 200

    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Credentials invalid!"'})