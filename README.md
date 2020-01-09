# Vipps Partner Signup API

This repository contains developer resources for the Vipps Partner Signup API.

API Documentation: https://vippsas.github.io/vipps-signup-api/


See the Vipps Developers repository for
a "getting started" guide,
information about product activation,
contact information,
contribution guidelines,
etc:
https://github.com/vippsas/vipps-developers 

## About Vipps Partner Signup API
The intention with Vipps Partner Signup API is to create signup forms for Vipps eCommerce to enable the merchant to get Vipps as a payment option and making the process simpler for the merchant by prefilling the form with certain data. We are also enabling the partner to automate the reception of API Keys with the Signup callback functionality.

### Process overview
![Vips Signup via Partner](images/vipps_signup_via_partner.png)

### The signup form
The partner can implement a signup registration form for merchants on the partner's website. The merchant enters their organization number and the url for their website in the form. When they click register, the signup is initiated.
![Vipps signup registration](images/vipps-signup-registration.png)

### Vipps signup form
The merchant is then redirected to the signup link, and can complete the registration form on vipps.no. When the form has been completed, and signed by the right person, Vipps and the partner handles the rest of the process, and the partner informs the merchant when the implementation is ready.
![Vipps signup registration form](images/vipps-signup-registration-form.png)


## Partner initiates the signup
We want to create a connection between the ecommerce partner ("Partner") and the merchant, as the partners have a relationship to the merchant we aim to make it easy for the merchants to complete the commercial and technical setup for Vipps. The process is initated by the partner, calling Vipps API to create a prefilled signup form.

**Request**
```html
{
    "orgnumber" : "819226032",
    "partnerId":"1234",
    "subscriptionPackageId":"1234",
    "merchantWebsiteUrl": "https://www.vipps.no",
    "signupCallbackToken":"",
    "signupCallbackUrl":"https://upload.credentials.to.partner.url",
    "form-type":"vippspanett"
}
```

## Partner receives the signup link
As response to partial signup initiation above the partner receives a signup id and a link to the signup. The partner has to forward this link to the merchant to complete the registration.

**Response**
```html
{
    "signup-id": "4188dea2-00d0-488a-88b7-b39b186151c0",
    "vippsURL": "https://vippsbedrift.no/signup/vippspanett/?r=4188dea2-00d0-488a-88b7-b39b186151c0"
}
```

## The signup form, KYC and signing process
Merchant completes the form and the signup form is processed by Vipps. This usually takes 2-3 days, unless we need more information from the merchant. If necessary, the merchant answers additional questions as part of Vipps KYC process.

## The signup callback
Once Vipps have completed the registration the signup callback is initiated to the partner signupCallback with the required API credentials for the merchant.


## Additional developer resources
See the Vipps Developers repository for a "getting started" guide,
information about product activation, contact information,
contribution guidelines, etc: https://github.com/vippsas/vipps-developers


## Frequently Asked Questions for the Signup API

### What is my partnerId?
The partnerId is used to identify the partner. Ask your contact in Vipps to provide you with your partnerId.

### What is my subscriptionPackageId?
The subscriptionPackageId is used to define which price the merchant will have. Ask your contact in Vipps to provide you with the correct subscriptionPackageIds.

### Will Vipps send the Signup link to the merchant?
The partner has to forward the signup link to the merchant.

### I sent a signup link to a merchant, but has not received any callback. When will I receive the callback?
The callback is sent after the merchant has completed the signup and signed the agreement AND after Vipps has done KYC and completed the registration process. This usually takes a couple of days, but sometimes it will take longer if Vipps needs to contact the merchant for more information to complete the registration. Please contact the merchant first, and confirm that they have completed the signup form and signed it.
