# Flask API

This is intended to be a multi-purpose API that can be used for multiple functions such as GroupMe Bots, Slack Bots, and frontends. The endpoints in this API will return a plain JSON object, so they can be used with any frontend languages or frameworks of choice. It currently runs in Google Cloud Platform's new serverless container offering, 'Cloud Run' and connects to a Google Cloud SQL database running MySQL.

## Functionality

### GroupMe Bot

The current functionality of the GroupMe Bot allows the user to type in `Food Gamble` and presents them back with a random suggestion for food. Also, users can also type `food search <restaurant query>` which will call the Google Places API and retrieve a restaurant matching the query. For example `Food Search Wings in Atlanta Georgia` returns the name of a wing restaurant in Atlanta with the corresponding address.

### API Routes

Currently, the long term plan is to build a separate frontend that allows a user to add, delete, and view recipes. I have a recipe book that my mother made for me with all sorts of recipes, but I have a tough time keeping up with it, and would also like access to its recipes anywhere I go. Even though there are websites out there that offer this sort of functionality, I wanted to build my own version as a learning experience. These endpoints are built with this end goal in mind.

```
https://api.edwarddayvii.com/login [POST] - Returns a JWT with a 30 minute expiration. Must authenticate using basic auth.
https://api.edwarddayvii.com/recipes/ingredients [GET] - Returns JSON with all recipes and corresponding ingredients for a specific user.
https://api.edwarddayvii.com/recipes/{recipeId}/ingredients [GET] - Returns JSON with recipe and corresponding ingredients for a specific user and recipe ID.
https://api.edwarddayvii.com/ingredients [GET] - Returns JSON with all ingredients in database.
https://api.edwarddayvii.com/recipes [GET] - Returns JSON with all recipes for the specific user in the database.
https://api.edwarddayvii.com/recipetest [GET] - Returns test JSON. Doesn't call database.
https://api.edwarddayvii.com/food/health [GET] - Check the status of the food bot.
```
### Authentication

To use the above endpoints, user must obtain a JWT from the `/login` endpoint. User must provide Basic Auth with the correct username and password to obtain a JWT. All subsequent calls must include the JWT in the header as `x-access-token`. 

## TODOs: 

  - Set up configurations for easier local testing.
  - Endpoints for updating and creating recipes.
  - User creation.
  - Restaurant Roulette allowing a random restaurant to be returned to user based on random latititude and longitude within a certain radius of the user's current location.
