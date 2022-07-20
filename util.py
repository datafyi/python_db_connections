import os

def set_environ_vars():
    os.environ.setdefault('PGDBNAME','postgres')
    os.environ.setdefault('PGUSER','postgres')
    os.environ.setdefault('PGPASSWORD','dev')
    os.environ.setdefault('PGHOST','localhost')
    os.environ.setdefault('PGPORT','5432')
