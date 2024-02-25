input = open("thesis3.txt", "r", encoding="utf-8")
output = open("thesis4.txt", "w", encoding="utf-8")

text = input.readlines()
for line in text:
    program, year, title, author, director = "", "", "", "", ""

    # Degree
    i = line.find("20")
    program = line[:i]
    output.write(f"Degree: {program}\n".replace(".", ""))

    # Year
    year = line[i:i+4]
    output.write(f"Year: {year}\n")

    # Title
    i += 6
    j = line.find(" presenta ")
    title = line[i:j]
    output.write(f"Title: {title}\n")

    # Author
    line = line[j:]
    line = line.replace(" presenta ", "")
    i = line.find(";")
    author = line[:i]
    output.write(f"Author: {author}\n")

    # Director
    line = line[i+1:].split()
    for word in line: 
        if word[0].islower(): continue
        else: director += word + " "
    output.write(f"Director(s): {director}\n\n")

input.close()
output.close()