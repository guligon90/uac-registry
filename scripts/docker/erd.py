# Base imports
import os
import subprocess
from typing import Iterable, Optional

# Project imports
from docker import common
from docker.run import run


RELEVANT_MODELS = [
    'Address',
    'Client',
    'User',
    'UserAddress',
]


ERD_FILE = f'{common.PROJECT_PREFIX}erd'
ERD_DOT_FILE = f'{ERD_FILE}.dot'
ERD_PNG_FILE = f'{ERD_FILE}.png'
DOCS_IMG_FOLDER = os.path.join(common.PROJECT_HOME, "docs", "img")


def erd(arguments: Iterable[str], deps: Optional[bool] = True) -> None:
    """
    Generates an ERD diagram .dot file, via the Graph Models
    extension from django-extensions.
    Section 4.3.8:
    https://readthedocs.org/projects/django-extensions/downloads/pdf/latest/
    """
    print(">>>>>>>>>> Generating ERD <<<<<<<<<<")

    base_cmd = ['backend', 'python3', common.MANAGE_PY, 'graph_models']

    base_args = [
        '-a -I', ','.join(RELEVANT_MODELS),     # Just generate it for the app models
        '--arrow-shape icurve',                 # Arrow edges for the relations
        '-o', ERD_DOT_FILE                      # Output file
    ]

    run(base_cmd + base_args + arguments, deps)

    dot_source = os.path.join(common.PROJECT_HOME, "src", "backend", "uac-registry", ERD_DOT_FILE)

    # Builds the destinations for both .dot and .png
    dot_destination = os.path.join(DOCS_IMG_FOLDER, ERD_DOT_FILE)
    png_destination = os.path.join(DOCS_IMG_FOLDER, ERD_PNG_FILE)

    # Copies the .dot to /docs/img
    os.replace(dot_source, dot_destination)

    # Converts the .dot file into an .png image file
    subprocess.call(['dot', '-Tpng', dot_destination, '-o', png_destination])
    subprocess.call(['rm', '-f', dot_destination])
