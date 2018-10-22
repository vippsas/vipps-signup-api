# Vipps Partner Signup API

This repository contains developer resources for the Vipps Partner Signup API.

API Documentation: https://vippsas.github.io/vipps-signup-api/

## About Vipps Partner Signup API
The intention with Vipps Partner Signup API is to create signup forms for Vipps eCommerce to enable the merchant to get Vipps as a payment option and making the process simpler for the merchant by prefilling the form with certain data. We are also enabling the partner to automate the reception of API Keys with the Signup callback functionality.

### Process overview

![Signup flow](vipps_signup_via_partner.png) 

### Partner initiates the signup
We want to create a connection between the ecommerce partner ("Partner") and the merchant, as the partners are having a relationship to the merchant we aim to make it easy for the merchants to complete the commercial and technical setup for Vipps. The process is initated by the partner, calling Vipps API to create a prefilled signup form.

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
### Partner receives the signup link
As response to partial signup initiation above the partner receives an signup id and a link to the signup which is forwarded to the merchant to complete the registration.

**Response**
```html
{
    "signup-id": "4188dea2-00d0-488a-88b7-b39b186151c0",
    "vippsURL": "https://vippsbedrift.no/signup/vippspanett/?r=4188dea2-00d0-488a-88b7-b39b186151c0"
}
```

### The signup form, KYC and signing process

Merchant completes the form and if necessary answers additional questions as part of Vipps KYC process.  

### The signup callback

Once Vipps have completed the registration the signup callback is initiated to the partner signupCallback with the required API credentials for the merchant.

## Additional developer resources

See the Vipps Developers repository for a "getting started" guide,
information about product activation, contact information,
contribution guidelines, etc: https://github.com/vippsas/vipps-developers
