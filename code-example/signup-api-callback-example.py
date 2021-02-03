# A simple example for the Vipps Signup API:
# Handle incoming callbacks from Vipps when a merchant has signed.
# https://github.com/vippsas/vipps-signup-api

from flask import Flask, request

# Create the Flask app
app = Flask(__name__)

@app.route('/vipps-signup-api/vipps-signup-callback', methods=['POST'])
def json_example():
    return 'JSON Object Example'
