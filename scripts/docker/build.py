import subprocess

from typing import Iterable

from docker import common


def build(arguments: Iterable[str]) -> int:
    print(">>>>>>>>>>>>>>>>>>>> Building <<<<<<<<<<<<<<<<<<<<")
    command = common.COMPOSE_COMMAND + ' build --pull ' + ' '.join(arguments)
    print(command)
    return subprocess.call(command, shell=True)
