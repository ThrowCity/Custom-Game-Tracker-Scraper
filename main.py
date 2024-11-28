import io
import bs4
import pandas as pd

filepath = input()

with open(filepath) as f:
    bs = bs4.BeautifulSoup(f, 'html.parser')

values = bs.find_all("div", {"class": "value"})
usernames = bs.select("span.trn-ign__username")
agentels = bs.select("div.image>img")
agents = [i.attrs['alt'] for i in agentels][::2]

columns = ["Name", "Agent", "ACS", "Kills", "Deaths", "Assists", "ADR", "HS%", "FB", "FD", "KAST", "Plants", "Deaths", "Econ"]
positions = [2, 3, 4, 5, 9, 10, 12, 13, 11]
data = []

for i in range(10):
    row2append = [usernames[i+1].text, agents[i]]
    offset = 13 * i
    for j in positions:
        row2append.append(float(values[j + offset].text.strip("%")))
    row2append += [0, 0, 0]
    data.append(row2append)

final_frame = pd.DataFrame(data=data, columns=columns)

print(final_frame)

### if its indented its in the trackergg, but not used for us
# 2 acs
# 3 kills
# 4 deaths
# 5 assists
#    6 positive
#    7 kd
#    8 ddr
# 9 adr
# 10 hs%
# 11 kast
# 12 fk
# 13 fd
#    14 mk

# C:\Users\qlels\Downloads\trackergame\i.htm