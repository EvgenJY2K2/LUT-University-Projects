import csv, sys

def menu():
    print("-1) Stop\n0) Calculate Airplanes\n1) Calculate Helicopters\n2) Calculate Ultralights\n3) Calculate Gliders and Powered Gliders\n4) Calculate Autogiros\n5) Calculate Balloons (hot-air)\n6) Calculate Airships")
    action = input("Please, make your selection:\n")
    return action

def main():
    name = input("Enter filename:\n")

    try:
        file = open(name, "r", encoding="utf-8")
    except:
        print("Error processing file '{}', stopping.".format(name))
        sys.exit(0)

    csvreader = csv.reader(file, delimiter = ";")

    header = []
    header = next(csvreader)
    
    rows = []
    types = []
    years = []

    for row in csvreader:
        rows.append(row)

    for item in rows:
        if item[2] not in types:
            types.append(item[2])

        try:
            date = []
            date = item[13].split('.')
            year = date[2]
            if year not in years:
                years.append(year)
        except:
            continue
    years.sort(reverse = True)
    air_dict = dict.fromkeys(years, 0)

    print("The file contains {} aircrafts".format(len(rows)))

    while True:
        oper = menu()

        try:
            oper = int(oper)
        except:
            print("Faulty user input. Exiting.")
            sys.exit(0)

        if oper == 0:
            print("Search type is:Airplanes")
            sum = 0
            ai = air_dict.copy()

            for item in rows:
                if item[2] == "Airplanes":
                    sum = sum + 1

                    date = []
                    date = item[13].split('.')
                    year = date[2]
                    
                    if year in ai:
                        ai[year] += 1

            print("Displaying Airplanes in descending order.")

            for i in sorted(ai, reverse=True):
                if ai[i] != 0:
                    print("{} - {} Airplanes".format(i, ai[i]))

            print("Total amount of Airplanes found: {}".format(sum))

        elif oper == 1:
            print("Search type is:Helicopters")
            sum = 0
            he = air_dict.copy()

            for item in rows:
                if item[2] == "Helicopters":
                    sum = sum + 1

                    date = []
                    date = item[13].split('.')
                    year = date[2]
                    
                    if year in he:
                        he[year] += 1
                        

            print("Displaying Helicopters in descending order.")

            for i in sorted(he, reverse=True):
                if he[i] != 0:
                    print("{} - {} Helicopters".format(i, he[i]))

            print("Total amount of Helicopters found: {}".format(sum))
            
        elif oper == 2:
            print("Search type is:Ultralights")
            sum = 0
            ul = air_dict.copy()

            for item in rows:
                if item[2] == "Ultralights":
                    sum = sum + 1

                    date = []
                    date = item[13].split('.')
                    year = date[2]
                    
                    if year in ul:
                        ul[year] += 1
                        

            print("Displaying Ultralights in descending order.")

            for i in sorted(ul, reverse=True):
                if ul[i] != 0:
                    print("{} - {} Ultralights".format(i, ul[i]))

            print("Total amount of Ultralights found: {}".format(sum))

        elif oper == 3:
            print("Search type is:Gliders and Powered Gliders")
            sum = 0
            gp = air_dict.copy()

            for item in rows:
                if item[2] == "Gliders and Powered Gliders":
                    sum = sum + 1

                    date = []
                    date = item[13].split('.')
                    year = date[2]
                    
                    if year in gp:
                        gp[year] += 1
                        

            print("Displaying Gliders and Powered Gliders in descending order.")

            for i in sorted(gp, reverse=True):
                if gp[i] != 0:
                    print("{} - {} Gliders and Powered Gliders".format(i, gp[i]))

            print("Total amount of Gliders and Powered Gliders found: {}".format(sum))

        elif oper == 4:
            print("Search type is:Autogiros")
            sum = 0
            au = air_dict.copy()

            for item in rows:
                if item[2] == "Autogiros":
                    sum = sum + 1

                    date = []
                    date = item[13].split('.')
                    year = date[2]
                    
                    if year in au:
                        au[year] += 1
                        

            print("Displaying Autogiros in descending order.")

            for i in sorted(au, reverse=True):
                if au[i] != 0:
                    print("{} - {} Autogiros".format(i, au[i]))

            print("Total amount of Ultralights found: {}".format(sum))

        elif oper == 5:
            print("Search type is:Balloons (hot-air)")
            sum = 0
            ba = air_dict.copy()

            for item in rows:
                if item[2] == "Balloons (hot-air)":
                    sum = sum + 1

                    date = []
                    date = item[13].split('.')
                    year = date[2]
                    
                    if year in ba:
                        ba[year] += 1
                        

            print("Displaying Balloons (hot-air) in descending order.")

            for i in sorted(ba, reverse=True):
                if ba[i] != 0:
                    print("{} - {} Balloons (hot-air)".format(i, ba[i]))

            print("Total amount of Balloons (hot-air) found: {}".format(sum))

        elif oper == 6:
            print("Search type is:Airships")
            sum = 0
            ah = air_dict.copy()

            for item in rows:
                if item[2] == "Airships":
                    sum = sum + 1

                    date = []
                    date = item[13].split('.')
                    year = date[2]
                    
                    if year in ah:
                        ah[year] += 1
                        

            print("Displaying Airships in descending order.")

            for i in sorted(ah, reverse=True):
                if ah[i] != 0:
                    print("{} - {} Airships".format(i, ah[i]))

            print("Total amount of Airships found: {}".format(sum))

        elif oper == -1:
            break

        else:
            print("Faulty selection. Please try again.")

main()
