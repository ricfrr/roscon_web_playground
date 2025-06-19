import pandas as pd

sponsor_file = "./sponsors.csv"
df = pd.read_csv(sponsor_file)
df['Name'] = df['Name'].str.lower()
df = df.sort_values(by="Name")

levels = ["Platinum","Gold","Silver","Bronze","Friend"]

preamble = """
<h{0} style="margin:auto;justify-content:space-around;">{1} Sponsor</h{0}>
<div style="display: flex; max-width:100%;flex-wrap:wrap;justify-content:space-around;padding:10px">
"""

i = 1 

for level in levels:
    temp = df[df["Level"]==level]
    if len(temp) == 0:
        continue
    print(preamble.format(i,level))
    if i <= 3:
        i = i + 1
    for row in temp.iterrows():
        print('{{% include sponsor.md type="{0}" url="{1}" file_path="img/{2}" %}}'.format(level.lower(),row[1]["URL"],row[1]["Image"]))
    print("</div>")
