### RESTFUL API

**What is a REST API?** REST is an acronym for **REpresentational State Transfer Application Programming Interface** an almost meaningless description of the most-used web service technology! A REST API is a way for two computer systems to communicate using the HTTP technologies found in web browsers and servers.

restful is an architectural style, design or principles to be followed when designing a web service (API), when these principles are applied while designing the web service we get a RESTful API, Its purpose is to induce performance, scalability, simplicity, modifiability, visibility, portability, and reliability.

### principles of a restful api

#### Uniform Interface

1. **resource**: REST API is **Resource-based**, a resource is an object and can be access by a URI. An object is “displayed”/transferred via a **representation** (typically JSON). HTTP methods will be actions on a resource.everything is a resource, you can define your modules e:g your database table classes as resources, you can define any data as a resource it's up to you, the key abstraction of information in REST is a resource, any information that can be named can be a resource e:g a document or image and so on

2. you can access any resource by a **URI** (uniform resource identifier), and always name your resource an nouns (good practice) e:g /employees/ and not /get-employees , as the http method will be our verb
#### URIs - resource name

- `GET /users`: path for listing all user resources
- `GET /users/12`: path for the user `id = 12`
- `GET /users/12/addresses`: path for listing all addresses of the user `id = 12`
- `POST /users`: path for creating a user resource
- `PUT /users/12`: path for updating the user `id = 12`
- `DELETE /users/12/addresses/2`: path for deleting the address `id = 2` of the user `id = 12`

3. **use HTTP methods** GET, POST, PUT, DELETE to CRUD

In the HTTP Response, the client should verify the information of two things:
- status code: result of the action
- body: JSON or XML representation of resources

Some important status code:
- `200`: OK
- `201`: created => after a `POST` request
- `204`: no content => can be return after a `DELETE` request
- `400`: bad request => the server doesn’t understand the request
- `401`: unauthorized => client user can’t be identified
- `403`: forbidden => client user is identified but not allowed to access a resource
- `404`: not found => resource doesn’t exist
- `500`: internal server error

4. manipulation of resources and representations, each resource can have one or more representations e:g XML or application/json, text/html, etc, clients and servers negotiate to select representation by <mark>Accept</mark> header e:g <mark>Accept: PNG</mark> like when you request a photo

5. **self descriptive messages**, requests and responses contain not only data but additional headers describing how the content should be handled such as **if it should be cached, authentication, requirements**, etc..

### statelessness

- all communication between client and server are stateless, so all requests and responses are stateless, meaning the server doesn't maintain any state of the system and each request from the client must contain all of the data that is necessary to handle the request, no need of storing any state on the server, each request is independent and doesn't depend on the previous requests.

- so the server should not require to store the state of a session, if the concept of a session is required all information should be **stored at client side** and **sent with every subsequent request**, this makes every request from client independent and a complete entity in itself.

- e:g if a person is adding items to his cart on a shopping website , the state of the cart should be stored at the client side only, and this state of the cart to be sent from the client to the server whenever required

- because server don't need to store the state of the session therefore it enhance webservice performance

#### caching
it happens on client side, whenever a client send a request, the server response with the actual data and another metdata or another information in the headers that **tells the client whether some data should be stored** locally in the client side or not, whether the client has to cache the response or not

- server doese this by includeing a <mark>Cache-Control</mark> and <mark>Last-Modified</mark> data value in http response headers

-there will also be something called <mark>Etag</mark> in the response header which is entity tag, every unique version of the resource ha a unique Etag, so if a resource changes there will be a new entity tag given to it

-so this co-ordination between client and server is essential for being stateless

#### layering
- there can be multiple layers in between client request and server response, it's called **http intermediaries**, they can be used for message translations/improving performance with caching, can include proxies and gateways, E:g a client may send the request to a proxy server instead of main server, porxy server evaluates the request to simplify or control it's complexity ,another e:g gateways may be used for managing traffic on the network, protocol translations etc..

- e:g layer to help us in caching, we use a layer (intermediary) that can cache a response and store it for an hour, if a new request comes from the client within an hour, the cached response will be sent from the intermediary without going until the server, so improves performance and scalability

- optional constraint of REST is code-on-demand, which is the ability to download and execute code at client side, e:g client request a resource and server returns resource with some js code

### authorization and authentication
- in terms of api we will always see authorization (in header) and not authentication
- authentication is validating a user or a service e:g when a person come to your home and you know him so you allow him come inside, so you validate the credentials, and he is authenticated to enter your home and use your drawing room, watch tv, but if goes to your bedroom you tell him that you are not authorized to access this area or this resource, and this what autorization is,  so when you gave him the authentication he becomes authorized to access some areas and resources in your home but not authorized to access another 
- e:g when you login to a website you are authenticated to use some service but you can't use another sections like admin section or other
- so authentication is who you are and authorization is what can you do


first step is always authentication like if used basic auth in you api request using username and pass or token based authorization, it first check your credentials and authentication, if your credentials are not correct you will not be able to access authorized resource

### ref
- [1](https://youtu.be/oTzNRv6X51o?si=58IpPCH9zmn0wEDv)
- [2](https://youtu.be/rq7DvjN1Gco?si=8e8AQYIHXFwHbPCm)
- [3](https://www.youtube.com/watch?v=dPNCFdoXdec)
- [4](https://www.youtube.com/watch?v=ByGJQzlzxQg)
- [5](https://www.youtube.com/watch?v=OVvTv9Hy91Q)
- [6](https://www.sitepoint.com/rest-api/)