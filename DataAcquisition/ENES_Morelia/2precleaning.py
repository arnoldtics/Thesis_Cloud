input = open("thesis1.txt", "r", encoding="utf-8")
output = open("thesis2.txt", "w", encoding="utf-8")

text, register = input.readlines(), ""
for line in text:
    if line.startswith("Licenciatura"):
        if register != "": output.write(register.replace("\n", "") + "\n")
        register = line
    else: register += line
output.write(register.replace("\n", "") + "\n")

input.close()
output.close()