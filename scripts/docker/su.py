# Base imports
from typing import Iterable, Optional

# Project imports
from docker import common
from docker.run import run


def su(arguments: Iterable[str], deps: Optional[bool] = True) -> int:
    print(">>>>>>>>>> Create Django Super User <<<<<<<<<<")
    run(['backend', 'python3', common.MANAGE_PY, 'createsuperuser', '--noinput'], deps)
