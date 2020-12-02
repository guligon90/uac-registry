import subprocess

from typing import Iterable

from docker import common


def dev(arguments: Iterable[str]) -> int:
    print(">>>>>>>>>>>>>>>>>>>> Starting Containers <<<<<<<<<<<<<<<<<<<<")
    command = common.COMPOSE_COMMAND + ' up ' + ' '.join(arguments)

    print(command)
    return subprocess.call(command, shell=True)
