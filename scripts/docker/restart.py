import subprocess

from typing import Iterable

from docker import common


def restart(arguments: Iterable[str]) -> int:
    print(">>>>>>>>>>>>>>>>>>>> Restarting Containers <<<<<<<<<<<<<<<<<<<<")
    command = common.COMPOSE_COMMAND + ' restart ' + ' '.join(arguments)

    print(command)
    return subprocess.call(command, shell=True)
