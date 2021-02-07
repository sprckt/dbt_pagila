import invoke


@task
def debug(c):
    c.run("dbt debug")

