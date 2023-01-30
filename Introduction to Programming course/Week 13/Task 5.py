from urllib.request import urlopen
import requests
import json

def get_and_print_data(url):
    count = 0
    r = requests.get(url)
    info = r.json()
    
    for i in info["results"]:
            print("ID:{} - name:{} - type:{} species:{} - origin:{} - status:{}".format(i["id"], i["name"], i["type"], i["species"], i["origin"]["name"], i["status"]))
            count = count + 1
    return count

def get_url(url):
    r = requests.get(url)
    info = r.json()
    try:
        next_page = info["info"]["next"]
        url = get_url(next_page, page)
    except:
        None
        
    return next_page

def menu():
    print("You have the following options\n0) Exit\n1) Get all dead characters\n2) Get characters by their name and living status")
    action = int(input("Enter your selection:\n"))
    return action

def main():

    print("Welcome to Rick & Morty API")

    while True:
        oper = menu()
        
        if oper == 0:
            break

        elif oper == 1:
            lim = int(input("Enter limit of pages:\n"))
            
            print("Getting page 1 url: https://rickandmortyapi.com/api/character?status=dead")
            
            link = get_url("https://rickandmortyapi.com/api/character/?status=dead")
            
            list_of_links = []
            list_of_links.append("https://rickandmortyapi.com/api/character/?status=dead")
            
            for page in range(2, lim+1):
                print("Getting page {} url: {}".format(page, link))
                list_of_links.append(link)
                link = get_url(link)
            
            count_dead = 0
            for link in list_of_links:
                count = get_and_print_data(link)
                count_dead = count_dead + count
            
            print("Total number of {} dead characters".format(count_dead))

        elif oper == 2:
            char = input("Enter character to search for:\n")
            stat = input("Enter living status (alive, dead, unknown):\n")
            lim = int(input("Enter limit of pages:\n"))
            make_link =  "https://rickandmortyapi.com/api/character?name=" + char + "&status=" + stat
            
            print("Getting page 1 url:", make_link)
            
            link = get_url(make_link)
            
            list_of_links = []
            list_of_links.append(make_link)
            
            for page in range(2, lim+1):
                while link != None:
                    print("Getting page {} url: {}".format(page, link))
                    list_of_links.append(link)
                    link = get_url(link)
            
            count_char = 0
            for link in list_of_links:
                count = get_and_print_data(link)
                count_char = count_char + count
            
            print("Total number of {} {} {}'s found".format(count_char, stat, char))
            
            
main()
