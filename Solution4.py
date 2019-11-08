import pandas as pd
import matplotlib.pyplot as plt
with open("startup_funding.csv",encoding="utf-8") as file_obj:
    df_start = pd.read_csv(file_obj)
investors_dictionary = {}
df_start.dropna(subset=['InvestmentType','InvestorsName'],inplace=True)
df_start['InvestmentType'].replace("Crowd funding","Crowd Funding",inplace=True)
df_start['InvestmentType'].replace("SeedFunding","Seed Funding",inplace=True)
df_start['InvestmentType'].replace("PrivateEquity","Private Equity",inplace=True)
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

for startupName,investmentType,investorsName in zip(df_start['StartupName'],df_start['InvestmentType'],df_start['InvestorsName']):
    investmentType = investmentType.strip()
    if investmentType != 'Private Equity':
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
plt.title('Bar Graph')
plt.xlabel('Investors')
plt.ylabel('Number of Investments in different Startups.')
plt.show()
explode = [0.1,0,0,0,0]
plt.pie(numberList,explode=explode,labels=investorList,autopct = "%.1f%%",counterclock=False,startangle=90)
plt.title('Pie Chart')
plt.show()
