PATH = "../DataAcquisition/Title-Author/"

with open("Titles.txt", "w", encoding="utf8") as output:
    def writeTitles(input):
        with open(input, "r", encoding="utf8") as file:
            lines = file.readlines()
            for line in lines:
                i = line.find("sustentante") + 11
                title = line[i:].strip().split()
                title = " ".join(title[:-1])
                if title[-1] == "/": title = title[:-1]
                output.write(title + "\n")

    writeTitles(PATH + "1800-1899.txt")
    writeTitles(PATH + "1900-1919.txt")
    for year in range(1920, 2026): writeTitles(PATH + str(year) + ".txt")

with open("Titles.txt", "r", encoding="utf8") as f:
    lines = f.readlines()

with open("Titles.txt", "w", encoding="utf8") as f:
    control = set()
    for line in lines:
        if line in control: continue
        f.write(line)
        control.add(line)