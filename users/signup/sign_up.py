import requests
import json


def sign_up(dict):
    """ 
    sign_up
    =======
    sign_up(*details)
    *details is all information passed by the user.  
    """
    
    url = "https://api-career-dev-quizz.herokuapp.com/users"

    request = requests.post(url = url, data = dict)

    if request.status_code == 200:
        print ("created a new user")
    else:
        return -1