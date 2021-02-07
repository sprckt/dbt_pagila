from invoke import task


@task
def build(c):
    print("Building docker compose infrastructure")
    c.run("docker-compose build")


@task
def shell(c):
    print("Running dbt container and entering...")
    c.run("docker-compose run dbt /bin/bash")


@task
def db(c):
    print("Running dbt db container")
    c.run("docker exec -it pagila_db pgcli -U postgres -d pagila")