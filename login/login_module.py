import requests
import json
from users.user_class import User
from users.administrator_class import Administrator
from users.student_class import Student 

def login (first_name, last_name, password):
    """login"""
    """find user in the database"""
    """create new user class depending on the class"""
    """return users details"""
    
    url = "https://api-career-dev-quizz.herokuapp.com/login"
    
    request = requests.get(url = url, data = {first_name, last_name, password})

    if request.status_code == 200:
        user = json.loads(request.text)
        user.pop("_id")
        user.pop("__v")
        if user["user_classification"] == "student":
            return Student(**user)
        else:
            return Administrator(**user) 
    else:
        return -1