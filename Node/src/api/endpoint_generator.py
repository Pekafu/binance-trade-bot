import re

tryFind = "@app"
f = open("api_server.py", "r")

 
for line in f.readlines():
    x = re.search(tryFind, line)
    if x is None:
        continue

    print(line[x.start(): (len(line) -1)])