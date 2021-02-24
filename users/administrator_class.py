from users.user_class import User

class Administrator(User):

    def __init__(self, id=0, name="", email="", password="", *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            super().__init__(id, name, email, password)
