# Flask API

This is intended to be a multi-purpose API that can be used for multiple functions such as GroupMe Bots, Slack Bots, and frontends. The endpoints in this API will return a plain JSON object, so they can be used with any frontend languages or frameworks of choice. It currently runs in Google Cloud Platform's new serverless container offering, 'Cloud Run'.

## Authentication

This API is secured using JSON Web Tokens (JWT). Upon authenticating with the login endpoint, the client will receive a JWT and can authenticate in subsequent requests by passing this token in the header as `x-access-token`. 

## Functionality

### GroupMe Bot

The current functionality of the GroupMe Bot allows the user to type in `Food Gamble` and presents them back with a random suggestion for food. Also, users can also type `food search <restaurant query>` which will call the Google Places API and retrieve a restaurant matching the query. For example `Food Search Wings in Atlanta Georgia` returns the name of a wing restaurant in Atlanta with the corresponding address.

### API Routes

Currently, the API is set up just for granting a JWT for a client. There is one route that returns sample data for testing the functionality/success of the JWT auth. More to come for this.

## TODOs: 

  - Authenticate users from DB (Google Cloud SQL).
  - Break out api file into multiple files to gain ability for better local testing and configurations.
  - Secure passwords in code by utilizing secure password store such as Hashicorp Vault.
  - Restaurant Roulette allowing a random restaurant to be returned to user based on random latititude and longitude within a certain radius of the user's current location.
