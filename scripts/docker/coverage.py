from typing import Optional, List

from docker.run import run


# Gives flexibility to add test coverage to a frontend project, for example
PARAMS = {
    "backend": ['backend', 'pytest', '--cov'],
}


def usage():
    print("From what service do you want a coverage report? <backend>")


def coverage(arguments: Optional[List[str]]):
    print(">>>>>>>>>> Running Coverage Report <<<<<<<<<<")

    if arguments is not None:
        params_from_args = PARAMS.get(arguments[0], [])
        return run(params_from_args + arguments[1:])

    return usage()
