string = "Python is a case sensitive language"


def remove_spaces(string):
    string = string.replace(' ', '')
    return string


print(remove_spaces("Python is a case sensitive language"))
