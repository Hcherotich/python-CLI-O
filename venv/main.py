import click
from models import User, Post
from database import Database

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

@cli.command()
@click.option('--title', prompt='Enter post title', help='Title of the post')
@click.option('--content', prompt='Enter post content', help='Content of the post')
@click.option('--user_id', prompt='Enter user ID', help='ID of the user who created the post')
def create_post(title, content, user_id):
    database = initialize_database()
    post = Post(database)
    post.create(title, content, user_id)
    click.echo(f'Post "{title}" created successfully')
    database.close()

@cli.command()
def list_posts():
    database = initialize_database()
    post = Post(database)
    posts = post.get_all()
    for p in posts:
        click.echo(f'Post ID: {p[0]}, Title: {p[1]}, Content: {p[2]}, User ID: {p[3]}')
    database.close()

if __name__ == '__main__':
    cli()
