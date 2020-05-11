# Vipps Partner Signup API

This repository contains developer resources for the Vipps Partner Signup API.

API Documentation: https://vippsas.github.io/vipps-signup-api/

Document version 1.1.0.

## About the Vipps Partner Signup API

The Vipps Partner Signup API lets partners create signup forms for Vipps
eCommerce for their merchants. The partners can make the process simpler for
the merchant by pre-filling the form with certain data.

We are also enabling the partner to automate the reception of API keys with
the Signup callback functionality.

**Please note:** The Signup API has some dependencies that are not in place
in our test environment. Because of this we recommend to "test in prod" by
signing up yourself.

### Process overview

![Signup flow](images/vipps_signup_via_partner.png)

### Partner initiates the signup

We want to create a connection between the ecommerce partner ("Partner") and
the merchant, as the partners are having a relationship to the merchant we aim
to make it easy for the merchants to complete the commercial and technical
setup for Vipps. The process is initiated by the partner, calling Vipps API to
create a pre-filled signup form.

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

As response to partial signup initiation above the partner receives an signup
id and a link to the signup which is forwarded to the merchant to complete the
registration.

**Response**
```html
{
    "signup-id": "4188dea2-00d0-488a-88b7-b39b186151c0",
    "vippsURL": "https://vippsbedrift.no/signup/vippspanett/?r=4188dea2-00d0-488a-88b7-b39b186151c0"
}
```

Please note that the link is valid for 30 days only.

### The signup form, KYC and signing process

Merchant completes the form and if necessary answers additional questions as
part of the Vipps KYC process.  

### The signup callback

Once Vipps have completed the registration the signup callback is initiated to
the partner `signupCallbackUrl` with the required API credentials for the merchant.

If the partner is unable to receive the callback, or the callback fails for
some reason, the merchant can log in with BankID on poertal.vipps.no and
retrieve the API keys as described in
[Getting started](https://github.com/vippsas/vipps-developers/blob/master/vipps-getting-started.md).

## Additional developer resources

See the the main developer page: https://github.com/vippsas/

## Questions?

We're always happy to help with code or other questions you might have!
Please create an [issue](https://github.com/vippsas/vipps-sdignup-api/issues),
a [pull request](https://github.com/vippsas/vipps-signup-api/pulls),
or [contact us](https://github.com/vippsas/vipps-developers/blob/master/contact.md).

Sign up for our [Technical newsletter for developers](https://github.com/vippsas/vipps-developers/tree/master/newsletters).
