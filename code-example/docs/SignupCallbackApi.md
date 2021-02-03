# swagger_client.SignupCallbackApi

All URIs are relative to *https://api.vippsbedrift.no*

Method | HTTP request | Description
------------- | ------------- | -------------
[**callback**](SignupCallbackApi.md#callback) | **POST** /signupcallbackURL | Sent Callback

# **callback**
> callback(body, authorization=authorization)

Sent Callback

The callback that is sent after the merchant's sale unit has been created.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SignupCallbackApi()
body = swagger_client.CallbackTriggerResponse() # CallbackTriggerResponse | callback
authorization = 'authorization_example' # str | Token is an exact copy of SignupCallbackToken. SignupCallbackToken is provided by the partner in partial signup request. Used so that the partner may authenticate the callback. (optional)

try:
    # Sent Callback
    api_instance.callback(body, authorization=authorization)
except ApiException as e:
    print("Exception when calling SignupCallbackApi->callback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CallbackTriggerResponse**](CallbackTriggerResponse.md)| callback | 
 **authorization** | **str**| Token is an exact copy of SignupCallbackToken. SignupCallbackToken is provided by the partner in partial signup request. Used so that the partner may authenticate the callback. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

