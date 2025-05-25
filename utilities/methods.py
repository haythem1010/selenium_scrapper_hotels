from utilities.consts import list_of_websites
from pprint import pprint

def get_my_website(name):
    name = name.lower()
    findr = False
    i = 0
    pprint(list_of_websites[i]['name'])
    while (not findr) or (i < len(list_of_websites)) :
        if list_of_websites[i]['name'] == name :
            website = i['website']
            findr = True
        else :
            continue
        i = i+1

    return website


