FROM python:3.8-alpine

LABEL maintainer="guligon90"

# Timezone from Docker Compose service
ARG TZ

ENV PYTHONBUFFERED 1
ENV BACKEND_ROOT /uac-registry/backend

WORKDIR $BACKEND_ROOT
COPY ["./uac-registry/requirements.txt", "./uac-registry/requirements-dev.txt", "./"]

RUN \
    # Setting timezone
    apk add --no-cache tzdata \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    # Installing dependencies
    # To build psycopg2 you need the packages gcc musl-dev and postgresql-dev.
    # Then you also need that pg_config executable: while simply installing
    # postgresql-dev will work, postgresql-libs does fine too and takes 
    # up some 12 MB less space.
    && apk add --no-cache postgresql-libs \
    && apk add --no-cache --virtual \
        .build-deps \
        gcc \
        musl-dev \
        postgresql-dev \
        libffi-dev \
        libressl-dev \
    && python3 -m pip install --upgrade pip \
    && python3 -m pip install wheel \
    && python3 -m pip install \
        -r requirements.txt \
        -r requirements-dev.txt \
        --no-cache-dir \
    && apk --purge del .build-deps

# Don't run as root
RUN addgroup -g 1000 python \
    && adduser -u 1000 -G python -s /bin/sh -D python \
    && chown -R python:python $BACKEND_ROOT

# USER affects only RUN, CMD and ENTRYPOINT
USER python:python

COPY --chown=python:python ./scripts/wait-for.sh ..
COPY --chown=python:python ./uac-registry .
RUN chmod +x ../wait-for.sh

EXPOSE 8080

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]