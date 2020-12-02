# Base imports
import subprocess
from typing import Iterable, Optional

# Project imports
from docker import common
from docker.run import run


def migrate(arguments: Iterable[str], deps: Optional[bool] = True) -> int:
    print(">>>>>>>>>> Running database migration <<<<<<<<<<")
    run(['backend', 'python3', common.MANAGE_PY, 'migrate'], deps)


def make_migrations(arguments: Iterable[str], deps: Optional[bool] = True) -> int:
    print(">>>>>>>>>> Running database migration <<<<<<<<<<")
    run(['backend', 'python3', common.MANAGE_PY, 'makemigrations'], deps)
