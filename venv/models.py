class User:
    def __init__(self, database):
        self.db = database

    def create(self, name):
        query = "INSERT INTO users (name) VALUES (?)"
        self.db.execute(query, (name,))

    def get_all(self):
        query = "SELECT * FROM users"
        return self.db.fetch_all(query)


class Post:
    def __init__(self, database):
        self.db = database

    def create(self, title, content, user_id):
        query = "INSERT INTO posts (title, content, user_id) VALUES (?, ?, ?)"
        self.db.execute(query, (title, content, user_id))

    def get_all(self):
        query = "SELECT * FROM posts"
        return self.db.fetch_all(query)
