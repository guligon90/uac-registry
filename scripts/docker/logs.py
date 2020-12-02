import subprocess

from typing import Iterable

from docker import common


def logs(arguments: Iterable[str]) -> int:
    print(">>>>>>>>>>>>>>>>>>>> Logs <<<<<<<<<<<<<<<<<<<<")
    command = common.COMPOSE_COMMAND + ' logs --follow ' + ' '.join(arguments)

    print(command)
    return subprocess.call(command, shell=True)
