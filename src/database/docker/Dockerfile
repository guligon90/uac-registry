FROM postgres:alpine

LABEL maintainer="guligon90"

# Set timezone
ARG TZ
RUN apk add --no-cache tzdata \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone

EXPOSE 5432

# Healthcheck script to verify if database is up.
COPY ./scripts/is-database-up.sh ./
RUN chmod +x is-database-up.sh

# two minutes should be enough to initialize the database
# 2min = 120s => 120s/5s = 24 retries...
HEALTHCHECK --interval=5s --timeout=2s --retries=24 CMD [ "./is-database-up.sh" ]
