# Basic Authentificatoin

## Objectives 
- What authentication and authorization means
- stateful and stateless
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header

### authentication
- to verify the identity of a user
- server response when not authenticated is (401 Unauthorized)
### authorization
- to verify permissions of authenticated user
- server response when not authorized(403 Forbidden)

### statful
- sessions using a cookie
### stateless
- token using JWT / OAuth /other

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

### Ref
- [basic authentification](https://www.youtube.com/watch?v=501dpx2IjGY)
