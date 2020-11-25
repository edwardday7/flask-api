# Flask API

This is intended to be a multi-purpose API that can be used for multiple functions such as GroupMe Bots, Slack Bots, and frontends. The endpoints in this API will return a plain JSON object, so they can be used with any frontend languages or frameworks of choice. It currently runs in Google Cloud Platform's new serverless container offering, 'Cloud Run' and connects to a Google Cloud SQL database running MySQL.

## Functionality

### GroupMe Bot

The current functionality of the GroupMe Bot allows the user to type in `Food Gamble` and presents them back with a random suggestion for food. Also, users can also type `food search <restaurant query>` which will call the Google Places API and retrieve a restaurant matching the query. For example `Food Search Wings in Atlanta Georgia` returns the name of a wing restaurant in Atlanta with the corresponding address.

## TODOs: 

  - Set up configurations for easier local testing.
  - Endpoints for updating and creating recipes.
  - User creation.
  - Restaurant Roulette allowing a random restaurant to be returned to user based on random latititude and longitude within a certain radius of the user's current location.
