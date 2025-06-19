import pandas as pd

sponsor_file = "./sponsors.csv"
df = pd.read_csv(sponsor_file)
df['fName'] = df['Name'].str.lower()
df = df.sort_values(by="fName")

levels = ["Platinum","Gold","Silver","Bronze","Friend"]

i = 1 

for level in levels:
    temp = df[df["Level"]==level]
    if len(temp) == 0:
        continue
    print("# {0} Sponsor".format(level))
    if i <= 3:
        i = i + 1
    for row in temp.iterrows():
        print('* [{0}]({1})'.format(row[1]["Name"],row[1]["URL"]))

