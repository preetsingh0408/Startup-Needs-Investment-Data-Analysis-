import pandas as pd
import matplotlib.pyplot as plt
with open("startup_funding.csv",encoding="utf-8") as file_obj:
    df_start = pd.read_csv(file_obj)
df_start.dropna(subset=['StartupName','InvestorsName'],inplace=True)
investors_dictionary = {}
startup = df_start['StartupName']
df_start['StartupName'] = df_start['StartupName'].replace("Olacabs","Ola")
df_start['StartupName'] = df_start['StartupName'].replace("Ola","Ola")
df_start['StartupName'] = df_start['StartupName'].replace("Ola Cabs","Ola")
df_start['StartupName'] = df_start['StartupName'].replace("Flipkart.com","Flipkart")
df_start['StartupName'] = df_start['StartupName'].replace("Oyo Rooms","Oyo")
df_start['StartupName'] = df_start['StartupName'].replace("OyoRooms","Oyo")
df_start['StartupName'] = df_start['StartupName'].replace("OYO Rooms","Oyo")
df_start['StartupName'] = df_start['StartupName'].replace("Oyorooms","Oyo")
df_start['StartupName'] = df_start['StartupName'].replace("Oyo","Oyo")
df_start['StartupName'] = df_start['StartupName'].replace("Paytm Marketplace","Paytm")
for startupName,investorsName in zip(df_start['StartupName'],df_start['InvestorsName']):
    for investor in investorsName.split(','):
        investor = investor.strip()
        if investor != '' and investor != 'Undisclosed Investors' and investor != 'Undisclosed investors':
            if investor in investors_dictionary and not startupName in investors_dictionary[investor]:
                investors_dictionary[investor].append(startupName.strip())
            else:
                investors_dictionary[investor] = []
                investors_dictionary[investor].append(startupName.strip())
for i in investors_dictionary:
    investors_dictionary[i] = len(investors_dictionary[i])
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
plt.ylabel('Number of Investments in different Startups')
plt.show()
plt.pie(numberList,explode=explode,autopct="%.2f%%",counterclock=False,labels=investorList,startangle=90)
plt.show()
