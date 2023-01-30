import json 
def menu():
    print("What would you like to do?\n1) Calculate total amount of inhabitants by gender\n2) Calculate inhabitants on a given year\n3) Calculate inhabitants after given year by age cohort\n0) Stop\n")
    action = int(input("Make your choice:\n"))
    return action

def main():
    print("Welcome to history data analyzer.")
    name = input("Enter the file to open:\n")
    file = open(name, "r")
    print("File read successfully, ready for analysis.")

    filecontent = file.read()
    json_stats = json.loads(filecontent)
    file.close()

    while True:
        oper = menu()

        if oper == 1:
            gender = int(input("Select your gender (0=male, 1=female):\n"))
            count = 0
            i = 0 

            if gender == 0:
                for data in json_stats["data"]:
                    if int(json_stats["data"][i]["key"][1]) == 0:
                        count = count + int(json_stats["data"][i]["values"][0])
                    i = i + 1
                print("There were a total of {} males in Helsinki between years 1900-1961".format(count))
            else:
                for data in json_stats["data"]:
                    if int(json_stats["data"][i]["key"][1]) == 1:
                        count = count + int(json_stats["data"][i]["values"][0])
                    i = i + 1
                print("There were a total of {} females in Helsinki between years 1900-1961".format(count))

        elif oper == 2:
            year = int(input("Please enter year for search (1900-1961):\n"))
            count = 0
            i = 0

            for data in json_stats["data"]:
                if int(json_stats["data"][i]["key"][0]) == year:
                    count = count + int(json_stats["data"][i]["values"][0])
                i = i + 1
            print("There were a total of {} inhabitants in Helsinki on year {}".format(count, year))
            

        elif oper == 3:
            year = int(input("Please enter year for search (1900-1961):\n"))
            age = int(input("Select age cohort (4=20-24, 5=25-29, 6=30-34, 7=35-39):\n"))
            count = 0
            i = 0

            if age == 4:
                group = "20-24"
            if age == 5:
                group = "25-29"
            if age == 6:
                group = "30-34"
            if age == 7:
                group = "35-39"

            for data in json_stats["data"]:
                if int(json_stats["data"][i]["key"][0]) >= year:
                    if int(json_stats["data"][i]["key"][2]) == age:
                        count = count + int(json_stats["data"][i]["values"][0])
                i = i + 1
            print("There were a total of {} inhabitants of ages {} between the years {} and 1961".format(count, group, year))
            
        elif oper == 0:
            print("bye!")
            break
        else:
            break
main()
