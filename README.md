[![Build Status](https://travis-ci.org/sourcefabric-innovation/citizendesk-interface.png?branch=master)](https://travis-ci.org/sourcefabric-innovation/citizendesk-interface)

## Citizen Desk Interface

This is one of the components in the [Citizen Desk
project](https://www.sourcefabric.org/en/citizendesk/)

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

#### Running

Like [Eve][eve], this component is a [Flask][flask] application, and
therefore a WSGI application. You can refer to the [deploying section
in the Flask doc](http://flask.pocoo.org/docs/0.10/deploying/) in
order to have more info about running and deploying the
app. Specifically i used Gunicorn in order to serve the app, and you
may find a few simple scripts i used in this repository root. The app
will look for a Mongo database on the same machine it is working on,
on the standard port, and it will look for an instance of [Citizen
Desk Core][core] at a location which is currently hardcoded. Some
initialisation scripts are contained in the `initialise` folder.

#### Running the tests

Running the tests requires an Elastic search and a Mongo instance
listening on the standard ports. Refer to the Travis file in case of
doubts.

[superdesk_server]: https://github.com/superdesk/superdesk-server
[core]: https://github.com/sourcefabric-innovation/citizendesk-core
[frontend]: https://github.com/sourcefabric-innovation/citizendesk-frontend
[eve]: http://python-eve.org/index.html
[flask]: http://flask.pocoo.org/