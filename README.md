# UAC (User-Address-Client) Registry API [WiP]

Technical assessment for the position of back-end engineer at @neoprospecta.

## Getting started
Make sure that you have installed in your system the latest stable releases of the following tools:

* [Docker](https://docs.docker.com/);
* [Docker Compose](https://docs.docker.com/compose/);
* [Git](https://git-scm.com/);
* [Python (3.8+)](https://www.python.org/downloads/release/python-384/).


### Cloning
To get the code base from this repository, you must open an terminal and execute:

```bash
~ $ git clone https://github.com/guligon90/uac-registry.git
```

### Building

#### Environment
In order to setting up the Python development environment, which is required to manipulate the project building processes via `docker-compose`, you must follow [these](scripts/README.md) instructions.

#### Application Server
With the environment all set up, you can now follow the [instructions](./src/backend/README.md) to build the Django application server, which provides the UAC Registry API.

### Usage
With the application server up and running, you can now access the [API documentation](http://localhost:8080/docs). There you can check out the endpoints' detailed specifications, concerning request and response formats.