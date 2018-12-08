import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("marathon_results_2017.csv")

# made a dictionary of countries
country = {}
for i in data['Country']:
    if i not in country:
        country[i] = 1
    else:
        country[i]+=1
# made a dictionary to record the amounts of runners of different continents
continent = {
    'Asia' : 0,
    'Europe' : 0,
    'North America' : 0,
    'South America' : 0,
    'Central America' : 0,
    'Africa' : 0,
    'Oceania' : 0
}

for i in country:
    if i == ('JPN' or 'CHN' or 'PHI' or 'HKG' or 'KOR' or 'TPE' or 'SIN' or 'VIE' or 'IND' or 'ISR'):
        continent['Asia'] += country[i]
    if i == ('NED' or 'ITA' or 'ESP' or 'LAT' or 'SVK' or 'FIN' or 'GBR' or 'FRA' or 'BEL' or 'DEN'
    or 'POL' or 'NOR' or 'LTU' or 'CZE' or 'CYP' or 'POL' or 'NOR' or 'POR' or 'LUX' or 'CZE' or
    'ROU' or 'LIE' or 'GRE' or 'SLO' or 'LTU' or 'EST'):
        continent['Europe'] += country[i]
    if i == ('MEX' or 'GUA' or 'CRC' or 'BER' or 'DOM'):
        continent['North America'] += country[i]
    if i == ('BRA' or 'CHI' or 'COL' or 'PER' or 'PER' or 'PAN' or 'VEN' or 'ARG' or 'URU'):
        continent['South America'] += country[i]
    if i == ('ESA'):
        continent['Central America'] += country[i]
    if i == ('ETH' or 'KEN' or 'ZIM' or 'UGA'or 'MOR'):
        continent['Africa'] += country[i]
    if i == ('NZL' or 'AUS'):
        continent['Oceania'] += country[i]

# Data to plot
labels=[]
for i in continent.keys():
    labels += [i]

sizes = []
for i in continent.values():
    sizes += [i]

pct = []
s = 0
for i in continent.values():
    s += i
for i in continent.values():
    pct += [i/s * 100]

colors = ['lightgreen', 'coral', 'gold', 'skyblue', 'white', 'cyan', 'pink']
explode = (0, 0, 0.1 , 0, 0, 0, 0)  # explode 1st slice

# plot
patches, texts = plt.pie(sizes, colors=colors, shadow=False, startangle=90)
plt.legend( loc = 'best', labels=['%s, %1.3f %%' % (l, s) for l, s in zip(labels, pct)])
# plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()
# plt.savefig('Runners Continents Bar Chart 2017.jpg', dpi = 500)
