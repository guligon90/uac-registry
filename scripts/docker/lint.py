from typing import Optional, List, Union

from docker.run import run


# Gives flexibility to add linting to a frontend project, for example
PARAMS = {
    "backend": ['backend', 'prospector'],
}


def usage() -> None:
    print("What do you want to check? <backend>")


def lint(arguments: Optional[List[str]]) -> Union[int, None]:
    print(">>>>>>>>>> Running Licenses Check <<<<<<<<<<")

    if arguments is not None:
        params_from_args = PARAMS.get(arguments[0], [])
        return run(params_from_args + arguments[1:])

    usage()
    return None
