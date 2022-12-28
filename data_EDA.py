import pandas as pd
import xlwings as xw

book = xw.Book('path')
df = book.sheets(1).used_range.options(pd.DataFrame).value

longi = []
for pnum_i in df.index:
    count = 0
    for pnum_j in df.index:
        if pnum_i == pnum_j:
            count += 1
    longi.append([pnum_i, count])
    
df_longi = pd.DataFrame(longi)

df_longi_group = df_longi.groupby(by=1)

for i in range(1, 6):
    df_longi_group.size()[i]/i
 
