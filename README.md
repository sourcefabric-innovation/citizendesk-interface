### citizendesk-interface

This provides the socket and REST interface for the citizendesk
frontend, working like a connector between the frontend and the
backend services

#### Deployment

This is a sails application, and can thus be deployed as specified in
the [sails
documentation](http://sailsjs.org/#!documentation/deployment). You
will have to:

- Clone this repository
- Install dependencies with `npm`
- Launch the application using `sails` and/or `forever`

Refer to the sails documentation link above for more details.

#### Interaction with other citizendesk components

After a successful deploy, you will have a service providing a REST
and Socket.io API. The service port is the default sails port,
`1337`. You can then plug applications like the [Citizendesk
frontend](https://github.com/sourcefabric-innovation/citizenfront) to
this service.

This service will convert API calls to operations on a Mongo database,
which is expected to listen on localhost on the default Mongo port,
`27017`. The Mongo database should be the same where citizendesk core
services are storing new reports.

Refer to the [citizendesk
architecture](https://docs.google.com/drawings/d/1lwjMj8gknz2LNCm-yg7Ee1c7Z8hN_3EISxb2n4zw3oM/edit?usp=sharing)
in order to have an overview.
