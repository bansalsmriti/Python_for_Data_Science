import pandas as pd
names1180=pd.read_csv('Python projects\Wes McKinney\yob1880.txt', names=['name','sex','birth'])

years = range(1880, 2011)
pieces = []
columns = ['name', 'sex', 'births']
for year in years:
    path = 'Python projects\Wes McKinney\yob1880.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)
names1180 = pd.concat(pieces, ignore_index=True)