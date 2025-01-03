import io
import bs4
import json
import pandas as pd
from sys import argv, stdout

filepath = argv[1]

with open(filepath) as f:
    bs = bs4.BeautifulSoup(f, 'html.parser')

values = bs.find_all("div", {"class": "info"})
usernames = bs.find_all("a", {"class": "info"})
agentels = bs.select("div.image>img")
agents = [i.attrs['alt'] for i in agentels][::2]

columns = ["Name", "Agent", "ACS", "Kills", "Deaths", "Assists", "ADR", "HS%", "FB", "FD", "KAST", "Plants", "Defuses", "Econ"]
positions = [2, 3, 4, 5, 9, 10, 12, 13, 11]
data = []

for i in range(10):
    row2append = [usernames[i].text, agents[i]]
    offset = 13 * i
    for j in positions:
        if not len(values[j+offset-2].findChildren()):
            continue
        row2append.append(float(values[j + offset - 2].findChildren()[0].text.strip("%")))
    row2append += [0, 0, 0]
    data.append(row2append)

print(json.dumps(data))

data_in = input().split(" ")

datanums = [float(i) for i in data_in]

for i in range(10):
    data[i][2] = datanums[i * 4]
    data[i][11] = datanums[1 + (i*4)]
    data[i][12] = datanums[2 + (i*4)]
    data[i][13] = datanums[3 + (i*4)]

finalframe = pd.DataFrame(data=data, columns=columns)
finalframe.to_csv("output.csv", index=False)
print("done")