from typing import Iterable

RED = '\033[91m'
BLUE = '\033[94m'
END = '\033[0m'


def red(string: str) -> str:
    return RED + string + END


def blue(string: str) -> str:
    return BLUE + string + END


def usage(_: Iterable[str] = None) -> None:
    print('''
    Usage:
        python3 devenv.py <command> <arguments>
        devenv.py <command> <arguments>

    Commands:
        build                     Downloads and builds images.
        clean                     Removes all containers, networks {volumes}.
        coverage                  Reports the test coverage of the service.
        dev                       Starts containers.
        kill                      Runs clean and {images}.
        licenses                  Runs license check in backend or frontend.
        lint                      Runs linter in backend or frontend.
        logs                      Attaches logs to terminal.
        package                   Create a production delivery.
        restart                   Restarts containers.
        run                       Runs an arbitrary command in a specified service (eg. 'run frontend build').
        start                     Start containers in detached mode.
        status                    Shows all containers, images, networks and volumes.
        stop                      Stops all containers.
        test                      Runs the test runner in all services
    '''.format(
        volumes=red('and volumes'),
        images=red('removes all images'),
    ))
