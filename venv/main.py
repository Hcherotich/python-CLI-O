import click
from database import database
from models import User, Post

# Initialize database tables
database.connect()
database.create_tables([User, Post])

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', prompt='Enter user name', help='Name of the user')
def create_user(name):
    with database:
        user = User(name=name)
        user.save()
        click.echo(f'User {user.name} created successfully')

@cli.command()
def list_users():
    with database:
        users = User.get_all()
        for user in users:
            click.echo(f'User ID: {user.id}, Name: {user.name}')

@cli.command()
@click.argument('user_id', type=int)
def delete_user(user_id):
    with database:
        user = User.find_by_id(user_id)
        if user:
            user.delete_instance()
            click.echo(f'User {user_id} deleted successfully')
        else:
            click.echo('User not found')

@cli.command()
@click.option('--title', prompt='Enter post title', help='Title of the post')
@click.option('--content', prompt='Enter post content', help='Content of the post')
@click.option('--user_id', prompt='Enter user ID', type=int, help='ID of the user who created the post')
def create_post(title, content, user_id):
    with database:
        user = User.find_by_id(user_id)
        if user:
            post = Post(title=title, content=content, user=user)
            post.save()
            click.echo(f'Post "{post.title}" created successfully')
        else:
            click.echo('User not found')

@cli.command()
@click.argument('user_id', type=int)
def list_posts(user_id):
    with database:
        user = User.find_by_id(user_id)
        if user:
            posts = user.posts
            for post in posts:
                click.echo(f'Post ID: {post.id}, Title: {post.title}, Content: {post.content}')
        else:
            click.echo('User not found')

if __name__ == '__main__':
    cli()
