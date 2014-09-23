[![Build Status](https://travis-ci.org/sourcefabric-innovation/citizendesk-interface.png?branch=master)](https://travis-ci.org/sourcefabric-innovation/citizendesk-interface)

## Citizen Desk Interface

Connection between the Citizen Desk [core][core] and the front ends.

#### The role of this component within Citizen Desk

*Interface* stands for Application Programming Interface, that is
API. The role of this component is to expose the entities in the
database, and the [core][core] functionalities, through an
authenticated API. Once exposed, they can be used by a web or mobile
frontend, see for example the web [Citizen Desk frontend][frontend].

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
[core]: https://github.com/sourcefabric-innovation/citizendesk-core
[frontend]: https://github.com/sourcefabric-innovation/citizendesk-frontend
