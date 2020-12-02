# UAC Registry :: Application Server

## Building and Running

The Docker Compose service, which creates an virtualized instance of the Django application server, can be built via the `devenv` script suite.

At the terminal, in the project root, execute the command:
```bash
(env) ~/uac-registry/ $ ./scripts/devenv.py build backend
```

To run the service, execute:
```bash
(env) ~/uac-registry/ $ ./scripts/devenv.py start backend
```

To make sure that the back-end is running properly, run `docker ps` in the terminal. The output should be something like:
```
CONTAINER ID        IMAGE                         COMMAND                  CREATED             STATUS                            PORTS                    NAMES
05b7869309aa        uac-registry-backend-image    "../wait-for.sh data…"   2 hours ago         Up 48 seconds                     0.0.0.0:8080->8080/tcp   uac-registry-backend
```

Alternatively, you can also follow the container logs by running `./scripts/devenv.py logs backend`. The output is similar to:
```
uac-registry-backend | Performing system checks...
uac-registry-backend | 
uac-registry-backend | System check identified no issues (0 silenced).
uac-registry-backend | December 02, 2020 - 19:12:16
uac-registry-backend | Django version 3.1.3, using settings 'app.settings'
uac-registry-backend | Starting development server at http://0.0.0.0:8080/
uac-registry-backend | Quit the server with CONTROL-C.
uac-registry-backend | Watching for file changes with StatReloader
```

To stop the container, just run `./scripts/devenv.py stop backend`.