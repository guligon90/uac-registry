#!/usr/bin/python3

import sys

from typing import Optional, List

#from docker.build import build
#from docker.clean import clean
#from docker.coverage import coverage
#from docker.dev import dev
#from docker.kill import kill
from docker.licenses import licenses
#from docker.lint import lint
from docker.logs import logs
from docker.migrate import migrate, make_migrations
#from docker.package import package
#from docker.restart import restart
from docker.run import run
#from docker.start import start
#from docker.status import status
#from docker.stop import stop
#from docker.test import test
from docker.usage import usage


def argument_to_command(arguments: Optional[List[str]]) -> None:
    commands = {
        #"build": build,
        #"clean": clean,
        #"coverage": coverage,
        #"dev": dev,
        #"kill": kill,
        "licenses": licenses,
        #"lint": lint,
        "logs": logs,
        "migrate": migrate,
        "make_migrations": make_migrations,
        #"package": package,
        #"restart": restart,
        "run": run,
        #"start": start,
        #"status": status,
        #"stop": stop,
        #"test": test,
    }

    ret = 0

    if arguments is not None:
        command = commands.get(arguments[0], usage)
        ret = command(arguments[1:])

    sys.exit(ret)


def main() -> None:
    arguments = sys.argv[1:]

    if not arguments:
        usage([])
        return

    try:
        argument_to_command(arguments)
    except KeyboardInterrupt:
        pass

    return


if __name__ == '__main__':
    main()
