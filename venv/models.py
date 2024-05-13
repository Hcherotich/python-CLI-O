class BaseModel:
    def __init__(self, database):
        self.db = database

class User(BaseModel):
    def create(self, name):
        query = "INSERT INTO users (name) VALUES (?)"
        self.db.execute(query, (name,))

    def get_all(self):
        query = "SELECT * FROM users"
        return self.db.fetch_all(query)
