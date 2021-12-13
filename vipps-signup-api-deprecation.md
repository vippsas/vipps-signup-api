# Deprecation of the Vipps Signup API

This is the message we sent to communicate the deprecation of the Vipps Signup API.

Document version 1.0.0.

<br/>
<br/>
<br/>

Hi

Vipps is constantly improving our services, and in some cases this requires us
to sunset legacy products and APIs.

On October 7th we added a deprecation notice to The Vipps eCom Signup API:

>**IMPORTANT:** This API is being phased out. Do _*NOT*_ integrate with this API now.
See
[the partner information](https://github.com/vippsas/vipps-partner)
for more, especially
[How to sign up new merchants](https://github.com/vippsas/vipps-partner#how-to-sign-up-new-merchants).
Please contact your partner contact in Vipps for more information.

This is the official deprecation notice:

# The Vipps Signup API will be shut down on May 1 2022

_**We strongly recommend that you stop using it as soon as possible.**_

There are better solutions available that are continuously improved,
and there is no longer a need to use the Vipps Signup API.

1. The Signup API uses the old, outdated signup form, where merchants make mistakes.
2. Applications from merchants that have used the old signup form takes longer to
   to process, and often require  manual follow-up on email for clarifications.
3. New products, such as
   [Vipps Checkout](https://vipps.no/produkter-og-tjenester/bedrift/ta-betalt-paa-nett/vipps-checkout/),
   can not be ordered using the Signup API.
   The old signup forms will not be updated to support new products.
4. The signup on portal.vipps.no already contains a _lot_ of improvements over the
   signup used by the Signup API, and is being continuously improved - practically
   every day. The Signup API gets none of these improvements.   
5. The callbacks to the partner (with API keys and MSN) often fail because of
   problems on the partner's side, and Vipps has an unacceptable amount of manual
   work to handle this by manually sending API keys with encrypted Excel files with
   passwords on SMS, etc.
6. Merchants that already have another Vipps product get a difficult user experience,
   where they have to provide the same information they have already provided
   (company details, etc), and sign again with BankID.
7. Vipps is making significant changes to the underlying data model for how
   merchants are represented, and we can not continue to maintain both the
   old Signup API and the current signup on portal.vipps.no.

And, of course: We are working on a new and better solution: The
[Vipps Partner API PoC](#vipps-partner-api-poc).

See:
* [Why is the Signup API being phased out?](https://github.com/vippsas/vipps-partner#why-is-the-signup-api-being-phased-out)
* [How to sign up new merchants](https://github.com/vippsas/vipps-partner#how-to-sign-up-new-merchants)
* [Partner keys](https://github.com/vippsas/vipps-partner#partner-keys)
* [Vipps Partner API PoC](https://github.com/vippsas/vipps-partner#vipps-partner-api-poc)
* [Vipps Partners](https://github.com/vippsas/vipps-partner#vipps-partner-api-poc)

# Questions?

Please contact your partner manager.

We're always happy to help with code or other questions you might have!
Please create an [issue](https://github.com/vippsas/vipps-ecom-api/issues),
a [pull request](https://github.com/vippsas/vipps-ecom-api/pulls),
or [contact us](https://github.com/vippsas/vipps-developers/blob/master/contact.md).

Sign up for our [Technical newsletter for developers](https://github.com/vippsas/vipps-developers/tree/master/newsletters).
