### security

> [!NOTE]
> If your site authenticates users, it should regenerate and resend session cookies, even ones that already exist, whenever a user authenticates. This approach helps prevent [session fixation attacks](https://developer.mozilla.org/en-US/docs/Web/Security/Types_of_attacks#session_fixation), where a third-party can reuse a user's session.