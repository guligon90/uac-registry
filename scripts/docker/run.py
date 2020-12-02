import subprocess

from typing import Iterable, Optional

from docker import common


def run(arguments: Iterable[str], deps: Optional[bool] = False) -> int:
    print(">>>>>>>>>> Running Command <<<<<<<<<<")
    compose_arguments = ' run --rm ' if deps else ' run --rm --no-deps '

    command = common.COMPOSE_COMMAND + compose_arguments + ' '.join(arguments)

    print(command)
    return subprocess.call(command, shell=True)
