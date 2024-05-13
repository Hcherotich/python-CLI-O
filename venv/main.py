import click
from database import Database
from models import User

@click.group()
def cli():
    pass

def initialize_database():
    db = Database('my_database.db')
    db.create_tables()
    return db

@cli.command()
@click.option('--name', prompt='Enter user name', help='Name of the user')
def create_user(name):
    database = initialize_database()
    user = User(database)
    user.create(name)
    click.echo(f'User {name} created successfully')
    database.close()

@cli.command()
def list_users():
    database = initialize_database()
    user = User(database)
    users = user.get_all()
    for u in users:
        click.echo(f'User ID: {u[0]}, Name: {u[1]}')
    database.close()

if __name__ == '__main__':
    cli()
