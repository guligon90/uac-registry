# UAC Registry :: Python Development Environment (`devenv`)

In order to run the building processes for the Docker containers that are configured in this project,
the `docker-compose` command must be executed, via the `devenv` python scripts, which were implemented
to facilitate the handling of the docker operations.


## Setting up

Firstly, with the Python distribution already installed in your workstation, a virtual environment (`venv`),
which is a tool that creates a copy of the Python distribution in the project, must be installed.
To accomplish that, you must execute in the terminal:

```bash
~ $ sudo apt install python3.8-venv -y
```

and wait for the `apt` to finish the installation process. 

Now, to create the environment and install the Python dependencies in it, run the following commands:

```bash
~ $ cd uac-registry/                                        # Project root
~/uac-registry $ python3.8 -m venv env                      # Makes the copy into a folder named 'env', created in the project root
~/uac-registry $ source env/bin/activate                    # Activate the environment, no longer requiring the native Python from the OS
(env) ~/uac-registry $ cd src/backend/uac-registry          # Go to the folder where the dependency files are         
(env) ~/uac-registry $ pip install --upgrade pip            # Upgrade the Python package manager to it's latest version
(env) ~/uac-registry $ pip install -r requirements.txt      # Install the Python production dependencies
(env) ~/uac-registry $ pip install -r requirements-dev.txt  # Install the Python development dependencies
```

**Note**: As long as the environment is active, the `(env)` tag will be visible in the command prompt.

## Usage

To make the `devenv` script executable, run the following commands in a terminal:
```bash
(env) ~/uac-registry $ chmod +x scripts/devenv.py
```

Finally, to check out the documentation of each `devenv` command, you can run:
```bash
(env) ~/uac-registry $ ./scripts/devenv.py usage
```

To no longer use the environment, run:
```bash
(env) ~/uac-registry $ deactivate
~/uac-registry $ # The tag (env) will disappear
```

## Python code linting
Inside the `requirements-dev.txt` file, are only two dependencies, that work together:

- [mypy](https://pypi.org/project/mypy/): Add type annotations to your Python programs, and use mypy to type check them.
- [prospector](https://pypi.org/project/prospector/): A tool to analyse Python code and output information about errors, potential problems, convention violations and complexity.

The prospector's profile, which act as the linter configuration module, can be found in the `.prospector.yaml` file, in the project root. Notice that `mypy` is set to run via `prospector`. So in order to execute code linting and also verify if there are type annotation inconsistencies, just run:

```bash
(env) ~/uac-registry $ prospector
```

If everything is OK, it will produce an output like so:

```
Check Information
=================
         Started: 2020-07-26 17:47:19.267705
        Finished: 2020-07-26 17:47:22.267428
      Time Taken: 3.00 seconds
       Formatter: grouped
        Profiles: .prospector.yaml, full_pep8, doc_warnings, no_test_warnings, strictness_veryhigh, no_member_warnings
      Strictness: from profile
  Libraries Used: 
       Tools Run: dodgy, mccabe, mypy, pep257, pep8, profile-validator, pyflakes, pylint
  Messages Found: 0
```
If there are problems, the output should be similar to:
```
Messages
========

scripts/docker/build.py
  Line: 10
    pep8: W291 / trailing whitespace (col 78)
  Line: 12
    mypy: error / Incompatible return value type (got "int", expected "str") (col 12)



Check Information
=================
         Started: 2020-07-26 22:20:01.922453
        Finished: 2020-07-26 22:20:04.407032
      Time Taken: 2.48 seconds
       Formatter: grouped
        Profiles: .prospector.yaml, full_pep8, doc_warnings, no_test_warnings, strictness_veryhigh, no_member_warnings
      Strictness: from profile
  Libraries Used: 
       Tools Run: dodgy, mccabe, mypy, pep257, pep8, profile-validator, pyflakes, pylint
  Messages Found: 2
```

## Next steps
With the environment all set, you can now follow the [instructions](../src/backend/README.md) to build the Django application server, that provides the API. Or you can [go back](../README.md) to the main documentation.