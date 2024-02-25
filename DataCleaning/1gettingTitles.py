output = open("Titles.txt", "w", encoding="utf-8")
PATH = "../DataAcquisition/Title-Author/"

def writeTitles(input):
    file = open(input, "r", encoding="utf-8")
    lines = file.readlines()
    if input == PATH + "1800-1899.txt" or input == PATH + "1900-1919.txt": lines.reverse()
    for line in lines: 
        i = line.find("sustentante") + 11
        output.write(line[i:-9].strip() + "\n")
    file.close()

writeTitles(PATH + "1800-1899.txt")
writeTitles(PATH + "1900-1919.txt")

for year in range(1920, 2025): writeTitles(PATH + str(year) + ".txt")

output.close()