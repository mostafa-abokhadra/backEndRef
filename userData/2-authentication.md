# Basic Authentificatoin

### What authentication means
### What Base64 is
### How to encode a string in Base64
### What Basic authentication means
### How to send the Authorization header

**watch this**

- [basic authentification](https://www.youtube.com/watch?v=501dpx2IjGY)

### Base64

```py
import base64
encoded = base64.base64encode(b'data to be encoded')
data = base64.base64decode(encoded)
```

### Authorization Header

- it is used to provide the server with the credentials that authenticate the user
- it is usually sent after the user attempt to request a protected resource w/o credintials
- the server respond with <mark>401 unathorized</mark> message the include at least one <mark>WWW-Authenticate</mark> header
- This header indicates what authentication schemes can be used to access the resource

##### Syntax

```
Authorization: auth-scheme auth-parameter
e:g Basic Credentials # (username:password but encoded using base64)
```
### Digest
```
Authorization: Digest username=<username>,
    realm="<realm>",
    uri="<url>",
    algorithm=<algorithm>,
    nonce="<nonce>",
    nc=<nc>,
    cnonce="<cnonce>",
    qop=<qop>,
    response="<response>",
    opaque="<opaque>"
```

### Ref
- [basic authentification](https://www.youtube.com/watch?v=501dpx2IjGY)
