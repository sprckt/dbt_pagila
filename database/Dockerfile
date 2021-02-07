FROM postgres

#pgcli as life is too short - https://www.pgcli.com/
RUN apt-get update && apt-get install -y \
    libpq-dev python-dev python3-pip; \
    rm -rf /var/lib/apt/lists/*; pip3 install pgcli

ENV POSTGRES_DB pagila
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres

COPY *.sh /docker-entrypoint-initdb.d/
COPY *.sql /docker-entrypoint-initdb.d/dump/

EXPOSE 5432
CMD ["postgres"]
