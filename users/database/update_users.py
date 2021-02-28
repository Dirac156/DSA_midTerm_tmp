import requests
import json

def update_users(lst_users):

    """
    update_users
    =============
    return -1 when failed.
    """

    url = "https://api-career-dev-quizz.herokuapp.com/users"
    

    if lst_users is None:
        return -1
    elif type(lst_users) is not "list":
        raise TypeError
    else:
        for user in lst_users:

            request = requests.put(url = url, data=user)

            if request.status_code == 200:
                print("updated a user")
            else:
                return -1
