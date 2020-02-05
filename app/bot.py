import os
import json
import random
import googlemaps
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import request, jsonify
from app import app


bot_id = "BOT ID HERE"
gmaps = googlemaps.Client(key='API KEY HERE')

################################################################################
#                                 FOOD BOT                                     # 
################################################################################

# URL receives a POST request every time a message is sent 
# in GroupMe that checks for specific message text.
@app.route('/food/bot', methods=['POST'])
def webhook():
    # 'message' is an object that represents a single GroupMe message.
    message = request.get_json()

    food_list = ['JR. Crickets Wings', 'Whole Foods Bar', 'Popeyes Sandwich', 'Cook Something', 'Five Guys']

    # If client wants to search for food instead of random food
    if 'food search' in message['text'].lower() and not sender_is_bot(message):
        query = message['text'].lower().replace("food search", "")
        result = gmaps.find_place(query, 'textquery', 
                                fields=['formatted_address', 'name'])
        for details in result['candidates']:
            reply('Here is what your search returned:\n\n' + details['name'] + '\n' + details['formatted_address'])
    elif 'food gamble' in message['text'].lower() and not sender_is_bot(message): # if message contains 'what should i eat'
        reply('Your food suggestion is: ' + random.choice(food_list))

    return "ok", 200

# Healthcheck for bot
@app.route('/food/health', methods=['GET'])
def healthcheck():
	return jsonify({'status' : 'Healthy'}), 200

# Send a message in the groupchat
def reply(msg):
	url = 'https://api.groupme.com/v3/bots/post'
	data = {
		'bot_id'		: bot_id,
		'text'			: msg
	}
	request = Request(url, urlencode(data).encode())
	json = urlopen(request).read().decode()

# Checks whether the message sender is a bot. 
# Not including causes infinite loop
def sender_is_bot(message):
	return message['sender_type'] == "bot"
