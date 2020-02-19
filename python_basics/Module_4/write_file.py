lines = ["This is line A", "This is line B", "This is line C"]
with open("./readMe2.txt", "w") as File:
    File.write("I learnt how to write to files using python!    \n")
    File.write("A new line \n")
    for line in lines:
        File.write(line + "\n")

with open("./readMe2.txt", "a") as File:
    File.write("\n")
    File.write("This is to append to the file")

with open("./readMe.txt", "r") as readFile:
    with open("./readMe2.txt", "a") as writeFile:
        writeFile.write("\n")
        writeFile.write(readFile.read())