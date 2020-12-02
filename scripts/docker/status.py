from typing import Iterable

import subprocess


def status(arguments: Iterable[str]) -> int:
    print(">>>>>>>>>>>>>>>>>>>> DOCKER STATUS <<<<<<<<<<<<<<<<<<<<")
    print("\n\nDOCKER CONTAINERS:")
    ret = subprocess.call('docker container ls -a' + ' '.join(arguments), shell=True)

    print("\n\nDOCKER IMAGES:")
    ret += subprocess.call('docker image ls' + ' '.join(arguments), shell=True)

    print("\n\nDOCKER VOLUMES:")
    ret += subprocess.call('docker volume ls' + ' '.join(arguments), shell=True)

    print("\n\nDOCKER NETWORKS:")
    ret += subprocess.call('docker network ls' + ' '.join(arguments), shell=True)

    return ret
