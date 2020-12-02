import subprocess

from typing import Iterable

from docker import common


def start(arguments: Iterable) -> int:
    print(">>>>>>>>>>>>>>>>>>>> Starting Containers <<<<<<<<<<<<<<<<<<<<")
    command = common.COMPOSE_COMMAND + ' up -d ' + ' '.join(arguments)

    print(command)
    return subprocess.call(command, shell=True)
