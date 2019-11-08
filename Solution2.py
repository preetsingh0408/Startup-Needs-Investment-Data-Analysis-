import pandas as pd
import matplotlib.pyplot as plt
with open("startup_funding.csv",encoding="utf-8") as file_obj:
    df_start = pd.read_csv(file_obj)
df_start.dropna(subset=['InvestorsName'],inplace=True)
investors_dictionary={}
for investorsName in df_start['InvestorsName']:
    for investor in investorsName.split(','):
        investor = investor.strip()
        if investor != '' and investor != 'Undisclosed Investors' and investor != 'Undisclosed investors':
            if investor in investors_dictionary:
                investors_dictionary[investor] += 1
            else:
                investors_dictionary[investor] = 1
top_5_investors = sorted(investors_dictionary.items(), key=lambda x: x[1],reverse=True)[0:5]
investorList = []
numberList = []
for investor in top_5_investors:
    print(investor[0],investor[1])
    investorList.append(investor[0])
    numberList.append(investor[1])

plt.bar(investorList,numberList,color='orange',edgecolor='magenta') 
plt.xticks(rotation=30)
plt.xlabel('Investors')
plt.ylabel('Number of Investments')
plt.show()
plt.pie(numberList,explode=explode,autopct="%.2f%%",counterclock=False,labels=investorList,startangle=90)
plt.show()
