class User:
    def __init__(self, user_id, name, email):
        self.id = user_id
        self.name = name
        self.email = email
    
    # getter
    def get_id(self): return self.id
    def get_name(self): return self.name
    def get_email(self): return self.email