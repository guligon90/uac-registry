import subprocess

from typing import Iterable

from docker import common


def stop(arguments: Iterable[str]) -> int:
    print(">>>>>>>>>>>>>>>>>>>> Stopping services <<<<<<<<<<<<<<<<<<<<")
    command = common.COMPOSE_COMMAND + ' stop ' + ' '.join(arguments)

    print(command)
    return subprocess.call(command, shell=True)
