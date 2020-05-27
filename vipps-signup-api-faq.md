## Frequently Asked Questions for the Signup API

Document version 3.2.0.

- [Who do I contact if I have problems?](#who-do--i-contact-if-i-have-problems)
- [What is my partnerId?](#what-is-my-partnerid)
- [What is my subscriptionPackageId?](#what-is-my-subscriptionpackageid)
- [How can I get an account in the test environment?](#how-can-i-get-an-account-in-the-test-environment)
- [Will Vipps send the signup link to the merchant?](#will-vipps-send-the-signup-link-to-the-merchant)
- [For how long is the signup URL valid?](#for-how-long-is-the-signup-url-valid)
- [What if the merchant does not have a website?](#what-if-the-merchant-does-not-have-a-website)
- [What happens if a partner sends multiple signup URLs for the same merchant?](#what-happens-if-a-partner-sends-multiple-signup-urls-for-the-same-merchant)
- [When will I receive the callback from Vipps?](#when-will-i-receive-the-callback-from-vipps)
- [Can Vipps re-send the callback?](#can-vipps-re-send-the-callback)
- [Questions?](#questions)

## Who do I contact if I have problems?

That depends on what you need help with:
* Your partnership with Vipps: partnerbestilling@vipps.no
* The Signup API: See [contact information here](https://github.com/vippsas/vipps-developers/blob/master/contact.md)

## What is my partnerId?

The `partnerId` is used to identify the partner.
Ask your contact in Vipps to provide you with your `partnerId`.

## What is my subscriptionPackageId?

The `subscriptionPackageId` is used to define the merchant's price package.
Ask your contact in Vipps to provide you with the correct `subscriptionPackageIds`.

## How can I get an account in the test environment?

The Signup API requires more backend functionality than we have available in
the test environment. For partners that need to test the Signup API
we recommend that the partner "test in prod"  and signs up itself in the
production environment.

## Will Vipps send the signup link to the merchant?

No, the partner has to send the signup link to the merchant.

## For how long is the signup URL valid?

30 days.

## What if the merchant does not have a website?

The partner can provide the URL to the partner's website.

## What happens if a partner sends multiple signup URLs for the same merchant?

If we receive multiple signups for the same organization number, Vipps will
attempt to use the latest one, but we _strongly_ recommend to only send one.

## When will I receive the callback from Vipps?

The callback is sent after the merchant has:
* Completed the signup form
* Signed the signup form

_and_ Vipps has:
* Completed the KYC process
* Completed the registration process

The last two steps usually takes a couple of days, but sometimes it will take
longer if Vipps needs to contact the merchant for more information to complete
the registration.

If there is a delay, it is almost always due to delays at the merchant side.
Please contact the merchant first, and confirm that they have completed the
signup form, and that the right person has signed it.

Follow-up questions from Vipps sometimes end up in the merchant's spam
folder - please have the merchant check there too.

## Can Vipps re-send the callback?

It is technically possible, but a manual and rather tedious process. Before
requesting this, please ask the merchant to retrieve the API keys from
portal.vipps.no as described here:
[Getting the API keys](https://github.com/vippsas/vipps-developers/blob/master/vipps-getting-started.md#getting-the-api-keys).

## Questions?

We're always happy to help with code or other questions you might have!
Please create an [issue](https://github.com/vippsas/vipps-signup-api/issues),
a [pull request](https://github.com/vippsas/vipps-signup-api/pulls),
or [contact us](https://github.com/vippsas/vipps-developers/blob/master/contact.md).

Sign up for our [Technical newsletter for developers](https://github.com/vippsas/vipps-developers/tree/master/newsletters).
