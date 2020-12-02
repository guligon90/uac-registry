import os

# File system related
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Project related
PROJECT_HOME = os.path.abspath(os.path.join(BASE_DIR, os.pardir, os.pardir))
PROJECT_PREFIX = "uac-registry-"

# Django manage.py location
MANAGE_PY = '/uac-registry/backend/manage.py'

# Docker compose related
COMPOSE_FILE = os.path.join(PROJECT_HOME, "docker-compose.yml")
COMPOSE_COMMAND = "docker-compose -f \"" + COMPOSE_FILE + "\""
