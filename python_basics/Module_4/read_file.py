with open("./readMe.txt", "r") as File1:
    fileFirstLine = File1.readline()
    fileFourChar = File1.readline(4)

print(File1.closed)
print(fileFirstLine)
print(fileFourChar)

with open("./readMe.txt", "r") as File1:
    file_stuff = File1.read()

print(file_stuff)