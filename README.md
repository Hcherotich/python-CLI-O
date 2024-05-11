This README provides a comprehensive overview of the Python CLI application you've developed for managing blog posts and user interactions. 
It utilizes a custom Object-Relational Mapper (ORM) and leverages the Click library for building the CLI interface.


Project Name: Blog Management System

Description:

This application allows you to manage a simple blog through a user-friendly command-line interface (CLI). 
It utilizes a custom Object-Relational Mapper (ORM) built with peewee and leverages the Click library for building the CLI interface.

Features:

•	User Management: 
o	Create new users.
o	List all users.

•	Post Management: 

o	Create new blog posts with titles, content, and author (user) association.

o	List all posts.

o	List posts authored by a specific user.

•	Basic CRUD Operations: 

o	Create, read (list and find by ID), update (not currently implemented), and delete functionality for users and posts.

•	Custom ORM: 

o	Implements a lightweight ORM using peewee for database interaction, adhering to the requirement of not using existing ORMs.

•	Informative Error Handling: 

o	Provides clear error messages for invalid user IDs, non-existent users, and other potential issues.

Getting Started:

1.	Prerequisites:
o	Python 3.x
o	peewee library (install using pip install peewee)
o	Click library (install using pip install click)

2.	Clone the Repository:

Bash

git clone https://github.com/Hcherotich/python-CLI-O.git

3.	Run the Application:
	Bash
cd Blog-Management-System

python3 main.py

The application will display a menu with available commands.

Usage:

The application provides a menu-driven interface. Use the corresponding commands for desired actions:

•	User Management: 
o	create-user: Creates a new user.
o	list-users: Lists all users.
•	Post Management: 
o	create-post: Creates a new blog post. 

Example:

create-post

Enter post title: Software Development
Enter post content: Steps to code
Enter user ID: 1  # Assuming user ID 1 exists

Post "Software Development" created successfully
* `list-posts`: Lists all posts.
* `list-posts <user_id>`: Lists posts authored by a specific user (provide user ID).
•	Other Commands: 
o	help: Provides information about available commands.
o	exit: Exits the application.

Example Usage:
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  create-post
  create-user
  list-posts
  list-users

Project Structure:

•	main.py: Main script containing the application logic.

•	models.py: Defines the custom ORM models (User, Post, Comment - Comment functionality not currently implemented).

•	database.py: Handles database connection and table creation.

•	README.md: This file (you're reading it now!).

Important Note:

•	While this application demonstrates basic functionalities, it can be extended to include features like: 

o	User authentication and authorization.

o	Post editing and deletion.

o	Commenting functionality.

o	Integration with a database engine like SQLite or PostgreSQL.

•	Feel free to modify and enhance the code based on your specific needs.

Testing:

While unit tests are not currently implemented, you can thoroughly test the application functionalities by running the script and interacting with the CLI menus. Explore various scenarios and validate expected behavior.

Contribution:

We welcome contributions to this project! Feel free to fork the repository, make improvements, and submit pull requests.


We hope you find this CLI application useful!

