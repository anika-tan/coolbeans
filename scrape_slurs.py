# get all slurs to slurs_list

from bs4 import BeautifulSoup
import requests

def get_slurs():
    link = "http://www.rsdb.org/full"
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, "lxml")
    slurs_list = []
    
    slur_table = soup.find("div", {"id": "slurs"}) # all info from table
    all_slurs = slur_table.find_all("td") # slur and group
    count = 3
    for slur in all_slurs:
        if (count % 3) == 0: # slur
            word = str(slur.a.contents)[2:-2].lower() # remove the extra characters
            slurs_list.append(word)
        else:
            pass
        count += 1

    return slurs_list
