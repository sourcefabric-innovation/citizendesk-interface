[![Build Status](https://travis-ci.org/sourcefabric-innovation/citizendesk-interface.png?branch=master)](https://travis-ci.org/sourcefabric-innovation/citizendesk-interface)

## Citizendesk interface

Interface part of the Citizen Desk 2.0

#### The role of this repository within the Citizendesk architecture

*Interface* stands for Application Programming Interface, that is API. The role of the code here is to expose the resources produced by the server-side, core Citizendesk components. Once exposed to an API, they can be used by a web or mobile frontend, see for example the web [Citizendesk frontend](https://github.com/sourcefabric-innovation/citizendesk-frontend)

### Technical notes

#### Installation

This project depends on [Superdesk Server][superdesk_server] which
does not specifies all its dependencies, so dependency handling has to
be handled with special care, through the `superdesk-dependencies.txt`
file. Currently not all the Superdesk dependencies are added there,
but just those that show to be necessary for the used modules.

##### Notes on dependencies

Eve 0.5-dev is used by Superdesk. Citizen Desk also depends directly
on Eve 0.5, because [it
included](https://github.com/nicolaiarocci/eve/commit/2c7d97952251434f32429e0ae7e945b822d53c9f)
a fix to a problem with documents embedding in lists


[superdesk_server]: https://github.com/superdesk/superdesk-server
