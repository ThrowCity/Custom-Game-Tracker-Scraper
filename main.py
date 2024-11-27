import io
import bs4

filepath = input()

with open(filepath) as f:
    bs = bs4.BeautifulSoup(f, 'html.parser')

values = bs.find_all("div", {"class": "value"})
usernames = bs.select("span.trn-ign__username")
agentels = bs.select("div.image>img")
agents = [i.attrs['alt'] for i in agentels][::2]

final = []

for i in range(10):
    ###                  username           agent             acs                       kills                      deaths                  assists                     adr                       hs%                           kast                        fb                      fd                    mulitkills
    final.append(f"{usernames[i+1].text},{agents[i]},{values[2 + 13*(i)].text},{values[3 + 13*(i)].text},{values[4+ 13*(i)].text},{values[5 + 13*(i)].text},{values[9 + 13*(i)].text},{values[10 + 13*(i)].text},{values[11 + 13*(i)].text},{values[12 + 13*(i)].text},{values[13 + 13*(i)].text},{values[14 + 13*(i)].text}")
    print(final[i])

### if its indented its in the trackergg, but not used for us
# 3 acs
# 4 kills
# 5 deaths
# 6 assists
#    7 positive
#    8 kd
#    9 ddr
# 10 adr
# 11 hs%
# 12 kast
# 13 fk
# 14 fd
# 15 mk