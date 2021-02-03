# swagger-client
Vipps Signup API enables a partner to initiate Vipps onboarding process on behalf of a merchant. The merchant needs to complete Vipps signup form to sign the merchant agreement with Vipps. After the signup form has been processed, Vipps will send the API keys to the defined callback endpoint. In order to complete the integration there is a need to: 1. Initiate the Signup to the Initiate endpoint 2. Accept the callback sent to the callback endpoint 3. Return a 202 response to acknowledge that the callback has been accepted.  

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.1.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SignupApi(swagger_client.ApiClient(configuration))
body = swagger_client.PartialSignup() # PartialSignup | partialSignup

try:
    # Create a signup
    api_response = api_instance.partial_signup(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignupApi->partial_signup: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.vippsbedrift.no*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*SignupApi* | [**partial_signup**](docs/SignupApi.md#partial_signup) | **POST** /v1/partial/signup | Create a signup
*SignupCallbackApi* | [**callback**](docs/SignupCallbackApi.md#callback) | **POST** /signupcallbackURL | Sent Callback

## Documentation For Models

 - [CallbackTriggerResponse](docs/CallbackTriggerResponse.md)
 - [PartialSignup](docs/PartialSignup.md)
 - [PartialSignupResponse](docs/PartialSignupResponse.md)
 - [SubscriptionKeys](docs/SubscriptionKeys.md)
 - [SubscriptionKeysInner](docs/SubscriptionKeysInner.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

