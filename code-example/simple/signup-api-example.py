# A simple example for the Vipps Signup API
# https://github.com/vippsas/vipps-signup-api

import requests
import json

# The URL for the partner to POST the data to:
url = "https://api-test.vippsbedrift.no/v1/partial/signup"

# The data for the new merchant
data = {
  "orgnumber": "918713867",
  "partnerId": "265536",
  "subscriptionPackageId": "2",
  "signupCallbackUrl": "https://example.com/signup-callback",
  "signupCallbackToken": "c00be7de-64c4-11e8-adc0-fa7ae01bbebc",
  "merchantWebsiteUrl": "https://www.vipps.no/",
  "form-type": "vippspanett"
}

# Make the POST request
response = requests.post(url, data)

# Print the response and content
print(response)
print(response.content)

response_dict = json.loads(response.text)
for i in response_dict:
    print("key: ", i, "val: ", response_dict[i])

# Vipps will make a callback when the merchant has signed the form
# provided on the URL in the response.
