with open("TitlesFromLinks.txt", "w", encoding="latin1") as output:
    PATH = "../DataAcquisition/Title-Author/"

    def writeTitles(input):
        with open(input, "r", encoding="latin1") as file:
            lines = file.readlines()
            if input == PATH + "1800-1899_thesis-link.txt" or input == PATH + "1900-1919_thesis-link.txt": lines.reverse()
            for line in lines:
                if not line.startswith("https://tesiunam.dgb.unam.mx"):
                    i = line.find("sustentante") + 11
                    output.write(line[i:-9].strip() + "\n")
    
    writeTitles(PATH + "1800-1899_thesis-link.txt")
    writeTitles(PATH + "1900-1919_thesis-link.txt")
    for year in range(1920, 2025): writeTitles(PATH + str(year) + "_thesis-link.txt")