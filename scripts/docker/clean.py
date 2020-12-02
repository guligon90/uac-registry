import subprocess

from typing import Optional, List

from docker import common


# runs command and captures output
def run(command: str) -> str:
    print(command)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    return process.communicate()[0].replace("\n", " ")


def clean(arguments: Optional[List[str]]):
    print(">>>>>>>>>> Removing Docker Containers <<<<<<<<<<")
    containers = run('docker ps -a -q -f \"name=' + common.PROJECT_PREFIX + '\"')
    run('docker rm -f ' + containers)

    print("\n>>>>>>>>>> Removing Docker Volumes <<<<<<<<<<")
    volume_prefix = common.PROJECT_PREFIX.replace('-', '_')  # docker volumes can't use '-'
    volumes = run('docker volume ls -q -f \"name=' + volume_prefix + '\" -f \"dangling=true\"')
    run('docker volume rm ' + volumes)

    print("\n>>>>>>>>>> Removing Docker Networks <<<<<<<<<<")
    networks = run('docker network ls -q -f \"name=' + common.PROJECT_PREFIX + '\"')

    clean_args = 'docker network rm ' + networks
    if arguments is not None:
        clean_args += ' '.join(arguments)

    run(clean_args)

    # ignore return codes since stuff may have already been removed and break
    return 0
