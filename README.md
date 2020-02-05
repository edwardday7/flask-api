# Flask API

This is intended to be a multi-purpose API that can be used for multiple functions such as GroupMe Bots, Slack Bots, and frontends. The endpoints in this API will return a plain JSON object, so they can be used with any frontend languages or frameworks of choice. It currently runs in Google Cloud Platform's new serverless container offering, 'Cloud Run'.

## Authentication

This API is secured using JSON Web Tokens (JWT). Upon authenticating with the login endpoint, the client will receive a JWT and can authenticate in subsequent requests by passing this token in the header as `x-access-token`. 

## TODOs: 

  - Authenticate users from DB (Google Cloud SQL).
  - Break out api file into multiple files to gain ability for better local testing and configurations.
  - Secure passwords in code by utilizing secure password store such as Hashicorp Vault.
  - Allow Bot users to specify current location and use Google Places API to present closest restaurants.
