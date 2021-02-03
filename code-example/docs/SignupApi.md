# swagger_client.SignupApi

All URIs are relative to *https://api.vippsbedrift.no*

Method | HTTP request | Description
------------- | ------------- | -------------
[**partial_signup**](SignupApi.md#partial_signup) | **POST** /v1/partial/signup | Create a signup

# **partial_signup**
> PartialSignupResponse partial_signup(body)

Create a signup

Initiate the signup in Vipps on behalf of a merchant for Vipps ecommerce. In the test environment it is recommended to use the provided example values for partnerId and subscriptionPackageId. For production values, contact Vipps.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SignupApi()
body = swagger_client.PartialSignup() # PartialSignup | partialSignup

try:
    # Create a signup
    api_response = api_instance.partial_signup(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignupApi->partial_signup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PartialSignup**](PartialSignup.md)| partialSignup | 

### Return type

[**PartialSignupResponse**](PartialSignupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

