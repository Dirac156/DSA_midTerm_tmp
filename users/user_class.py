
class User:
    """
    Class User
    """
    def __init__(self, id=0, name="", email="", password="", *args, **kwargs):
        """ init method"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

        else:
            self.__id = id
            self.__name = name
            self.__email = email
            self.__password = password
            