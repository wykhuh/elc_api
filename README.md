# EarthLife Consortium API (api_v1)

The ELC API is a composite api which generates and dispaches queries for the Neotoma and Paleobiology (PBDB)  
databases using a simplified, common resource retrival specification. Results are returned as aggregated JSON objects.

This project follows an "API first" development process where:
* The interface schema, complient with the OpenAPI (formally known as Swagger) version 2.0 specification, is first defined.
* Server stubs are generated from this definition.
* Routing is automatically handled by a Swagger complient interface library.
* Finally the server backend code is developed for each generated function.
* Changes to the API can be made in the schema during development and the changes pushed down through the code.
* A Swagger HTML5 based user interface is also generated for browsing the API documentation and testing the parameter calls.

This project is currently under development.  

## Contributers

Development team:
* [Julian Jenkins](http://github.com/jpjenk)
* [Simon Goring](http://github.com/SimonGoring)
* with Michael McClennen (PBDB), Mike Anderson (Neotoma), Mike Stryker (Neotoma)

For more infomation about the EarthLife Consortium and it's members visit [EarthLifeConsortium.org](http://earthlifeconsortium.org).


## Technical Description

The API is being developed with the following modern open source tools:
* [Python](https://www.python.org)
* [Flask](http://flask.pocoo.org) (Python micro web framework)
* [Connexion](http://connexion.readthedocs.io/en/latest) (Flask based routing library that is complient with OpenAPI 2.0)
* [Requests](http://docs.python-requests.org) (HTTP library for Python)
* [git](https://git-scm.com) (for version control) and [GitHub](http://github.com) (for repository hosting and issue tracking)
Optionally
* [swagger-codegen](http://swagger.io/swagger-codegen) (Java based templating engine which can use Flask+Connexion to generate the server)
* [swagger-edit](https://github.com/swagger-api/swagger-editor) (a Node.js based editor and validator for OpenAPI spec YAML files)


## Starting and Building the API

The API requires Python 3.5 or greater. To run the server, first install Connexion from the Cheese Shop (PyPI). This also installs Flask if it is not already installed:
```
pip3 install -r requirements.txt
python3 -m swagger_server
```
The api documentation and user interface will be available at:
```
http://127.0.0.1:8080/api_v1/ui
```
The raw OpenAPI definition is at:

```
http://127.0.0.1:8080/api_v1/swagger.json
```
To initially build the server and generate controller stubs we used [swagger-codegen](http://swagger.io/swagger-codegen). This is not required if you are simply cloning this repository.
```
swagger-codegen generate -i ./swagger.yaml -l python-flask -o [your
path]/elc_api
```

## Error reporting

The API reports all excemptions as serialized JSON strictly conforming to the Internet Engineering Task Force [IETF standard](https://tools.ietf.org/html/draft-ietf-appsawg-http-problem-00)


## Production Environment

See README-Deploy for informaton regarding production deployment as a uWSGI app.
