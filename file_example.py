filename = "text.txt"

# the first way of reading from a file
fp = open(filename)
print(fp.read())
fp.close()

# second way of reading from a file"
with open(filename) as fp:
    for line in fp:
        line = line.replace("\n")
        print(f"Line: {line}", end="")
        # at the end, the file will be closed automatically
        
        