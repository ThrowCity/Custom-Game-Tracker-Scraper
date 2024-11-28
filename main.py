import io
import bs4
import json
import pandas as pd
from sys import argv, stdout

filepath = argv[1]

with open(filepath) as f:
    bs = bs4.BeautifulSoup(f, 'html.parser')

values = bs.find_all("div", {"class": "value"})
usernames = bs.select("span.trn-ign__username")
agentels = bs.select("div.image>img")
agents = [i.attrs['alt'] for i in agentels][::2]

columns = ["Name", "Agent", "ACS", "Kills", "Deaths", "Assists", "ADR", "HS%", "FB", "FD", "KAST", "Plants", "Defuses", "Econ"]
positions = [2, 3, 4, 5, 9, 10, 12, 13, 11]
data = []

for i in range(10):
    row2append = [usernames[i+1].text, agents[i]]
    offset = 13 * i
    for j in positions:
        row2append.append(float(values[j + offset].text.strip("%")))
    row2append += [0, 0, 0]
    data.append(row2append)

print(json.dumps(data))
input()