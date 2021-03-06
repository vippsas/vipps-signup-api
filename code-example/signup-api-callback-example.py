# A simple example for the Vipps Signup API:
# Handle incoming callbacks from Vipps when a merchant has signed.
# https://github.com/vippsas/vipps-signup-api

# Flask: https://flask.palletsprojects.com/en/1.1.x/
from flask import Flask, request

# Create the Flask app
app = Flask(__name__)

# Handle incoming POST requests to the URL specified in the original POST to Vipps.
@app.route('/vipps-signup-api/vipps-signup-callback', methods=['POST'])
def vipps_signup_callback():
    content = request.get_json()
    print(content)
    # TODO:
    # Verify the signupCallbackToken: content['signupCallbackToken'].
    # Do your processing.

# Run
if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)
