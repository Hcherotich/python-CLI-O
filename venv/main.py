import click
from models import User, Post, Comment
from database import database

# Initialize database tables
database.connect()
database.create_tables([User, Post, Comment])

@click.group()
def cli():
    pass

# User CLI commands
@cli.command()
@click.option('--name', prompt='Enter user name', help='Name of the user')
def create_user(name):
    user = User.create(name=name)
    click.echo(f'User {user.name} created successfully')

@cli.command()
def list_users():
    users = User.select()
    for user in users:
        click.echo(f'User ID: {user.id}, Name: {user.name}')

@cli.command()
@click.argument('user_id', type=int)
def delete_user(user_id):
    user = User.get_or_none(User.id == user_id)
    if user:
        user.delete_instance()
        click.echo(f'User {user_id} deleted successfully')
    else:
        click.echo('User not found')

@cli.command()
@click.option('--attribute', prompt='Enter attribute name', help='Name of the attribute')
@click.option('--value', prompt='Enter attribute value', help='Value of the attribute')
def find_user(attribute, value):
    users = User.select().where(getattr(User, attribute) == value)
    for user in users:
        click.echo(f'User ID: {user.id}, Name: {user.name}')

# Post CLI commands
@cli.command()
@click.option('--title', prompt='Enter post title', help='Title of the post')
@click.option('--content', prompt='Enter post content', help='Content of the post')
@click.option('--user_id', prompt='Enter user ID', type=int, help='ID of the user who created the post')
def create_post(title, content, user_id):
    user = User.get_or_none(User.id == user_id)
    if user:
        post = Post.create(title=title, content=content, user=user)
        click.echo(f'Post "{post.title}" created successfully')
    else:
        click.echo('User not found')

@cli.command()
@click.argument('user_id', type=int)
def list_posts(user_id):
    posts = Post.select().join(User).where(User.id == user_id)
    for post in posts:
        click.echo(f'Post ID: {post.id}, Title: {post.title}, Content: {post.content}')

@cli.command()
@click.option('--attribute', prompt='Enter attribute name', help='Name of the attribute')
@click.option('--value', prompt='Enter attribute value', help='Value of the attribute')
def find_post(attribute, value):
    posts = Post.select().where(getattr(Post, attribute) == value)
    for post in posts:
        click.echo(f'Post ID: {post.id}, Title: {post.title}, Content: {post.content}')

# Comment CLI commands
@cli.command()
@click.option('--content', prompt='Enter comment content', help='Content of the comment')
@click.option('--post_id', prompt='Enter post ID', type=int, help='ID of the post to comment on')
def create_comment(content, post_id):
    post = Post.get_or_none(Post.id == post_id)
    if post:
        comment = Comment.create(content=content, post=post)
        click.echo(f'Comment "{comment.content}" created successfully')
    else:
        click.echo('Post not found')

@cli.command()
@click.argument('post_id', type=int)
def list_comments(post_id):
    comments = Comment.select().join(Post).where(Post.id == post_id)
    for comment in comments:
        click.echo(f'Comment ID: {comment.id}, Content: {comment.content}')

@cli.command()
@click.option('--attribute', prompt='Enter attribute name', help='Name of the attribute')
@click.option('--value', prompt='Enter attribute value', help='Value of the attribute')
def find_comment(attribute, value):
    comments = Comment.select().where(getattr(Comment, attribute) == value)
    for comment in comments:
        click.echo(f'Comment ID: {comment.id}, Content: {comment.content}')

if __name__ == '__main__':
    cli()
