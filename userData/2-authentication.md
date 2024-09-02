# Basic Authentificatoin

## Objectives 
- What authentication and authorization means
- difference between stateful and stateless
- sessions based authentication
- token Based authentication
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

### Sessions Based Authentication

1. user submits login credentials
2. server verifies the credentials against the DB
3. server creates a temporary user **Session**
4. server issues a **cookie** with a **session ID**
5. user sends the cookie with each request
6. server validates it against the session store and grants access
7. when user logs out, server destroys the session and clears the cookie

##### Features
- every user session is stored server-side (stateful)
    - memory (e:g file system)
    - cache (e:g redis, Memchached)
    - DB (e:g postgress, MongoDB)
- each user is identified by a session ID also know as 
opaque reference because the session id has no actual data it is just a random string so no 3rd party can extract data out of it, only issued server can map back to data
- stored in cookie
    - signed with a secret stored in the server
    - protected with flags
- used in web apps, and frameworks

### Cookies
- it just a header just like authorization and Content-Type
- used in session management, personalization, tracking
- consists of name, value, and optional attributes / flags
- set with `Set-Cookie` header by the server, and when sent back again to the server by the browser it exists in the `Cookie` header

### Token Based Authentication
- user submits login credentials
- server verifies credentials against DB
- server generates a temporary **token** and embeds user data into it
- server responds back with the token in body or header
- user stores the token in client storage
- user sends the token and grants acess
- when user logout token is cleared from client storage

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
