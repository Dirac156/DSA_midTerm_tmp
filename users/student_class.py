from users.user_class import User


class Student(User):
    """
    student class
    =============
    Student(id, name, email, password, faculty, promotion, **alldetails)
    **alldetails: use to recreate a user when details comes from the database.
    """

    def __init__(self, id=0, name="", email="", password="", faculty="",
                 promotion="", *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            super().__init__(id, name, email, password)
            self.__faculty = faculty
            self.__promotion = promotion
            self.__score = 0
            self.__level = 0
